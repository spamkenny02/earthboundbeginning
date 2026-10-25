# V78 — Snowman et copies du pilote

Jalon interne du lot400, sans release. Zéro nouvelle source : WELCOME TO est déjà compté. Le compteur reste15 sources depuisfbd987c,264 historiques dont137 publiées et127 en attente ;297 plages originales. Cinq champs français supplémentaires corrigés, sans les compter comme traduction nouvelle (15 corrections françaises dans cette exécution).

La bannière Snowman devient BIENVENUE ; le nom SNOWMAN et les décors restent identiques. Quatre paires de tuiles exactement identiques dans les deux couches libèrent les lettres. Animations protégées, attributs, pointeurs et toutes les cellules hors inscription conservés ; indices sous512. Aucun essai photo revendiqué.

Une réserve originale nulle de572 octets,3EF944–3EFB80, sans cible brute ni chevauchement de sprite, reçoit433 octets de scripts : service25B27C copié à3EF944 (284 octets), message25D1C0 à3EFA60 (149). Cinq opérandes typés373912/373990/373BD0/373C02/373C27 sont redirigés et les deux destinations intérieures rebassées. Les commandes de jeu sont conservées après normalisation de ces destinations déclarées. Banque25 originale, tableNPC et empreinte des sprites identiques. L’ancienne réserve328A70–330FC0 demeure épuisée : il s’agit d’un nouvel alignement qualifié, pas d’une réutilisation non sûre.

Le pluriel s’insère maintenant avant « de billet » :1 talon/3 talons de billet. Le rappel du service emploie « talons de billet ». Le rappel est relu statiquement ; son affichage après achat réel n’est pas certifié. Les anciennes copies restent physiquement intactes ; les cinq appels connus suivent les nouvelles copies. Aucun classement global des appels calculés ou du texte dormant.

101 tests V78 passent avec la ROM privée,58,839s : protections des deux couches, décompression, copie, cibles, commandes, banque25, sprites, registre et captures. Les deux IPS ont été reconstruits. Preuves publiques : `tests/emulation_v78_snowman_desert/coverage.json`,96 PNG et20 rapports expurgés.48 paires,10 paires différentes ; chaque différence est limitée aux rectangles déclarés. Quatre correspondances graphiques de la bannière et huit témoins après modification d’usage des copies.

Les scénarios1/3 talons et le premier appelNPC sont artificiels, par scripts complets et quantités natives préparées ; aucune écriture directeWRAM. La bannière est observée aprèswarp natif. Le pilote210 est aussi rencontré sur la carte par déplacement et commande Parler ordinaires aprèswarp à(5344,9272), déplacement Haut12 images et préparation du portefeuille vide. Les pointeurs3EF971/3EF98C/3EF990/3EF9C0 montrent l’usage de la copie, puis le refus faute d’argent est affiché. Le trajet initial, l’achat d’un vol et les montants/effets d’un remboursement ne sont pas certifiés.

SHA256 IPS accents : `5c383386e0cbe1593f8b93b50394da2fe547119cc65c275b7b31955c08d20d71`.

SHA256 IPS ASCII : `77f8b9823450db88ee60dcaed8c6b118834446a86a98792a6faa07e5184ee7e3`.

ROM, cœur, états, historiques et dumps privés restent exclus du dépôt. Traduction et relecture globales non certifiées ; aucune preuve d’un reste global inférieur400.
