# Restaurer le jalon Snowman et pilote

Ce complément sauvegarde le commit local b613ca66b94972b01f92e0d60512204dbda8ac28, arbre a4e65afbb25a32d28923f44a159d75d987312430. Il inclut aussi le jalon de relecture4ec7bc4 et la confirmation89a0617. Pas de release ni de mise à jourmain.

Restaurer d’abord la chaîne de bundles jusqu’à584e8b6 décrite dans RESTAURER_V78_584e8b6.md. Puis :

```
git bundle verify EarthBound_FR_V78_b613ca6.bundle
git fetch EarthBound_FR_V78_b613ca6.bundle checkpoint/v78-snowman-desert:checkpoint/v78-snowman-desert
git switch checkpoint/v78-snowman-desert
```

Le bundle exige584e8b6cfd3f48004388df954dfdd280a62c1535. Taille847502 octets, SHA2569fa38b696ce6b26e681c646e71a8083959e8bdd3d1013b15504ea1cb5d32a101 ; SHA du blobGit07e3f778618db8e4c514d964e4f0130defa1437a. Restauration locale dans un dépôt distinct vérifiée, commit et arbre identiques.

101 tests V78 réussis, puis quatre tests ciblés après ajout de la reconnaissance des preuves par hashes.96 captures/48 paires Snowman/pilote et80 captures/40 paires de relecture des talons. Les limites des préparations et effets sont détaillées dans RAPPORT_V78_SNOWMAN_PILOTE.md et RAPPORT_V78_ACCORDS_TALONS.md.

Aucune donnée ROM/cœur/état/dump incluse. Compteur conservé15 nouvelles sources depuisfbd987c,264 historiques ; le lot400 et la traduction complète restent ouverts. Le dépôt a changé de nom de propriétaire : l’identifiant1411795251 confirme que spamkenny02/earthboundbeginning est le même dépôt que l’ancienne URLspamkenny02-commits.
