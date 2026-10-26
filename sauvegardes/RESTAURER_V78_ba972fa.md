# Checkpoint V78 — alerte critique, raccrochage et nom réservé

Même lot400 ouvert :124 nouvelles sources depuisfbd987c,373 historiques/550 unités,137 publiées/236 en attente ;59 corrections françaises hors quota. Trois nouvelles sources, preuves alerte/contrôle/raccrochage260 références/130 paires/60 PNG et nommage naturel52 références/26 paires/19 PNG.46 différences limitées au texte.11 tests ciblés passent,152 distincts connus sans répétition globale152 ; reconstruction incrémentale exacte depuis5170b1a. Main demeure V77, ni400 ni100% certifiés.

- Commit : `ba972faa65ffee40e96499c2ffb2256ada076778`
- Arbre : `1b0881c441c4a5b9113302cc249e17df9f1e96f3`
- Ref : `refs/heads/checkpoint/v78-critical-name-validated`
- Prérequis : `5170b1a4a3be0598e55aa2129073945dc4af630a`
- Bundle : `EarthBound_FR_V78_ba972fa.bundle`,415227 octets
- SHA256 : `435b9614e3e0905348205368293cb8a60c103130be0265263458f5c8cd56aa18`

Restaurer la chaîne de `RESTAURER_V78_5170b1a.md`, puis :

```sh
git bundle verify EarthBound_FR_V78_ba972fa.bundle
git fetch EarthBound_FR_V78_ba972fa.bundle refs/heads/checkpoint/v78-critical-name-validated:refs/heads/checkpoint/v78-critical-name-validated
git show --stat ba972faa65ffee40e96499c2ffb2256ada076778
```

Vérifier commit/arbre avant fusion et préserver les modifications locales. L'ancien travail récupéré avant restauration5170b1a reste sous `checkpoint/recovered-local-before-5170b1a`. Ce checkpoint protège le lot en cours, ce n'est pas sa publication finale. Suite : question française tronquée du nommage d'Ana (hors quota), victoire instantanée, PNJ créés dynamiquement et inventaire global. Aucune ROM, aucun cœur, état ou dump mémoire inclus.
