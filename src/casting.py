from c_int import Int
from c_pointer import Pointer
from c_struct import Struct
from c_union import Union
from globals_consts import cname
from c_double import Double
from c_complex import Complex
from c_void import Void
from c_function import Function

types = {
    'int': Int(),
    'char': Int(),
    'double': Double(),
    'complex': Complex(),
    'void': Void(),
    'float': Double()
}


def cast(t1, t2):
    t1, t2 = sorted([t1, t2], key=cname)  # hahaha sort go brrr
    tt1, tt2 = cname(t1), cname(t2)
    if tt1 == tt2:
        return t1
    if tt1 == 'Int' and tt2 == 'Pointer':
        return t2
    if tt1 == 'Char' and tt2 == 'Int':
        return t2
    if tt1 == 'Complex' and tt2 == 'Pointer':
        return t2
    if tt1 == 'Complex' and tt2 == 'Double':
        return t1
    if tt1 == 'Double' and tt2 == 'Int':
        return t1
    if tt1 == 'Complex' and tt2 == 'Int':
        return t1
    if tt1 == 'Void' or tt2 == 'Void':
        return t1
    raise NotImplementedError(t1, t2)


def get_type(var_type, vs=None, vt=None, allow_unprocessed=False):
    while cname(var_type) == 'Decl': var_type = var_type.type
    if cname(var_type) in ['ArrayDecl', 'PtrDecl']:
        return Pointer(get_type(var_type.type))
    elif cname(var_type) == 'TypeDecl' and cname(var_type.type) == 'IdentifierType':

        name = ' '.join(var_type.type.names)
        if allow_unprocessed and name not in types:
            return name
        return types[name]
    elif cname(var_type) == 'TypeDecl' and cname(var_type.type) == 'Enum':

        for i, val in enumerate(var_type.type.values):
            vt[val.name] = Int()
            vs[val.name] = [f'${i}']
        types[f'enum {var_type.type.name}'] = Int()
        return Int()
    elif cname(var_type) == 'TypeDecl' and cname(var_type.type) == 'Struct':

        if var_type.type.decls is not None:
            things = {}
            for val in var_type.type.decls:
                things[val.name] = get_type(val.type, allow_unprocessed=True)
            ty = Struct(things)
            types[f'struct {var_type.type.name}'] = ty
            return ty
        else:
            return f'struct {var_type.type.name}'
    elif cname(var_type) == 'Union':

        things = {}
        for val in var_type.decls:
            things[val.name] = get_type(val.type, allow_unprocessed=True)
        return Union(things)
    elif cname(var_type) == 'FuncDecl':
        return Function([get_type(x.type) for x in var_type.args.params], get_type(var_type.type))
    print(var_type)
    print(var_type.coord)
    raise NotImplementedError()


def parse_arguments(args):
    if args is None:
        args = []
    return [get_type(a.type) for a in args if cname(a) != 'EllipsisParam']


def update_types():
    for t in types: types[t].update(types)


def add_type(name, type):
    types[name] = type
