"""Test Game class."""
from itertools import cycle
from unittest.mock import patch

from src.lotto_bingo.game import Game
from src.lotto_bingo.game_strategy import InitialGameState
from src.lotto_bingo.player import get_players


@patch("builtins.print", return_value=None)
@patch("builtins.input", side_effect=cycle([""]))
def test_game(*_) -> None:
    """Test game"""
    game = Game()
    game.start(InitialGameState(players=get_players(10)))


@patch("builtins.print", return_value=None)
@patch("builtins.input", side_effect=cycle(["1", "2"]))
def test_player_can_lose(*_) -> None:
    """Test player can lose"""
    winner = None
    for _ in range(100):
        winner = Game().start()
        if not winner:
            break
    assert not winner
