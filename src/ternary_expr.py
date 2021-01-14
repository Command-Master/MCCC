from c_int import Int
from casting import cast
from globals_consts import NAMESPACE
from temps import get_temp, used_temps, get_temp_func


def ternary_expression(copy_strings, expression, target, variables_name, vtypes):
    from expression import generate_expression
    code = ''
    c1, t1, tt1 = generate_expression(None, expression.cond, vtypes, variables_name, copy_strings, False)
    code += c1
    tv = get_temp()
    used_temps.append(tv)
    code += t1.cast(Int(), tt1, [tv])
    if_true = get_temp_func()
    if_false = get_temp_func()
    if_true_f = open(f'{if_true}.mcfunction', 'w')
    if_false_f = open(f'{if_false}.mcfunction', 'w')
    c2, t2, tt2 = generate_expression(None, expression.iffalse, vtypes, variables_name, copy_strings,
                                      False)
    c3, t3, tt3 = generate_expression(None, expression.iftrue, vtypes, variables_name, copy_strings,
                                      False)
    ot = cast(t2, t3)
    if target is None:
        target = [get_temp() for _ in range(ot.size)]
        used_temps.extend(target)
    if_true_f.write(c3)
    if len(target) != 0:
        if_true_f.write(t3.cast(ot, tt3, target))
    if_false_f.write(c2)
    if len(target) != 0:
        if_false_f.write(t2.cast(ot, tt2, target))
    if_true_f.close()
    if_false_f.close()
    used_temps.remove(tv)
    for ttt in tt1: used_temps.remove(ttt)
    for ttt in tt2: used_temps.remove(ttt)
    for ttt in tt3: used_temps.remove(ttt)
    code += f'execute if score {tv} {NAMESPACE} matches 0 run function {NAMESPACE}:{if_false}\n'
    code += f'execute unless score {tv} {NAMESPACE} matches 0 run function {NAMESPACE}:{if_true}\n'
    return code, ot, target