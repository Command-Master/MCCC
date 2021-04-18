import os, re
from globals_consts import NAMESPACE
from temps import get_temp_func

from file_utils import get_callers


def goto_postprocess():
    labels = {}
    gotoers = {}
    for file in os.listdir('.'):
        if file == 'main.mcfunction': continue
        if os.path.isdir(file): continue
        content = open(file).read()
        m = re.findall(r'label (.*)', content)
        content = re.split(r'label .*', content)
        fname = file
        file = open(file, 'w')
        file.write(content[0].strip())
        for a, b in zip(m, content[1:]):
            new_file = get_temp_func()
            file.write(f'\nfunction {NAMESPACE}:{new_file}')
            file.close()
            file = open(new_file + '.mcfunction', 'a')
            file.write(b.strip())
            labels[a] = new_file
        file.write('\n')
        if len(m) != 0:
            gotoers[fname[:-len('.mcfunction')]] = file
    print(gotoers)
    while len(gotoers) > 0:
        ng = {}
        print(gotoers)
        for a in gotoers:
            c = get_callers(a)
            assert len(c) == 1, 'Too many callers for label'
            oc = c[0]
            c = c[0] + '.mcfunction'
            content = open(c).read().split(f'function {NAMESPACE}:{a}')
            assert len(content) == 2, 'Too many callers for label'
            file = open(c, 'w')
            file.write(content[0] + f'function {NAMESPACE}:{a}')
            file.close()
            new_file = get_temp_func()
            gotoers[a].write(f'\nfunction {NAMESPACE}:{new_file}')
            gotoers[a].close()
            file = open(new_file + '.mcfunction', 'w')
            file.write(content[1])
            if not oc.startswith('method_'):
                ng[oc] = file
        gotoers = ng
    for file in os.listdir('.'):
        if file == 'main.mcfunction': continue
        if os.path.isdir(file): continue
        content = open(file).read()
        open(file,'w').write(re.sub(r'goto (.*)', lambda a: f'function {NAMESPACE}:{labels[a.group(1)]}', content))