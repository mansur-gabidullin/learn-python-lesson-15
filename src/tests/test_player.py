"""
Tests for class Player
"""
from unittest.mock import patch

import pytest

from src.lotto_bingo.card import Card
from src.lotto_bingo.kegs_bag import KegsBag
from src.lotto_bingo.player import HumanPlayer, ComputerPlayer, Player, get_players


class TestPlayer:
    """Test Player Entity"""

    def setup(self):
        self.bag = KegsBag([1])

    def test_human_player(self):
        human_player = HumanPlayer("Human Tester", Card([1]))
        assert human_player.name == "Human Tester"
        assert human_player.type == "human"

        keg = self.bag.get_next()
        assert keg in human_player.card


def test_player() -> None:
    """Test player"""
    bag = KegsBag([1])

    computer_player = ComputerPlayer("Computer Tester", Card([2]))
    assert computer_player.name == "Computer Tester"
    assert computer_player.type == "computer"

    keg = bag.get_next()
    assert keg not in computer_player.card

    with pytest.raises(TypeError):
        Player("test", Card())  # pylint: disable=abstract-class-instantiated


@patch("builtins.print", return_value=None)
def test_get_players(*_) -> None:
    with patch("builtins.input", side_effect=["2", "1", "Test-1", "2", "Test-2"]):
        players = list(get_players())
        assert len(players) == 2
        assert all(isinstance(player, Player) for player in players)
        assert isinstance(players[0], ComputerPlayer)
        assert players[0].name == "Test-1"
        assert isinstance(players[1], HumanPlayer)
        assert players[1].name == "Test-2"

    with patch("builtins.input", return_value="10"):
        players = list(get_players(10, ComputerPlayer))
        assert len(players) == 10
        assert all(isinstance(player, ComputerPlayer) for player in players)

    with patch("builtins.input", side_effect=["-1"]):
        players = list(get_players())
        assert len(players) == 0

    with patch("builtins.input", side_effect=["-1", "-1"]):
        players = list(get_players(1))
        assert len(players) == 1
