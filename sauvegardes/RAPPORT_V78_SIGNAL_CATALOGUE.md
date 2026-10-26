# V78 — signal Escargo et champs inchangés

Le refus d’Escargo35CE5D examine nativement le drapeau0302 et appelle075929, « Beeeep… ». Cette occurrence oubliée devient « Bip… », dans les huit octets de glyphes d’origine, complétés d’un espace. Commandes, durée des pauses, son, pointeurs et données adjacentes restent identiques. Par prudence elle est traitée comme phonétique partagée avec le raccrochage déjà traduit, zéro nouvelle source ; ni la source partagée ni ses profils ne sont recomptés.125 nouvelles sources/374 historiques/553 unités restent inchangées ;61 corrections françaises hors quota,137 publiées/237 en attente. Le même lot400 reste ouvert.

Huit essais (deux profils×état du drapeau×avant/après),16 références/8 paires/9 PNG. Seules deux paires changent dans le mot, bbox116,18–149,29 à l’intérieur de la fenêtre104,16–248,48. Contrôle disponible et retours identiques. Le compteur de pointeurs observés est identique,075932 uniquement dans le cas indisponible. Le service35CE5D complet est appelé par le wrapper privé, après commande native040203 ou050203 ; le buzzer n’est pas appelé directement et aucune WRAM n’est écrite. L’arrivée d’un coursier, la demande initiale de livraison et les transferts ne sont pas prouvés par ce test.

## Relecture des81 champs inchangés

`review_unchanged_catalog.py` et `unchanged_catalog_review.json` classent chacun des81 champs encore identiques à la source dans le catalogue de700 champs. Cette comparaison est effectuée sur le dernier ROM privé, même si l’inventaire de provenance est un snapshot antérieur. Tous les offsets et octets sont gardés.

- 60 noms propres ou emprunts déjà corrects en français : personnages, lieux, marques, Hamburger, Pizza, Croissant, Bazooka, Nachos. Les noms ne sont pas modifiés pour le quota.
- 16 noms réservés : leur identité sert aussi au comparateur natif, ils restent inchangés.
- 3 champs Mono/PSI : graphies françaises valides ou acronyme conservé.
- Un ancien No : le lecteur01F364 pointe désormais vers03FDF4 Non ; conserver le littéral source ne signifie pas afficher No.
- Un PSI(????) : nom index1 utilisé par quatre lignes sans niveau d’apprentissage natif, sans activation certifiée ; préservé.

Cette relecture n’est pas un inventaire exhaustif des tables natives, dialogues, accès calculés ou graphiques. L’ancien inventaire comporte834 plages candidates, dont des données héritées, menus de débogage, onomatopées et noms propres. Elles ne sont pas834 traductions à faire et ne donnent pas encore de borne globale sous400.

## Vérifications et reprise

Huit tests ciblés passent, zéro ignoré, deux méthodes nouvelles :162 distincts connus sans nouvelle suite globale162. Reconstruction incrémentale exacte depuis65bec38, commande native et données hors champ préservées, images et contrôle disponible vérifiés. Le test du stage précédent conserve son préfixe historique, l’IPS ayant été prolongé.

Le bundle65bec38 a été téléchargé, son SHA256 confirmé, puis importé dans le dépôt de base : commit65bec386… et arbre4f9b0213… reproduits exactement. Le guide est relu et l’arbre distantf0243d51… reconstruit localement. Main reste V77, aucun lot final publié. Pas de ROM, cœur, états, SRAM ou dump mémoire distribué.

Le dialogue anglais09886F de NPC390 est seulement une piste : placement dans secteur30, mais aucune porte de type2 ni warp statique entrant dans ce secteur trouvé. Les trois portes sortantes mènent vers secteurs3/98/3. Cela ne prouve pas son inaccessibilité par marche, préparation ou appel calculé ; il n’est pas traduit ni utilisé pour remplir le quota. Poursuivre sa qualification et les lecteurs natifs non résolus, puis la couverture graphique et la relecture intégrale.
