# Checkpoint PSI / combat natif V78

Ce complément protège43 nouvelles sources traduites (17 aides PSI et26 messages de combat) et leur validation bornée. Le lot400 reste ouvert, main reste V77. Les276 captures/138 paires ne prouvent pas les effets ni les acquisitions naturelles.109 tests distincts validés (108 dans la suite, contrôle de compteur actualisé relancé séparément).

- Commit local : `2098424d8aa27e396642183c2de303eac933838e`
- Arbre : `c61e910e1fa0a80849f79d3ff715b859f27d3e49`
- Ref dans le bundle : `refs/heads/checkpoint/v78-native-battle-psi`
- Prérequis : `8b0ac2a9e3d2ae1bc9a2732751e8c4be2df4d38f`
- Fichier : `EarthBound_FR_V78_2098424.bundle`,860582 octets
- SHA256 : `6bb62cd27b73db11a88e6d467fa60682cba5c66301bc8b04df8bf2e331f15962`

Restaurer d'abord la chaîne du guide `RESTAURER_V78_8b0ac2a.md`, puis télécharger ce complément depuis cette même branche de sauvegarde. Dans le dépôt restauré :

```sh
git bundle verify EarthBound_FR_V78_2098424.bundle
git fetch EarthBound_FR_V78_2098424.bundle refs/heads/checkpoint/v78-native-battle-psi:refs/heads/restored-native-battle-psi
git rev-parse restored-native-battle-psi restored-native-battle-psi^{tree}
```

Les deux SHA attendus sont ceux ci-dessus. La restauration a été essayée dans un dépôt distinct et l'arbre correspond exactement. Les états, cœur d'émulation, ROM et dumps mémoire restent privés ; aucun n'est dans ce bundle.

Compteurs :58 nouvelles sources depuisfbd987c,307 historiques (137 publiées/170 en attente),370 plages originales. Les corrections françaises et les traductions partagées ne sont pas recomptées. Suite détaillée dans `REPRISE_TRADUCTION.md` et `RAPPORT_V78_PSI_COMBAT_NATIF.md` du commit restauré ; autres lecteurs de combat, graphiques/fins, puis relecture complète restent ouverts.
