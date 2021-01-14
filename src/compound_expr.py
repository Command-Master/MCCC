from c_void import Void
from casting import get_type
from globals_consts import cname, NAMESPACE
from temps import used_temps, get_temp_func
from locals import create_local, remove_locals


def compound_expression(copy_strings, expression, target, variables_name, vtypes):
    from expression import generate_expression
    code = ''
    returns = 'Return' in str(expression)  # lolol
    breaks = 'Break' in str(expression)  # lolol
    to_free = []
    clocals = 0
    for e in expression.block_items:
        if cname(e) == 'Decl':
            name = e.name
            ctype = e.type
            vtypes[name] = get_type(ctype)
            cvals = []
            for _ in range(vtypes[name].size):
                cvals.append(create_local())
                clocals += 1
            variables_name[name] = cvals
            if cname(ctype) == 'ArrayDecl':
                alloc_size = int(ctype.dim.value)
                assert alloc_size < 1024, 'Too big local array, make it global!'
                code += f'''data modify storage {NAMESPACE}:main temp set from storage {NAMESPACE}:main alloc[{{used:0}}].index
execute store result score {cvals[0]} {NAMESPACE} run data get storage {NAMESPACE}:main temp
function {NAMESPACE}:tree/mark_used
scoreboard players operation {cvals[0]} {NAMESPACE} *= $1024 {NAMESPACE}
scoreboard players add {cvals[0]} {NAMESPACE} 536870912
'''
                to_free.append(cvals[0])
    if not (returns or breaks):
        for e in expression.block_items:
            c1, t1, tt1 = generate_expression([], e, vtypes, variables_name, copy_strings, True)
            code += c1
            for ttt in tt1:
                used_temps.remove(ttt)
    else:
        for e in expression.block_items:
            cf = get_temp_func()
            cff = open(f'{cf}.mcfunction', 'w')
            c1, t1, tt1 = generate_expression([], e, vtypes, variables_name, copy_strings, True)
            cff.write(c1)
            for ttt in tt1:
                used_temps.remove(ttt)
            code += f'execute if score $returned {NAMESPACE} matches 0 if score $broken {NAMESPACE} matches 0 run function {NAMESPACE}:{cf}\n'
    if target is None:
        target = []
    remove_locals(clocals)
    for tof in to_free:
        code += f'scoreboard players operation $index {NAMESPACE} = {tof} {NAMESPACE}\n'
        code += f'function {NAMESPACE}:tree/free\n'
    return code, Void(), target