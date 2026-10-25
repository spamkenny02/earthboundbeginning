# V78 — message conditionnel de gros gain de PV

« Sweet! » à2F7B94 devient « Super! » dans les six octets existants, pour les deux profils. Une nouvelle source, comptée une seule fois. Une autre occurrence originale8F440 reste inchangée et n’est pas requalifiée par ce test. Compteurs :106 nouvelles depuisfbd987c,355 historiques,464 unités/plages d’origine ;137 publiées et218 en attente. Les55 corrections de phrases françaises antérieures restent hors quota. Le lot400 demeure ouvert.

## Activation observée

La préparation utilise les commandes natives : Ninten ramené au niveau1, bonus de vitalité16, Teddy ajouté et porté au niveau99, Pendentif étoilé donné puis équipé à Ninten avec l’emplacement retourné par le don, soin et attente1020 images. Le combat17 est gagné par Auto. Le moteur attribue3317 EXP par personnage puis fait monter Ninten du niveau1 au niveau2.

Le recalcul natif produit un gain de240 PV max ; la condition du script2F7B83 (comparaison à20) active le message Sweet!/Super!. Le niveau suivant produit un gain ordinaire de15 PV max, sans ce message. Aucun appel direct du message, aucune écriture directe de résultat ou de mémoire vive. L’acquisition naturelle du bonus de vitalité et le trajet initial ne sont pas certifiés.

## Affichage et conservation

Quatre parcours avant/après, accents/ASCII, produisent68 références d’images,34 paires et23 PNG uniques. Seules deux paires changent, aux coordonnées52,18–76,29, entièrement dans le mot d’encouragement. Le nombre240, les autres statistiques, l’expérience, les messages des niveaux suivants, le gain ordinaire15 et tout le reste des images sont identiques. Aucun débordement ou nom tronqué dans ces captures.

Les six glyphes sont les seules différences de ROM par rapport au checkpointbd9b803. Le seuil20, sa branche vers2F7B9D, les commandes, pointeurs, frontières et tous les autres octets sont conservés. Le préfixe IPS du checkpoint complet est vérifié ; son ajout gardé reproduit exactement les IPS actuels. Une reconstruction de tous les graphismes déjà validés n’a pas été répétée pour ce seul champ.

La suite globale précédente de130 tests passe. Dix contrôles ciblés passent ensuite : deux nouveaux tests, compteurs, préfixes IPS, champs modifiés et garde du moteur. Cela représente132 tests distincts connus, sans prétendre à une nouvelle exécution globale de132 tests. Résultat : `tools/v78/validation_levelup_sweet_tests.json`.

L’inventaire borné sans HP résiduel est réutilisé : la seule mutation est Sweet!→Super!, de même longueur, sans HP, sans modification de commande ni de fermeture typée. Le SHA du nouveau produit est actualisé ; aucun nouvel audit global n’est revendiqué.

Aucune ROM, aucun cœur, état ou dump mémoire n’est distribué. Preuves : `tests/emulation_v78_levelup_sweet`. Les préparations natives restent distinctes d’un parcours naturel complet.
