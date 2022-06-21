"""Player Entity."""
from abc import ABCMeta, abstractmethod
from functools import total_ordering
from typing import Literal, Iterator, Type, cast

from src.lotto_bingo.card import Card
from src.lotto_bingo.utils import clear, bolded, underlined


class Player(metaclass=ABCMeta):
    """Player class"""

    def __init__(self, name: str | None = None, card: Card = None):
        self.__name = name or "anonymous"
        self.__card = card if card is not None else Card()

    def __str__(self) -> str:
        return f"{bolded(underlined(self.name))} ({self.type})"

    def __eq__(self, other: object) -> bool:
        return self is other

    def __gt__(self, other: object) -> bool:
        return bool(self.card > cast(Player, other).card)

    @property
    def name(self) -> str:
        """Player name property"""
        return self.__name

    @property
    def card(self) -> Card:
        """Player card property"""
        return self.__card

    @property
    @abstractmethod
    def type(self) -> Literal["human", "computer"]:
        """Player type property"""
        raise NotImplementedError


@total_ordering
class HumanPlayer(Player):
    """HumanPlayer class"""

    @property
    def type(self) -> Literal["human"]:
        return "human"


@total_ordering
class ComputerPlayer(Player):
    """ComputerPlayer class"""

    @property
    def type(self) -> Literal["computer"]:
        return "computer"


def get_players(
    players_count: int | None = None, player_class: Type[ComputerPlayer] | Type[HumanPlayer] | None = None
) -> Iterator[ComputerPlayer | HumanPlayer]:
    """generate (yields) a player sequence"""

    if not players_count:
        print("Сколько игроков будет играть?")
        try:
            players_count = int(input())
        except ValueError:
            players_count = 0

    for i in range(players_count):
        clear()
        default_name = f"Игрок {i + 1}"

        if player_class:
            current_player_class = player_class
        else:
            print("Выберите тип игрока:")
            print("1. Компьютер")
            print("2. Человек")
            try:
                if (answer := int(input())) not in [1, 2]:
                    raise ValueError()
                current_player_class = ComputerPlayer if answer == 1 else HumanPlayer
            except ValueError:
                current_player_class = ComputerPlayer

        clear()
        name = input("Укажите имя игрока: ").strip() or default_name
        yield current_player_class(name, Card())
