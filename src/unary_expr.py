from assignment_target import assignment_target
from c_pointer import Pointer
from globals_consts import NAMESPACE
from locals import local_size
from temps import get_temp, used_temps, gtemps


def address_unary(expression, variables_name, vtypes):
    tv = get_temp()
    used_temps.append(tv)
    start_addr = variables_name[expression.expr.name][0]
    if start_addr in gtemps:
        i = 2 ** 30 + gtemps.index(start_addr)
        return f'scoreboard players set {tv} {NAMESPACE} {i}\n', Pointer(vtypes[expression.expr.name]), [tv]
    else:
        assert start_addr.startswith('$l')
        li = int(start_addr[2:])
        assert li < local_size(), 'Trying to address bad thing'
        i = 2 ** 30 + 2 ** 29 + li
        code = f'scoreboard players set {tv} {NAMESPACE} {i}\n'
        code += f'scoreboard players operation {tv} {NAMESPACE} += $stackSize {NAMESPACE}\n'
        return code, Pointer(vtypes[expression.expr.name]), [tv]


def dereference_unary(copy_strings, expression, variables_name, vtypes):
    from expression import generate_expression
    c1, t1, tt1 = generate_expression(None, expression.expr, vtypes, variables_name, copy_strings, False)
    code = c1
    assert type(t1) == Pointer
    code += f'scoreboard players operation $index {NAMESPACE} = {tt1[0]} {NAMESPACE}\n'
    targets = [get_temp() for _ in range(t1.ptr.size)]
    used_temps.extend(targets)
    for ttt in tt1: used_temps.remove(ttt)
    for t in targets:
        code += f'function {NAMESPACE}:get_heap\n'
        code += f'scoreboard players operation {t} {NAMESPACE} = $value {NAMESPACE}\n'
        code += f'scoreboard players add $index {NAMESPACE} 1\n'
    return code, t1.ptr, targets


def operator_unary(copy_strings, expression, variables_name, vtypes, op, pre):
    from expression import generate_expression
    code = ''
    c1, t1, tt1 = generate_expression(None, expression.expr, vtypes, variables_name, copy_strings, False)
    code += c1
    start, targets, end, out_type = assignment_target(expression.expr, vtypes, variables_name)
    if end != '':
        for ttt in targets:
            if ttt in used_temps:
                used_temps.remove(ttt)
    code += start
    c2 = out_type.get_value(1, targets)
    code += c2
    code += out_type.binary(op, tt1, targets, targets)
    code += end
    if not pre:
        for t1, t2 in zip(targets, tt1):
            code += f'scoreboard players operation {t2} {NAMESPACE} = {t1} {NAMESPACE}\n'
    return code, out_type, tt1