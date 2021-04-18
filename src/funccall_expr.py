from function_stack import save_temps, save_locals, unsave_temps, unsave_locals
from globals_consts import return_types, cname, NAMESPACE, arguments as fargs
from locals import local_size
from temps import used_temps, get_temp, get_temp_func

functrees = {}

def funccall_expression(copy_strings, expression, variables_name, vtypes):
    from expression import generate_expression
    arguments = []
    code = ''
    # print(vtypes)
    direct = True
    if expression.name.name in vtypes:
        crtype = vtypes[expression.name.name].ptr.ret_type
        funcargs = vtypes[expression.name.name].ptr.args
        direct = False
    else:
        crtype = return_types[expression.name.name]
        funcargs = fargs[expression.name.name]
    if expression.args is not None:
        for i, expr in enumerate(expression.args.exprs):
            c1, t1, tt1 = generate_expression(None, expr, vtypes, variables_name, copy_strings, False)
            code += c1
            if i < len(funcargs) and cname(funcargs[i]) != cname(t1):
                ctemps = [get_temp() for _ in range(funcargs[i].size)]
                code += t1.cast(funcargs[i], tt1, ctemps)
                arguments.extend(ctemps)
                used_temps.extend(ctemps)
                for arg in tt1:
                    used_temps.remove(arg)
            else:
                arguments.extend(tt1)
    for arg in arguments:
        used_temps.remove(arg)
    code += save_temps(used_temps)
    code += save_locals(local_size())
    for i, arg in enumerate(arguments):
        code += f'scoreboard players operation $l{i} {NAMESPACE} = {arg} {NAMESPACE}\n'
    if direct:
        code += f'function {NAMESPACE}:method_{expression.name.name.lower()}\n'
    else:
        if (crtype, tuple(funcargs)) not in functrees:
            functrees[(crtype, tuple(funcargs))] = get_temp_func()
            possibilities = list(filter(lambda x: return_types[x]==crtype and fargs[x]==funcargs, list(return_types)))
            assert len(possibilities), 'No function of matching type'
            if len(possibilities) == 1:
                functrees[(crtype, tuple(funcargs))] = possibilities[0]
            else:
                code += f'scoreboard players operation $func_id {NAMESPACE} = {variables_name[expression.name.name][0]} {NAMESPACE}\n'
                raise NotImplementedError()
            # print(possibilities)
        # print(return_types, crtype, fargs, funcargs)
        code += f'function {NAMESPACE}:method_{functrees[(crtype, tuple(funcargs))]}\n'
    code += unsave_temps(used_temps)
    code += unsave_locals(local_size())
    targets = [get_temp() for _ in range(crtype.size)]
    used_temps.extend(targets)
    for i, t in enumerate(targets):
        code += f'scoreboard players operation {t} {NAMESPACE} = $r{i} {NAMESPACE}\n'
    return code, crtype, targets
