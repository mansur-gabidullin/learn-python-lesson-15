import pytest

from src.lotto_bingo.KegsBag import KegsBag


class TestKegsBag:
    def test_sample(self):
        kegs_bag = KegsBag(10)
        sample = kegs_bag.get_sample(10)
        assert len(sample) == 10
        assert any(number in kegs_bag.numbers for number in sample)

    def test_next(self):
        kegs_bag = KegsBag(1)
        next(kegs_bag)
        assert len(kegs_bag) == 0

        with pytest.raises(StopIteration):
            next(kegs_bag)

    def test_iter(self):
        kegs_bag = KegsBag(10)
        assert all(isinstance(keg, int) and keg in kegs_bag.numbers for keg in kegs_bag)
