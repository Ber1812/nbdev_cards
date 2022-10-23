# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_deck.ipynb.

# %% auto 0
__all__ = ['Deck']

# %% ../nbs/01_deck.ipynb 3
from .card import *

# %% ../nbs/01_deck.ipynb 5
class Deck:
    def __init__(self): self.cards = [Card(s,r) for s in range (4) for r in range (1, 14)]
    def __str__(self): return '; '.join(map(str, self.cards))
    __repr__ = __str__
