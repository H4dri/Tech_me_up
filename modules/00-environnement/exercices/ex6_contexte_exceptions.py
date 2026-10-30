"""Exercice 6 : exceptions et gestionnaires de contexte (`with`).

Tests : uv run pytest modules/00-environnement/exercices/test_ex6_contexte_exceptions.py
"""


def parse_age(text):
    """Convertit une chaîne en âge (un entier positif ou nul).

    parse_age("42")   ->  42
    parse_age(" 7 ")  ->  7
    parse_age("abc")  ->  ValueError avec le message : âge invalide : 'abc'
    parse_age("-3")   ->  ValueError avec le message : âge négatif : -3
    """
    raise NotImplementedError


class Timer:
    """Gestionnaire de contexte qui mesure la durée d'un bloc `with`.

    with Timer() as timer:
        do_something()
    timer.elapsed  ->  la durée du bloc, en secondes (un float)

    Si le bloc lève une exception, elle ne doit pas être étouffée,
    et `elapsed` doit quand même être rempli.

    Utile : time.perf_counter() renvoie un instant précis, en secondes.
    """
