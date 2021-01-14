import struct

from globals_consts import NAMESPACE, cname


class Double:
    size = 1

    def cast(self, ot, itemps, otemps):
        if type(ot) == Double:
            return f'scoreboard players operation {otemps[0]} {NAMESPACE} = {itemps[0]} {NAMESPACE}\n'
        if cname(ot) == 'Int':
            return f'scoreboard players operation $val {NAMESPACE} = {itemps[0]} {NAMESPACE}\nfunction {NAMESPACE}:f2i\nscoreboard players operation {otemps[0]} {NAMESPACE} = $out {NAMESPACE}\n'
        if cname(ot) == 'Pointer':
            return f'scoreboard players operation $val {NAMESPACE} = {itemps[0]} {NAMESPACE}\nfunction {NAMESPACE}:f2i\nscoreboard players operation {otemps[0]} {NAMESPACE} = $out {NAMESPACE}\nscoreboard players operation {otemps[0]} {NAMESPACE} *= ${ot.ptr.size} {NAMESPACE}\n'
        if cname(ot) == 'Complex':
            return f'scoreboard players operation {otemps[0]} {NAMESPACE} = {itemps[0]} {NAMESPACE}\nscoreboard players set {otemps[1]} {NAMESPACE} 0\n'
        raise NotImplementedError(ot)

    def binary(self, op, in1, in2, oval):
        if op == '==':
            return f'execute store result score {oval} {NAMESPACE} if score {in1[0]} {NAMESPACE} = {in2[0]} {NAMESPACE}\n'
        if op == '+':
            code = ''
            code += f'scoreboard players operation $aval {NAMESPACE} = {in1[0]} {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} = {in2[0]} {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_add\n'
            code += f'scoreboard players operation {oval[0]} {NAMESPACE} = $out {NAMESPACE}\n'
            return code
        if op == '-':
            code = ''
            code += f'scoreboard players operation $aval {NAMESPACE} = {in1[0]} {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} = {in2[0]} {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} += $-inf {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_add\n'
            code += f'scoreboard players operation {oval[0]} {NAMESPACE} = $out {NAMESPACE}\n'
            return code
        if op == '*':
            code = ''
            code += f'scoreboard players operation $aval {NAMESPACE} = {in1[0]} {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} = {in2[0]} {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_mul\n'
            code += f'scoreboard players operation {oval[0]} {NAMESPACE} = $out {NAMESPACE}\n'
            return code
        if op == '/':
            code = ''
            code += f'scoreboard players operation $aval {NAMESPACE} = {in2[0]} {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_inv\n'
            code += f'scoreboard players operation $aval {NAMESPACE} = $out {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} = {in1[0]} {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_mul\n'
            code += f'scoreboard players operation {oval[0]} {NAMESPACE} = $out {NAMESPACE}\n'
            return code
        if op == '<':
            code = ''
            code += f'scoreboard players set $out {NAMESPACE} -1\n'
            a = in1[0]
            b = in2[0]
            code += f'execute store result score $signa {NAMESPACE} if score {a} {NAMESPACE} matches ..-1\n'
            code += f'execute store result score $signb {NAMESPACE} if score {b} {NAMESPACE} matches ..-1\n'
            code += f'execute unless score $signa {NAMESPACE} = $signb {NAMESPACE} run scoreboard players operation $out {NAMESPACE} = $signa {NAMESPACE}\n'
            code += f'execute if score {a} {NAMESPACE} = {b} {NAMESPACE} run scoreboard players set $out 0\n'
            code += f'execute if score $out {NAMESPACE} matches -1 store result score $out {NAMESPACE} if score {a} {NAMESPACE} < {b} {NAMESPACE}\n'
            # code += f'execute if score $temp {NAMESPACE} matches 1 if score $signa {NAMESPACE} matches 1 store result score $out {NAMESPACE} if score $out {NAMESPACE} matches 0\n'
            code += f'scoreboard players operation {oval[0]} {NAMESPACE} = $out {NAMESPACE}\n'
            return code
        print(op)
        raise NotImplementedError()

    def negate(self, temp):
        return f'scoreboard players operation {temp[0]} {NAMESPACE} += $-inf {NAMESPACE}\n'

    def get_value(self, val, ot):
        a = struct.unpack('<I', struct.pack('<f', val))[0]
        return f'scoreboard players set {ot[0]} {NAMESPACE} {a}\n'

    def update(self, _):
        pass