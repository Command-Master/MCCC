from assignment_target import assignment_target
from c_int import Int
from c_pointer import Pointer
from c_struct import Struct
from c_void import Void
from casting import get_type
from id_expr import id_expression
from compound_expr import compound_expression
from const_expr import parse_int, parse_char, parse_string_const, parse_double
from globals_consts import cname, NAMESPACE, BinaryOp
from for_expr import for_expression
from if_expr import if_expression
from bin_expr import binary_expression
from funccall_expr import funccall_expression
from unary_expr import address_unary, dereference_unary, post_increment_unary
from ternary_expr import ternary_expression
from while_expr import while_expression
from temps import used_temps, get_temp
from locals import get_rtype


def generate_expression(target, expression, vtypes, variables_name, copy_strings=False,
                        ignore_output=False):

    if not ignore_output:
        if cname(expression) == 'ID':
            return id_expression(expression, target, variables_name, vtypes)
        elif cname(expression) == 'Constant':
            if expression.type == 'int':
                return parse_int(expression, target)
            elif expression.type == 'char':
                return parse_char(expression, target)
            elif expression.type == 'string':
                return parse_string_const(copy_strings, expression, target)
            elif expression.type == 'double':
                return parse_double(expression, target)
    else:
        if cname(expression) == 'Compound':
            return compound_expression(copy_strings, expression, target, variables_name, vtypes)
        elif cname(expression) == 'For':
            return for_expression(copy_strings, expression, target, variables_name, vtypes)
        elif cname(expression) == 'If':
            return if_expression(copy_strings, expression, target, variables_name, vtypes)
        elif cname(expression) == 'While':
            return while_expression(copy_strings, expression, target, variables_name, vtypes)
        elif cname(expression) == 'Return':
            code = ''
            if expression.expr is not None:
                c1, t1, tt1 = generate_expression(None, expression.expr, vtypes, variables_name, copy_strings, False)
                code += c1
                code += t1.cast(get_rtype(), tt1, [f'$r{i}' for i in range(get_rtype().size)])
                for ttt in tt1: used_temps.remove(ttt)
            code += f'scoreboard players set $returned {NAMESPACE} 1\n'
            return code, Void(), []
        elif cname(expression) == 'Break':
            code = f'scoreboard players set $broken {NAMESPACE} 1\n'
            return code, Void(), []
    if cname(expression) == 'Decl':
        if expression.init is None:
            return '', Void(), []
        code = ''
        dname = expression.name
        out_type = vtypes[dname]
        targets = variables_name[dname]
        c3, t3, tt3 = generate_expression(None, expression.init, vtypes, variables_name, copy_strings, False)
        for ttt in tt3: used_temps.remove(ttt)
        code += c3
        code += t3.cast(out_type, tt3, targets)
        return code, Void(), []
    if cname(expression) == 'Assignment':
        start, targets, end, out_type = assignment_target(expression.lvalue, vtypes, variables_name)
        if target is None:
            target = [get_temp() for _ in range(len(targets))]
            used_temps.extend(target)
        code = ''
        code += start
        c3, t3, tt3 = generate_expression(None, expression.rvalue, vtypes, variables_name, copy_strings, False)
        for ttt in tt3: used_temps.remove(ttt)
        if end != '':
            for ttt in targets:
                if ttt in used_temps:
                    used_temps.remove(ttt)
        code += c3
        if expression.op == '=':
            code += t3.cast(out_type, tt3, targets)
            if not ignore_output:
                for t1, t2 in zip(target, targets):
                    code += f'scoreboard players operation {t1} {NAMESPACE} = {t2} {NAMESPACE}\n'
        elif expression.op in ['+=', '*=']:
            if not target:
                target = [get_temp() for _ in range(len(targets))]
                used_temps.extend(target)
            code += t3.cast(out_type, tt3, target)
            c4, t4, tt4 = generate_expression(None, expression.lvalue, vtypes, variables_name, copy_strings, False)
            code += c4
            code += out_type.binary(expression.op[0], target, tt4, targets)
            for ttt in tt4: used_temps.remove(ttt)
            for t1, t2 in zip(target, targets):
                code += f'scoreboard players operation {t1} {NAMESPACE} = {t2} {NAMESPACE}\n'
        elif expression.op == '|=':
            if not target:
                target = [get_temp() for _ in range(len(targets))]
                used_temps.extend(target)
            code += t3.cast(out_type, tt3, target)
            n = int(expression.rvalue.value)
            assert n & (n - 1) == 0, 'Powers of two'
            code += f'scoreboard players operation $temp {NAMESPACE} = {targets[0]} {NAMESPACE}\n'
            code += f'scoreboard players operation $temp {NAMESPACE} /= ${n} {NAMESPACE}\n'
            code += f'scoreboard players operation $temp {NAMESPACE} %= %2 {NAMESPACE}\n'
            code += f'execute if score $temp {NAMESPACE} matches 0.. run scoreboard players add {targets[0]} {NAMESPACE} {n}\n'
            for t1, t2 in zip(target, targets):
                code += f'scoreboard players operation {t1} {NAMESPACE} = {t2} {NAMESPACE}\n'
        else:
            raise NotImplementedError(expression)
        code += end
        return code, out_type, target
    elif cname(expression) == 'TernaryOp':
        return ternary_expression(copy_strings, expression, target, variables_name, vtypes)
    elif cname(expression) == 'BinaryOp':
        return binary_expression(copy_strings, expression, target, variables_name, vtypes)
    elif cname(expression) == 'ExprList':
        code = ''
        for expr in expression.exprs[:-1]:
            c1, t1, tt1 = generate_expression([], expr, vtypes, variables_name, copy_strings, True)
            for ttt in tt1: used_temps.remove(ttt)
            code += c1
        c1, t1, tt1 = generate_expression(target, expression.exprs[-1], vtypes, variables_name, copy_strings,
                                          False)
        code += c1
        return code, t1, tt1
    elif cname(expression) == 'Cast':
        c1, t1, tt1 = generate_expression(target, expression.expr, vtypes, variables_name, copy_strings,
                                          False) # wait why am I no casting really?
        type_cast = get_type(expression.to_type.type)
        target = [get_temp() for _ in range(type_cast.size)]
        used_temps.extend(target)
        c1 += t1.cast(type_cast, tt1, target)
        return c1, type_cast, target
    elif cname(expression) == 'UnaryOp':
        if expression.op == 'p++':
            return post_increment_unary(copy_strings, expression, variables_name, vtypes)
        elif expression.op == '-':
            c1, t1, tt1 = generate_expression(None, expression.expr, vtypes, variables_name, copy_strings, False)
            code = c1
            code += t1.negate(tt1)
            return code, t1, tt1
        elif expression.op == '!':
            c1, t1, tt1 = generate_expression(None, expression.expr, vtypes, variables_name, copy_strings, False)
            code = c1
            targett = get_temp()
            used_temps.append(targett)
            code += t1.cast(Int(), tt1, [targett])
            for ttt in tt1: used_temps.remove(ttt)
            code += f'execute store result score {targett} {NAMESPACE} if score {targett} {NAMESPACE} matches 0\n'
            return code, Int(), [targett]
        elif expression.op == '*':
            return dereference_unary(copy_strings, expression, variables_name, vtypes)
        elif expression.op == 'sizeof':
            tv = get_temp()
            used_temps.append(tv)
            return f'scoreboard players set {tv} {NAMESPACE} {get_type(expression.expr.type).size}\n', Int(), [tv]
        elif expression.op == '&':
            return address_unary(expression, variables_name, vtypes)
        raise NotImplementedError(expression)
    elif cname(expression) == 'ArrayRef':
        c1, t1, tt1 = generate_expression(None, BinaryOp('+', expression.name, expression.subscript), vtypes,
                                          variables_name, copy_strings, False)
        code = c1
        assert type(t1) == Pointer
        code += f'scoreboard players operation $index {NAMESPACE} = {tt1[0]} {NAMESPACE}\n'
        targets = [get_temp() for _ in range(t1.ptr.size)]
        used_temps.extend(targets)
        for t in targets:
            code += f'function {NAMESPACE}:get_heap\n'
            code += f'scoreboard players operation {t} {NAMESPACE} = $value {NAMESPACE}\n'
            code += f'scoreboard players add $index {NAMESPACE} 1\n'
        for ttt in tt1: used_temps.remove(ttt)
        return code, t1.ptr, targets
    elif cname(expression) == 'FuncCall':
        return funccall_expression(copy_strings, expression, variables_name, vtypes)
    elif cname(expression) == 'StructRef':
        assert expression.type == '->'
        c1, t1, tt1 = generate_expression(None, expression.name, vtypes, variables_name, copy_strings, False)
        code = ''
        code += c1
        for t in tt1: used_temps.remove(t)
        assert type(t1) == Pointer
        assert type(t1.ptr) == Struct
        out_type = t1.ptr.get_field_type(expression.field.name)
        offset = t1.ptr.get_field_offset(expression.field.name)
        target = [get_temp() for _ in range(out_type.size)]
        used_temps.extend(target)
        code += f'scoreboard players operation $index {NAMESPACE} = {tt1[0]} {NAMESPACE}\n'
        code += f'scoreboard players add $index {NAMESPACE} {offset}\n'
        for t in target:
            code += f'function {NAMESPACE}:get_heap\n'
            code += f'scoreboard players operation {t} {NAMESPACE} = $value {NAMESPACE}\n'
            code += f'scoreboard players add $index {NAMESPACE} 1\n'
        return code, out_type, target
    elif cname(expression) == 'EmptyStatement':
        return '# empty statement lol\n', Void(), []
    print(expression, ignore_output)
    raise NotImplementedError(cname(expression))