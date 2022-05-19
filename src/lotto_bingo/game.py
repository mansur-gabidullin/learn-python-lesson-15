"""Game Entity."""
from itertools import cycle
from typing import Callable, Optional, Any, Iterator, List

from src.lotto_bingo.card import Card
from src.lotto_bingo.kegs_bag import KegsBag
from src.lotto_bingo.player import HumanPlayer, ComputerPlayer, Player
from src.lotto_bingo.utils import (
    clear,
    need_break,
    underlined,
    greened,
    blinked,
    bolded,
    wait,
)


class Game:
    """Game class"""

    def __init__(self, players_count: Optional[int] = None, is_auto: bool = False):
        self._losers: List[Player] = []
        self._winner = None
        self._is_need_ask_break = True
        self._is_auto = is_auto
        self._kegs = KegsBag()
        self._players = list(self._get_players(players_count))
        self._clear()

    def _print(self, *args: Any, **kwargs: Any) -> None:
        if not self._is_auto:
            print(*args, **kwargs)

    def _clear(self) -> None:
        if not self._is_auto:
            clear()

    def _ask_need_break(self) -> bool:
        if self._is_auto or not self._is_need_ask_break:
            return False

        if not need_break():
            print("Больше не спрашивать о завершении игры?")
            print("1. Продолжать спрашивать")
            print("2. Не спрашивать")
            try:
                self._is_need_ask_break = int(input()) == 1
            except ValueError:
                self._is_need_ask_break = True
            return False

        return True

    def _wait(self) -> None:
        if not self._is_auto:
            wait()

    def _get_players(self, count: Optional[int] = None) -> Iterator[Player]:
        if not count:
            self._print("Сколько игроков будет играть?")
            try:
                players_count = int(input())
            except ValueError:
                players_count = 0
        else:
            players_count = count

        for i in range(players_count):
            if not self._is_auto:
                self._clear()
                default_name = f"Игрок {i + 1}"

                self._print("Выберите тип игрока:")
                self._print("1. Человек")
                self._print("2. Компьютер")
                try:
                    get_player = HumanPlayer if int(input()) == 1 else ComputerPlayer
                except ValueError:
                    get_player = HumanPlayer

                self._clear()
                name = input("Укажите имя игрока: ").strip() or default_name
                yield get_player(name, Card())
                continue

            yield ComputerPlayer(f"Игрок {i + 1}", Card())

    def _show_players_cards(self, filter_fn: Callable[[Player], bool]) -> None:
        if self._is_auto or len(self._players) == 1:
            return

        self._print("\nПосмотреть карточки других игроков?")
        self._print("1. Нет")
        self._print("2. Да")

        try:
            need_show_other_cards = int(input()) == 2
        except ValueError:
            need_show_other_cards = False

        if need_show_other_cards:
            self._clear()
            other_players = filter(filter_fn, self._players)
            computers = list(filter(lambda p: p.type == "computer", other_players))
            humans = list(filter(lambda p: p.type == "human", other_players))

            if len(computers) > 0:
                self._print("Компьютеры:")

                for computer in computers:
                    self._print(f'Карточка "{computer.name}":')
                    self._print(computer.card)

            if len(humans) > 0:
                self._wait()
                self._print("Люди:")

                for human in humans:
                    self._print(f'Карточка "{human.name}":')
                    self._print(human.card)

            self._wait()
            self._clear()

    def _computer_move(self, current_player: ComputerPlayer, keg: int) -> None:
        current_card = current_player.card
        if keg in current_card:
            current_card.strike_out(keg)
        self._print(f"Новый бочонок: {blinked(bolded(str(keg)))} (осталось {len(self._kegs)})")
        self._print(f'Ходит игрок "{current_player.name}" (Компьютер)')
        self._print("Карточка игрока:")
        self._print(current_card)
        self._wait()

    def _human_move(self, current_player: HumanPlayer, keg: int) -> None:
        current_card = current_player.card
        self._show_players_cards(lambda player: player is not current_player and player not in self._losers)
        self._print(f"Новый бочонок: {blinked(bolded(str(keg)))} (осталось {len(self._kegs)})")
        self._print(f'Ходит игрок "{current_player.name}" (Человек)')
        self._print("Ваша карточка:")
        self._print(current_card)

        self._print(f"Вычеркнуть номер {blinked(bolded(str(keg)))} из карточки?")
        self._print("1. Нет")
        self._print("2. Да")
        try:
            need_strike = int(input()) == 2
        except ValueError:
            need_strike = False

        if keg in current_card and not need_strike or keg not in current_card and need_strike:
            self._losers.append(current_player)
            self._clear()
            self._print(blinked(f'Игрок "{current_player.name}" (Человек) ' + underlined(bolded("ПРОИГРАЛ!"))))
            self._wait()

        if need_strike and keg in current_card:
            current_card.strike_out(keg)

    def start(self) -> Optional[Player]:
        """Start the game"""
        self._losers = []

        for current_player in cycle(self._players):
            if len(self._kegs) == 0:
                break

            if current_player in self._losers:
                continue

            self._clear()

            current_card = current_player.card
            keg = self._kegs.get_next()

            if current_player.type == "computer":
                self._computer_move(current_player, keg)
            else:
                self._human_move(current_player, keg)

            if len(current_card) == 0:
                self._winner = current_player
                break

            self._clear()

            if self._ask_need_break():
                break

        self._clear()

        if not self._winner:
            self._print("Победителя нет!")
        else:
            current_player_type_name = "Компьютер" if self._winner.type == "computer" else "Человек"
            self._print(f"Победил игрок {bolded(underlined(self._winner.name))} ({current_player_type_name}) !")
            self._print(blinked(greened(bolded("!!! ПОЗДРАВЛЯЕМ !!!"))))

        return self._winner

    def who_wins(self) -> None:
        """Print who wins"""
        if self._winner:
            print(self._winner.name)
