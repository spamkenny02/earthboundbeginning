# Checkpoint V78 — sac plein et ciblage

Même gros lot400 ouvert :105 nouvelles sources depuisfbd987c,354 historiques,137 publiées/217 en attente ;463 unités/plages d’origine. Deux nouvelles sources Jeter/Annuler, quatre occurrences Oui/Non partagées sans recomptage. Une correction française de ciblage porte à55 les corrections de phrases hors quota.130 tests globaux passent, zéro erreur ou ignoré ; reconstruction identique des deux IPS.

- Commit : `bd9b803d1cb9f86ea96d1cf14e170a83bbf811d6`
- Arbre : `620d68df8161376fd8ebfd6b784a15e394114412`
- Ref : `refs/heads/checkpoint/v78-full-bag-row-validated`
- Prérequis : `7dbd4d4182792804d4f6fc86943797d5b8ff8c4b`
- Bundle : `EarthBound_FR_V78_bd9b803.bundle`,294319 octets
- SHA256 : `de7fb5d26b23b971104dc324eb3ef62d289fd34168e543d5db5d6fb969cb7d33`

Restaurer la chaîne de `RESTAURER_V78_7dbd4d4.md`, puis :

```sh
git bundle verify EarthBound_FR_V78_bd9b803.bundle
git fetch EarthBound_FR_V78_bd9b803.bundle refs/heads/checkpoint/v78-full-bag-row-validated:refs/heads/restored-full-bag-row
git rev-parse restored-full-bag-row restored-full-bag-row^{tree}
```

La restauration dans un dépôt distinct reproduit commit/arbre exacts. Les trois choix de butin ont des effets d’inventaire observés après un vrai combat préparé ; aucun trajet initial naturel certifié.88 paires de captures,84 strictes et4 déphasages sombres du fond explicitement séparés. Voir `RAPPORT_V78_SAC_PLEIN_CIBLAGE.md`. Sources, IPS, PNG et rapports seulement : aucune ROM, aucun cœur, état ou dump mémoire. Main reste V77, sans publication de micro-lot.
