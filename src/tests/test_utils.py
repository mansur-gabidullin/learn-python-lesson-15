"""Test utilities."""

from typing import Any
from unittest.mock import patch

from src.lotto_bingo.utils import need_break, wait


@patch("builtins.print", return_value=None)
def test_need_break(_: Any) -> None:
    """Test need break method"""
    with patch("builtins.input", return_value="2"):
        assert need_break() is True
    with patch("builtins.input", return_value="-1"):
        assert need_break() is False
    with patch("builtins.input", return_value="foo"):
        assert need_break() is False


@patch("builtins.print", return_value=None)
def test_wait(_: Any) -> None:
    """Test wait method"""
    with patch("builtins.input", return_value="foo"):
        assert wait() is None
