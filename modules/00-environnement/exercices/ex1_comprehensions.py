"""Exercice 1 : compréhensions et dictionnaires.

Remplace chaque `raise NotImplementedError` par ton code.
Tests : uv run pytest modules/00-environnement/exercices/test_ex1_comprehensions.py
"""


def squares_of_evens(numbers):
    """Renvoie la liste des carrés des nombres pairs de `numbers`, dans l'ordre.

    squares_of_evens([1, 2, 3, 4])  ->  [4, 16]

    Contrainte : le corps tient en une ligne, avec une compréhension de liste.
    """
    return [x**2 for x in numbers if x % 2 == 0]


def count_words(text):
    """Compte les mots d'un texte, sans tenir compte des majuscules.

    count_words("Le chat et le chien")  ->  {"le": 2, "chat": 1, "et": 1, "chien": 1}

    Les mots sont séparés par des espaces. Pas de ponctuation à gérer.
    """
    text = text.lower()
    texte_en_liste = text.split()
    LeDict = {}
    for mot in texte_en_liste :
        LeDict[mot] = texte_en_liste.count(mot)
    #rep = {mot : texte_en_liste.count(mot) for mot in texte_en_liste}
    return LeDict
