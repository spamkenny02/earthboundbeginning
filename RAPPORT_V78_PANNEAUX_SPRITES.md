# V78 — inscriptions des panneaux d’hôtel et du vendeur d’indices

Travail interne du même lot400, après le checkpoint2233c85. Le lot n’est pas terminé et aucune nouvelle release n’est publiée.

- Groupe442 : la source exacte est **HOTEL / WELCOME**, et non HOTEL/STAY/HERE. WELCOME devient **ACCUEIL** dans les deux profils ; HOTEL devient HÔTEL dans le profil accents. L’ornement, le lit et le cadre restent identiques.
- Groupe446 : **HINT → INDICE**, dans ses deux poses natives. Le personnage, son animation et les bordures restent identiques.
- Décompte : **une** nouvelle source distincte, HINT. WELCOME est rattaché au même accueil déjà enregistré sous `@Welcome!` (sept plages littérales), sans huitième texte ni faux offset littéral. La correction du cognat HOTEL ne compte pas. Le présent travail poursuit les dix familles du checkpoint précédent :11 sources nouvelles depuisfbd987c,260 au registre historique, dont137 publiées et123 en attente. Les297 plages littérales et249 sources littérales sont inchangées.

## Intégration et protection des pixels

Trois images4bpp de512 octets :293A40 (442),296500 et296300 (446). Les huit références de442 et les huit de446 sont contrôlées ; aucun autre groupe parmi464 ne partage ces images. Dimensions32×32, palettes, descripteurs et références restent identiques. Seuls les masques de lettres déclarés sont modifiés. Les deux poses de446 conservent leur décalage horizontal natif. L’encodage est redécodé et vérifié ; en restaurant ces trois images, la ROM entière retrouve exactement son état d’entrée. Des tests distincts vérifient tous les pixels hors masque.

Les anciens tests de préservation globale des sprites normalisent seulement ces trois images déclarées ; les nouveaux tests garantissent leur usage exclusif et le périmètre des lettres. Les tests des enseignes de décors et leur vérificateur utilisent désormais le préfixe exact de leur propre étape. Leurs112 captures historiques restent attachées à leurs empreintes d’origine ; elles ne sont pas attribuées à la nouvelle ROM.

## Affichage observé

`tests/emulation_v78_sprite_signs/coverage.json` contient56 captures natives,28 paires avant/après, six cas et deux profils : hôtels dePodunk, Merrysville, Reindeer, Ellay et Spookane ; vendeur d’indices placé dans la salle8104/1776. Les deux poses de ce vendeur sont observées. Les28 différences de frame restent intégralement dans les rectangles des inscriptions possédées. Les formes de pixels indexés sont comparées aux captures. ÀSpookane, la partie basse du panneau est partiellement occultée ; quatre comparaisons utilisent seulement l’inscription, et non une prétendue correspondance du sprite entier.

Préparation déclarée : destination native warp2 modifiée dans une fixture privée, puis touches ordinaires. Aucune écriture WRAM directe, aucun appel direct au dialogue cible. Ce n’est pas un parcours initial naturel. ROM, cœur, états et historiques mémoire ne sont pas distribués.

Les91 tests V78 passent avec la ROM privée (suite complète,126,485s). IPS accents : `c90915913a55dcd99af9421a10f4eb2f6140e500f5043edfdc9ab84f711807b7`. IPS ASCII : `dd26efc71efead108464068892105e7278d0bd5834d30a52934490c8df7ab1ec`.

## Restes précisément bornés

Le groupe436 YOU ARE HERE n’est pas traduit : son seul PNJ835 n’a aucun placement trouvé ; la carte dePodunk observée emploie un curseurNinten différent. Cette absence de placement ne prouve pas à elle seule un état dormant global. Le groupe213 n’a pas une inscription suffisamment lisible pour le nommer.

Les légendes2CF1F9 sont chargées par le menu de carte, mais ne sont pas apparues àPodunk dans l’essai normal avec objetCA préparé. Un essai supplémentaire avec cinq drapeaux de légendes préparés explicitement n’en a pas affiché non plus. Aucun nom ou légende n’est traduit pour remplir le quota ; ces essais ne prouvent ni leur présence naturelle ni leur suppression globale. Poursuivre les libellés graphiques de l’écran de mélodies20B16D avec son consommateur réel, les circonflexes du décor dePodunk, puis les catégories et validations finales encore ouvertes. Aucun400, aucun100% et aucun reste global inférieur à400 ne sont établis.
