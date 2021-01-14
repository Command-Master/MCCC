import tree_gen
from globals_consts import NAMESPACE
from temps import gtemps


def generate_trees():
    def callback(val):
        if val == 0:
            return f'scoreboard players add $count {NAMESPACE} 8'  # stupid bin(0) = 0b0
        else:
            return f'scoreboard players add $count {NAMESPACE} {10 - len(bin(val))}'

    tree_gen.generate(0, 255, NAMESPACE, callback, NAMESPACE, 'tree/count_leading_zeros_8', score='$a')

    def callback(val):
        if val == 0:
            return f'execute store result storage {NAMESPACE}:main temp double {"%.100f" % 2 ** -149}' \
                   f' run scoreboard players get $sig {NAMESPACE}\n'  # denormalized numbers are annoying and shall die
        else:
            return f'execute store result storage {NAMESPACE}:main temp double {"%.100f" % 2 ** (val - 150)} run' \
                   f' scoreboard players add $sig {NAMESPACE} 8388608\n'

    tree_gen.generate(0, 255, NAMESPACE, callback, NAMESPACE, 'tree/scale_float', score='$exp')
    callback = lambda val: f'data modify storage {NAMESPACE}:main heap[{val}].selected set value 1\n'
    tree_gen.generate(0, 1023, NAMESPACE, callback, NAMESPACE, 'tree/heap_select', score='$search1')
    callback = lambda \
            val: f'execute store result score $value {NAMESPACE} run' \
                 f' data get storage {NAMESPACE}:main heap[{{selected:1}}].value[{val}]\n'
    tree_gen.generate(0, 1023, NAMESPACE, callback, NAMESPACE, 'tree/heap_get', score='$search2')
    callback = lambda \
            val: f'execute store result storage {NAMESPACE}:main heap[{{selected:1}}].value[{val}] int 1 run' \
                 f' scoreboard players get $value {NAMESPACE}\n'
    tree_gen.generate(0, 1023, NAMESPACE, callback, NAMESPACE, 'tree/heap_set', score='$search2')
    callback = lambda val: f'data modify storage {NAMESPACE}:main alloc[{val}].selected set value 1\n'
    tree_gen.generate(0, 1023, NAMESPACE, callback, NAMESPACE, 'tree/alloc_select', score='$search1')
    callback = lambda \
            val: f'execute store result score $value {NAMESPACE} run' \
                 f' data get storage {NAMESPACE}:main alloc[{{selected:1}}].value[{val}]\n'
    tree_gen.generate(0, 1023, NAMESPACE, callback, NAMESPACE, 'tree/alloc_get', score='$search2')
    callback = lambda \
            val: f'execute store result storage {NAMESPACE}:main alloc[{{selected:1}}].value[{val}] int 1 run' \
                 f' scoreboard players get $value {NAMESPACE}\n'
    tree_gen.generate(0, 1023, NAMESPACE, callback, NAMESPACE, 'tree/alloc_set', score='$search2')
    callback = lambda val: f'data modify storage {NAMESPACE}:main alloc[{val}].used set value 1\n'
    tree_gen.generate(0, 1023, NAMESPACE, callback, NAMESPACE, 'tree/mark_used', score='$r0')
    callback = lambda val: f'data modify storage {NAMESPACE}:main alloc[{val - 536870912 // 1024}].used set value 0\n'
    tree_gen.generate(536870912 // 1024, 536870912 // 1024 + 1023, NAMESPACE, callback, NAMESPACE, 'tree/free',
                      score='$index', scale=1024)
    callback = lambda \
            val: f'data modify storage {NAMESPACE}:main ibuffer append value {repr(chr(val))}'
    tree_gen.generate(32, 126, NAMESPACE, callback, NAMESPACE, 'tree/putc', score='$value')
    callback = lambda val: f'scoreboard players set $p2 {NAMESPACE} {2 ** val}'
    tree_gen.generate(0, 30, NAMESPACE, callback, NAMESPACE, 'tree/power_of_two', score='$2p')
    callback = lambda val: f'scoreboard players operation $value {NAMESPACE} = {gtemps[val - 2 ** 30]} {NAMESPACE}'
    tree_gen.generate(2 ** 30, 2 ** 30 + len(gtemps) - 1, NAMESPACE, callback, NAMESPACE, 'tree/var_get',
                      score='$index')
    callback = lambda val: f'scoreboard players operation {gtemps[val - 2 ** 30]} {NAMESPACE} = $value {NAMESPACE}'
    tree_gen.generate(2 ** 30, 2 ** 30 + len(gtemps) - 1, NAMESPACE, callback, NAMESPACE, 'tree/var_set',
                      score='$index')
    callback = lambda val: f'scoreboard players operation $value {NAMESPACE} = $l{val} {NAMESPACE}'
    tree_gen.generate(0, 63, NAMESPACE, callback, NAMESPACE, 'tree/local_get',
                      score='$search2')
    callback = lambda val: f'scoreboard players operation $l{val} {NAMESPACE} = $value {NAMESPACE}'
    tree_gen.generate(0, 63, NAMESPACE, callback, NAMESPACE, 'tree/local_set',
                      score='$search2')
    callback = lambda val: f'data modify storage {NAMESPACE}:main templ set from storage {NAMESPACE}:main lstack[{val}]'
    tree_gen.generate(0, 1023, NAMESPACE, callback, NAMESPACE, 'tree/local_copy',
                      score='$search1', scale=1024)
    callback = lambda \
            val: f'execute store result score $value {NAMESPACE} run data get storage {NAMESPACE}:main templ[{val}]\n'
    tree_gen.generate(0, 63, NAMESPACE, callback, NAMESPACE, 'tree/templ_get', score='$search2')
    callback = lambda \
            val: f'execute store result storage {NAMESPACE}:main templ[{val}] int 1 run scoreboard players get $value {NAMESPACE}\n'
    tree_gen.generate(0, 63, NAMESPACE, callback, NAMESPACE, 'tree/templ_set', score='$search2')
    callback = lambda val: f'data modify storage {NAMESPACE}:main lstack[{val}] set from storage {NAMESPACE}:main templ'
    tree_gen.generate(0, 1023, NAMESPACE, callback, NAMESPACE, 'tree/local_paste',
                      score='$search1', scale=1024)