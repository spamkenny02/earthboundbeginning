# Checkpoint V78 — marchand d’armes

Même lot400 ouvert :106 nouvelles sources depuisfbd987c,355 historiques,137 publiées/218 en attente ;464 unités/plages d’origine. Deux réparations françaises supplémentaires,57 au total hors quota. Le marchand est vérifié après véritable confiscation préparée : refus, paiement52 dollars, restitution, stock vide.144 références/72 paires/59 PNG. Les anciennes affirmations d’équipement basées sur le retour du don sont retirées.136 tests distincts validés :135 dans la suite globale, puis correction et retest du registre ; zéro ignoré. Reconstruction complète identique dans les deux profils. Aucun400 ni100% certifié ; main reste V77.

- Commit : `afe23eda2a6100ba49516d59497e7d983d08879a`
- Arbre : `0be1ce200d920b0f34024b6881c0da4ec39152dd`
- Ref : `refs/heads/checkpoint/v78-arms-service-validated`
- Prérequis : `088247d6acabead46444aa7b5d162af51608d4a6`
- Bundle : `EarthBound_FR_V78_afe23ed.bundle`,366627 octets
- SHA256 : `15299ffa8287831cdaa406ae8f7a33076ceb502b7f9be063a86ced99935c6c21`

Restaurer la chaîne de `RESTAURER_V78_088247d.md`, puis :

```
git bundle verify EarthBound_FR_V78_afe23ed.bundle
git fetch EarthBound_FR_V78_afe23ed.bundle refs/heads/checkpoint/v78-arms-service-validated:refs/heads/checkpoint/v78-arms-service-validated
git switch -c reprise-v78-marchand checkpoint/v78-arms-service-validated
git rev-parse HEAD HEAD^{tree}
```

Le bundle ne contient ni ROM, cœur, état privé ni dump mémoire. Les essais et leurs limites sont décrits dans `RAPPORT_V78_MARCHAND_ARMES.md` et `RAPPORT_V78_PREPARATION_EQUIPEMENT.md`.
