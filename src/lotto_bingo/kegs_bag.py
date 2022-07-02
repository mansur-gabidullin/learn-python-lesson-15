"""Kegs Bag Entity."""

import random
from functools import total_ordering
from typing import List, Iterator, Any

from src.lotto_bingo.constants import KEGS_COUNT


@total_ordering
class KegsBag:
    """KegsBag class"""

    def __init__(self, kegs: List[int] | None = None):
        if kegs is not None:
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

    def __eq__(self, other: Any) -> bool:
        if not isinstance(self, other.__class__):
            return False
        return all((keg in other for keg in self))

    def __gt__(self, other: Any) -> bool:
        return len(self) > len(other)

    def get_next(self) -> int:
        """Get next keg"""
        keg = random.choice(self.__kegs)
        return self.__kegs.pop(self.__kegs.index(keg))
