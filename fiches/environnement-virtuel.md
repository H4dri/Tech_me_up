---
titre: "uv et l'environnement virtuel (.venv)"
theme: Outils
tags: [python, uv, venv, dependances]
module: m0
date: 2026-10-22
---

## Le problème

Un projet a besoin de bibliothèques (FastAPI, uvicorn…) qui ne sont pas fournies avec Python. Si on les installe pour tout l'ordinateur, les projets se marchent dessus : l'un veut la version 1, l'autre la version 2.

## L'idée

Chaque projet a son **environnement virtuel**, un dossier `.venv` qui contient sa propre copie de Python et de ses bibliothèques. `uv` le crée et le remplit à partir de la liste déclarée dans `pyproject.toml` (versions figées dans `uv.lock`).

Le code se copie, l'environnement se **recrée** sur chaque machine.

uv lui-même est un programme installé sur le Mac (`~/.local/bin/uv`), **hors du dépôt**, comme Git. Dans le dépôt, il y a trois choses qu'il lit ou fabrique :

| Fichier | Image | Dans Git ? |
|---|---|---|
| `pyproject.toml` | la recette : de quoi le projet a besoin | oui |
| `uv.lock` | la liste de courses précise : les versions exactes | oui |
| `.venv/` | le placard : les bibliothèques réellement installées | non, uv le recrée |

## En pratique

```bash
uv add fastapi      # ajoute une dépendance (pyproject.toml + uv.lock + .venv)
uv add --dev pytest # une dépendance réservée aux développeurs
uv run python       # ouvre l'interpréteur interactif de l'environnement
uv run plateforme   # crée/met à jour .venv si besoin, puis lance la commande dedans
uv sync             # seulement mettre .venv à jour
rm -rf .venv        # le supprimer : uv le recrée au prochain lancement
```

## Pourquoi c'est comme ça

Avec une liste de dépendances écrite dans un fichier, n'importe qui peut reconstruire exactement le même environnement en une commande, sur n'importe quelle machine.

## Pièges

- `.venv` contient des chemins absolus : si on déplace le projet, il faut le supprimer et le laisser se recréer.
- `.venv` ne va pas dans Git (il est dans `.gitignore`) : il est lourd et propre à chaque machine.
- Ne pas mettre un projet de code dans un dossier synchronisé (iCloud, Dropbox…). La synchro peut supprimer des fichiers en local ou les marquer « cachés », et Python 3.12 ignore certains fichiers cachés de `.venv`.
