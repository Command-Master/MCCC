from c_complex import Complex
from c_int import Int
from globals_consts import NAMESPACE
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
        out_type = vtypes[expression.name]
        if target is None:
            target = [get_temp() for _ in range(out_type.size)]
            used_temps.extend(target)
        return ''.join(f'scoreboard players operation {a} {NAMESPACE} = {b} {NAMESPACE}\n' for a, b in
                       zip(target, variables_name[expression.name])), out_type, target