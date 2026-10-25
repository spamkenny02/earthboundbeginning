# V78 — légende de fin alternative et enchaînement final préparé

Le graphisme natif « TO BE CONTINUED… » devient « À SUIVRE… » dans le profil accents et « A SUIVRE… » en ASCII. Une seule nouvelle source est comptée, à20E851. Les corrections des occurrences partagées Attendre et Tirer n’ajoutent aucune source : le provisoire103 de l’ancien checkpoint de paralysie avait été retiré ; le103 actuel provient exclusivement de cette nouvelle légende.

Compteurs du même travail :103 nouvelles sources depuisfbd987c,352 historiques,461 unités/plages d’origine ;137 publiées et215 en attente. Le lot400 reste ouvert. Cinquante-quatre corrections de phrases françaises et la jauge graphique PV restent hors quota.

## Qualification et préparation

Deux portes typées du secteur864 (1BF97B/1BF980, opérande0F193D) appellent386817. Le moteur déroule l’introduction, le combat449, le chant natif et le retrait de Giygas ; il revient ensuite à386904, passe par386920 et teste03B2 à3869F5. Drapeau absent :38ED3E crée l’animation6, qui reste affichée au terminal38ED87. Cette observation remplace la qualification antérieure insuffisante conservée dans `ending_animation_qualification.json`.

Le test appelle la scène complète386817 par un petit auxiliaire privé, dans128 octets originellement vides à3EFC50, hors sprites, pointeurs et graphismes alloués. Il ajoute Ana/Lloyd, prépare leurs statistiques, donne et équipe trois Pendentifs étoilés en utilisant les emplacements réellement retournés par le don natif, soigne l’équipe, attend les compteurs et prépare mélodies/Chanter. Les menus sont ensuite pilotés à la manette. Aucun appel direct de la fin ou du chargeur d’animation, aucune écriture directe en mémoire vive. L’auxiliaire et la ROM préparée ne font pas partie des IPS.

Le trajet initial vers la porte et l’acquisition naturelle des drapeaux ne sont pas certifiés. Le test supplémentaire, répété dans les deux profils avec464 références d’images et218 PNG uniques (`tests/emulation_v78_complete_story_branch/coverage.json`), avec03B2 préparé représente le retour scénaristique de Lloyd : il observe le générique puis le père au téléphone, sans remplacer cette limite par une prétendue partie complète.

## Conservation et rendu

Le bloc compressé reste dans20E851–20EA74 :485 octets pour les accents,479 pour ASCII, budget547. Décompression native et recompression reproduisent exactement les2312 octets attendus. La palette, les bits de retournement/priorité, la tuile vide partagée et tous les pixels hors rectangle64,104–200,120 sont conservés. L’entrée20EAA4, les pointeurs, les sprites et la banque25 restent identiques.

Quatre parcours avant/après aboutissent au même retrait et au même terminal,199 étapes chacun. Les816 références d’images représentent408 paires et192 PNG uniques. Huit paires changent, toutes dans la légende ; les autres images sont identiques, notamment les combats et transitions précédents. Le titre est entièrement lisible, sans débordement ; le grave apparaît seulement dans le profil accents. Preuves : `tests/emulation_v78_alternate_ending/coverage.json` et les quatre rapports assainis.

Deux nouveaux contrôles automatisés vérifient la propriété exclusive du bloc, le budget, la palette, les drapeaux de tuiles, le rejet d’une entrée modifiée, l’intégrité des PNG et les différences de l’ensemble des images appariées. La reconstruction complète reproduit les deux IPS octet pour octet. Sur125 tests collectés,124 passent ; le seul échec était le calcul de registre qui omettait la nouvelle légende. Ses deux assertions (compte et ensemble des adresses) ont été actualisées, puis le test passe séparément. Ainsi125 tests distincts sont validés, sans prétendre avoir répété une suite125 intégralement verte. Résultat structuré : `tools/v78/validation_caption_tests.json`.

Aucune ROM, aucun cœur, état ou dump mémoire n’est distribué. Ce rapport est un checkpoint interne du gros lot, pas une publication finale.
