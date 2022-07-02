"""
Tests for class Player
"""
from typing import Any
from unittest.mock import patch

import pytest

from src.lotto_bingo.card import Card
from src.lotto_bingo.kegs_bag import KegsBag
from src.lotto_bingo.player import HumanPlayer, ComputerPlayer, Player, generate_players

# pylint: disable=no-self-use,attribute-defined-outside-init
from src.lotto_bingo.utils import bolded, underlined


class TestPlayer:
    """Test Player Entity"""

    def setup(self) -> None:
        """set kegs bag for every test"""
        self.bag = KegsBag([1])

    def test_raising_error_while_attempting_call_abstract_player_class(self) -> None:
        """checks raising error while attempting call abstract player class"""
        with pytest.raises(TypeError):
            Player("test abstract player")  # pylint: disable=abstract-class-instantiated

    def test_instantiate_human_player_without_params(self) -> None:
        """checks instantiate human player without params"""
        human_player = HumanPlayer()
        assert human_player.type == "human"
        assert isinstance(human_player.name, str) and isinstance(human_player.card, Card)

    def test_instantiate_human_player_with_given_params(self) -> None:
        """checks instantiate human player with given params"""
        test_card = Card([1])
        human_player = HumanPlayer("test name", test_card)
        assert human_player.type == "human"
        assert human_player.name == "test name" and human_player.card == test_card

    def test_instantiate_computer_player_without_params(self) -> None:
        """checks instantiate computer player without params"""
        computer_player = ComputerPlayer()
        assert computer_player.type == "computer"
        assert isinstance(computer_player.name, str) and isinstance(computer_player.card, Card)

    def test_instantiate_computer_player_with_given_params(self) -> None:
        """checks instantiate computer player with given params"""
        test_card = Card([1])
        computer_player = ComputerPlayer("test name", test_card)
        assert computer_player.type == "computer"
        assert computer_player.name == "test name" and computer_player.card == test_card

    def test_printing_player_name(self) -> None:
        """checks player class __str__ method"""
        player = ComputerPlayer("test name")
        player_name = str(player)
        assert f"{bolded(underlined(player.name))} ({player.type})" == player_name

    def test_players_are_equal(self) -> None:
        """checks players are equal"""
        player_one = ComputerPlayer(name="test player")
        player_other = player_one
        assert player_one == player_other
        assert player_one != {"name": "test player"}

    def test_one_player_is_great_then_other(self) -> None:
        """checks player is great then other"""
        player_one = ComputerPlayer(card=Card([1]))
        player_other = ComputerPlayer(card=Card([]))
        assert player_one > player_other


@patch("builtins.print", return_value=None)
def test_generate_players(*_: Any) -> None:
    """checks get players method"""
    with patch("builtins.input", side_effect=["2", "1", "Test-1", "2", "Test-2"]):
        players = list(generate_players())
        assert len(players) == 2
        assert all(isinstance(player, Player) for player in players)
        assert isinstance(players[0], ComputerPlayer)
        assert players[0].name == "Test-1"
        assert isinstance(players[1], HumanPlayer)
        assert players[1].name == "Test-2"

    with patch("builtins.input", return_value="10"):
        players = list(generate_players(10, ComputerPlayer))
        assert len(players) == 10
        assert all(isinstance(player, ComputerPlayer) for player in players)

    with patch("builtins.input", side_effect=["foo-bar-baz"]):
        players = list(generate_players())
        assert len(players) == 0

    with patch("builtins.input", side_effect=["-1"]):
        players = list(generate_players())
        assert len(players) == 0

    with patch("builtins.input", side_effect=["-1", "-1"]):
        players = list(generate_players(1))
        assert len(players) == 1
