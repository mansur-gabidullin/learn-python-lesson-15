from src.lotto_bingo.Card import Card
from src.lotto_bingo.KegsBag import KegsBag
from src.lotto_bingo.Player import HumanPlayer, ComputerPlayer
from src.lotto_bingo.utils import clear, need_break, underlined, greened, blinked, bolded


class Game:
    def __init__(self, players_count: int = None, is_auto=False):
        if not is_auto:
            clear()
        self.__is_auto = is_auto
        self.__kegs = KegsBag()
        self.__players = list(self.__get_players(players_count))

    def __print(self, *args, **kwargs):
        if not self.__is_auto:
            print(*args, **kwargs)

    def __get_players(self, count: int = None):
        if not count:
            try:
                self.__print('Сколько игроков будет играть?')
                players_count = int(input())
            except ValueError:
                players_count = 0
        else:
            players_count = count

        for i in range(players_count):
            default_name = f'Игрок {i + 1}'

            if not self.__is_auto:
                clear()
                self.__print('Выберите тип игрока:')
                self.__print('1. Человек')
                self.__print('2. Компьютер')
                try:
                    get_player = HumanPlayer if int(input()) == 1 else ComputerPlayer
                except ValueError:
                    get_player = ComputerPlayer

                clear()
                name = input('Укажите имя игрока: ').strip() or default_name
                yield get_player(name, Card())
            else:
                yield ComputerPlayer(default_name, Card())

    def start(self):
        winner = None
        losers = []

        for _ in range(len(self.__kegs)):
            if winner:
                break

            keg = self.__kegs.get_next()

            for player in self.__players:
                if player in losers:
                    continue

                if not self.__is_auto:
                    clear()
                self.__print(f'Новый бочонок: {keg} (осталось {len(self.__kegs)})')
                self.__print(f'Ходит игрок по имени {player.name}')
                self.__print('Ваша карточка:')
                self.__print(player.card)

                if keg in player.card:
                    player.card.strike_out(keg)
                    if len(player.card) == 0:
                        winner = player
                        break

                if not self.__is_auto and need_break():
                    break

        if not self.__is_auto:
            clear()

        if not winner:
            self.__print('Победителя нет!')
        else:
            self.__print(f'Победил игрок {bolded(underlined(winner.name))}!')
            self.__print(blinked(greened(bolded('!!! ПОЗДРАВЛЯЕМ !!!'))))

        return winner
