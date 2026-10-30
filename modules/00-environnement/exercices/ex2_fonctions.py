"""Exercice 2 : fonctions (*args, **kwargs, closures).

Tests : uv run pytest modules/00-environnement/exercices/test_ex2_fonctions.py
"""


def average(*numbers):
    """Renvoie la moyenne de tous les nombres passés en arguments.

    average(2, 4, 6)  ->  4.0
    average()         ->  lève une ValueError (et pas une ZeroDivisionError)
    """
    raise NotImplementedError


def describe(name, **details):
    """Décrit un objet à partir d'un nom et d'un nombre quelconque de détails nommés.

    describe("Rex", species="dog", age=3)  ->  "Rex (species=dog, age=3)"
    describe("Rex")                        ->  "Rex"
    """
    raise NotImplementedError


def make_counter(start=0):
    """Renvoie une fonction qui, à chaque appel, renvoie le nombre suivant.

    counter = make_counter()
    counter()  ->  1
    counter()  ->  2

    make_counter(10) : le premier appel renvoie 11.
    Deux compteurs créés séparément ne se mélangent pas.
    """
    raise NotImplementedError
