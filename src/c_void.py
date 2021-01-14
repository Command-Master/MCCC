class Void:
    size = 0

    def cast(self, ot, itemps, otemps):
        assert type(ot) == Void, f'{ot} != void'
        return ''
        # raise NotImplementedError()

    def update(self, _): pass