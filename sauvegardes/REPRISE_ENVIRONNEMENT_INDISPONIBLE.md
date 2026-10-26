# Reprise d'urgence — environnement d'exécution indisponible

Blocage constaté le26 octobre2026 : l'environnement sélectionné est devenu indisponible. Une commande Git de lecture échoue avec « No usable execution environment is available. Wait for an environment to become available before using this tool. ». Il est impossible de lire/committer les dernières modifications locales, de reconstruire ou de relancer l'émulation. Cela ne signifie pas que la ROM, le cœur ou les états ont été supprimés : ils étaient présents et utilisables avant l'interruption, leur récupération reste à vérifier.

## Dernière sauvegarde complète vérifiée

Branche distante checkpoint/v78-proofreading-44984fc, dernier commit avant ce dossier : cf643ac433dac596796695dce71277ccef4d3ff3, arbrec2feab81d125cacc4d3a1c8f5f8bef87c781a0bc. Elle contient le bundle du commit local0df2d43c6c64b54cc2e7cbf8faa1dffd2fbbb749, arbre2fe445ee696271ae5d3f75f75a9a8e8679142963, 73312octets, SHA2568c84ade58762afe6f56f4fa40f8380f43bd98deccca73c1c90f5d937aad240d6. Ce bundle a été téléchargé, haché et restauré exactement dans le dépôt de base ; guide comparé et arbre distant reconstruit avant l'interruption. Il dépend de65bec38, lui-même des bundles antérieurs archivés.

Cette base protège les deux IPS, les outils et les preuves jusqu'au signal Escargo et à la classification des81 champs inchangés :125 nouvelles sources dans la même exécution,374 historiques/553 unités physiques,137 publiées/237 en attente ;61 corrections françaises hors quota.162 tests distincts connus, sans suite globale162. Main reste V77db524666b87ecd006f4c313ad32233da2ac8137c. Aucun lot400 ni100% déclaré.

## Dernier ajout local, à récupérer en priorité

Le correctif Teddy a ensuite été intégré aux deux IPS et testé localement, mais n'a pas pu être committé avant l'indisponibilité. Fichiers attendus : tools/v78/teddy_check_stage.py, probe_teddy_check.py, collect_teddy_check.py, test_teddy_check.py ; tests/emulation_v78_teddy_check ; fixtures, plan, registre, constructeur et compteurs actualisés. Le rapport local est RAPPORT_V78_EXAMEN_TEDDY.md. Ne pas écraser ces fichiers s'ils réapparaissent.

Le présent dossier protège des copies de récupération reconstituées à partir des commandes exécutées dans la conversation, et l'enregistrement IPS exact. Les empreintes des fichiers locaux ne sont plus accessibles : aucune identité octet par octet avec le workspace perdu n'est prétendue. Les PNG/JSON du dernier essai ne sont pas récupérés dans cette sauvegarde d'urgence. Les fichiers sources de récupération n'ont pas été exécutés de nouveau après reconstitution.

Source352D53 : « He lays very quiet and still. » devient « Il reste calme et immobile. »,30octets à taille constante avec deux espaces. L'enregistrement complet est dans patch_teddy.json, identique pour accents/ASCII. Commandes, autres réponses et données hors champ restent inchangées dans l'ajout testé. Une seule nouvelle source/plage :126 nouvelles dans la même exécution,375 historiques/554 unités,137 publiées/238 en attente ;61 corrections françaises maintenues. Ne pas remettre ce compteur à zéro ni recompter Teddy après reprise.

Avant l'interruption : huit essais en émulation,40 références/20 paires/12 PNG ; quatre différences dans la seule phrase, bbox111,18–226,29. Les dix tests ciblés ont terminé avec10réussites,0échec,0erreur,0ignoré ; deux méthodes nouvelles portent le total distinct connu à164, sans suite globale164. Ce sont des observations de l'exécution locale interrompue, pas des preuves reproduites après restauration. Les rapports/captures doivent être récupérés ou rejoués.

## Reproduction exacte du cas

La ROM privée doit avoir le SHA256e878b83e9b00b51f8da6d038a5cbaf31cb9dccff5e11f0a7014048f4511f582c ; le cœur utilisé avait le SHA256f15fbd2724a62c5f9df0327cb41f07a1b111dfe966c65b27e0f21c06ad3e05b6. États privés d'hôtel reference_v71_lodging/{accents,ascii}/accept/handoff.state. Ces fichiers ne sont pas distribués.

Le vrai hook natif Check38799B est appelé par1327F ; son cas NPC607 retourne352D42. Il avait été rapproché à tort du débogage. Teddy est placé à6445,4319, secteur537, apparition03B4. Le setter03B4 est36A7EE, dans une branche issue deNPC836 ; clear352DD3 dans un script de porte. Le voyage et la blessure ne sont pas joués naturellement par les sondes.

