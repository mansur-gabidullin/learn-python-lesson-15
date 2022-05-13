from src.lotto_bingo.Card import Card
from src.lotto_bingo.KegsBag import KegsBag
from src.lotto_bingo.utils import clear


class Game:
    def __init__(self):
        self.card = Card()
        self.kegs_bag = KegsBag()

    def start(self):
        clear()
        keg_number = self.kegs_bag.get_next()

        print(keg_number)

        if keg_number in self.card:
            print('found')
            self.card.strike_out(keg_number)

        print(self.card)
