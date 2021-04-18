from c_complex import Complex
from c_int import Int
from c_pointer import Pointer
from c_function import Function
from globals_consts import return_types, NAMESPACE, arguments as fargs
from temps import get_temp, used_temps


def id_expression(expression, target, variables_name, vtypes):
    if expression.name == 'I':
        out_type = Complex()
        if target is None:
            target = [get_temp() for _ in range(out_type.size)]
            used_temps.extend(target)
        return Complex().get_value(1j, target), Complex(), target
    elif expression.name == 'stdin':
        out_type = Int()
        if target is None:
            target = [get_temp() for _ in range(out_type.size)]
            used_temps.extend(target)
        return f'scoreboard players set {target[0]} {NAMESPACE} 0\n', Int(), target
    else:

        if expression.name in vtypes:
            out_type = vtypes[expression.name]
            out_source = variables_name[expression.name]
        else:
            out_type = Pointer(Function(fargs[expression.name], return_types[expression.name]))
            if target is None:
                target = [get_temp()]
                used_temps.extend(target)
            return f'scoreboard players set {target[0]} {NAMESPACE} {list(return_types).index(expression.name)}\n', out_type, target
        if target is None:
            target = [get_temp() for _ in range(out_type.size)]
            used_temps.extend(target)
        return ''.join(f'scoreboard players operation {a} {NAMESPACE} = {b} {NAMESPACE}\n' for a, b in
                       zip(target, out_source)), out_type, target