Préparation présente :04B4030503000504001F2102 ; absente :05B4030503000504001F2102. Le warp2 privé arrive à6440,4336,direction1. Depuis l'état d'hôtel :60images ; A,Droite,A,A,A ;1800images ; B huit fois ;60images puis une image échantillonnée ; Haut huit images puis une image échantillonnée. Teddy présent : position6440,4328. Pour chaque examen : A,Bas,Bas,A ;600images puis une image échantillonnée ; capturer ; A,120images,A,120images ; capturer le retour. Quatre examens présents, un absent.

Les quatre pointeurs de message observés présents sont352D72/352D90/352DB2/352D72. Après fermeture, drapeaux0003/0004 :1/0,1/1,0/0,1/0, identiques avant/après. Les drapeaux sont numérotés à partir de1 : le lecteur21628 décrémente avant le masque ; pour0003/0004, bits4/8 de l'octet9C08. Le cas absent sélectionne921, affiche R.A.S. et garde les deux drapeaux nuls. Aucun script Teddy appelé directement, aucune écriture WRAM. L'initialisation est déclarée artificielle.

## Intégration après restauration

1. Vérifier processus/verrou/Git et préserver tous les locaux. Retrouver d'abord l'ancien workspace s'il existe ; ne pas importer aveuglément ce dossier par-dessus un ajout Teddy déjà présent.
2. À défaut, restaurer la chaîne de bundles jusqu'à0df2d43 et vérifier commit/arbre. Copier les quatre sources de ce dossier vers tools/v78 dans une copie de travail isolée.
3. Dans build_v78.py, après courier_buzzer : affecter son résultat à plan, importer extend de teddy_check_stage, puis le retourner. Appliquer l'extension incrémentale à la ROM épinglée, aux deux IPS et aux fixtures/plan. Ne pas l'appliquer deux fois.
4. Ajouter les entrées teddy_check au générateur update_ledger.py ; mettre à jour execution_records.json et son dernier run125→126, ajouter352D53 aux offsets. Actualiser les assertions de compteurs375/554/126 et la liste de stages IPS dans les tests existants. Préserver le préfixe historique du test courier_buzzer et son snapshot de catalogue.
5. Rejouer probe_teddy_check.py avec ROM/cœur/états privés, puis collect_teddy_check.py. Récupérer ou reconstruire les40 références/12 PNG, vérifier les effets et relire les images ; lancer test_teddy_check et les tests de registre/préfixe/compteur concernés. Les rapports initiaux ne valident pas une ROM différente.
6. Réconcilier les métadonnées sans inventer des preuves, puis commit local et bundle de protection vérifié. Pas de publication main tant que le lot400, une exception globale étayée ou la finalisation complète ne sont pas établis.

## Analyses locales supplémentaires et errata à préserver

La fermeture typée incluant les spawns a parcouru4095racines sans erreur de parsing.191 commandes1A0C ont37cibles natives. Commandes de scène :3→3occurrences,5→22,6→25,7→1,9→1,12→1. Le générique actuel est1F410C à38ED14 ; aucun1F410B CAST dans cette fermeture. Le relevé des rappels a357contextes/22902états, six racines parsées sans plage alphabétique et sept limites natives non résolues. Les sources locales inventory_special_scenes.py, inventory_room_access.py et l'extension de inventory_native_action_closure.py n'ont pas de bundle après0df2d43 ; les récupérer si le workspace revient, sinon refaire ces analyses. Ce sont des indications bornées, pas une couverture globale ni une borne sous400.

Erratum à RAPPORT_V78_SIGNAL_CATALOGUE.md : les destinations des portes sont en unités de8pixels. Le garde006CFC est a00800b70a0a0a0a8502a00600b70a851429ff3f0a0a0a8504. Le secteur30 a des portes entrantes depuis62/157/919 et sortantes vers62/157/919. L'ancien constat d'absence de porte et les destinations3/98/3 doivent être retirés. NPC390 est un objet présent à7868,203, voisin de391 à7868,219 ; son anglais09886F n'a pas été activé par les essais normaux Parler/Voir. Ne pas le traduire pour remplir le quota.

Reste concret suivant : HÔTEL/HÔPITAL de Podunk restent sans circonflexe dans le profil accents. L'essai de recherche de doublons graphiques compatibles avec les flips et les deux couches a été interrompu avant tout résultat ; il ne valide aucune allocation ni correction. Préserver sprites, animations, palettes, couches et limite photo512. Restent aussi qualification des accès calculés, recherche graphique globale et relecture intégrale. Aucun achèvement annoncé.

L'automatisation est suspendue pour absence d'environnement d'exécution utilisable, pas parce que la traduction est terminée. Reprendre le même lot et ses126sources acquises quand le poste et les preuves seront de nouveau disponibles.
