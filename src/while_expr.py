from c_int import Int
from c_void import Void
from globals_consts import NAMESPACE
from temps import get_temp, used_temps, get_temp_func


def while_expression(copy_strings, expression, target, variables_name, vtypes):
    from expression import generate_expression
    code = ''
    c1, t1, tt1 = generate_expression(None, expression.cond, vtypes, variables_name, copy_strings, False)
    code += c1
    tv = get_temp()
    used_temps.append(tv)
    code += t1.cast(Int(), tt1, [tv])
    loop = get_temp_func()
    loop_f = open(f'{loop}.mcfunction', 'w')
    if_true = get_temp_func()
    if_true_f = open(f'{if_true}.mcfunction', 'w')
    c2, t2, tt2 = generate_expression(None, expression.stmt, vtypes, variables_name, copy_strings, True)
    if_true_f.write(c2)
    if_true_f.write(f'function {NAMESPACE}:{loop}\n')
    if_true_f.close()
    code += f'execute unless score {tv} {NAMESPACE} matches 0 if score $returned {NAMESPACE} matches 0 if score $broken {NAMESPACE} matches 0 run function {NAMESPACE}:{if_true}\n'
    loop_f.write(code)
    loop_f.close()
    used_temps.remove(tv)
    for ttt in tt1: used_temps.remove(ttt)
    for ttt in tt2: used_temps.remove(ttt)
    return f'function {NAMESPACE}:{loop}\n' \
           f'scoreboard players set $broken {NAMESPACE} 0\n', Void(), target