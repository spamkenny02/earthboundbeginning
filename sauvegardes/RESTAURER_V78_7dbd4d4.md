# Checkpoint V78 — fin alternative et commandes partagées

Même lot400 toujours ouvert :103 nouvelles sources depuisfbd987c,352 historiques,137 publiées/215 en attente,461 unités d’origine. Le nouveau titre À SUIVRE… compte une source ; Attendre et Tirer sont des occurrences partagées, sans recomptage.125 tests distincts validés (124 passent dans la suite, puis le contrôle de registre actualisé passe séparément). Deux IPS reconstruits identiques. Retrait et deux branches de fin observés depuis une scène complète préparée ; aucun parcours initial naturel certifié.

- Commit : `7dbd4d4182792804d4f6fc86943797d5b8ff8c4b`
- Arbre : `b168b2febd2f491b1282cbf0b3923cfce2c89517`
- Ref : `refs/heads/checkpoint/v78-alternate-ending`
- Prérequis : `4970cd47612ac7f2b3b60e48df7cbc90e7a34e99`
- Bundle : `EarthBound_FR_V78_7dbd4d4.bundle`,2151645 octets
- SHA256 : `69872d28da1cac378c3e82bd992098d98c86bb0f892cac0ebdb20196cbb80431`

Restaurer d’abord la chaîne de `RESTAURER_V78_4970cd4.md`, puis :

```sh
git bundle verify EarthBound_FR_V78_7dbd4d4.bundle
git fetch EarthBound_FR_V78_7dbd4d4.bundle refs/heads/checkpoint/v78-alternate-ending:refs/heads/restored-alternate-ending
git rev-parse restored-alternate-ending restored-alternate-ending^{tree}
```

La restauration dans un dépôt distinct reproduit commit et arbre exacts. Sources, IPS, captures et rapports sont inclus ; aucune ROM, aucun cœur, état ou dump mémoire. Consulter `RAPPORT_V78_FIN_ALTERNATIVE.md`, `RAPPORT_V78_COMMANDES_PARTAGEES.md` et la reprise. Main reste V77 ; ce checkpoint ne publie pas un micro-lot.
