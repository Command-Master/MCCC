li = 0
rtype = None


def create_local():
    global li
    t = f'$l{li}'
    li += 1
    return t


def remove_locals(i):
    global li
    li -= i


def reset_locals():
    global li
    li = 0


def local_size():
    return li


def set_rtype(type):
    global rtype
    rtype = type

def get_rtype():
    return rtype