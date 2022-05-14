from abc import ABCMeta, abstractmethod

from src.lotto_bingo.Card import Card


class Player(metaclass=ABCMeta):
    def __init__(self, name: str, card: Card = None):
        self.__name, self.__card = name, card

    @property
    def name(self) -> str:
        return self.__name

    @property
    def card(self) -> Card:
        return self.__card

    @property
    @abstractmethod
    def type(self) -> str:
        raise NotImplementedError


class HumanPlayer(Player):
    @property
    def type(self):
        return 'human'


class ComputerPlayer(Player):
    @property
    def type(self):
        return 'computer'
