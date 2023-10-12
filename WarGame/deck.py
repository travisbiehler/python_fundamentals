import random
from card import Card
from suit import Suit


class Deck:

    SUITS = ("clubs", "diamonds", "hearts", "spades")

    def __init__(self, is_empty=False):
        self._cards = []

        if not is_empty:
            self.build()
# by default deck will not be empty -> will build deck
        
    @property
    def size(self):
        return len(self._cards)
# determines size of deck


    def build(self):
        for suit in Deck.SUITS:
            for value in range(2,15):
                self._cards.append(Card(Suit(suit), value))
# builds deck within given values with suit


    def show(self):
        for card in self._cards:
            card.show()
# shows card 


    def shuffle(self):
        random.shuffle(self._cards)
# shuffles list of cards using random moodule


    def draw(self):
        if self._cards:
            return self._cards.pop()
        else:
            return None
# removes card from top of list using pop


    def add(self, card):
        self._cards.insert(0, card)
# adds cards won to winners deck