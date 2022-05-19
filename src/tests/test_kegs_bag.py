"""Test KegsBag class."""
import pytest

from src.lotto_bingo.kegs_bag import KegsBag


def test_iter() -> None:
    """Test iterating on kegs"""
    kegs_bag = KegsBag(list(range(11)))
    assert all(isinstance(keg, int) and keg in kegs_bag for keg in kegs_bag)


def test_get_next() -> None:
    """Test getting next keg"""
    kegs_bag = KegsBag([1])
    assert len(kegs_bag) == 1
    kegs_bag.get_next()
    assert len(kegs_bag) == 0
    with pytest.raises(IndexError):
        kegs_bag.get_next()
