from collections import OrderedDict

from globals_consts import cname


class Struct:
    def __init__(self, values):
        self.size = sum(map(lambda x: x.size, values.values()))
        self.values = OrderedDict(values)  # need consistent order

    def update(self, types):
        for val in self.values:
            if cname(self.values[val]) == 'str':
                self.values[val] = types[val]
            else:
                self.values[val].update(types)

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