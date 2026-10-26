# V78 — relecture des questions du nommage initial

Deux formulations françaises raccourcies, zéro nouvelle source : « Quel est son nom à elle ? » devient « Quel est son nom ? » à04C1BC ; « Quel est ton plat préféré ? » devient « Ton plat préféré ? » à04C25C. Les champs natifs de40 octets, leurs terminateurs et les données voisines sont préservés. Les noms saisis, commandes, lecteurs et décisions du jeu ne changent pas. Compteurs inchangés :124 nouvelles sources dans le même lot400,373 historiques/550 unités,137 publiées/236 en attente ;61 corrections françaises hors quota.

## Qualification et affichage

La troncature « nom à elle ? » provenait d'un essai avec état repris. Elle n'a pas été reproduite dans les essais retenus, effectués depuis un démarrage vierge. L'affirmation antérieure d'un débordement général est retirée ; les modifications présentes sont des améliorations de lisibilité et de concision, pas deux nouvelles traductions ni une preuve d'un défaut généralisé.

Les cinq champs réellement demandés au départ sont contrôlés : Ninten, Ana, Lloyd, Teddy et plat préféré. Les anciens champs de chien et d'activité préférée, marqués Error dans cette ROM, ne sont pas présentés comme utilisés. Les valeurs A/B/C/D/E sont entrées avec les touches ; le récapitulatif les conserve. Un autre parcours saisit Mary, observe deux refus, puis accepte Maryy et rejoint le nommage d'Ana. Aucun état n'est chargé, aucun texte ou callback appelé directement, aucune modification temporaire de ROM : SHA de fixture identique au produit, liste d'écritures vide. Le choix d'un nom maximal n'est pas certifié par ces essais.

Huit essais avant/après, deux profils et deux parcours :120 références/60 paires/47 PNG uniques,16 différences dans la seule zone de question136,40–248,56. Les anciennes grandes formulations restaient lisibles sur le parcours vierge ; les nouvelles tiennent entièrement et libèrent de la place. Les autres questions, noms, refus et récapitulatif restent identiques. Les captures françaises des cinq questions et du parcours de refus ont été relues en accents et ASCII. Voir `tests/emulation_v78_initial_naming_prompt/coverage.json`.

Sept tests ciblés passent, dont deux nouveaux : reconstruction incrémentale depuisba972fa identique, seuls les deux champs autorisés changent, gardes altérées refusées, compteur inchangé et preuves image vérifiées.154 tests distincts connus, sans nouvelle suite globale154 ni recompression des graphismes. Voir `tools/v78/validation_initial_naming_tests.json`.

## Inventaire élargi des restes — qualification en cours

`inventory_live_residue.py` réunit les877 PNJ placés hors développeur86, portes typées, constantes natives immédiates, effets/aides des153 objets qualifiés,53 aides PSI apprises et entrées de fin connues. Le parseur de la fin native est utilisé ; les créations natives1F17 ajoutent les PNJ102,727,728 et741. Les700 champs du catalogue sont comparés entièrement, avec81 champs inchangés à classer.

Le relevé compte901 paires de constantes natives vers539 destinations,5213 racines explorées et834 plages inchangées/760 chaînes distinctes. Ces nombres ne sont pas des textes anglais à traduire : les candidats incluent noms propres, vocalisations, débogage, ancien EarthBound, données graphiques ressemblant à des chaînes et chemins non qualifiés.278 racines candidates ne se décodent pas comme scripts ; aucune racine directe des surfaces typées PNJ/portes/objets/PSI/fin ne figure dans ces échecs. Cela ne certifie pas tous les lecteurs ou dispatchs calculés. L'inventaire global pertinent sous400 et la couverture graphique complète restent non établis.

Les nouveaux lecteurs potentiels des monologues de Giygas en366A3C–366CDB sont conservés pour qualification : aucune traduction ne leur est attribuée sans accès observé. Les seules écritures de drapeaux0080/0095 relevées par ce graphe proviennent du sélecteur de scènes3749EC ; l'absence d'autre écriture littérale ne prouve pas leur dormance globale. Suite concrète : victoire instantanée2F7A28, sauvegarde perdue07C973 et qualification des lecteurs/spawns supplémentaires. Main demeure V77. Aucune ROM, aucun cœur, état ou dump mémoire distribué.
