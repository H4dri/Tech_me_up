---
titre: "Le cycle Git : status, add, commit, push"
theme: Outils
tags: [git, github, commit]
module: m0
date: 2026-10-25
---

## Le problème

On veut des points de retour fiables (« la version d'hier qui marchait ») et une copie hors de la machine. Une synchro comme iCloud ne fait ni l'un ni l'autre : elle recopie aussi les erreurs.

## L'idée

Un **commit** est une **photo** du projet, prise quand **tu** la demandes, avec une légende. Les photos s'enchaînent (chacune pointe vers la précédente) et forment l'historique, rangé dans `.git`. **GitHub** en garde une copie, mise à jour à chaque `git push`.

```
modifié  --git add-->  préparé  --git commit-->  historique local  --git push-->  GitHub
```

## En pratique

```bash
git status                  # où en suis-je ? (à taper sans modération)
git add .                   # prépare tout (sauf ce qui est dans .gitignore)
git commit -m "Ajoute la fiche sur Git"
git push                    # envoie les nouveaux commits sur GitHub
git log --oneline           # l'historique, une ligne par commit
git clone <adresse>         # récupère un dépôt entier sur une autre machine
```

Les trois états d'un fichier :

| État | Sens | Dans `git status` |
|---|---|---|
| **untracked** | jamais suivi : dans aucun commit, et pas de `git add` | `Untracked files` |
| **modified** | suivi, changé depuis le dernier commit, pas encore préparé | `Changes not staged for commit` |
| **staged** | préparé : entrera dans la prochaine photo | `Changes to be committed` |

Après un commit, les fichiers *staged* reviennent à l'état « rien à signaler ». Les *untracked* le restent.

## Pourquoi c'est comme ça

- **Deux temps (`add`, puis `commit`)** : pour choisir ce qui entre dans chaque photo et garder des commits nets, un sujet par commit.
- **Le hash** (`edd766c`) est calculé à partir du contenu. Changer une virgule donne un autre hash, donc personne ne peut modifier une photo en douce.
- **`.gitignore`** : ce qui se recrée (`.venv`) ou ce qui est propre à une machine ne se versionne pas.

## Pièges

- **Message de commit** : une ligne courte qui dit ce que **fait** le commit (« Ajoute… », « Corrige… »), pas l'état du projet. Relire la liste des fichiers pour ne rien oublier, et éviter le participe passé (« rajouté… »).
- `git rm --cached` retire de la préparation, mais `git rm` **sans** `--cached` efface aussi le fichier du disque.
- Un commit n'est pas sur GitHub tant qu'on n'a pas fait `git push`.
- Pour le premier push, créer le dépôt GitHub **vide** (sans README).
