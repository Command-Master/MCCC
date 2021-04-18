import os, re, sys
from globals_consts import NAMESPACE


def remove_zerolines():
    changed = True
    deleted = []
    while changed:
        changed = False
        for file in os.listdir('.'):
            if file == 'main.mcfunction': continue
            if os.path.isdir(file): continue
            content = open(file).read()
            for thing in deleted:
                content = re.sub(rf'.*function {NAMESPACE}:{thing[:-len(".mcfunction")]}', '', content)
            content = re.sub(r'\n{2,}', '\n', content)
            content = content.strip()
            open(file, 'w').write(content)
            if content == '':
                changed = True
                os.remove(file)
                deleted.append(file)
                break
    print('deleted', len(deleted), '0 line files -', deleted)


def inline_oneline():
    changed = True
    onelines = {}
    while changed:
        changed = False
        for file in os.listdir('.'):
            if file == 'main.mcfunction': continue
            if os.path.isdir(file): continue
            content = open(file).read()
            for thing in onelines:
                content = re.sub(rf'function {NAMESPACE}:{thing[:-len(".mcfunction")]}', onelines[thing], content)
            open(file, 'w').write(content)
            if content.count('\n') == 0:
                changed = True
                os.remove(file)
                onelines[file] = content
                break
    print('inlined', len(onelines), '1 line files -', onelines)


def rmcfunction(abc):
    if abc.endswith('.mcfunction'):
        return abc[:-len('.mcfunction')]
    else:
        return ''


def remove_unused():
    used = set()
    things = ['main']
    all_files = [*[rmcfunction(i) for i in os.listdir('.')], *['tree/'+rmcfunction(i) for i in os.listdir('tree')]]
    while '' in all_files: all_files.remove('')
    # print(all_files)
    while things:
        a = things.pop()
        if a in used: continue
        try:
            content = open(f'{a}.mcfunction').read()
            used.add(a)
            if a in all_files:
                all_files.remove(a)
            else:
                print(f'Calling unknown function {a}', file=sys.stderr)
            functions = re.findall(rf'function {NAMESPACE}:(.*)', content)
            things.extend(functions)
        except FileNotFoundError:
            print(f'Calling unknown function {a}', file=sys.stderr)
    for f in all_files:
        try:
            os.remove(f + '.mcfunction')
        except FileNotFoundError:
            print('Trying to remove unexisting file', f)