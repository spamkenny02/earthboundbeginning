# Restaurer le checkpoint interne V78 — enseignes

Ce complément conserve le commit `2233c85d521ccd8510d8972fd7345f67cabc852b`, arbre `18d4fe95354b273d782820bda726a6d579f15c35`. Ce n’est pas une release : dix nouvelles familles graphiques, 32 champs, 88 tests distincts validés ; le lot de 400 et l’achèvement général ne sont pas certifiés. Les circonflexes des enseignes de Podunk restent ouverts. Voir `RAPPORT_V78_ENSEIGNES.md` après restauration.

Le bundle `EarthBound_FR_V78_2233c85.bundle` nécessite le commit `32413fb0e3e02fa33ebbadf3ba4f5fd79d00a817`. Restaurer d’abord les trois bundles précédents dans cet ordre, selon leurs guides : `44984fc`, `f1425be`, puis `32413fb`. Copier les quatre bundles et leurs guides hors du répertoire de travail avant de changer de branche : les commits restaurés contiennent les sources et IPS, pas les bundles d’archivage.

Empreintes du complément :

- Taille : 1 190 472 octets.
- SHA-256 : `38e61427ae4200fa78640ba0fc26eb3d41812ea686ee88bf8856038c046ea9c6`.
- Objet blob Git : `efac2394d4419de6eadd87f2ef90abfe1f21ba95`.

Depuis le dépôt ayant déjà restauré `32413fb`, avec les bundles conservés à côté du dépôt :

```sh
git bundle verify ../bundles/EarthBound_FR_V78_2233c85.bundle
git fetch ../bundles/EarthBound_FR_V78_2233c85.bundle refs/heads/checkpoint/v78-town-signs:refs/heads/reprise-v78-enseignes
git switch reprise-v78-enseignes
git rev-parse HEAD
git rev-parse 'HEAD^{tree}'
```

Les deux dernières valeurs doivent être le commit et l’arbre indiqués en tête. La chaîne complète a été effectivement restaurée dans un dépôt privé initialement limité à V77 ; les valeurs correspondent. Les captures publiques et métadonnées y figurent, sans ROM, cœur, état ni dump mémoire.

IPS restaurés :

| Profil | SHA-256 du patch |
|---|---|
| Accents | `218e4eb502c13b1ec56cdcaaeec5d55a82b1fd59d567981a53eb5d2a13f64fb4` |
| ASCII | `ddbcf79688efa4acab3d64f6b34ad55aa8485eb858356014dd5ac4cdf0b4304a` |

Pour reconstruire et tester, fournir séparément la ROM et le cœur privés selon les scripts du dépôt. Leur absence interdit toute nouvelle affirmation de validation en émulation. Les résultats conservés sont ceux du checkpoint, avec déplacement natif préparé et accès naturel initial non certifié.
