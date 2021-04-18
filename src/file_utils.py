import os
from globals_consts import NAMESPACE


def get_callers(function):
    callers = []
    for file in os.listdir('.'):
        if os.path.isdir(file): continue
        # print(f'function {function}')
        if f'function {NAMESPACE}:{function}' in open(file).read():
            callers.append(file[:-len('.mcfunction')])
    return callers