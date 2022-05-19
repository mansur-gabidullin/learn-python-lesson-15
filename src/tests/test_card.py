"""Test Card class."""
import re

import pytest

from src.lotto_bingo.card import Card
from src.lotto_bingo.utils import striked


def test_card() -> None:
    """Test card"""
    card = Card(list(range(1, 16)))
    assert re.sub("[- \n]", "", str(card)) == "123456789101112131415"
    card = Card()
    assert len(card) == 15
    card = Card([1])
    with pytest.raises(ValueError):
        card.strike_out(None)
    assert 1 in card
    card.strike_out(1)
    assert 1 not in card
    assert re.sub("[- \n]", "", str(card)) == striked("1")
