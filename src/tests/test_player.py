"""
Tests for class Player
"""
import pytest

from src.lotto_bingo.card import Card
from src.lotto_bingo.kegs_bag import KegsBag
from src.lotto_bingo.player import HumanPlayer, ComputerPlayer, Player


def test_player() -> None:
    """Test player"""
    bag = KegsBag([1])

    human_player = HumanPlayer("Human Tester", Card([1]))
    assert human_player.name == "Human Tester"
    assert human_player.type == "human"

    computer_player = ComputerPlayer("Computer Tester", Card([2]))
    assert computer_player.name == "Computer Tester"
    assert computer_player.type == "computer"

    keg = bag.get_next()
    assert keg in human_player.card
    assert keg not in computer_player.card

    with pytest.raises(TypeError):
        Player("test", Card())  # pylint: disable=abstract-class-instantiated
