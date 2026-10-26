# V78 — appel du père après une longue session

Cinq sources complètes nouvellement traduites : la question partagée, puis les réponses Oui/Non adressées à Ninten ou à son compagnon. Six occurrences physiques,31 plages alphabétiques ; les deux copies de la question sont une source, les libellés Oui/Non déjà acquis ne sont pas recomptés. Compteurs du même lot400 :121 nouvelles depuisfbd987c,370 historiques,137 publiées/233 en attente,535 unités/plages sources ;59 corrections françaises hors quota. Aucun400, reste global sous400 ou100% certifié.

## Déclenchement et effets

Le minuteur natif9E54 est initialisé à1687 et décrémenté par le moteur tous les256 frames. Les états privés ont été préparés par attente effective depuis la chambre de référence, jusqu'à1 ou2 ; aucun compteur n'a été écrit, aucun appel au dialogue du père n'a été injecté. Le délai franchit ensuite zéro par700 frames ordinaires. L'appel se présente d'abord sans fenêtre, en attente de A. Après les pages et le vrai choix Oui/Non, le raccrochage réarme le minuteur :1687 dans les essais Ninten,1686 avec compagnon, avant/après identiques.

La branche compagnon est obtenue par commandes natives déclarées `1F1102 1905010103` (Ana rejoint le groupe, Ninten est diamantsé), hors IPS. L'affliction et le recrutement ne sont pas acquis naturellement. Le déclenchement temporel et la sélection des branches, eux, suivent le moteur normal depuis ces préparations. Les branches anciennes conditionnées par0095/0080 ne sont pas qualifiées et restent intactes.

## Intégrité et affichage

Les quatre réponses et les deux questions conservent les commandes, noms dynamiques, choix, délais et appels de raccrochage. La copie de la question Ninten part de07D36E pour préserver l'alias conservateur07D37E et toute l'ancienne question. Des segments utilisent uniquement les plages originales nulles qualifiées du décor17, hors pointeurs conservateurs, allocations antérieures et auxiliaire privé3EFC50–3EFCD0.392 octets alloués accents,369 ASCII. Banque25, sprites, pointeurs des branches non qualifiées et code du minuteur restent identiques.

Un essai préparatoire a révélé qu'un saut ne doit jamais couper l'argument terminé par02 de la commande de menu1902. Le découpage exclut désormais explicitement ces frontières ; le test vérifie cet invariant. Le suivi du menu accepte aussi le pointeur de reprise situé juste après11, avant un saut de segment vers12. Les essais préparatoires défaillants ne sont pas des preuves publiées.

Les16 essais retenus couvrent deux profils, deux états d'équipe et deux choix, chacun avant/après.204 références de captures,102 paires,82 PNG uniques ;86 différences dans104,16–240,72 seulement,16 paires identiques (sonnerie et retour à la carte). Touches, nombre de captures et valeurs du minuteur identiques dans chaque paire. Les huit parcours français sont relus visuellement, noms et retours à la ligne compris ; pas de débordement observé. Le bruit de raccrochage `click! Beeeeeeep...` reste anglais et constitue un reste concret à localiser, sans prétendre la scène intégralement française.

## Contrôles et reprise

Douze tests ciblés passent, dont quatre nouveaux : reconstruction incrémentale depuis02443c1 identique, concaténation des segments/commandes native, gardes/allocation altérées refusées, preuves d'émulation et décompte dédupliqué.147 tests distincts connus avec les validations antérieures ; pas de nouvelle suite globale147 ni reconstruction globale inutile. Le premier essai du registre a échoué car son générateur n'incluait pas encore les deux occurrences de question ; générateur corrigé puis douze tests réussis. Voir `tools/v78/validation_dad_phone_tests.json` et `tests/emulation_v78_dad_phone/coverage.json`.

Le nouveau relevé borné de boucle principale00B7D8 compte900 contextes,77522 états,150 racines,11 transferts non résolus et zéro frontière restante. Une garde exacte de SETJMP008F42 permet son seul retour normal M/X16 ; LONGJMP n'est pas modélisé. `tools/v78/native_main_loop_inventory.json` conserve ses limites : ce n'est pas une couverture globale. Sources assembleur primaires : ebsrc68aec5c, `src/system/main.asm`, `src/system/setjmp.asm`, `src/overworld/load_dad_phone.asm`, `process_overworld_tasks.asm`, `process_queued_interactions.asm`.

Suite : bruit partagé du raccrochage, alerte d'état critique, refus de nom déjà utilisé et victoire instantanée ; qualifier les accès avant traduction. Le lot400 reste ouvert, main demeure V77. La sauvegarde distante02443c1 est téléchargée, vérifiée par SHA256, restaurée dans un dépôt à base seule ; arbre distant d33e45f reproduit exactement par les trois entrées sauvegardées. Aucune ROM, aucun cœur, état ou dump mémoire distribué.
