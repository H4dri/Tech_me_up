# Test de positionnement Python, partie 2 : bilan

*Séance du 2026-11-01. Six exercices à coder, vérifiés par des tests pytest, dans `modules/00-environnement/exercices/`.*

## Résultats

| Exercice | Thème | Résultat |
|---|---|---|
| 1 | Compréhensions, dictionnaires | ✅ |
| 2 | `*args`, `**kwargs`, closures | `average` ✅, `describe` ✅ après correction, `make_counter` ❌ |
| 3 | Générateurs, itérateurs | `chunks` ✅, `Countdown` ❌ |
| 4 | POO : classe, héritage, `__repr__` | ✅ |
| 5 | Décorateurs, y compris avec argument | ✅ |
| 6 | Exceptions, gestionnaire de contexte | ✅ |

**Solide :** POO, décorateurs, exceptions, `with`, compréhensions.
**À travailler :** ce que fabrique une fonction qui contient `yield`, les closures, le style « pro ».

## La leçon du jour : une fonction avec `yield` n'exécute pas son corps

L'expérience à refaire dans l'interpréteur (`uv run python`) :

```python
def f():
    print("je démarre")
    return 42

def g():
    print("je démarre")
    yield 42

f()          # affiche « je démarre », renvoie 42
g()          # n'affiche RIEN, renvoie <generator object g at 0x...>
x = g()
next(x)      # maintenant seulement : « je démarre », puis 42
```

Quand Python **lit** un `def`, il regarde si le corps contient un `yield`. Si oui, la fonction devient une **fabrique de générateurs** : l'appeler construit une machine en pause, avec le marque-page posé avant la première ligne. Le corps ne démarre qu'au premier `next()`.

*Pourquoi :* un générateur produit ses valeurs à la demande, parfois sans fin. Si l'appel exécutait le corps, un générateur infini ne rendrait jamais la main.

### Pourquoi `Countdown` bouclait à l'infini

```python
class Countdown:
    def __next__(self):
        if self.n < 1:
            raise StopIteration
        result = self.n
        self.n = self.n - 1
        yield result          # ← le problème
```

`next(countdown)` appelle `countdown.__next__()`. Comme `__next__` contient un `yield`, l'appel renvoie **un nouveau générateur en pause**, et pas un nombre. Aucune ligne du corps ne s'exécute : `self.n` ne baisse jamais, et `StopIteration` n'arrive jamais. `list()` empile alors des générateurs sans fin.

**Règle :** dans un itérateur écrit à la main, `__next__` **renvoie** (`return`) une valeur. On écrit **soit** une classe avec `__iter__` et `__next__`, **soit** une fonction avec `yield`, mais pas un mélange des deux.

Même confusion dans `make_counter` : la fonction devait **renvoyer une fonction** (une closure). Avec un `yield`, elle renvoyait un générateur, que le test ne pouvait pas appeler (`'generator' object is not callable`).

## Remarques de style (à travailler dans le module 1)

- Noms **en anglais** et en `snake_case` : `word_list` plutôt que `texte_en_liste`, `counts` plutôt que `LeDict`. Les majuscules sont réservées aux classes.
- Pas d'espace avant les deux-points : `if x > 0:`, pas `if x > 0 :`.
- Les `import` se mettent en haut du fichier, pas dans les méthodes.
- Ne pas recopier `__repr__` dans la classe fille juste pour changer le nom : `type(self).__name__` donne le nom de la classe réelle.
- Pour un décorateur, `functools.wraps` copie le nom, la docstring et le reste. C'est plus sûr que `wrapper.__name__ = ...`.
- La seconde version de `describe` est le bon réflexe : `", ".join(f"{key}={value}" for key, value in details.items())` plutôt que de construire la chaîne morceau par morceau.

## Au passage : uv et pytest

```
Tech_me_up/
├── pyproject.toml   ← la recette : les dépendances du projet (versionnée)
├── uv.lock          ← les versions exactes de chaque paquet (versionnée)
└── .venv/           ← les bibliothèques installées, recréées par uv (ignorée par Git)
```

uv lui-même est un programme installé sur le Mac (`~/.local/bin/uv`), hors du dépôt, comme Git. `uv add --dev pytest` ajoute pytest à la recette, en tant qu'outil de développeur dont l'app n'a pas besoin pour tourner. Il met aussi à jour `uv.lock`, puis installe pytest dans `.venv`. Un commit qui contient ces changements **ajoute pytest aux dépendances**, il n'installe rien.
