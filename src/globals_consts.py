from collections import namedtuple
NAMESPACE = 'mccc'
cname = lambda x: type(x).__name__
return_types = {}
arguments = {}
BinaryOp = namedtuple('BinaryOp', ['op', 'left', 'right'])