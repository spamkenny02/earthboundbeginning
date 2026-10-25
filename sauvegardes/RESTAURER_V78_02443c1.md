# Checkpoint V78 — avertissements du menu

Même lot400 ouvert :116 nouvelles sources depuisfbd987c,365 historiques,137 publiées/228 en attente ;504 unités/plages sources. Deux nouveaux avertissements du menu Util./PSI,72 références/36 paires/23 PNG, six différences confinées au texte. Le contrôle PV+ avec PP suffisants reste inchangé,257→252 PP.15 tests ciblés passent :143 distincts connus, sans répétition globale143. Reconstruction incrémentale gardée depuis78ffca5 identique. Main reste V77 ; aucun400 ni100% certifié.

- Commit : `02443c1d3cb269369556f2e859118aee1ccbd49a`
- Arbre : `d6813e71cfc4e2647b2bfc8fb55264bf0e5f264a`
- Ref : `refs/heads/checkpoint/v78-native-field-refusals-validated`
- Prérequis : `78ffca54ac1e30b0080bb930dd5a6b1ce0929ea1`
- Bundle : `EarthBound_FR_V78_02443c1.bundle`,154020 octets
- SHA256 : `d21d24c756266fc0e8faccbfa30616559b2d14e535ce5a554cd68c01cb06edf0`

Restaurer la chaîne de `RESTAURER_V78_78ffca5.md`, puis :

```
git bundle verify EarthBound_FR_V78_02443c1.bundle
git fetch EarthBound_FR_V78_02443c1.bundle refs/heads/checkpoint/v78-native-field-refusals-validated:refs/heads/checkpoint/v78-native-field-refusals-validated
git switch -c reprise-v78-avertissements checkpoint/v78-native-field-refusals-validated
git rev-parse HEAD HEAD^{tree}
```

Voir `RAPPORT_V78_AVERTISSEMENTS_MENU.md` pour les préparations natives et leurs limites. Le bundle ne distribue ni ROM, cœur, état privé ni dump mémoire.
