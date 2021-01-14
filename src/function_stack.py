from globals_consts import NAMESPACE


def save_temps(temps):
    if temps:
        code = ''
        code += f'data modify storage {NAMESPACE}:main temp set value {[0] * len(temps)}\n'
        code += f'data modify storage {NAMESPACE}:main temps append from storage {NAMESPACE}:main temp[]\n'
        for i, t in enumerate(temps):
            code += f'execute store result storage {NAMESPACE}:main temps[{-i - 1}] int 1 run scoreboard players get {t} {NAMESPACE}\n'
        return code
    return ''


def unsave_temps(temps):
    if temps:
        code = ''
        for t in temps:
            code += f'execute store result score {t} {NAMESPACE} run data get storage {NAMESPACE}:main temps[-1]\n'
            code += f'data remove storage {NAMESPACE}:main temps[-1]\n'
        return code
    return ''


def save_locals(lSize):
    if lSize != 0:
        code = ''
        code += f'data modify storage {NAMESPACE}:main temp set value {[0] * lSize}\n'
        code += f'scoreboard players add $stackSize {NAMESPACE} 1024\n'
        code += f'data modify storage {NAMESPACE}:main lstack append from storage {NAMESPACE}:main temp\n'
        for i in range(lSize):
            code += f'execute store result storage {NAMESPACE}:main lstack[-1][{i}] int 1 run scoreboard players get $l{i} {NAMESPACE}\n'
        return code
    return ''


def unsave_locals(lSize):
    if lSize != 0:
        code = ''
        for i in range(lSize):
            code += f'execute store result score $l{i} {NAMESPACE} run data get storage {NAMESPACE}:main lstack[-1][{i}]\n'
        code += f'data remove storage {NAMESPACE}:main lstack[-1]\n'
        code += f'scoreboard players remove $stackSize {NAMESPACE} 1024\n'
        return code
    return ''