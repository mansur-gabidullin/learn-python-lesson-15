"""Test Game Strategy Entity."""
from typing import Any
from unittest.mock import patch, PropertyMock, MagicMock

from src.lotto_bingo.card import Card
from src.lotto_bingo.constants import KEGS_COUNT
from src.lotto_bingo.game_strategy import GameStrategy, InitialGameState, MESSAGE_GAME_CONTINUE, MESSAGE_GAME_FINISHED
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
    def test_prepare_method(self, *_: Any) -> None:
        """checks prepare method"""
        strategy = GameStrategy()
        strategy.prepare()
        assert not strategy.winner

    @patch("src.lotto_bingo.game_strategy.get_players", return_value=[ComputerPlayer("Test", Card())])
    def test_prepare_method_with_empty_state(self, *_: Any) -> None:
        """checks prepare method with given an empty state"""
        state = InitialGameState()
        strategy = GameStrategy()
        strategy.prepare(state)
        assert not strategy.winner

    def test_prepare_method_with_custom_state(self, *_: Any) -> None:
        """checks prepare method with given a custom state"""
        computer = ComputerPlayer("custom computer", Card())
        state = InitialGameState(players=[computer], losers=[computer], kegs=KegsBag(list(range(KEGS_COUNT))))
        strategy = GameStrategy()
        strategy.prepare(state)
        assert not strategy.winner

    def test_prepare_method_with_incorrect_state(self, *_: Any) -> None:
        """checks prepare method with given an incorrect state"""
        state = InitialGameState(players=[], losers=[], kegs=KegsBag([]))
        strategy = GameStrategy()
        strategy.prepare(state)
        assert not strategy.winner

    def test_computer_move(self, *_: Any) -> None:
        """checks computer movement"""
        computer = ComputerPlayer("custom computer", Card([1]))
        state = InitialGameState(players=[computer], losers=[], kegs=KegsBag([1]))
        strategy = GameStrategy()
        strategy.prepare(state)
        strategy.cycle()
        assert strategy.winner == computer

    @patch("builtins.input", side_effect=("2", "2"))
    def test_human_move(self, *_: Any) -> None:
        """checks human movement"""
        human = HumanPlayer("custom human", Card([1]))
        state = InitialGameState(players=[human], losers=[], kegs=KegsBag([1]))
        strategy = GameStrategy()
        strategy.prepare(state)
        strategy.cycle()
        assert strategy.winner == human

    def test_not_showing_other_players_cards_when_others_not_exist(self, print_mock: MagicMock, *_: Any) -> None:
        """checks no cards is printed when no other players"""
        human = HumanPlayer("custom human")
        state = InitialGameState(players=[human])
        strategy = GameStrategy()
        strategy.prepare(state)
        strategy.show_other_players_cards(human)
        assert not print_mock.called

    @patch("builtins.input", return_value="2")
    def test_showing_only_computer_player_card(self, *_: Any) -> None:
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
    def test_showing_only_human_players_cards(self, *_: Any) -> None:
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
    def test_winner(self, *_: Any) -> None:
        """checks correct winner"""
        human = HumanPlayer("custom human", Card([1]))
        human2 = HumanPlayer("custom human 2", Card([1]))
        computer = ComputerPlayer("custom computer", Card([1]))
        state = InitialGameState(players=[human, human2, computer], losers=[], kegs=KegsBag([1]))
        strategy = GameStrategy()
        strategy.prepare(state)
        strategy.cycle()
        assert strategy.winner == human2

    def test_losers(self, *_: Any) -> None:
        """checks losers"""
        human = HumanPlayer("custom human", Card([1]))
        human2 = HumanPlayer("custom human 2", Card([1]))
        computer = ComputerPlayer("custom computer", Card([1]))
        state = InitialGameState(players=[human, human2, computer], losers=[human, human2, computer], kegs=KegsBag([1]))
        strategy = GameStrategy()
        strategy.prepare(state)
        strategy.cycle()
        assert not strategy.winner

    def test_continue_strategy_status(self, *_: Any) -> None:
        """checks continue strategy status"""
        human = HumanPlayer("custom human", Card([1]))
        state = InitialGameState(players=[human], kegs=KegsBag([1]))
        strategy = GameStrategy()
        strategy.prepare(state)
        assert MESSAGE_GAME_CONTINUE in str(strategy)

    def test_finished_strategy_status(self, *_: Any) -> None:
        """checks finished strategy status"""
        state = InitialGameState(players=[])
        strategy = GameStrategy()
        strategy.prepare(state)
        assert MESSAGE_GAME_FINISHED in str(strategy)

    def test_game_strategies_are_equal(self, *_: Any) -> None:
        """checks game strategies are equal"""
        strategy_one = GameStrategy()
        strategy_other = GameStrategy()
        assert strategy_one == strategy_other
        assert strategy_one != {"winner": None}

    def test_one_game_strategy_is_great_then_other(self, *_: Any) -> None:
        """checks game strategy is great then other"""
        strategy_one = GameStrategy()
        strategy_one.prepare(InitialGameState(players=[ComputerPlayer("test computer")]))
        strategy_other = GameStrategy()
        strategy_other.prepare(InitialGameState(players=[]))
        assert strategy_one > strategy_other
