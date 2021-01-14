from c_pointer import Pointer
from c_struct import Struct
from temps import get_temp, used_temps


def assignment_target(target, vtypes, variables_name):
    from globals_consts import cname, BinaryOp, NAMESPACE
    from expression import generate_expression
    if cname(target) == 'ID':
        return '', variables_name[target.name], '', vtypes[target.name]
    elif cname(target) == 'ArrayRef':
        code = ''
        c, t, out = generate_expression(None, BinaryOp('+', target.name, target.subscript), vtypes, variables_name,
                                        False, False)
        if cname(t) != 'Pointer' or len(out) != 1:
            raise NotImplementedError(target)
        outtargs = [get_temp() for _ in range(t.ptr.size)]
        used_temps.extend(outtargs)
        code += c
        code += f'scoreboard players operation $index {NAMESPACE} = {out[0]} {NAMESPACE}\n'
        for target in outtargs:
            code += f'scoreboard players operation $value {NAMESPACE} = {target} {NAMESPACE}\n'
            code += f'function {NAMESPACE}:set_heap\n'
            code += f'scoreboard players add $index {NAMESPACE} 1\n'
        for tt in out: used_temps.remove(tt)
        return '', outtargs, code, t.ptr
    elif cname(target) == 'UnaryOp':
        if target.op == '*':
            code = ''
            c, t, out = generate_expression(None, target.expr, vtypes, variables_name,
                                            False, False)
            outtargs = [get_temp() for _ in range(t.ptr.size)]
            used_temps.extend(outtargs)
            if cname(t) != 'Pointer' or len(out) != 1:
                raise NotImplementedError(target)
            code += c
            code += f'scoreboard players operation $index {NAMESPACE} = {out[0]} {NAMESPACE}\n'
            for target in outtargs:
                code += f'scoreboard players operation $value {NAMESPACE} = {target} {NAMESPACE}\n'
                code += f'function {NAMESPACE}:set_heap\n'
                code += f'scoreboard players add $index {NAMESPACE} 1\n'
            for tt in out: used_temps.remove(tt)
            return '', outtargs, code, t.ptr
    elif cname(target) == 'StructRef':
        assert target.type == '->'
        c1, t1, tt1 = generate_expression(None, target.name, vtypes, variables_name, False, False)
        code = ''
        code += c1
        for t in tt1: used_temps.remove(t)
        assert type(t1) == Pointer
        assert type(t1.ptr) == Struct
        out_type = t1.ptr.get_field_type(target.field.name)
        offset = t1.ptr.get_field_offset(target.field.name)
        target = [get_temp() for _ in range(out_type.size)]
        used_temps.extend(target)
        code += f'scoreboard players operation $index {NAMESPACE} = {tt1[0]} {NAMESPACE}\n'
        code += f'scoreboard players add $index {NAMESPACE} {offset}\n'
        for t in target:
            code += f'scoreboard players operation $value {NAMESPACE} = {t} {NAMESPACE}\n'
            code += f'function {NAMESPACE}:set_heap\n'
            code += f'scoreboard players add $index {NAMESPACE} 1\n'

        return '', target, code, out_type
    print(target)
    raise NotImplementedError(cname(target))
