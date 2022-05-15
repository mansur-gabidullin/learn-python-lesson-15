from src.lotto_bingo.Game import Game


def test_game():
    Game(players_count=100, is_auto=True).start()


def test_player_can_lose():
    winner = None
    for _ in range(100):
        winner = Game(players_count=2, is_auto=True).start()
        if not winner:
            break
    assert not winner


def test_player_can_win():
    winner = Game(players_count=1, is_auto=True).start()
    assert winner
