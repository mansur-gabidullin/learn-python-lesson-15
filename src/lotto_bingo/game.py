"""Game Entity."""
from functools import total_ordering
from typing import cast

from src.lotto_bingo.game_strategy import GameStrategy, InitialGameState
from src.lotto_bingo.player import Player
from src.lotto_bingo.utils import clear, greened, blinked, bolded


# pylint: disable=too-few-public-methods
@total_ordering
class Game:
    """Game class"""

    _strategy: GameStrategy

    def __init__(self, initial_state: InitialGameState | None = None):
        self._strategy = GameStrategy(initial_state)

    def __str__(self) -> str:
        """Print the game status"""
        winner = self._strategy.winner

        clear()

        is_running_status = str(self._strategy)
        winner_status = "Победителя нет!"

        if winner:
            winner_status = f"Победил игрок {winner} !\n \
            {blinked(greened(bolded('!!! ПОЗДРАВЛЯЕМ !!!')))}"

        return f"{is_running_status}\n\n{winner_status}\n"

    def __eq__(self, other: object) -> bool:
        if not isinstance(self, other.__class__):
            return False
        return bool(self._strategy == cast(Game, other)._strategy)

    def __gt__(self, other: object) -> bool:
        return bool(self._strategy > cast(Game, other)._strategy)

    def start(self) -> Player | None:
        """Start the game"""
        clear()
        self._strategy.cycle()
        print(self)
        return self._strategy.winner
