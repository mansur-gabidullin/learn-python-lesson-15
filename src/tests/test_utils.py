from unittest.mock import patch

from src.lotto_bingo.utils import need_break


def test_need_break() -> None:
    """Test need break method"""
    with patch("builtins.input", return_value=""):
        assert need_break() is False
