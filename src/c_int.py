from globals_consts import NAMESPACE, cname
from c_double import Double


class Int:
    size = 1

    def cast(self, ot, itemps, otemps):
        if type(ot) == Int:
            return f'scoreboard players operation {otemps[0]} {NAMESPACE} = {itemps[0]} {NAMESPACE}\n'
        if cname(ot) == 'Pointer':
            return f'scoreboard players operation {otemps[0]} {NAMESPACE} = {itemps[0]} {NAMESPACE}\nscoreboard players operation {otemps[0]} {NAMESPACE} *= ${ot.ptr.size} {NAMESPACE}\n'
        code = ''
        if cname(ot) == 'Complex':
            ot = Double()  # hahaha they ar ethe same!
            code += f'scoreboard players set {otemps[1]} {NAMESPACE} 0\n'  # 0i
        if type(ot) == Double:
            # a hhahahah now i need to think!!! ):
            code += f'execute store result score $sign {NAMESPACE} if score {itemps[0]} {NAMESPACE} matches ..-1\n'
            code += f'execute if score {itemps[0]} {NAMESPACE} matches 0 run scoreboard players set {otemps[0]} {NAMESPACE} 0\n'  # * 1325400064
            code += f'execute if score {itemps[0]} {NAMESPACE} matches -2147483648 run scoreboard players set {otemps[0]} {NAMESPACE} -1325400064\n'  # * 1325400064
            code += f'scoreboard players operation $sig {NAMESPACE} = {itemps[0]} {NAMESPACE}\n'
            code += f'execute if score $sign {NAMESPACE} matches 1 run scoreboard players operation $sig {NAMESPACE} *= $-1 {NAMESPACE}\n'
            code += f'scoreboard players set $exp {NAMESPACE} 156\n'
            code += f'function {NAMESPACE}:norm_round_pack\n'
            code += f'scoreboard players operation {otemps[0]} {NAMESPACE} = $out {NAMESPACE}\n'
            return code
        print(ot, itemps, otemps)
        raise NotImplementedError(ot)

    def binary(self, op, in1, in2, oval):  # in1 op= in2
        in1 = in1[0]
        in2 = in2[0]
        oval = oval[0]
        if op in ['>', '<', '>=', '<=']:
            return f'execute store result score {oval} {NAMESPACE} if score {in1} {NAMESPACE} {op} {in2} {NAMESPACE}\n'
        if op == '==':
            return f'execute store result score {oval} {NAMESPACE} if score {in1} {NAMESPACE} = {in2} {NAMESPACE}\n'
        if op == '!=':
            return f'execute store result score {oval} {NAMESPACE} unless score {in1} {NAMESPACE} = {in2} {NAMESPACE}\n'
        if op in ['+', '-', '*', '/', '%']:
            return f'scoreboard players operation $temp {NAMESPACE} = {in1} {NAMESPACE}\n' \
                   f'scoreboard players operation $temp {NAMESPACE} {op}= {in2} {NAMESPACE}\n' \
                   f'scoreboard players operation {oval} {NAMESPACE} = $temp {NAMESPACE}\n'
        # if op == '&&':
        #     return f'execute unless score {in1} {NAMESPACE} matches 0 run scoreboard players operation {oval} {NAMESPACE} = {in2} {NAMESPACE}\n'
        else:
            raise NotImplementedError(op)

    def negate(self, temp):
        return f'scoreboard players operation {temp[0]} {NAMESPACE} *= $-1 {NAMESPACE}\n'

    def get_value(self, val, ot):
        return f'scoreboard players set {ot[0]} {NAMESPACE} {val}\n'

    def update(self, _):
        pass