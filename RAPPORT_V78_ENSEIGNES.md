# V78 — enseignes françaises et deux couches de décor

Checkpoint interne du lot de 400, sans release : **10 nouvelles sources distinctes**, **32 champs graphiques**. Total historique : 259 sources, dont 137 publiées et122 en attente ;297 plages de texte littéral restent dans le registre, les emplacements graphiques sont décrits séparément. Les anciens249 textes, variantes accents/ASCII, copies par ville, noms propres, captures et les corrections du cognat HOTEL ne sont pas recomptés. Le lot de 400 n’est pas atteint ; aucun inventaire global sous 400 ni achèvement général n’est certifié.

## Intégration et protections

Banques1,2,3,4,15,16,18 : mairies, magasins, restaurants, hôpitaux, hôtels, gares, école Twinkle et Petite usine. Les noms Podunk, Spookane, Reindeer, Merrysville, Twinkle et Union sont conservés. Ellay utilise SNACK, les autres restaurants RESTO ; ces contextes sont regroupés conservativement dans une seule famille BURGER SHOP. La liste exacte des dix sources et des emplacements est dans `tools/v78/batch_ledger.json` et `v78_fixtures.json`.

La carte réelle est décodée avant modification :256×320 blocs, secteurs8×4 blocs et table32×80. Chaque inscription modifiée possède des coordonnées réellement référencées. Le rendu utilise deux couches : pour un indice inférieur à 384, la seconde couche utilise le motif àindice+512. Les doublons ne sont recyclés que si classe et **deux motifs** coïncident ; les nouveaux glyphes sous 384 disposent aussi de leur motif de premier plan. Les cellules hors inscriptions conservent leurs attributs et les pixels des deux couches dans les 1024 arrangements de chaque banque. Les destinations d’animation sont exclues du recyclage.

Une première tentative ne vérifiait que la première couche et produisait desZ parasites à l’école. Elle a été rejetée. Les captures de cette tentative restent privées et ne sont pas des preuves du checkpoint. Les comparaisons finales vérifient les deux couches ; l’école affiche désormaisÉCOLE/ECOLE, sans parasites.

Chaque conteneur comprimé reste borné par son espace d’origine ; le vide nul de 121 octets entre les deux flux de la banque 4 est gardé comme partie de ce conteneur. Sept pointeurs typés d’arrangements sont ajustés à la nouvelle frontière de flux. Les pointeurs de graphismes, palettes, collisions, carte, commandes et toutes les empreintes de sprites restent inchangés. Le compresseur est déterministe ; chaque flux est relu par le décompresseur indépendant existant. Les indices utilisés restent sous 512 : borne statique de chargement en photographie, sans prétendre avoir exécuté une scène photo.

## Affichage et contrôles

28 arrivées préparées par le déplacement natif 2, dans les deux profils, avant/après :112 captures,56 paires. Le wrapper et un seul enregistrement de destination sont propres aux fixtures privées ; aucun dialogue d’enseigne n’est appelé directement, aucune WRAM n’est écrite. Les déplacements initiaux naturels ne sont pas certifiés.

Les 32 champs distincts sont couverts dans chaque profil. Au total, 66 inscriptions visibles ont leur motif indexé comparé à l’image du cœur standard, avant et après, en tenant compte des deux couches et des couleurs effectives du secteur. Les champs effacés sont comparés à leur fond d’origine.54/56 paires ne changent que dans les rectangles d’enseigne ; les deux essais de l’hôtel d’Ellay sont exclus de ce confinement strict, car le taxi et le lampadaire changent de phase. Leurs motifs d’enseigne correspondent néanmoins. Les planches des28 scènes avec accents et la scène ECOLE ASCII ont aussi été relues visuellement.

87 tests de la suite globale passent. Le nouveau contrôle des captures et motifs natifs passe ensuite avec les trois contrôles graphiques : **88 tests distincts validés**, sans présenter deux exécutions du même test comme deux contrôles différents. Les audits textuels historiques sont reproduits contre leur snapshot exact avant cette étape graphique ; les nouveaux contrôles prouvent séparément les bornes des modifications graphiques. Aucun audit de texte historique n’est annoncé comme nouveau travail de traduction.

## Reste précis

- Podunk : HOPITAL et HOTEL restent sans circonflexe, y compris dans le profil accents. LeV réutilise l’ancien B retiré ; M est le W natif retourné verticalement. Aucun autre doublon à deux couches n’a été trouvé pour ajouterÔ dans ce périmètre conservateur. Résoudre cette capacité graphique sans altérer un caractère de Podunk ni les couches hors inscription ; ne pas annoncer ces accents comme terminés.
- Petits panneaux encore anglais : sprite 442, HOTEL/STAY/HERE, réellement visible devant les hôtels ; sprite 436, YOU ARE HERE, et 446, HINT ; qualifier finement 213 avant de nommer son inscription. Modifier seulement les pixels textuels possédés si cette étape est traitée, pas les personnages, bordures, dimensions ou collisions.
- Pictogrammes de carte : bloc comprimé2CF1F9 (9216 octets décomprimés, fin2CFA8B), champsFOOD/HOSPITAL/DEPTSTORE/HINT/SHOP/HOTEL et toponymes descriptifs ; ensuite étiquettes des mélodies20B16D. Les noms propres et cognats ne servent pas au quota.
- LIVE HOUSE demande une décision de terminologie contextualisée ; ne pas le classer arbitrairement comme texte dormant. Les conditions naturelles de fin, accès calculés non résolus et la relecture complète restent ouverts. Les états privés disponibles sont précoces.

Sources de format : [CoilSnake 346cfc7](https://github.com/pk-hack/CoilSnake/tree/346cfc753644bc3703b6fc4eaa0a5d6bdcb9bb4a), [lecteur natif des deux couches](https://github.com/Herringway/ebsrc/blob/68aec5c39e67f3ef4f0be138ee58c1ba0cc33d62/src/overworld/load_map_row_vram.asm).
