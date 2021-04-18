from collections import OrderedDict

from globals_consts import cname, NAMESPACE


class Struct:
    def __init__(self, values):
        self.values = OrderedDict(values)  # need consistent order
        self.size = -1

    def cast(self, ot, itemps, otemps):
        assert self == ot
        code = ''
        for t1, t2 in zip(itemps, otemps):
            code += f'scoreboard players operation {t2} {NAMESPACE} = {t1} {NAMESPACE}\n'
        return code

    def update(self, types):
        for val in self.values:
            if cname(self.values[val]) == 'str':
                self.values[val] = types[val]
            else:
                self.values[val].update(types)
        self.size = sum(map(lambda x: x.size, self.values.values()))

    def get_field_type(self, name):
        if name in self.values:
            return self.values[name]
        if name in self.values[None].values:
            return self.values[None].values[name]

    def get_field_offset(self, name):
        if name not in self.values:
            name = None
        s = 0
        for i in self.values:
            if i == name:
                break
            else:
                s += self.values[i].size
        return s