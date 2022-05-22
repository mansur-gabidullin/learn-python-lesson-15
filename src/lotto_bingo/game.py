"""Game Entity."""

from src.lotto_bingo.game_strategy import GameStrategy, InitialGameState
from src.lotto_bingo.player import Player
from src.lotto_bingo.utils import clear, underlined, greened, blinked, bolded


class Game:
    """Game class"""

    _strategy: GameStrategy = GameStrategy()

    def start(self, initial_state: InitialGameState | None = None) -> Player | None:
        """Start the game"""
        clear()

        self._strategy.prepare(initial_state)
        self._strategy.cycle()
        winner = self._strategy.winner

        clear()

        if winner:
            print(f"Победил игрок {bolded(underlined(winner.name))} ({winner.type}) !")
            print(blinked(greened(bolded("!!! ПОЗДРАВЛЯЕМ !!!"))))
        else:
            print("Победителя нет!")

        return winner
