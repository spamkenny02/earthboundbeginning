# V78 — occurrence de récompense de victoire instantanée

Le lecteur natif0263CA atteint2F7A28 après une collision de carte remportée automatiquement. L’écran anglais « Ninten gained 8 exp. » devient « Ninten : + 8 EXP. ». La formule existe déjà en français dans36761A et36765C : aucun nouveau texte distinct n’est compté. Les deux fragments physiques ` gained ` et ` exp` constituent une occurrence de phrase partagée. Les compteurs du lot restent124 nouvelles depuisfbd987c,373 historiques/550 unités sources,137 publiées/236 en attente,61 réparations françaises. Le lot400 reste ouvert ; aucun reste global inférieur à400 ni100% établi.

## Intégration

La source2F7A28–2F7A4D et tous ses accès intérieurs sont conservés. Une copie garde chaque commande et remplace uniquement les glyphes. Le lecteur0263CA change ses deux octets d’adresse et son octet de banque ; instructions, destinations de registres et appel d’affichage restent identiques. La réserve3EF580–3EF600 est nulle dans la ROM source et le produit d’entrée, après la fin réelle du flux graphique17, sans sprite ni cible conservative de pointeur. Banque25 et sprites restent identiques. `instant_win_stage.py` reconstruit exactement l’ajout aux deux IPS du commit385f804. Les métadonnées anciennes conservent leurs empreintes de stage ; le test du nommage vérifie désormais le préfixe historique de l’IPS prolongé.

## Accès et préparations

`prepare_instant_win_states.py` prépare indépendamment chaque profil depuis l’état privé d’hôtel. Commandes natives `050B00 1E080163 1E000164 10FF 10FF 10FF 10FF 1F2102` : activation des rencontres, niveau99, soin, attente et warp2. Un enregistrement de warp privé est fixé à6752,3936, direction nord ; le wrapper utilise le créneau de probe habituel. Les modifications temporaires ne sont jamais dans l’IPS. La position du joueur est l’entité24, les entités adverses sont lues sans écrire en RAM.776 déplacements au contrôleur rejoignent un ennemi réellement généré ; l’ultime Gauche+B pendant4 images puis une image relâchée déclenche la collision. Aucun script de combat ni de message n’est appelé directement. Le trajet initial et l’obtention du niveau99 ne sont pas naturels.

Les états avant contact sont ensuite chargés sans aucune modification de ROM temporaire. `probe_instant_win.py` rejoue la même dernière action avant/après traduction. L’ennemi natif43 donne8 EXP et10 dollars selon sa fiche. Les témoins scalaires donnent8071613→8071621 EXP,0→10 dollars en banque,20→20 en poche, drapeau debug0. L’argent est crédité avant la fermeture du message, l’EXP après ; cet ordre est identique. Les adresses EXP99D4, banque9835, poche9831, debug436C et tableau des ennemis9F8A/9F8C sont vérifiées contre les lecteurs assembleur natifs ; aucun dump mémoire n’est conservé.

## Preuves et limites

`tests/emulation_v78_instant_win/coverage.json` : quatre essais (deux profils×avant/après),8 références de captures,4 paires et4 PNG uniques. Les deux paires du message ne changent que dans40,16–216,56 ; texte complet sur une ligne, noms et nombre visibles. Les deux retours carte ont un déphasage d’animation après texte plus court, explicitement exclu d’une comparaison graphique stricte. Les effets scalaires restent identiques. Ninten seul est qualifié ; pas de validation extrapolée à un groupe ou à d’autres adversaires.

Cinq tests ciblés passent, zéro ignoré ; trois méthodes nouvelles portent le total distinct connu à157, sans prétendre avoir relancé toute cette suite. Reconstruction incrémentale exacte, source/lecteur/réserve altérés refusés et témoins/captures relus. Les états, ROM, cœur et lectures RAM privées ne sont pas distribués. La sauvegarde précédente385f804 a été téléchargée, vérifiée et restaurée exactement ; métadonnées dans `remote_checkpoint.json`.
