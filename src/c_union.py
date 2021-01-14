from globals_consts import cname


class Union:
    def __init__(self, values):
        self.size = max(map(lambda x: x.size, values.values()))
        self.values = values

    def update(self, types):
        for val in self.values:
            if cname(self.values[val]) == 'str':
                self.values[val] = types[val]
            else:
                self.values[val].update(types)