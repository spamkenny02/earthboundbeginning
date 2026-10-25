# V78 — PV dans les jauges et retrait préparé de Giygas

Le libellé graphique HP devient PV dans les jauges du combat et de la carte. Cette harmonisation reprend la terminologie française PV/PV+ existante : zéro nouvelle source ajoutée au quota. Les compteurs restent102 nouvelles sources depuisfbd987c,351 historiques/460 plages originales,137 publiées et214 en attente ;28 corrections françaises antérieures ne sont pas recomptées. La passe terminologique ajoute26 corrections de phrases (neuf messages/aides PSI et17 descriptions d’objets), soit54 corrections françaises de phrases dans cette exécution ; la jauge graphique est suivie séparément. Le lot400 continue.

## Propriété des données et chargeurs

Les glyphes H/P partagés8,9,10,24,25,26 restent identiques. Le P initial est celui du libellé PP natif. Un V est dessiné dans deux tuiles brutes initialement nulles129/145. Leurs bits sont réservés dans le masque initial020968/02096A et leurs protections dans LOCKED_TILES043996/0439A6. L'allocateur de texte ne peut donc plus les attribuer, et FREE_TILE ne peut pas les libérer. La capacité dynamique diminue de deux tuiles ; tous les cas extrêmes de fenêtres ne sont pas certifiés.

La table native03E3F8 remplace uniquement ses quatre premiers octets HP ; les quatre octets PP suivants sont inchangés. Les deux chemins de chargement immédiat/différé de044963 ne transféraient que128 et144 : leurs tailles passent de16 à32 octets aux opérandes044A08,044A20,044A9B,044AB3, couvrant les deux nouvelles tuiles. Les destinations et toutes les autres instructions sont inchangées. Les données graphiques décompressées ne changent que pour129/145. Elles sont recompressées en1692 octets dans la réserve déjà possédée177800–177FD0 ; pointeur de chargement inchangé, décompression inverse exacte, banque25 et sprites conservés.

Sources primaires locales : ebsrc68aec5c39e67f3ef4f0be138ee58c1ba0cc33d62, `src/text/hp_pp_window/draw.asm`, `src/text/free_tile.asm`, `src/unknown/C4/C40085.asm`, `C43F53.asm`, `C44963.asm`, `src/system/load_window_gfx.asm`. Les octets des lecteurs et des tables sont vérifiés contre la ROM source. Le premier prototype sans extension des transferts n'affichait pas le V ; il n'a jamais été intégré aux IPS.

## Combat préparé et portée de la preuve

Depuis l'état privé d'hébergement : joindre Ana et Lloyd, niveau99 pour les trois personnages, soins natifs100%, attente1020 images, drapeaux mélodiquesB6–BD et0380, combat449. La préparation native fait63 octets plus02 dans le wrapper réservé330FC0. Aucune écriture directe en WRAM ; aucun appel direct au retrait, à la fin ni au générique. Le véritable menu sélectionne Chanter, action331.

Les quatre essais référence/PV × accents/ASCII atteignent les dix parties du chant, le dialogue32DB78, le retour sur la carte préparée, puis l'ouverture du menu.111 étapes/30245 images par essai. Ninten906, Ana465 et Lloyd604 HP/PV avant et après le combat. Le texte « Comment ai-je pu perdre à cause de cette chanson? », puis l'annonce du retour de Giygas et « Ninten! Nous nous REVERRONS! » sont lisibles dans les deux profils.

456 captures/228 paires et journaux nettoyés sont conservés dans `tests/emulation_v78_hud_pv`. Les18 paires stabilisées contrôlées pixel par pixel ne diffèrent que dans les trois rectangles des libellés HP/PV ; les PP et le reste des images sont identiques. Les positions tiennent compte de la jauge relevée du personnage actif. Quelques images transitoires présentent aussi un décalage de déformation du boss, de déplacement/roulement des jauges ou du prompt clignotant après les transferts plus longs. Les commandes et sélections restent identiques ; ces images sont enregistrées sans prétendre à une différence limitée au texte. Les images finales de dialogue et de carte ont été relues dans les deux profils.

