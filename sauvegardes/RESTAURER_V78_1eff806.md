# Checkpoint complément natif V78

44 autres sources distinctes sont traduites dans47 scripts/90 plages originales. Deux copies du retour à la normale comptent une fois ; deux suffixes de fuite partagés ne comptent pas à nouveau. Les408 captures/204 paires couvrent les fenêtres0E/01, par appels isolés ; effets et parcours naturels non certifiés.113 tests distincts validés, dont112 dans la suite et un nouveau test de fenêtre01 séparément. Les53 aides PSI apprises ont une relecture bilingue statique bornée, sans nouvelle source comptée.

- Commit : `1eff8062f85bdca7153bdc567ca7699eff6c0452`
- Arbre : `ca0f1e0f49580311c2f87b429e05199c10275b63`
- Ref : `refs/heads/checkpoint/v78-native-messages`
- Prérequis : `2098424d8aa27e396642183c2de303eac933838e`
- Bundle : `EarthBound_FR_V78_1eff806.bundle`,1085589 octets
- SHA256 : `e55a716394bbbc4ce83c2ac03087e8f26d37a11e198a72276f3f340ec4a9e0e3`

Restaurer la chaîne décrite dans `RESTAURER_V78_2098424.md`, puis télécharger ce complément depuis la même branche :

```sh
git bundle verify EarthBound_FR_V78_1eff806.bundle
git fetch EarthBound_FR_V78_1eff806.bundle refs/heads/checkpoint/v78-native-messages:refs/heads/restored-native-messages
git rev-parse restored-native-messages restored-native-messages^{tree}
```

Les deux SHA attendus figurent ci-dessus. La restauration dans un dépôt distinct a reproduit le commit et l'arbre exactement. ROM, états, cœur et dumps mémoire ne sont jamais distribués.

Compteurs :102 nouvelles sources depuisfbd987c,351 historiques dont137 publiées/214 en attente,460 plages originales. Le lot400 reste ouvert, sans release ni mise à jourmain à ce jalon de protection. La traduction complète, les fins naturelles, les graphiques et la relecture intégrale ne sont pas déclarés achevés. Reprise : `REPRISE_TRADUCTION.md` et `RAPPORT_V78_MESSAGES_NATIFS_COMPLEMENT.md` du commit restauré.
