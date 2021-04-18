import json
import pathlib
import argparse
import os
import subprocess
import shutil

from pycparser import CParser

from casting import get_type, update_types, add_type, parse_arguments
from pause import make_pausable
from globals_consts import NAMESPACE, cname, return_types, arguments
from expression import generate_expression
from function_trees import generate_trees
from goto import goto_postprocess
from optimizations import remove_zerolines, inline_oneline, remove_unused
from temps import get_temp, stringss, get_position, register_space, clear_used, gtemps, new_cid
from locals import set_rtype, create_local, reset_locals

HEAP_SIZE = 2 ** 20


def main():
    argparser = argparse.ArgumentParser(description='Compile C to a Minecraft datapack')
    argparser.add_argument('file', metavar='Cfile', type=pathlib.Path, help='Path to the C file')
    argparser.add_argument('target', metavar='target', type=pathlib.Path, help='Location to write functions in')
    argparser.add_argument('--preprop', dest='preprop', action='store_const', const=True, default=False,
                           help='Don\'t run the C preprocessor on the file')
    argparser.add_argument('--file-input', help='Take constant input from file', dest='finput', metavar='file',
                           default=False, type=pathlib.Path)
    program_args = argparser.parse_args()
    if program_args.preprop:
        preprocessed = open(program_args.file).read()
    else:
        preprocessed = subprocess.check_output(
            ['gcc', '-nostdinc', '-E', program_args.file, f'-I{os.path.dirname(os.path.abspath(__file__))}/libc']).decode()
    print(program_args.target)
    if program_args.finput:
        inp = list(reversed(program_args.finput.open('rb').read()))
    try:
        shutil.rmtree(program_args.target / 'functions')
    except IOError:
        pass
    os.mkdir(program_args.target / 'functions')
    os.mkdir(program_args.target / 'functions' / 'tree')
    copy_stdlib(program_args.target / 'functions')
    os.chdir(program_args.target / 'functions')
    parser = CParser()
    parsed = parser.parse(preprocessed)
    obj_name = {}
    vtypes = {}
    vars = {}
    methods = {}
    for global_definition in parsed.ext:
        if cname(global_definition) == 'Typedef':
            add_type(global_definition.name, get_type(global_definition.type, obj_name, vtypes))
        elif cname(global_definition) == 'Decl' and cname(global_definition.type) != 'FuncDecl':
            vars[global_definition.name] = global_definition
            global varaddr
        elif cname(global_definition) == 'Decl' and cname(global_definition.type) == 'FuncDecl':
            return_types[global_definition.name] = get_type(global_definition.type.type)
            arguments[global_definition.name] = parse_arguments(global_definition.type.args)
        elif cname(global_definition) == 'FuncDef':
            return_types[global_definition.decl.name] = get_type(global_definition.decl.type.type)
            arguments[global_definition.decl.name] = parse_arguments(global_definition.decl.type.args)
            # print(functions)
            methods[global_definition.decl.name] = global_definition
        else:
            print(cname(global_definition))
    update_types()
    file = open('main.mcfunction', 'w')
    file.write(generate_head(vars, obj_name, vtypes))
    for method in methods:
        f = open(f'method_{method.lower()}.mcfunction', 'w')
        set_rtype(return_types[method])
        args = methods[method].decl.type.args
        if args is None:
            args = []
        clear_used()
        reset_locals()
        j = 0
        for arg in args:
            if cname(arg) == 'EllipsisParam':
                j += 10
                for i in range(10): create_local()
                break
            var_type = arg.type
            vtypes[arg.name] = get_type(var_type)
            obj_name[arg.name] = [create_local() for i in range(get_type(arg.type).size)]
            j += vtypes[arg.name].size
        new_cid()
        f.write(generate_expression([], methods[method].body, vtypes, obj_name, False, True)[0])
        f.write(f'scoreboard players set $returned {NAMESPACE} 0')
        f.close()
    generate_trees()
    if program_args.finput:
        file.write(f'data modify storage {NAMESPACE}:main input set value {inp}\n')
    file.write(f'data modify storage {NAMESPACE}:main rec set value []\n')
    file.write(f'data modify storage {NAMESPACE}:main ibuffer set value []\n')

    for strg in stringss:
        for i, c in enumerate(stringss[strg]):
            # TODO: change it to direct access to the heap, as index is known in compile time.
            file.write(f'scoreboard players set $index {NAMESPACE} {strg + i}\n')
            file.write(f'scoreboard players set $value {NAMESPACE} {c}\n')
            file.write(f'function {NAMESPACE}:set_heap\n')
    file.write(f'function {NAMESPACE}:method_main\n')
    file.close()
    goto_postprocess()
    remove_zerolines()
    inline_oneline()
    make_pausable({'method_getc', 'method__get_setjmp'})
    remove_unused()


