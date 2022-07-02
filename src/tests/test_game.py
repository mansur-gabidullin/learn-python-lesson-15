"""Test Game class."""
from itertools import cycle
from typing import Any
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

    def test_game(self, *_: Any) -> None:
        """checks game is running without errors"""
        game = Game()
        game.start()

    def test_game_with_given_state(self, *_: Any) -> None:
        """checks game with given state is running without errors"""
        game_state = InitialGameState(players=[ComputerPlayer("test computer", Card([1]))], kegs=KegsBag([1]))
        game = Game(game_state)
        winner = game.start()
        assert winner

    def test_game_without_winner(self, *_: Any) -> None:
        """checks game with given state is running without errors"""
        game_state = InitialGameState(players=[ComputerPlayer("test computer", Card([1]))], kegs=KegsBag([2]))
        game = Game(game_state)
        winner = game.start()
        assert not winner

    def test_printing_game_status_contains_winner(self, *_: Any) -> None:
        """checks printing the game status"""
        player = ComputerPlayer("test computer", Card([1]))
        game_state = InitialGameState(players=[player], kegs=KegsBag([1]))
        game = Game(game_state)
        game.start()
        assert str(player) in str(game)

    def test_printing_game_status_not_contain_player(self, *_: Any) -> None:
        """checks printing the game status"""
        player = ComputerPlayer("test computer", Card([1]))
        game_state = InitialGameState(players=[player], kegs=KegsBag([2]))
        game = Game(game_state)
        game.start()
        assert str(player) not in str(game)

    def test_games_are_equal(self, *_: Any) -> None:
        """checks games are equal"""
        player = ComputerPlayer("test computer")
        game_state = InitialGameState(players=[player], kegs=KegsBag([2]))
        game_one = Game(game_state)
        game_other = Game(game_state)
        assert game_one == game_other
        assert game_one != {"start": None}

    def test_one_game_is_great_then_other(self, *_: Any) -> None:
        """checks one game is great then other"""
        player_one = ComputerPlayer("test computer")
        player_two = ComputerPlayer("test computer")
        game_one = Game(InitialGameState(players=[player_one, player_two], kegs=KegsBag([2])))
        game_other = Game(InitialGameState(players=[player_one], kegs=KegsBag([2])))
        assert game_one > game_other
