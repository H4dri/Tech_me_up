"""Exercice 3 : générateurs et itérateurs.

Tests : uv run pytest modules/00-environnement/exercices/test_ex3_iterateurs.py
"""


def chunks(items, size):
    """Générateur qui découpe `items` en paquets de `size` éléments.

    list(chunks([1, 2, 3, 4, 5], 2))  ->  [[1, 2], [3, 4], [5]]

    Ce doit être un générateur (avec `yield`), pas une fonction qui renvoie une liste.
    """
    raise NotImplementedError


class Countdown:
    """Itérateur qui compte à rebours, écrit à la main, SANS `yield`.

    list(Countdown(3))  ->  [3, 2, 1]

    Il faut les deux méthodes spéciales du protocole d'itération.
    """