def copy_stdlib(loc):
    stdlib_address = '/'.join(os.path.split(__file__)[:-1] + ("stdlib",))
    for file in os.listdir(stdlib_address):
        f1 = open(stdlib_address + '/' + file, 'r')
        f2 = open(loc / file, 'w')
        c = f1.read()

        f2.write(c.replace('namespace', NAMESPACE))
        f1.close()
        f2.close()


def init_heap(size):
    a = int(size ** 0.5)
    b = size // a
    assert a * b == size, f'{size} isn\'t a prefect square'  # otherwise we need to do factorization and it might
    # result in sub-optimal results
    thing = [{'value': [0] * b, 'selected': 0}] * a
    thing2 = [{'value': [0] * 1024, 'selected': 0, 'used': 0, 'index': i} for i in range(1024)]
    return f'data modify storage {NAMESPACE}:main heap set value {json.dumps(thing)}\n' \
           f'data modify storage {NAMESPACE}:main alloc set value {json.dumps(thing2)}\n'


def generate_head(vars, store, vtypes):
    code = ''
    code += f'gamerule maxCommandChainLength 200000\n'
    code += f'scoreboard objectives add {NAMESPACE} dummy\n' \
            f'scoreboard players set $-1 {NAMESPACE} -1\n'
    code += f'scoreboard players set $65536 {NAMESPACE} 65536\n'
    code += f'scoreboard players set $256 {NAMESPACE} 256\n'
    code += f'scoreboard players set $128 {NAMESPACE} 128\n'
    code += f'scoreboard players set $64 {NAMESPACE} 64\n'
    code += f'data modify storage {NAMESPACE}:main temps set value []\n'
    code += f'data modify storage {NAMESPACE}:main setjmp set value []\n'
    code += f'scoreboard players set $32 {NAMESPACE} 32\n'
    code += f'scoreboard players set $2 {NAMESPACE} 2\n'
    code += f'scoreboard players set $3 {NAMESPACE} 3\n'
    code += f'scoreboard players set $7 {NAMESPACE} 7\n'
    code += f'scoreboard players set $5 {NAMESPACE} 5\n'
    code += f'scoreboard players set $6 {NAMESPACE} 6\n'
    code += f'scoreboard players set $4 {NAMESPACE} 4\n'
    code += f'scoreboard players set $8 {NAMESPACE} 8\n'
    code += f'scoreboard players set $stackSize {NAMESPACE} 0\n'  # NOTE: multiplied by 1024
    code += f'data modify storage {NAMESPACE}:main lstack set value []\n'
    code += f'scoreboard players set $1 {NAMESPACE} 1\n'
    code += f'scoreboard players set $1024 {NAMESPACE} 1024\n'
    code += f'scoreboard players set $1073741824 {NAMESPACE} 1073741824\n'
    code += f'scoreboard players set $16777216 {NAMESPACE} 16777216\n'
    code += f'scoreboard players set $8388608 {NAMESPACE} 8388608\n'
    code += f'scoreboard players set $-inf {NAMESPACE} -2147483648\n'
    code += f'scoreboard players set $returned {NAMESPACE} 0\n'
    code += f'scoreboard players set $broken {NAMESPACE} 0\n'
    code += f'scoreboard players set $lasta {NAMESPACE} -1\n'
    code += f'scoreboard players set $lastb {NAMESPACE} -1\n'
    code += f'scoreboard players set $setjmpctr {NAMESPACE} -1\n'
    code += f'scoreboard players set $1048576 {NAMESPACE} 1048576\n'
    code += f'scoreboard players set $61681 {NAMESPACE} 61681\n'
    code += f'scoreboard players set $33554432 {NAMESPACE} 33554432\n'
    code += f'scoreboard players set $16777216 {NAMESPACE} 16777216\n'
    code += f'scoreboard players set $134217728 {NAMESPACE} 134217728\n'
    code += f'scoreboard players set $16 {NAMESPACE} 16\n'
    code += f'scoreboard players set $2097152 {NAMESPACE} 2097152\n'
    code += f'scoreboard players set $2048 {NAMESPACE} 2048\n'
    code += f'scoreboard players set $4096 {NAMESPACE} 4096\n'
    code += init_heap(HEAP_SIZE)
    for var_name in vars:
        var = vars[var_name]
        var_type = var.type
        vtypes[var_name] = get_type(var_type)
        store[var_name] = [get_temp() for _ in range(vtypes[var_name].size)]
        gtemps.extend(store[var_name])
        if cname(var_type) == 'ArrayDecl':
            size = int(var_type.dim.value)
            code += f'scoreboard players set {store[var_name][0]} {NAMESPACE} {get_position()}\n'
            register_space(size * vtypes[var_name].ptr.size)
        else:
            for varrr in store[var_name]:
                code += f'scoreboard players set {varrr} {NAMESPACE} 0\n'
    for var_name in vars:
        var = vars[var_name]
        if var.init is not None:
            code += generate_expression(store[var_name], var.init, vtypes, store, True, False)[0]
    return code


if __name__ == '__main__':
    main()
