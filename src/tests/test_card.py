"""Test Card class."""
import re

import pytest

from src.lotto_bingo.card import Card, get_cells
from src.lotto_bingo.constants import CARD_NUMBERS_COUNT_IN_ROW, CARD_ROWS_COUNT, KEGS_COUNT
from src.lotto_bingo.utils import striked


class TestCellsGenerator:
    """Test a Card Cells Generator"""

    def setup(self):
        """setups cells list"""
        numbers = list(range(KEGS_COUNT))
        self.cells = get_cells(numbers, 5, 15)

    def test_length(self):
        """checks cells list length"""
        assert len(list(self.cells)) == 15

    def test_numbers_count(self):
        """checks numbers count in cells list"""
        assert len(list(filter(bool, self.cells))) == 5

    def test_numbers(self):
        """checks numbers in cells list"""
        assert list(filter(bool, self.cells)) == ["0", "1", "2", "3", "4"]

    def test_empty(self):
        """checks generate correct list if given empty list of numbers"""
        assert len(list(get_cells([], 10, 5))) == 0


class TestCard:
    """Test Card"""

    def setup(self):
        """setup card"""
        self.card = Card(list(range(KEGS_COUNT)))

    def test_init_with_defaults(self):
        """checks initialization with defaults"""
        card = Card()
        assert len(card) == CARD_ROWS_COUNT * CARD_NUMBERS_COUNT_IN_ROW

    def test_init(self):
        """checks initialization with given numbers"""
        assert len(self.card) == KEGS_COUNT

    def test_strike_out(self):
        """checks can strike out number"""
        self.card.strike_out(0)
        assert len(self.card) == KEGS_COUNT - 1

    def test_strike_out_exception(self):
        """checks raising exception if attempt to strike out absenting number"""
        with pytest.raises(ValueError):
            self.card.strike_out(-1)

    def test_contains_method(self):
        """checks contains method"""
        assert (KEGS_COUNT - 1) in self.card

    def test_grid(self):
        """checks card grid"""
        grid_columns = CARD_NUMBERS_COUNT_IN_ROW + (CARD_NUMBERS_COUNT_IN_ROW - 1)
        grid_string = str(self.card)
        rows = grid_string.split("\n")
        assert rows[0], rows[4] == ["-".join(["--"] * grid_columns)] * 2
        for row in rows[1:4]:
            assert len(list(filter(lambda cell: cell != "", row)))

    def test_grid_with_striked_cell(self):
        """checks card grid after striking out number"""
        self.card.strike_out(0)
        test_striked_cell = striked("0")
        assert test_striked_cell in str(self.card)
