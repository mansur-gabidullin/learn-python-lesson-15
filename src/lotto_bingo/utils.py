def clear():
    print('\x1bc')


def strike(text):
    return '\x1b[2m\x1b[9m\x1b[90m' + text + '\x1b[22m\x1b[29m\x1b[39m'
