"""Test Game class."""
from itertools import cycle
from typing import Any, Iterable
from unittest.mock import patch

from src.lotto_bingo.card import Card
from src.lotto_bingo.game import Game
from src.lotto_bingo.game_strategy import InitialGameState
from src.lotto_bingo.kegs_bag import KegsBag
from src.lotto_bingo.player import ComputerPlayer


# pylint: disable=no-self-use
@patch("builtins.print", return_value=None)
@patch("builtins.input", side_effect=cycle(["10", "-1"]))
class TestGame:
    """Test game"""

    def test_game(self, *_: Iterable[Any]) -> None:
        """checks game is running without errors"""
        game = Game()
        game.start()

    def test_game_with_given_state(self, *_: Iterable[Any]) -> None:
        """checks game with given state is running without errors"""
        game = Game()
        game_state = InitialGameState(players=[ComputerPlayer("test computer", Card([1]))], kegs=KegsBag([1]))
        winner = game.start(game_state)
        assert winner

    def test_game_without_winner(self, *_: Iterable[Any]) -> None:
        """checks game with given state is running without errors"""
        game = Game()
        game_state = InitialGameState(players=[ComputerPlayer("test computer", Card([1]))], kegs=KegsBag([2]))
        winner = game.start(game_state)
        assert not winner
