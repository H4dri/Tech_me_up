"""Exercice 5 : écrire des décorateurs.

Tests : uv run pytest modules/00-environnement/exercices/test_ex5_decorateurs.py
"""


def count_calls(func):
    """Décorateur qui compte les appels de la fonction décorée.

    @count_calls
    def greet(name):
        return f"salut {name}"

    greet("Ada")     ->  "salut Ada"   (le résultat ne change pas)
    greet("Alan")
    greet.calls      ->  2
    greet.__name__   ->  "greet"       (et pas "wrapper")

    La fonction décorée peut avoir n'importe quels arguments.
    """
    raise NotImplementedError


def repeat(times):
    """Bonus : un décorateur qui prend lui-même un argument.

    @repeat(3)
    def roll():
        ...

    roll()  ->  appelle la fonction d'origine 3 fois, et renvoie la liste des 3 résultats.
    """
    raise NotImplementedError
