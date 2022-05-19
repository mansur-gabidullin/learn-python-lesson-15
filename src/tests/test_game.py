"""Test Game class."""
from src.lotto_bingo.game import Game


def test_game() -> None:
    """Test game"""
    Game(players_count=100, is_auto=True).start()


def test_player_can_lose() -> None:
    """Test player can lose"""
    winner = None
    for _ in range(100):
        winner = Game(players_count=2, is_auto=True).start()
        if not winner:
            break
    assert not winner


def test_player_can_win() -> None:
    """Test player can win"""
    winner = Game(players_count=1, is_auto=True).start()
    assert winner
