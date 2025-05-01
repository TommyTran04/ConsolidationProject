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

    
