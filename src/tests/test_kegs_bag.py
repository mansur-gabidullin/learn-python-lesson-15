import pytest

from src.lotto_bingo.KegsBag import KegsBag
from src.lotto_bingo.constants import KEGS_COUNT


class TestKegsBag:
    def test_kegs_count(self):
        assert len(KegsBag.KEG_NUMBERS) == KEGS_COUNT

    def test_sample(self):
        sample = KegsBag.get_sample(10)
        assert len(sample) == 10
        assert any((number in KegsBag.KEG_NUMBERS for number in sample))

    def test_next(self):
        kegs_bag = KegsBag(1)
        next(kegs_bag)
        assert len(kegs_bag) == 0

        with pytest.raises(StopIteration):
            next(kegs_bag)
