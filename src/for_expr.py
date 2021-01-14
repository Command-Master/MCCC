from c_void import Void
from globals_consts import NAMESPACE
from temps import used_temps, get_temp_func


def for_expression(copy_strings, expression, target, variables_name, vtypes):
    from expression import generate_expression
    code = ''
    if expression.init is not None:
        c1, t1, tt1 = generate_expression([], expression.init, vtypes, variables_name, copy_strings, True)
        code += c1
        for ttt in tt1: used_temps.remove(ttt)
    temp_name = get_temp_func()
    code += f'function {NAMESPACE}:{temp_name}\n'
    new = open(f'{temp_name}.mcfunction', 'w')
    a, b, c = generate_expression([], expression.stmt, vtypes, variables_name, copy_strings, True)
    for t in c: used_temps.remove(t)
    if expression.cond is not None:
        nc, nt, temps = generate_expression(None, expression.cond, vtypes, variables_name, copy_strings, False)
        new.write(nc)
        t2 = get_temp_func()
        new.write(
            f'execute unless score {temps[0]} {NAMESPACE} matches 0 if score $broken {NAMESPACE} matches 0 run function {NAMESPACE}:{t2}\n')
        new.write(
            f'execute unless score {temps[0]} {NAMESPACE} matches 0 if score $returned {NAMESPACE} matches 0 if score $broken {NAMESPACE} matches 0 run function {NAMESPACE}:{temp_name}\n')
        for temp in temps: used_temps.remove(temp)
        f2 = open(f'{t2}.mcfunction', 'w')
        f2.write(a)
        if expression.next is not None:
            a, b, c = generate_expression(None, expression.next, vtypes, variables_name, copy_strings, True)
            for t in c: used_temps.remove(t)
            f2.write(a)
        f2.close()
    else:
        new.write(a)
        if expression.next is not None:
            a, b, c = generate_expression(None, expression.next, vtypes, variables_name, copy_strings, True)
            for t in c: used_temps.remove(t)
            new.write(a)
        new.write(f'execute if score $broken {NAMESPACE} matches 0 run function {NAMESPACE}:{temp_name}\n')
    new.close()
    if target is None:
        target = []
    code += f'scoreboard players set $broken {NAMESPACE} 0\n'
    return code, Void(), target