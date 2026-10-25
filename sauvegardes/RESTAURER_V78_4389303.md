# Restaurer la relecture bilingue des objets

Complément du jalon4389303e42576eeac3d96b34572d2c6ab6c62af2, arbre5a947879514e0d2f6333471004405523cd2cb117. Il conserve aussi la confirmationb3190e7 du jalon précédent.

Restaurer la chaîne jusqu’àb613ca6 avec RESTAURER_V78_b613ca6.md, puis :

```
git bundle verify EarthBound_FR_V78_4389303.bundle
git fetch EarthBound_FR_V78_4389303.bundle checkpoint/v78-item-fidelity:checkpoint/v78-item-fidelity
git switch checkpoint/v78-item-fidelity
```

Prérequisb613ca66b94972b01f92e0d60512204dbda8ac28 ;654267 octets ; SHA2567818fee7cecd98476f2ae21b676a36139018be25676cabcd3e225963688c8ae3 ; blobGit092c86bc4cf04af16fcea78471f03a375620de17. Restauration locale, commit et arbre identiques vérifiés.

153 fiches relues,203 plages principales alphabétiques ;13 champs français corrigés,140 captures/70 paires,104 tests réussis. Compteurs inchangés :15 nouvelles sources depuisfbd987c,264 historiques. Zéro nouvelle source pour cette relecture. Voir RAPPORT_V78_FIDELITE_OBJETS.md et ses limites.

Pas de ROM, cœur, état ou dump. Pas de release ni mise à jourmain ; lot400 et finalisation encore ouverts. Dépôt actuelspamkenny02/earthboundbeginning, même identifiant1411795251 que l’ancienne URL.
