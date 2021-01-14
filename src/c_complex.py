import struct

from globals_consts import NAMESPACE
from c_int import Int
from c_double import Double
from c_pointer import Pointer


class Complex:
    size = 2

    def cast(self, ot, itemps, otemps):
        if type(ot) == Complex:
            return f'scoreboard players operation {otemps[0]} {NAMESPACE} = {itemps[0]} {NAMESPACE}\nscoreboard players operation {otemps[1]} {NAMESPACE} = {itemps[1]} {NAMESPACE}\n'
        if type(ot) == Int:
            return Double.cast(None, ot, itemps, otemps)
        if type(ot) == Pointer:
            return Double.cast(None, ot, itemps, otemps)
        print(ot)
        raise NotImplementedError()

    def binary(self, op, in1, in2, oval):
        if op in ['+', '-']:
            return Double.binary(None, op, [in1[0]], [in2[0]], [oval[0]]) + Double.binary(None, op, [in1[1]], [in2[1]],
                                                                                          [oval[0]])
        if op == '*':
            code = ''
            code += f'scoreboard players operation $aval {NAMESPACE} = {in1[0]} {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} = {in2[0]} {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_mul\n'
            code += f'scoreboard players operation $tt1 {NAMESPACE} = $out {NAMESPACE}\n'
            code += f'scoreboard players operation $aval {NAMESPACE} = {in1[1]} {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} = {in2[1]} {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_mul\n'
            code += f'scoreboard players operation $aval {NAMESPACE} = $tt1 {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} = $out {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_sub\n'
            code += f'scoreboard players operation $tt2 {NAMESPACE} = $out {NAMESPACE}\n'
            code += f'scoreboard players operation $aval {NAMESPACE} = {in1[0]} {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} = {in2[1]} {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_mul\n'
            code += f'scoreboard players operation $tt1 {NAMESPACE} = $out {NAMESPACE}\n'
            code += f'scoreboard players operation $aval {NAMESPACE} = {in1[1]} {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} = {in2[0]} {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_mul\n'
            code += f'scoreboard players operation $aval {NAMESPACE} = $tt1 {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} = $out {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_add\n'
            code += f'scoreboard players operation {oval[1]} {NAMESPACE} = $out {NAMESPACE}\n'
            code += f'scoreboard players operation {oval[0]} {NAMESPACE} = $tt2 {NAMESPACE}\n'
            return code
        if op == '/':
            code = ''
            # calculate scale
            code += f'scoreboard players operation $aval {NAMESPACE} = {in1[0]} {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} = {in1[0]} {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_mul\n'
            code += f'scoreboard players operation $val1 {NAMESPACE} = $out {NAMESPACE}\n'
            code += f'scoreboard players operation $aval {NAMESPACE} = {in1[1]} {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} = {in1[1]} {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_mul\n'
            code += f'scoreboard players operation $aval {NAMESPACE} = $out {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} = $val1 {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_add\n'
            code += f'scoreboard players operation $aval {NAMESPACE} = $out {NAMESPACE}\n'
            code += f'tellraw @a ["scale: ", {{"score":{{"name":"$out","objective":"{NAMESPACE}"}}}}]\n'
            code += f'function {NAMESPACE}:float_inv\n'
            code += f'scoreboard players operation $val1 {NAMESPACE} = $out {NAMESPACE}\n'

            code += f'scoreboard players operation $aval {NAMESPACE} = {in1[0]} {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} = {in2[0]} {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_mul\n'
            code += f'scoreboard players operation $tt1 {NAMESPACE} = $out {NAMESPACE}\n'
            code += f'scoreboard players operation $aval {NAMESPACE} = {in1[1]} {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} = {in2[1]} {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_mul\n'
            code += f'scoreboard players operation $aval {NAMESPACE} = $tt1 {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} = $out {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_add\n'
            code += f'scoreboard players operation $aval {NAMESPACE} = $out {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} = $val1 {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_mul\n'
            code += f'scoreboard players operation $tt2 {NAMESPACE} = $out {NAMESPACE}\n'
            # calculate real

            code += f'scoreboard players operation $aval {NAMESPACE} = {in1[0]} {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} = {in2[1]} {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_mul\n'
            code += f'scoreboard players operation $tt1 {NAMESPACE} = $out {NAMESPACE}\n'
            code += f'scoreboard players operation $aval {NAMESPACE} = {in1[1]} {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} = {in2[0]} {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_mul\n'
            code += f'scoreboard players operation $aval {NAMESPACE} = $tt1 {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} = $out {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_sub\n'
            code += f'scoreboard players operation $aval {NAMESPACE} = $out {NAMESPACE}\n'
            code += f'scoreboard players operation $bval {NAMESPACE} = $val1 {NAMESPACE}\n'
            code += f'function {NAMESPACE}:float_mul\n'
            # calculate imag

            code += f'scoreboard players operation {oval[1]} {NAMESPACE} = $out {NAMESPACE}\n'
            code += f'scoreboard players operation {oval[0]} {NAMESPACE} = $tt2 {NAMESPACE}\n'
            # save
            return code
        print(op, in1, in2)
        raise NotImplementedError()

    def get_value(self, val, ot):
        a = struct.unpack('<I', struct.pack('<f', val.real))[0]
        b = struct.unpack('<I', struct.pack('<f', val.imag))[0]
        return f'scoreboard players set {ot[0]} {NAMESPACE} {a}\n' + f'scoreboard players set {ot[1]} {NAMESPACE} {b}\n'

    def update(self, _):
        pass