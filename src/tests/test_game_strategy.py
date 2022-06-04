"""Test Game Strategy Entity."""
from typing import Any, Iterable
from unittest.mock import patch, PropertyMock, MagicMock

from src.lotto_bingo.card import Card
from src.lotto_bingo.constants import KEGS_COUNT
from src.lotto_bingo.game_strategy import GameStrategy, InitialGameState
from src.lotto_bingo.kegs_bag import KegsBag
from src.lotto_bingo.player import ComputerPlayer, HumanPlayer
from src.lotto_bingo.utils import identity


# pylint: disable=no-self-use
@patch("builtins.print", return_value="")
@patch("src.lotto_bingo.game_strategy.need_break", return_value=False)
@patch("src.lotto_bingo.game_strategy.wait", return_value=None)
@patch("src.lotto_bingo.game_strategy.clear", return_value=None)
@patch("src.lotto_bingo.game_strategy.blinked", side_effect=identity)
@patch("src.lotto_bingo.game_strategy.bolded", side_effect=identity)
@patch("src.lotto_bingo.game_strategy.underlined", side_effect=identity)
class TestGameStrategy:
    """Test GameStrategy class"""

    @patch("src.lotto_bingo.game_strategy.get_players", return_value=[ComputerPlayer("Test", Card())])
    def test_prepare_method(self, *_: Iterable[Any]) -> None:
        """checks prepare method"""
        strategy = GameStrategy()
        strategy.prepare()
        assert not strategy.winner

    @patch("src.lotto_bingo.game_strategy.get_players", return_value=[ComputerPlayer("Test", Card())])
    def test_prepare_method_with_empty_state(self, *_: Iterable[Any]) -> None:
        """checks prepare method with given an empty state"""
        state = InitialGameState()
        strategy = GameStrategy()
        strategy.prepare(state)
        assert not strategy.winner

    def test_prepare_method_with_custom_state(self, *_: Iterable[Any]) -> None:
        """checks prepare method with given a custom state"""
        computer = ComputerPlayer("custom computer", Card())
        state = InitialGameState(players=[computer], losers=[computer], kegs=KegsBag(list(range(KEGS_COUNT))))
        strategy = GameStrategy()
        strategy.prepare(state)
        assert not strategy.winner

    def test_prepare_method_with_incorrect_state(self, *_: Iterable[Any]) -> None:
        """checks prepare method with given an incorrect state"""
        state = InitialGameState(players=[], losers=[], kegs=KegsBag([]))
        strategy = GameStrategy()
        strategy.prepare(state)
        assert not strategy.winner

    def test_computer_move(self, *_: Iterable[Any]) -> None:
        """checks computer movement"""
        computer = ComputerPlayer("custom computer", Card([1]))
        state = InitialGameState(players=[computer], losers=[], kegs=KegsBag([1]))
        strategy = GameStrategy()
        strategy.prepare(state)
        strategy.cycle()
        assert strategy.winner == computer

    @patch("builtins.input", side_effect=("2", "2"))
    def test_human_move(self, *_: Iterable[Any]) -> None:
        """checks human movement"""
        human = HumanPlayer("custom human", Card([1]))
        state = InitialGameState(players=[human], losers=[], kegs=KegsBag([1]))
        strategy = GameStrategy()
        strategy.prepare(state)
        strategy.cycle()
        assert strategy.winner == human

    def test_not_showing_other_players_cards_when_others_not_exist(
        self, print_mock: MagicMock, *_: Iterable[Any]
    ) -> None:
        """checks no cards is printed when no other players"""
        human = HumanPlayer("custom human")
        state = InitialGameState(players=[human])
        strategy = GameStrategy()
        strategy.prepare(state)
        strategy.show_other_players_cards(human)
        assert not print_mock.called

    @patch("builtins.input", return_value="2")
    def test_showing_only_computer_player_card(self, *_: Iterable[Any]) -> None:
        """checks only computer player is printed"""

        with patch("src.lotto_bingo.player.HumanPlayer.card", PropertyMock()) as human_card_mock:
            with patch("src.lotto_bingo.player.ComputerPlayer.card", PropertyMock()) as computer_card_mock:
                human = HumanPlayer("custom human")
                computer = ComputerPlayer("custom computer")
                state = InitialGameState(players=[human, computer])
                strategy = GameStrategy()
                strategy.prepare(state)
                strategy.show_other_players_cards(human)

                assert not human_card_mock.called
                assert computer_card_mock.called

    @patch("builtins.input", return_value="2")
    def test_showing_only_human_players_cards(self, *_: Iterable[Any]) -> None:
        """checks only human player is printed"""

        with patch("src.lotto_bingo.player.HumanPlayer.card", PropertyMock()) as human_card_mock:
            with patch("src.lotto_bingo.player.ComputerPlayer.card", PropertyMock()) as computer_card_mock:
                human = HumanPlayer("custom human")
                computer = ComputerPlayer("custom computer")
                state = InitialGameState(players=[human, computer])
                strategy = GameStrategy()
                strategy.prepare(state)
                strategy.show_other_players_cards(computer)

                assert human_card_mock.called
                assert not computer_card_mock.called

    @patch("builtins.input", side_effect=("2", "-1", "-1", "2"))
    def test_winner(self, *_: Iterable[Any]) -> None:
        """checks correct winner"""
        human = HumanPlayer("custom human", Card([1]))
        human2 = HumanPlayer("custom human 2", Card([1]))
        computer = ComputerPlayer("custom computer", Card([1]))
        state = InitialGameState(players=[human, human2, computer], losers=[], kegs=KegsBag([1]))
        strategy = GameStrategy()
        strategy.prepare(state)
        strategy.cycle()
        assert strategy.winner == human2

    def test_losers(self, *_: Iterable[Any]) -> None:
        """checks losers"""
        human = HumanPlayer("custom human", Card([1]))
        human2 = HumanPlayer("custom human 2", Card([1]))
        computer = ComputerPlayer("custom computer", Card([1]))
        state = InitialGameState(players=[human, human2, computer], losers=[human, human2, computer], kegs=KegsBag([1]))
        strategy = GameStrategy()
        strategy.prepare(state)
        strategy.cycle()
        assert not strategy.winner
