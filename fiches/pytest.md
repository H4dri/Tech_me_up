---
titre: Tester son code avec pytest
theme: Python
tags: [python, tests, pytest]
module: m0
date: 2026-11-01
---

## Le problème

Vérifier son code à la main (un `print`, on regarde, on recommence) est lent, et on oublie de revérifier ce qui marchait déjà. Une correction à un endroit en casse une autre sans qu'on le voie.

## L'idée

On écrit, une fois pour toutes, des **exemples avec leur résultat attendu**. pytest est un programme qui les exécute tous en une commande et dit lesquels échouent.

## En pratique

```bash
uv add --dev pytest                       # une fois par projet
uv run pytest chemin/test_fichier.py      # lancer les tests d'un fichier
uv run pytest chemin/                     # lancer tous les tests d'un dossier
```

```python
from ex1_comprehensions import squares_of_evens   # le code à tester

def test_squares_of_evens():                      # pytest exécute chaque fonction test_...
    assert squares_of_evens([1, 2, 3, 4]) == [4, 16]
```

- pytest cherche les fichiers `test_*.py`, puis les fonctions `test_*` qu'ils contiennent.
- `assert condition` : si la condition est fausse, le test échoue, et pytest affiche la valeur obtenue à côté de la valeur attendue.
- `with pytest.raises(ValueError):` vérifie qu'une erreur est bien levée.

## Pourquoi c'est comme ça

- `--dev` : pytest sert aux développeurs, pas à l'app. Un serveur qui fait tourner l'app n'a pas besoin de lui.
- Tout passer en revue à chaque fois coûte une seconde et garantit qu'on n'a rien cassé ailleurs.

## Pièges

- Un test qui semble « planté » cache souvent une boucle infinie dans le code testé. `Ctrl+C` pour l'arrêter.
- Lire le message d'échec avant de toucher au code : il dit souvent exactement ce qui cloche (`'generator' object is not callable`).
