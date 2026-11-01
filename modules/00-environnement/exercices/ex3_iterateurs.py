"""Exercice 3 : générateurs et itérateurs.

Tests : uv run pytest modules/00-environnement/exercices/test_ex3_iterateurs.py
"""


def chunks(items, size):
    """Générateur qui découpe `items` en paquets de `size` éléments.

    list(chunks([1, 2, 3, 4, 5], 2))  ->  [[1, 2], [3, 4], [5]]

    Ce doit être un générateur (avec `yield`), pas une fonction qui renvoie une liste.
    """
    if size <= 0 :
        raise ValueError("Size must be a positive integer")
    rank = 0
    while rank < len(items) :
        yield items[rank: rank + size]
        rank += size
    '''for loop in range(int(len(items)/size)) :
        yield items[rank+loop:size]'''


class Countdown:              #list(Countdown(3))  ->  [3, 2, 1]
    
    def __init__(self,start) :
        self.n = int(start)
    
    def __iter__(self) :
        return self
    
    def __next__(self) :
        if self.n < 1:
            raise StopIteration
        result = self.n
        self.n = self.n - 1
        return result
        

