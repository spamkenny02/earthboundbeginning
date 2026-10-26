# V78 — avertissement critique, raccrochage et refus de nom

Trois nouvelles sources complètes,15 plages originales : alerte d'état critique, bruit du raccrochage partagé, nom déjà porté par un personnage. Les six composants des deux auxiliaires de genre font partie de l'alerte, sans devenir six sources supplémentaires. Compteurs du même lot400 :124 nouvelles depuisfbd987c,373 historiques/550 unités sources,137 publiées/236 en attente ;59 corrections françaises hors quota. Aucun400, reste global sous400 ou100% certifié.

## Alerte et raccrochage

Après une préparation native du niveau99, des PV diminués de90% et du rhume, les dégâts périodiques de l'exploration appellent normalement07C7AF. Le texte français indique l'état critique et « Il/Elle s'écroulera si son état reste sans soins. ». Ninten et Ana sont contrôlés ; l'état sain avec rhume conserve assez de PV et ne déclenche pas l'alerte. Le recrutement, le niveau et l'affliction sont préparés par commandes du moteur, hors IPS ; leur acquisition initiale n'est pas naturelle. Ni appel direct de l'avertissement ni écriture du testeur en WRAM.

L'alias intérieur07C7DF reste intact. Un pont de cinq octets au début de l'alerte mène à une copie ; les commandes sont identiques après normalisation des deux pointeurs d'auxiliaires. Les auxiliaires originaux restent inchangés ; les copies conservent classification et dispatch à trois branches, avec Il/Elle/Ça et son/son/son. Il/Elle sont observés ; Ça reste seulement vérifié statiquement.

La copie réemploie159 octets dans3EF580–3EF944 : remplissage original nul, également nul dans les deux profils d'entrée, après la fin réellement décodée du flux graphique17. Fins originales/currentes :3EF55E/3EF579. Cette réserve est comprise dans le bourrage d'alignement d'un ancien enregistrement IPS ; elle ne fait pas partie du flux compressé actif. Décompression, pointeurs conservateurs, empreintes de sprites, banque25 et auxiliaire privé restent contrôlés. Aucun graphisme n'est recompressé ou modifié.

Le champ partagé07DE3E devient « @clic ! Biiiiip... », à taille compatible, commandes inchangées. Le témoin est l'appel temporel du père après attente réelle du minuteur, choix Oui et réarmement observé. Les états d'attente ont été recréés après la restauration du workspace ; le compteur n'est jamais forcé. Les autres branches du téléphone déjà validées ne sont pas toutes rejouées pour ce seul bruit partagé.

Les16 essais retenus produisent260 références/130 paires/60 PNG uniques :42 différences confinées à104,16–240,72 ; les contrôles hors alerte sont identiques. Le raccrochage ne change qu'en page8. Voir `tests/emulation_v78_critical_phone_tail/coverage.json`. Les passages français et les genres sont relus dans les deux profils, sans débordement observé.

## Nom réservé — accès naturel

Depuis un démarrage vierge, sans état, SRAM du testeur ou ROM temporairement modifiée, le vrai menu Nouvelle partie mène au nommage de Ninten. Les touches saisissent Mary, refusé deux fois ; Maryy est ensuite accepté et le nommage d'Ana apparaît. La comparaison avant/après conserve exactement les touches et toutes les images hors du texte de refus.52 références/26 paires/19 PNG, quatre différences limitées à24,96–232,120. « Un personnage porte déjà ce nom. » tient intégralement, accents/ASCII. Le lecteur natif38C3E8, les noms réservés et les commandes du message restent identiques.

Cette protection concerne le nom d'un personnage au démarrage. Le nom du joueur demandé plus tard suit un autre chemin ; une saisie à cet endroit n'est pas une preuve du refus. Aucune branche n'a été qualifiée par un appel artificiel au texte de refus. Voir `tests/emulation_v78_name_collision/coverage.json`.

## Contrôles, sauvegarde et suite

Onze tests ciblés passent : cinq nouveaux, soit152 distincts connus avec les validations antérieures ; pas de nouvelle suite globale152. Les ajouts incrémentaux depuis5170b1a reproduisent les IPS exacts, les gardes altérées sont refusées, commandes et auxiliaires sont contrôlés et les preuves image sont revérifiées. Voir `tools/v78/validation_critical_name_tests.json`.

Le workspace est revenu à775b0a6 pendant la reprise. Les cinq anciens fichiers locaux sont protégés par stash et `checkpoint/recovered-local-before-5170b1a`. Dix bundles téléchargés sur le checkpoint distant ont été vérifiés/fetchés dans l'ordre ;5170b1a et son arbre948c8fbd sont restaurés exactement, sans toucher l'archive locale préexistante. Les nouveaux fichiers d'alerte/raccrochage perdus avant leur checkpoint ont été réintégrés et leurs preuves rejouées, sans nouveau recomptage. Un premier essai d'émulation n'avait pas attendu la création de son état temporel : l'échec est exclu des preuves ; seules les sorties terminées et leurs SHA servent au collecteur.

Suite concrète : la question française du nommage d'Ana déborde et ne laisse voir que « nom à elle ? » ; corriger cette formulation existante, hors quota. Puis qualifier le message d'expérience de victoire instantanée, le PNJ102 créé dynamiquement et les restes calculés. L'inventaire global du périmètre reste à établir ; main demeure V77. Aucune ROM, aucun cœur, état ou dump mémoire distribué.
