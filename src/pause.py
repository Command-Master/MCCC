import os
from globals_consts import NAMESPACE
from tree_gen import generate

from typing import List

tid = 1


def make_pausable(cur):
    global tid
    prev = set()
    while prev != cur:
        prev = cur.copy()
        for file in os.listdir('.'):
            if file in ['main.mcfunction']: continue
            if os.path.isdir(file): continue
            content = open(file).read()
            m = False
            for c in cur:
                if f'function {NAMESPACE}:{c}' in content:
                    m = True
                    break
            if m:
                cur.add(file[:-len('.mcfunction')])
    for file in os.listdir('.'):
        if file == 'main.mcfunction': continue  # splitn'nt main
        if os.path.isdir(file): continue
        content = [open(file).read()]
        for c in cur:
            newc = []
            for cc in content:
                b = cc.split(f'function {NAMESPACE}:{c}')
                for a in b[:-1]:
                    newc.append(a + f'function {NAMESPACE}:{c}')
                newc.append(b[-1])
            content = newc
        content = list(filter(lambda a: a != '', map(lambda a: a.strip(), content)))
        nf = False
        for c in content[:-1]:
            cid = tid
            tid += 1
            arr: List[str] = c.split('\n')
            if nf:
                arr = [f'data remove storage {NAMESPACE}:main rec[-1]'] + arr
            arr.insert(-1, f'data modify storage {NAMESPACE}:main rec append value {cid}')
            arr.append(f'function {NAMESPACE}:t{cid}')
            open(file, 'w').write('\n'.join(arr))
            file = f't{cid}.mcfunction'
            nf = True
        open(file, 'w').write((f'data remove storage {NAMESPACE}:main rec[-1]\n' if nf else '') + content[-1])

    def callback(a):
        return f'function {NAMESPACE}:t{a}\n' \
               f'scoreboard players set $rectemp {NAMESPACE} {a}' # to prevent breaking the tree

    generate(1, tid, NAMESPACE, callback, NAMESPACE, 'tree/recover', score='$rectemp')