from c_double import Double
from c_int import Int
from c_pointer import Pointer
from c_void import Void
from function_stack import save_temps, save_locals, unsave_temps, unsave_locals
from globals_consts import return_types, NAMESPACE
from locals import local_size
from temps import used_temps, get_temp


def funccall_expression(copy_strings, expression, variables_name, vtypes):
    from expression import generate_expression
    arguments = []
    code = ''
    crtype = None
    if expression.name.name == 'getc': crtype = Int()
    if expression.name.name == 'cabs': crtype = Double()
    if expression.name.name in ['calloc', 'malloc']: crtype = Pointer(Int())
    if expression.name.name in ['exit', 'float_print', 'puts', 'putchar', 'int_print', 'free']: crtype = Void()
    if expression.name.name in return_types: crtype = return_types[expression.name.name]
    assert crtype is not None, f'Unknown function {expression.name.name}'
    if expression.args is not None:
        for expr in expression.args.exprs:
            c1, t1, tt1 = generate_expression(None, expr, vtypes, variables_name, copy_strings, False)
            code += c1
            arguments.extend(tt1)
    for arg in arguments: used_temps.remove(arg)
    code += save_temps(used_temps)
    code += save_locals(local_size())
    for i, arg in enumerate(arguments):
        code += f'scoreboard players operation $l{i} {NAMESPACE} = {arg} {NAMESPACE}\n'
    code += f'function {NAMESPACE}:method_{expression.name.name.lower()}\n'
    code += unsave_temps(used_temps)
    code += unsave_locals(local_size())
    targets = [get_temp() for _ in range(crtype.size)]
    used_temps.extend(targets)
    for i, t in enumerate(targets):
        code += f'scoreboard players operation {t} {NAMESPACE} = $r{i} {NAMESPACE}\n'
    return code, crtype, targets