TI = 0
ft = 0
used_temps = []
gtemps = []
context_id = 1


def get_cid():
    return context_id


def new_cid():
    global context_id
    context_id += 1


def get_temp():
    global TI
    TI += 1
    return f'$t{TI}'


def get_temp_func():
    global ft
    ft += 1
    return f'temp_{ft}'


ai = 1
stringss = {}


def clear_used():
    global used_temps
    used_temps = []


def get_position():
    return ai


def register_space(size):
    global ai
    ai += size
