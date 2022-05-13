import random
from typing import Final

from src.lotto_bingo.constants import KEGS_COUNT


class KegsBag:
    KEG_NUMBERS: Final = range(1, KEGS_COUNT + 1)

    @classmethod
    def get_sample(cls, count):
        return random.sample(cls.KEG_NUMBERS, count)

    def __init__(self, count: int = None):
        self.__kegs = KegsBag.get_sample(count or KEGS_COUNT)

    def __len__(self):
        return len(self.__kegs)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self) == 0:
            raise StopIteration

        keg = random.choice(self.__kegs)
        return self.__kegs.pop(self.__kegs.index(keg))
