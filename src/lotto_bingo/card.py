"""Card Entity."""
import random
from typing import List, Optional, Iterator

from src.lotto_bingo.constants import (
    CARD_ROWS_COUNT,
    CARD_COLS_COUNT,
    CARD_NUMBERS_COUNT_IN_ROW,
    KEGS_COUNT,
)
from src.lotto_bingo.utils import striked


def get_cells(numbers: List[int]) -> Iterator[str]:
    """Card cells generator"""
    number_index = 0
    rest_cells = min(CARD_COLS_COUNT, len(numbers))
    rest_numbers = CARD_NUMBERS_COUNT_IN_ROW

    for _ in range(CARD_COLS_COUNT):
        if rest_cells and rest_numbers / rest_cells > random.random():
            yield str(numbers[number_index])
            number_index += 1
            rest_numbers -= 1
        else:
            yield ""
        rest_cells -= 1


class Card:
    """Card class"""

    def __init__(self, numbers: Optional[List[int]] = None):
        if numbers:
            self.__numbers = numbers.copy()
        else:
            numbers_count = CARD_ROWS_COUNT * CARD_NUMBERS_COUNT_IN_ROW
            numbers_range = range(1, KEGS_COUNT + 1)
            self.__numbers = random.sample(numbers_range, numbers_count)

        self.__grid = [list(get_cells(self.__numbers[i * CARD_NUMBERS_COUNT_IN_ROW :])) for i in range(CARD_ROWS_COUNT)]

    def __contains__(self, key: int) -> bool:
        return key in self.__numbers

    def __str__(self) -> str:
        return "\n".join(
            [
                "-".join(["--"] * 9),
                *(" ".join(map(lambda cell: cell.rjust(2), row)) for row in self.__grid),
                "-".join(["--"] * 9),
            ]
        )

    def __len__(self) -> int:
        return len(self.__numbers)

    def strike_out(self, number: int) -> None:
        """Strike out given keg number from card"""
        self.__numbers.remove(number)
        cell = str(number)
        for row in self.__grid:
            if cell in row:
                cell_index = row.index(str(number))
                row[cell_index] = striked(row[cell_index])
