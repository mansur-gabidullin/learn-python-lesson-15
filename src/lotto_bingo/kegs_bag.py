"""Kegs Bag Entity."""
import random
from typing import List, Optional, Iterator

from src.lotto_bingo.constants import KEGS_COUNT


class KegsBag:
    """KegsBag class"""

    def __init__(self, kegs: Optional[List[int]] = None):
        if kegs:
            self.__kegs = kegs
        else:
            numbers = range(1, KEGS_COUNT + 1)
            self.__kegs = random.sample(numbers, KEGS_COUNT)

    def __len__(self) -> int:
        return len(self.__kegs)

    def __contains__(self, key: int) -> bool:
        return key in self.__kegs

    def __iter__(self) -> Iterator[int]:
        return iter(self.__kegs)

    def __str__(self) -> str:
        return str(self.__kegs)

    def get_next(self) -> int:
        """Get next keg"""
        keg = random.choice(self.__kegs)
        return self.__kegs.pop(self.__kegs.index(keg))
