"""Test KegsBag class."""
import pytest

from src.lotto_bingo.constants import KEGS_COUNT
from src.lotto_bingo.kegs_bag import KegsBag


# pylint: disable=no-self-use
class TestKegsBag:
    """Test Kegs Bag Entity"""

    def test_init(self) -> None:
        """checks initialization"""
        kegs_bag = KegsBag()
        assert len(kegs_bag) == KEGS_COUNT

    def test_init_with_kegs_list(self) -> None:
        """checks initialization with passed kegs list"""
        kegs_bag = KegsBag([1])
        assert len(kegs_bag) == 1

    def test_bag_contains_keg(self) -> None:
        """checks kegs bag contains keg"""
        kegs_bag = KegsBag([1])
        assert 1 in kegs_bag

    def test_iteration_on_kegs_bag(self) -> None:
        """checks iterating on kegs"""
        kegs_bag = KegsBag(list(range(11)))
        assert all(isinstance(keg, int) and keg in kegs_bag for keg in kegs_bag)

    def test_string_presentation(self) -> None:
        """checks kegs bag string presentation"""
        kegs_bag = KegsBag([1])
        assert str(kegs_bag) == "[1]"

    def test_getting_next_keg(self) -> None:
        """checks getting next keg from kegs bag"""
        kegs_bag = KegsBag([1])
        keg = kegs_bag.get_next()
        assert isinstance(keg, int) and len(kegs_bag) == 0

    def test_raising_index_error_for_getting_next_keg_on_empty_kegs_bag(self) -> None:
        """checks raising IndexError for getting next keg on empty kegs bag"""
        kegs_bag = KegsBag([])
        with pytest.raises(IndexError):
            kegs_bag.get_next()

    def test_kegs_bags_are_equal(self) -> None:
        """checks kegs bags are equal"""
        kegs_bag_one = KegsBag()
        kegs_bag_other = KegsBag()
        assert kegs_bag_one == kegs_bag_other
        assert kegs_bag_one != {"get_next": None}

    def test_one_kegs_bag_is_great_then_other(self) -> None:
        """checks kegs bag is great then other"""
        kegs_bag_one = KegsBag([1])
        kegs_bag_other = KegsBag([])
        assert kegs_bag_one > kegs_bag_other
