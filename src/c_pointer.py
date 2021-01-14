from globals_consts import NAMESPACE
from c_int import Int


class Pointer:
    size = 1

    def get_value(self, val, ot):
        return f'scoreboard players set {ot[0]} {NAMESPACE} {val}\n'

    def binary(self, op, in1, in2, oval):  # in1 op= in2
        return Int.binary(None, op, in1, in2, oval)

    def __init__(self, pt):
        self.ptr = pt

    def cast(self, ot, itemps, otemps):
        if type(ot) == Pointer:
            return f'scoreboard players operation {otemps[0]} {NAMESPACE} = {itemps[0]} {NAMESPACE}\n'
        return Int.cast(None, ot, itemps, otemps)
        # raise NotImplementedError()

    def update(self, types):
        if type(self.ptr) == str:
            self.ptr = types[self.ptr]