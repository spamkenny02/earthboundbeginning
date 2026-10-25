# V78 — commande conditionnelle de chant

Le combat449 affiche encore Sing lorsque le drapeau0380 est actif. Le champ375213 est chargé par le lecteur natif375AD6 ; le test de drapeau passe par021628. Une écriture native0380 est présente à366DE5. Les libellés voisins Throw/Blast/Check étaient déjà français (Jeter/Tirer/Voir) et ne sont ni modifiés ni recomptés.

Chanter est placé dans huit octets originaux nuls3EFAF8–3EFB00, après les copies sûres du pilote. Seuls les immédiats de donnée du lecteur (mots375AD7 et375ADC) deviennent FE:FAF8. Le contrôle de flux natif est identique ; les champs originaux, données adjacentes, banque25 et sprites restent inchangés. La nouvelle réserve est vérifiée sans cible brute d’origine ou du patch précédent. Le mot mesure34 pixels et s’affiche intégralement avant Auto.

16 captures,8 paires avant/après, quatre différences limitées à(112,18)–(148,30) ; Auto est identique. Les quatre paires sans drapeau0380 sont intégralement identiques. Les deux positions de curseur sont observées dans les profils accents/ASCII. La fenêtre est atteinte par le vrai moteur de combat après commandes natives : niveau99 de Ninten, récupération totale de santé, quatre crèmes, huit drapeaux de mélodie et0380, puis combat449. Aucun appel direct de la fenêtre ni écritureWRAM. Le trajet initial et la victoire finale ne sont pas certifiés.

La source Sing était déjà traduite en Ch. au champ historique0BD82B. Cette occurrence supplémentaire ne constitue donc pas une nouvelle source distincte : compteur maintenu15 depuisfbd987c,264 historiques,297 plages originales. Les28 corrections de français existant ne sont pas augmentées artificiellement par cette occurrence partagée. Lot400 et complétude globale ouverts.

106 tests passent avec la ROM privée (62,271s). IPS accents SHA256`72d8c1beccfc82e6f3f7144fecf8364b65108f8fd3bfcee344f1983f8c57d17b`, ASCII`b667e5b15c97457285842ab83d37c1079788a060728d35aa083c4947d393b926`. Preuves : `tests/emulation_v78_sing_label/coverage.json`. ROM, cœur, états et dumps restent privés.

Une exploration séparée de la victoire avec Ninten seul n’a pas produit de victoire certifiée et ne figure pas parmi les preuves validées. La suite essaie une préparation native de plusieurs personnages, en conservant cette distinction.
