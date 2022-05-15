def clear():
    print("\x1bc")


def need_break():
    print("Завершить игру?")
    print("1. Нет")
    print("2. Да")
    try:
        return int(input()) == 2
    except ValueError:
        return False


def wait():
    print("Нажмите ВВОД чтобы продолжить...")
    input()


def strike(text):
    return "\x1b[2m\x1b[9m\x1b[90m" + text + "\x1b[22m\x1b[29m\x1b[39m"


def bolded(text):
    return "\x1b[1m" + text + "\x1b[21m"


def underlined(text):
    return "\x1b[4m" + text + "\x1b[24m"


def greened(text):
    return "\x1b[32m" + text + "\x1b[39m"


def blinked(text):
    return "\x1b[5m" + text + "\x1b[25m"
