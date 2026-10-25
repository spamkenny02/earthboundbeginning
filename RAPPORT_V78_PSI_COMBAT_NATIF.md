# Descriptions PSI et messages natifs de combat

## Traductions et comptage

17 paragraphes d'aide des capacités PSI apprises et26 messages complets de combat nouvellement traduits, soit43 sources distinctes, dans73 plages littérales originales. Les deux annexes partagées des aides ne sont pas deux sources supplémentaires. Les noms dynamiques et quantités ne multiplient pas le comptage. Les variantes accents/ASCII sont un seul travail.

Le compteur de cette exécution passe de15 à58 nouvelles sources ; le total historique passe de264 à307, dont137 déjà publiées et170 en attente. Les28 corrections françaises antérieures restent hors quota. Le lot de400 n'est pas achevé, aucune release n'est publiée à ce jalon de protection.

Exemples : récupération de HP/PP, poison, nausée, mini-fantôme, immobilisation, écrans et miroirs PSI, échec d'une attaque et absorption de PP. Les aides précisent les quantités, les cibles et les effets des écrans. La formulation de Foudre conserve le caractère approximatif des dégâts.

## Qualification et intégration

La table actuellement lue par le jeu est382915 :68 lignes de15 octets, aide à+11, niveaux d'apprentissage à+6..8. Les lecteurs01B694/01BB34 et toutes les lignes restent identiques. Les17 aides retenues ont un niveau d'apprentissage non nul ; cela ne prouve pas leur acquisition naturelle dans une partie complète.

Les messages de combat ont des lecteurs assembleur typés et un chemin statique depuis des actions liées aux ennemis, objets ou PSI qualifiés. L'analyse actualisée suit les retours de fonctions et résume les modes du processeur, avec PHP/PLP équilibrés :449 contextes,28843 états, aucun état en attente, six arêtes non résolues. Les branches restent abstraites ; les interactions de pile non modélisées et les appels indirects empêchent toute affirmation d'exhaustivité. L'échec2F766E avait également été observé en anglais dans une tentative privée de combat préparé ; cette tentative ne valide pas la victoire finale.

Les textes français sont recomprimés avec les seules entrées littérales inchangées du dictionnaire natif. Décodage français vérifié pour chaque profil ; aucune modification du dictionnaire ou du moteur. Chaque script tient dans sa plage initiale, commandes et destinations conservées. Les anciennes données après la nouvelle terminaison restent identiques. Les références intérieures sont conservées ou qualifiées dans des pixels réellement typés ; aucune référence brute ambiguë n'est ignorée.

Le message2F6AE0 n'est pas modifié : son adresse intérieure2F6AEE est référencée à195989, sans qualification suffisante du conteneur. Les graphismes supposés du jeu d'origine ne constituent pas une preuve valable pour ce port. Les banques25 et les sprites protégés sont identiques à l'entrée de cette phase.

## Affichage

276 PNG,138 paires avant/après,86 témoins source/profil. Toutes les différences sont confinées aux fenêtres de texte. Les17 aides sont affichées dans la fenêtre native2F, et les26 messages dans0E ; les deux profils ont été relus visuellement. Les premières sondes dans la petite fenêtre de conversation ont été écartées du dossier de validation.

Ces essais appellent artificiellement chaque script après préparation native des fenêtres et ajoutent une attente dans la fixture privée. Ils montrent le rendu et les retours à la ligne, avec Ninten et une quantité1 ; ils ne prouvent ni effets de combat, ni acquisition PSI, ni tous les noms longs, ni accès naturel aux scènes. Aucun état, cœur, ROM ou dump mémoire n'est joint.

Dossier : `tests/emulation_v78_native_battle_psi/coverage.json`. Contrôles : `tools/v78/test_native_battle_psi.py`, registre et contrôles globaux V78. 109 tests distincts validés avec ROM privée :108 passent dans la suite globale, puis le contrôle de registre actualisé passe séparément. Les échecs intermédiaires portaient sur les anciens compteurs figés, corrigés pour inclure les43 sources sans recompter les réparations françaises.

## Suite concrète

Poursuivre les autres lecteurs natifs de combat : variations d'attaque/défense/vitesse/cran, réveil et guérisons, retour à la normale, déviation PSI, arrivée d'un allié et croissance d'une graine. Les références exactes figurent dans `tools/v78/native_action_closure_inventory.json`. La sortie contient aussi des sources déjà françaises et des libellés à qualifier ; elle ne constitue ni un compteur d'anglais restant, ni un inventaire global sous400. Les accès calculés, graphiques et fins, puis la relecture complète restent ouverts.
