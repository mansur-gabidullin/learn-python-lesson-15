import random
from math import floor
from typing import List

from src.lotto_bingo.constants import CARD_ROWS_COUNT, CARD_COLS_COUNT, CARD_NUMBERS_COUNT_IN_ROW, KEGS_COUNT
from src.lotto_bingo.utils import strike


def get_cells(numbers: List[int]):
    number_index = 0
    rest_cells = min(CARD_COLS_COUNT, len(numbers))
    rest_numbers = CARD_NUMBERS_COUNT_IN_ROW

    for _ in range(CARD_COLS_COUNT):
        if rest_cells and rest_numbers / rest_cells > random.random():
            yield str(numbers[number_index])
            number_index += 1
            rest_numbers -= 1
        else:
            yield ''
        rest_cells -= 1


class Card:
    def __init__(self, numbers: List[int] = None):
        if numbers:
            self.__numbers = numbers
        else:
            numbers_count = CARD_ROWS_COUNT * CARD_NUMBERS_COUNT_IN_ROW
            numbers_range = range(1, KEGS_COUNT + 1)
            self.__numbers = random.sample(numbers_range, numbers_count)

        self.__grid = [list(get_cells(self.__numbers[i * CARD_NUMBERS_COUNT_IN_ROW:])) for i in range(CARD_ROWS_COUNT)]

    def __contains__(self, key):
        return key in self.__numbers

    def __str__(self):
        return '\n'.join([
            '-'.join(['--'] * 9),
            *(' '.join(map(lambda cell: cell.rjust(2), row)) for row in self.__grid),
            '-'.join(['--'] * 9),
        ])

    def __len__(self):
        return len(self.__numbers)

    def strike_out(self, number):
        index = self.__numbers.index(number)
        row = floor(index / CARD_NUMBERS_COUNT_IN_ROW)
        cell = self.__grid[row].index(str(number))
        cell_content = self.__grid[row][cell]
        self.__grid[row][cell] = strike(cell_content)
        del self.__numbers[index]
