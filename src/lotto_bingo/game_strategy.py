"""Game Strategy Entity"""
from itertools import cycle
from typing import Optional, List, TypedDict, Iterable

from src.lotto_bingo.kegs_bag import KegsBag
from src.lotto_bingo.player import get_players, ComputerPlayer, HumanPlayer
from src.lotto_bingo.utils import wait, blinked, bolded, clear, underlined, need_break

InitialGameState = TypedDict(
    "InitialGameState",
    {"kegs": KegsBag, "losers": List[ComputerPlayer | HumanPlayer], "players": Iterable[ComputerPlayer | HumanPlayer]},
    total=False,
)


class GameStrategy:
    """GameStrategy class"""

    _winner: Optional[ComputerPlayer | HumanPlayer] = None
    _kegs: KegsBag = None
    _losers: List[ComputerPlayer | HumanPlayer] = []
    _players: List[ComputerPlayer | HumanPlayer] = []

    @property
    def winner(self):
        return self._winner

    def prepare(self, initial_state: InitialGameState | None = None):
        if initial_state is None:
            initial_state = InitialGameState()

        self._winner = None
        self._kegs = initial_state.get("kegs", KegsBag())
        self._losers = initial_state.get("losers", [])
        self._players = initial_state.get("players", list(get_players()))

    def cycle(self):
        players = self._get_active_players()

        while self._is_running() and not need_break():
            current_player = next(players)
            self._move(current_player)

            if len(current_player.card) == 0:
                self._winner = current_player

    def _is_running(self):
        return all(
            [not self._winner, len(self._kegs) != 0, not all(player in self._losers for player in self._players)]
        )

    def _get_active_players(self):
        for player in cycle(self._players):
            if player not in self._losers:
                yield player

    def _move(self, player: ComputerPlayer | HumanPlayer) -> None:
        clear()
        keg = self._kegs.get_next()
        current_card = player.card

        print(f"Новый бочонок: {blinked(bolded(str(keg)))} (осталось {len(self._kegs)})")
        print(f'Ходит игрок "{player.name}" ({player.type})')

        if player.type == "computer":
            if keg in current_card:
                current_card.strike_out(keg)
            print("Карточка игрока:")
            print(current_card)
        else:
            self._show_players_cards(player)

            print(f"Вычеркнуть номер {blinked(bolded(str(keg)))} из карточки?")
            print("1. Нет")
            print("2. Да")
            try:
                if (answer := int(input())) not in [1, 2]:
                    raise ValueError()
                need_strike = answer == 2
            except ValueError:
                need_strike = False

            if keg in current_card and not need_strike or keg not in current_card and need_strike:
                self._losers.append(player)
                clear()
                print(blinked(f'Игрок "{player.name}" ({player.type}) ' + underlined(bolded("ПРОИГРАЛ!"))))
                wait()

            if need_strike and keg in current_card:
                current_card.strike_out(keg)

    def _show_players_cards(self, current_player) -> None:
        print("Ваша карточка:")
        print(current_player.card)

        if len(self._players) == 1:
            return

        print("\nПосмотреть карточки других игроков?")
        print("1. Нет")
        print("2. Да")

        try:
            if (answer := int(input())) not in [1, 2]:
                raise ValueError()
            need_show_other_cards = answer == 2
        except ValueError:
            need_show_other_cards = False

        if need_show_other_cards:
            clear()
            other_players = filter(lambda player: player is not current_player, self._get_active_players())
            computers = list(filter(lambda p: p.type == "computer", other_players))
            humans = list(filter(lambda p: p.type == "human", other_players))

            if len(computers) > 0:
                print("Компьютеры:")

                for computer in computers:
                    print(f'Карточка "{computer.name}":')
                    print(computer.card)

            if len(humans) > 0:
                wait()
                print("Люди:")

                for human in humans:
                    print(f'Карточка "{human.name}":')
                    print(human.card)

            wait()
            clear()
