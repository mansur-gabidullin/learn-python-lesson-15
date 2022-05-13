import random
from typing import List

from src.lotto_bingo.constants import KEGS_COUNT


class KegsBag:
    def __init__(self, count: int = None, numbers: List[int] = None):
        numbers = numbers or range(1, KEGS_COUNT + 1)
        self.__kegs = random.sample(numbers, count or KEGS_COUNT)

    def __len__(self):
        return len(self.__kegs)

    def __contains__(self, key):
        return key in self.__kegs

    def __iter__(self):
        return iter(self.__kegs)

    def get_next(self):
        keg = random.choice(self.__kegs)
        return self.__kegs.pop(self.__kegs.index(keg))
