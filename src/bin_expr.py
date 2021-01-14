from c_int import Int
from casting import cast
from globals_consts import NAMESPACE
from temps import used_temps, get_temp, get_temp_func


def binary_expression(copy_strings, expression, target, variables_name, vtypes):
    from expression import generate_expression
    c1, t1, tt1 = generate_expression(None, expression.left, vtypes, variables_name, copy_strings, False)
    c2, t2, tt2 = generate_expression(None, expression.right, vtypes, variables_name, copy_strings, False)
    for ttt in tt1: used_temps.remove(ttt)
    for ttt in tt2: used_temps.remove(ttt)
    ot = cast(t1, t2)
    rt = ot
    if expression.op in ['<', '>', '<=', '>=', '==', '!=', '&&']:
        rt = Int()
    if target is None or target == []:
        target = [get_temp() for _ in range(ot.size)]
        used_temps.extend(target)
    code = ''
    if expression.op in ['&&', '||']:
        if expression.op == '&&':
            code += c1
            code += t1.cast(ot, tt1, target)
            f2 = get_temp_func()
            f2h = open(f'{f2}.mcfunction', 'w')
            f2h.write(c2)
            f2h.write(t2.cast(ot, tt2, target))
            f2h.close()
            code += f'execute unless score {target[0]} {NAMESPACE} matches 0 run function {NAMESPACE}:{f2}\n'
        elif expression.op == '||':
            code += c1
            code += t1.cast(ot, tt1, target)
            f2 = get_temp_func()
            f2h = open(f'{f2}.mcfunction', 'w')
            f2h.write(c2)
            f2h.write(t2.cast(ot, tt2, target))
            f2h.close()
            code += f'execute if score {target[0]} {NAMESPACE} matches 0 run function {NAMESPACE}:{f2}\n'
    else:
        if ot == t1:
            code += c1
            code += c2
            code += t2.cast(ot, tt2, target)
            code += ot.binary(expression.op, tt1, target, target)
        else:
            code += c1
            code += t1.cast(ot, tt1, target)
            code += c2
            code += ot.binary(expression.op, target, tt2, target)
    return code, rt, target