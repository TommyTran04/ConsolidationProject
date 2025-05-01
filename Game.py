import os
import json #this is for saving purposes
import random # this is randomly drawing cards and such

class Card: #This serves as the main identifier for cards of all types EXCEPT King cards
    def __init__(self, suit: str, rank: str):
        self.suit = suit
        self.rank = rank

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def __repr__(self) -> str:
        return f"Card('{self.suit}', '{self.rank}')"

  @property
  def value(self) -> int:
        rank_values = {
            'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5,
            '6': 6, '7': 7, '8': 8, '9': 9,
            '10': 10, 'Jack': 11, 'Queen': 12
        }
        return rank_values[self.rank]


class Deck: #This serves as the deck on hand that YOU the player will have.
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        self.discard_pile = []

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, count: int) -> List[Card]:
        return [self.cards.pop() for _ in range(min(count, len(self.cards)))]

    def reveal_card(self) -> Optional[Card]:
        if self.cards:
            card = self.cards.pop()
            self.discard_pile.append(card)
            return card
        return None

    
