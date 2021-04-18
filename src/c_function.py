from globals_consts import NAMESPACE, cname

class Function:
    size = 1

    def cast(self):
        raise NotImplementedError('liken\'t cast function pointers')

    def __init__(self, args, ret_type):
        self.args = args
        self.ret_type = ret_type