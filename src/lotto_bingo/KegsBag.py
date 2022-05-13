import random
from typing import List

from src.lotto_bingo.constants import KEGS_COUNT


class KegsBag:
    def __init__(self, count: int = None, numbers: List[int] = None):
        self.__numbers = numbers or range(1, KEGS_COUNT + 1)
        self.__kegs = self.get_sample(count or KEGS_COUNT)

    def __len__(self):
        return len(self.__kegs)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self) == 0:
            raise StopIteration

        keg = random.choice(self.__kegs)
        return self.__kegs.pop(self.__kegs.index(keg))

    def __contains__(self, key):
        return key in self.__numbers

    def get_sample(self, count):
        return random.sample(self.__numbers, count)
