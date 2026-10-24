# Restaurer les panneaux et les légendes de mélodies V78

Checkpoint local584e8b6cfd3f48004388df954dfdd280a62c1535, arbre e783d09b63630d2bc37912208ed9686b1cc7039e. Il inclut le checkpoint intermédiaire71f6b84 des panneaux. Sauvegarde de travail, sans releaseV78 ni mise à jour de main ; aucune certification400/100%.

Bundle complémentaire : `sauvegardes/EarthBound_FR_V78_584e8b6.bundle`,1437916 octets.
SHA256 : `0249d0ad4e85c4e8f5f3f75c72ae00884c2534b57f8397b3ba8b53a07e0c3429`.
Objet blobGit : `6c8cd1be45f21ceab642433771e210cfbe4454ae`.
Base nécessaire :2233c85d521ccd8510d8972fd7345f67cabc852b.

Restaurer d’abord la chaîne existante depuisV77, dans cet ordre :44984fc, f1425be,32413fb,2233c85. Suivre leurs guides et contrôler chaque empreinte. Après restauration de2233c85, importer ce complément :

```bash
git bundle verify sauvegardes/EarthBound_FR_V78_584e8b6.bundle
git fetch sauvegardes/EarthBound_FR_V78_584e8b6.bundle checkpoint/v78-melody-labels:checkpoint/v78-melody-labels
git rev-parse 'checkpoint/v78-melody-labels^{tree}'
```

L’arbre attendu est celui indiqué plus haut. La chaîne a effectivement été importée dans un dépôt distinct ne contenant que les checkpoints restaurés, avec HEAD et arbre identiques. Les octets du blob distant doivent correspondre à l’empreinteGit et auSHA256 ci-dessus.

Ce jalon conserve15 nouvelles sources graphiques depuisfbd987c,264 historiques (137 publiées/127 en attente),297 plages littérales inchangées. Les137 sources publiées ne sont pas recomptées.94 tests passent avec les dépendances privées ;32 paires natives de mélodies et28 paires de panneaux sont limitées aux inscriptions. Les arrivées, l’objetOcarina et les drapeaux de mélodies ont une préparation explicite ; le parcours et l’apprentissage naturels ne sont pas certifiés. Les rapports exacts et captures publiques sont dans le bundle.

La sauvegarde contient les sources,IPS, outils, rapports,PNG etJSON publics suivis parGit. Aucune ROM, aucun cœur d’émulation, état privé ou dump mémoire n’est inclus. Les notes ajoutées après ce checkpoint seront conservées par le prochain complément.

Suite : courts fragments et assemblages hors relectures déjà validées, légendes de carte et autres accès encore non qualifiés, puis validation finale et relecture complète. Ne pas présenter ce checkpoint intermédiaire comme un lot400 terminé.
