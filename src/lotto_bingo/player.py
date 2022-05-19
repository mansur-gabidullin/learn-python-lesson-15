"""Player Entity."""
from abc import ABCMeta, abstractmethod
from typing import Literal

from src.lotto_bingo.card import Card

PlayerType = Literal["human", "computer"]


class Player(metaclass=ABCMeta):
    """Player class"""

    def __init__(self, name: str, card: Card = None):
        self.__name, self.__card = name, card

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
    def type(self) -> PlayerType:
        """Player type property"""
        raise NotImplementedError


class HumanPlayer(Player):
    """HumanPlayer class"""

    @property
    def type(self) -> Literal["human"]:
        return "human"


class ComputerPlayer(Player):
    """ComputerPlayer class"""

    @property
    def type(self) -> Literal["computer"]:
        return "computer"
