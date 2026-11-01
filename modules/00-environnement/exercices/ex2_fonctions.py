"""Exercice 2 : fonctions (*args, **kwargs, closures).

Tests : uv run pytest modules/00-environnement/exercices/test_ex2_fonctions.py
"""
"""Renvoie la moyenne de tous les nombres passés en arguments.

    average(2, 4, 6)  ->  4.0
    average()         ->  lève une ValueError (et pas une ZeroDivisionError)
"""


def average(*numbers):
    if len(numbers) == 0 :
        raise ValueError
    result = 0
    for x in numbers :
        result += x
    result = result / len(numbers)
    return result



def describe(name, **details):
    """Décrit un objet à partir d'un nom et d'un nombre quelconque de détails nommés.

    describe("Rex", species="dog", age=3)  ->  "Rex (species=dog, age=3)"
    describe("Rex")                        ->  "Rex"
    """
    if not details:
        return name
    carc = ", ".join(f"{cle}={valeur}" for cle, valeur in details.items())
    return f"{name} ({carc})"


def make_counter(start=0):
    """Renvoie une fonction qui, à chaque appel, renvoie le nombre suivant.

    counter = make_counter()
    counter()  ->  1
    counter()  ->  2

    make_counter(10) : le premier appel renvoie 11.
    Deux compteurs créés séparément ne se mélangent pas.
    """
    n = start
    while True :
        n += 1
        yield n
    