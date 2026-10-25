# V78 — confirmations de sac plein et ciblage PSI

Deux sources nouvellement traduites : « Throw away » → « Jeter » et « Don't do it » → « Annuler ». Les définitions originales2F7D56/2F7D63 sont conservées ; leurs copies actives32FE76/32FE83 sont traduites. Les deux menus Yes/No de cette branche deviennent Oui/Non, sans nouveau décompte pour ces sources déjà traduites ailleurs. Une correction du français existant remplace « À ligne avant » par « À l'avant ».

Compteurs du même lot :105 nouvelles sources depuisfbd987c,354 historiques,463 unités/plages d’origine ;137 publiées et217 en attente. Cinquante-cinq corrections de phrases françaises, la jauge graphique PV et les occurrences partagées restent hors quota. Le lot400 n’est pas achevé ; aucun reste global inférieur à400 n’est établi.

## Victoire et trois branches effectivement observées

La préparation native porte Ninten au niveau99, le soigne, attend les compteurs puis tente vingt dons de Talon4D. Les dons qui excèdent la capacité ne sont pas comptés comme vingt objets reçus. Le sac effectivement affiché contient la Carte bancaire et treize talons. Un vrai combat17 est déclenché ; Auto gagne le combat et le moteur propose son cadeau, un Champi. sauvage. Aucun script de remise, résultat de butin ou menu de confirmation n’est appelé/forcé directement. Le petit auxiliaire privé3EFC50 est qualifié sur128 octets originellement vides, sans cible de pointeur ni sprite.

Trois parcours sont pilotés dans chaque profil, avant et après les changements :

| Choix | Inventaire final observé |
|---|---|
| Oui, Talon, Jeter | Carte bancaire,12 talons,1 Champi. sauvage |
| Oui, Talon, Annuler, puis laisser le cadeau | Carte bancaire,13 talons |
| Non, puis laisser le cadeau | Carte bancaire,13 talons |

Les douze résultats sont vérifiés par correspondance exacte des cellules de glyphes visibles de l’inventaire. Les références et rectangles sont fournis dans la couverture ; il ne s’agit ni d’un OCR supposé ni d’un dump mémoire. La Carte bancaire reste intacte. Les touches et attentes sont identiques entre chaque paire avant/après. L’accès initial depuis le début du jeu n’est pas certifié.

Les176 références d’images forment88 paires et32 PNG uniques. Vingt paires changent. Quatre-vingt-quatre paires prouvent des différences limitées à la fenêtre de texte. Quatre autres, aux étapes de confirmation/acceptation du cadeau laissé, ont aussi un déphasage du fond animé :5257/5209 pixels sombres au maximum, composantes RGB au plus64, écart maximal9 (un niveau de canal SNES). Elles sont consignées séparément et ne prouvent pas une conservation pixel par pixel de l’ensemble de l’image. Les inventaires finaux avant/après restent identiques pour chaque choix.

## Conservation des commandes et des accès

Jeter et Annuler tiennent dans les champs existants, complétés d’espaces. Non demande un caractère supplémentaire : un espace redondant est consommé dans chaque région de menu. Les deux régions gardent exactement leur taille, sans allocation. Avant déplacement des définitions internes, l’absence de toute cible HiROM intérieure est contrôlée dans la source et le produit. Les séquences de commandes, les destinations des branches, les limites des scripts, les autres octets, les sprites et la banque25 sont conservés.

## Ciblage de PK Feu

Après ajout natif d’Ana, niveaux99, soin et combat5, les touches ordinaires passent de Parer pour Ninten à PSI/Attaque/PK Feu α pour Ana. La fenêtre affiche « À l'avant » intégralement. Douze captures/six paires : deux différences confinées au libellé, menus des personnages inchangés. Le préfixe partagé À/A de trois octets reste intact afin de préserver les cibles nommées.

Les231 lignes de configuration ennemie ont leur champ de rangée à zéro. Les essais privés de paramétrage d’une rangée arrière n’en ont pas démontré la sélection ; le libellé arrière est donc conservé et aucune preuve de son affichage n’est revendiquée. Le sort n’est pas lancé dans ce test de libellé.

## Vérifications et sauvegarde

La reconstruction complète reproduit les deux IPS octet par octet. Les cinq nouveaux tests portent sur les champs possédés, les ancres de lecteurs, les cibles intérieures interdites, les commandes, toutes les images appariées et les effets visibles sur les inventaires. La suite complète collecte130 tests : tous réussissent, sans erreur ni test ignoré. Résultat structuré : `tools/v78/validation_row_drop_tests.json`.

L’espace de travail a de nouveau été retrouvé à775b0a6 pendant cette continuation. Les cinq anciens fichiers locaux ont été préservés dans un stash sélectif et la refcheckpoint/recovered-local-before-7dbd4d4 ; le fichier ZIP étranger est resté intact. Les quatre bundles2098424/1eff806/4970cd4/7dbd4d4 ont été téléchargés depuis l’archive distante, leurs SHA256 vérifiés, puis restaurés en avance rapide. Le commit7dbd4d4 et l’arbreb168b2fe ont été retrouvés exactement. Les captures de ciblage perdues après ce checkpoint ont été refaites ; elles ne sont pas revendiquées comme conservées par le bundle antérieur.

Aucune ROM, aucun cœur, état ou dump mémoire n’est distribué. Les commits de protection ne constituent pas une publication de micro-lot.
