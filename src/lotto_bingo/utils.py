def clear():
    print('\x1bc')


def need_break():
    print('Продолжить?')
    print('1/Enter. Да')
    print('2. Нет')
    try:
        return int(input()) == 2
    except ValueError:
        return False


def strike(text):
    return '\x1b[2m\x1b[9m\x1b[90m' + text + '\x1b[22m\x1b[29m\x1b[39m'


def bolded(text):
    return '\x1b[1m' + text + '\x1b[21m'


def underlined(text):
    return '\x1b[4m' + text + '\x1b[24m'


def greened(text):
    return '\x1b[32m' + text + '\x1b[39m'


def blinked(text):
    return '\x1b[5m' + text + '\x1b[25m'
