import pytest

from src.lotto_bingo.Game import Game


def test_game():
    assert Game(players_count=1, is_auto=True).start()


@pytest.mark.slow
def test_player_can_win():
    winner = None
    for _ in range(100):
        winner = Game(100, True).start()
        if winner:
            break
    assert winner


@pytest.mark.slow
def test_player_can_not_lose():
    lose = False
    for _ in range(100):
        winner = Game(100, True).start()
        if not winner:
            lose = True
        if lose:
            break
    assert not lose
