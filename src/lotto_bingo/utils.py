"""Utilities."""
from typing import Any


def clear() -> None:
    """Clear terminal screen"""
    print("\x1bc")


def need_break() -> bool:
    """Check is need break game"""
    print("Завершить игру?")
    print("1. Нет")
    print("2. Да")
    try:
        if (user_answer := int(input())) not in [1, 2]:
            raise ValueError()
        return user_answer == 2
    except ValueError:
        return False


def wait() -> None:
    """Wait user interaction"""
    print("Нажмите ВВОД чтобы продолжить...")
    input()


def striked(text: str) -> str:
    """Add strikethrough style to text"""
    return "\x1b[2m\x1b[9m\x1b[90m" + text + "\x1b[22m\x1b[29m\x1b[39m"


def bolded(text: str) -> str:
    """Add bolded style to text"""
    return "\x1b[1m" + text + "\x1b[21m"


def underlined(text: str) -> str:
    """Add underlined style to text"""
    return "\x1b[4m" + text + "\x1b[24m"


def greened(text: str) -> str:
    """Add greened style to text"""
    return "\x1b[32m" + text + "\x1b[39m"


def blinked(text: str) -> str:
    """Add blinked style to text"""
    return "\x1b[5m" + text + "\x1b[25m"


def identity(_: Any) -> Any:
    """returns identity stuff"""
    return _
