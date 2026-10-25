# Checkpoint V78 — transferts d’objets

Même lot400 ouvert :114 nouvelles sources depuisfbd987c,363 historiques,137 publiées/226 en attente ;501 unités/plages sources. Huit messages nouvellement traduits du sous-menu Donne et deux réparations françaises hors quota (59 cumulées).432 références/216 paires/96 PNG,30 différences limitées au texte et à sa flèche ;96 témoins d’inventaire.139 tests réussis dans la suite140, puis correction et retest réussi du compteur natif :140 distincts validés, aucune deuxième suite globale140 revendiquée. Reconstruction complète identique. Main reste V77 ; aucun400 ni100% certifié.

- Commit : `78ffca54ac1e30b0080bb930dd5a6b1ce0929ea1`
- Arbre : `271d752ccd7c17445622728f46077ecd449f5ba2`
- Ref : `refs/heads/checkpoint/v78-inventory-transfers-validated`
- Prérequis : `afe23eda2a6100ba49516d59497e7d983d08879a`
- Bundle : `EarthBound_FR_V78_78ffca5.bundle`,507555 octets
- SHA256 : `c14c1a5e641e13b236f1c26320722cb9b27a8f396485a96b66975f755abfde72`

Restaurer la chaîne de `RESTAURER_V78_afe23ed.md`, puis :

```
git bundle verify EarthBound_FR_V78_78ffca5.bundle
git fetch EarthBound_FR_V78_78ffca5.bundle refs/heads/checkpoint/v78-inventory-transfers-validated:refs/heads/checkpoint/v78-inventory-transfers-validated
git switch -c reprise-v78-transferts checkpoint/v78-inventory-transfers-validated
git rev-parse HEAD HEAD^{tree}
```

Les inventaires et états sont préparés par commandes natives puis le sous-menu ordinaire exerce les vrais transferts/refus ; aucun appel direct des messages. Voir `RAPPORT_V78_TRANSFERTS_INVENTAIRE.md`. Ni ROM, cœur, état privé ni dump mémoire dans ce bundle.