Le retrait observé suit Chanter37EBE5 →3674EE →32DB78. Il ne prouve pas le callback de mort distinct37F0EF. Le trajet initial naturel, la destination d'une partie normale après ce boss, la visite de fin et le générique ne sont pas certifiés par cet essai. Les anciens essais de générique forcé restent des preuves séparées.

## Fiches IA secondaires

EnemyExtender245 au lecteur025466 utilise l'argument de sa case pour changer de fiche ennemie. La fermeture de119 graines atteint131 fiches,12 supplémentaires, via26 références, dont des cycles. Actions et arguments sont identiques à la source. Aucun callback ni texte anglais supplémentaire :805 contextes/59812 états/233 lecteurs, frontière vide,15 contrôles non résolus. Les conditions sont abstraites ; toutes les branches ne sont pas déclarées naturellement accessibles.

## Sauvegarde et reprise

Après le retour inattendu de l'espace de travail à775b0a6, les modifications locales ont été conservées dans `checkpoint/recovered-local-before-1eff806` et le stash correspondant. Les bundles2098424 puis1eff806 ont été récupérés depuis la sauvegarde distante ; leurs SHA256, commits et arbres correspondent exactement. Les essais PV et de retrait perdus ont été rejoués, et seules les nouvelles captures présentes dans le dépôt fondent cette validation.

Suite : harmonisation des mentions HP/PV dans les phrases françaises qualifiées, autres accès calculés et fin naturelle. Le professeur062AE7 n'est toujours pas qualifié dans le scénario actuel. Aucune preuve globale d'un reste inférieur à400 ni de traduction terminée.

## Harmonisation des phrases et aides d’objets

Les neuf fragments natifs de récupération, dégâts et aides PSI, puis17 plages dans15 racines d’aides d’objets, passent de HP à PV. Les remplacements font exactement deux octets, à des positions textuelles parsées et vérifiées séparément pour accents/ASCII. Les racines, commandes, tailles, pointeurs et PP restent identiques. Les variantes d’une même source ne sont jamais recomptées. Les quatre paragraphes PSI relus sont « Rend100/300 PV à un allié », « Rétablit les PV d’un allié » et « +400 PV au groupe ». Les descriptions d’aliments, pommade et insecticide conservent leurs quantités et leurs effets.

La fermeture réactualisée comprend3902 racines, y compris les152 aides principales des153 objets qualifiés, sans échec de parsing ni occurrence isolée HP dans les deux profils. Cela ne certifie pas tous les appelants calculés ni tous les textes du jeu. Le premier relevé de3703 racines ne comprenait pas les aides d’objets ; ce complément est explicitement ajouté à la couverture. Les neuf corrections natives ont56 captures/28 paires, dont26 changées et deux premiers écrans encore vides ; les neuf racines présentent ensuite PV. Ces appels restent artificiels, sans nouvelle preuve d’effet de soin ou de dégâts.

Le mouvement historique670, qui appelle la préparation de téléportation style5 puis062AE7, n’est ni un mouvement initial d’un PNJ placé ni la cible des212 commandes de changement de mouvement de la fermeture des3405 racines placées. Cela n’exclut pas tous les accès natifs indirects ; ce texte reste non traduit et non compté tant qu’un appel actuel n’est pas établi.

Les17 corrections d’aides d’objets ont252 captures/126 paires,44 paires changées dans la seule fenêtre native96,8–248,72 ; les quinze racines montrent leur correction. La Barre cacahuète357FD5 demande sept captures successives pour atteindre le dernier paragraphe, les autres racines quatre. Les captures d’aides isolées partent d’un ancien état vidéo sans rechargement des graphismes : elles ne certifient pas le nouveau V des jauges ; cette preuve vient du combat préparé qui recharge les tuiles, puis du retour sur la carte. Les deux profils de chaque aide ont été relus.

Validation finale de cette harmonisation :119 tests collectés/exécutés, zéro échec, zéro erreur, zéro test ignoré,161,748 secondes. Le compte rendu structuré est `tools/v78/validation_pv_tests.json`. Les deux IPS avaient été reconstruits identiquement pour PV et les neuf premières corrections ; le complément de17 corrections est reproduit depuis son préfixe exact par le test des écritures bornées, et la chaîne finale est comparée intégralement aux enregistrements déclarés. `git diff --check` est propre.
