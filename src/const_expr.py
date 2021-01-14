import struct

from c_double import Double
from c_int import Int
from c_pointer import Pointer
from globals_consts import NAMESPACE
from utils import parse_string
from temps import used_temps, get_temp, get_position, register_space, stringss


def parse_double(expression, target):
    dval = float(expression.value)
    if target is None:
        target = [get_temp()]
        used_temps.extend(target)
    ival = struct.unpack('<I', struct.pack('<f', dval))[0]  # hahaha eval struct
    return f'scoreboard players set {target[0]} {NAMESPACE} {ival}\n', Double(), target


def parse_string_const(copy_strings, expression, target):
    if copy_strings:
        a = eval('b' + expression.value)
        code = ''
        a = list(a)
        # + [0] - initalized to 0 anyway, no need to specify this
        code += f'scoreboard players operation $index {NAMESPACE} = {target[0]} {NAMESPACE}\n'
        for co, c in enumerate(a):
            code += f'scoreboard players set $value {NAMESPACE} {c}\n'
            code += f'function {NAMESPACE}:set_heap\n'
            code += f'scoreboard players add $index {NAMESPACE} 1\n'
        return code, Pointer(Int()), target
    else:
        a = parse_string(expression.value).encode()
        # a = eval('b' + expression.value)
        if target is None:
            target = [get_temp()]
            used_temps.extend(target)
        code = f'scoreboard players set {target[0]} {NAMESPACE} {get_position()}\n'
        a = list(a) + [0]
        stringss[get_position()] = a
        register_space(len(a))
        return code, Pointer(Int()), target


def parse_char(expression, target):
    if target is None:
        target = [get_temp()]
        used_temps.extend(target)
    v = parse_string(expression.value)
    return f'scoreboard players set {target[0]} {NAMESPACE} {ord(v)}\n', Int(), target


def parse_int(expression, target):
    if target is None:
        target = [get_temp()]
        used_temps.extend(target)
    v = expression.value
    if v.lower().startswith('0x'):
        v = int(v, 16)
    elif v.startswith('0'):
        v = int(v, 8)
    return f'scoreboard players set {target[0]} {NAMESPACE} {v}\n', Int(), target
