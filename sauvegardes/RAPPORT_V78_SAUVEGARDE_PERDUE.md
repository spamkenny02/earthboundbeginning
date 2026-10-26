# V78 — perte et récupération native de sauvegarde

Le message système07C973 est réellement déclenché au démarrage de cette ROM. Une source complète, trois plages originales, devient « Nous sommes désolés… La sauvegarde {numéro} est perdue… ». L’excuse et l’explication forment un seul message, compté une fois quel que soit le numéro.125 nouvelles sources dans le même lot depuisfbd987c,374 historiques/553 unités physiques,137 publiées/237 en attente ;61 corrections françaises hors quota. Le lot400 reste ouvert ; aucune borne globale sous400 ni finalisation déclarée.

## Déclenchement et témoins

`probe_lost_save.py` génère une SRAM synthétique de8192 octets, sans lire ni modifier une sauvegarde utilisateur. Les six blocs utilisent la signature originale « HAL Laboratory, inc. », un pas de0550 octets et deux sommes de contrôle sur0530 octets de données ; la version0530 est à1FFE. Ces valeurs proviennent des instructions de la ROM actuelle, pas seulement de l’assembleur EarthBound de référence, dont les tailles diffèrent. Les gardes portent sur2F0591,2F05A9 et la séquence de version unique.

Une donnée est volontairement altérée sans modifier les sommes : les deux copies du slot1,2 ou3 ; la copie principale seule ; la copie secondaire seule ; aucune corruption. Le frontend reçoit cette SRAM au chargement, avant la première image. Aucun état repris, appel direct de validation/message, modification de ROM ou écriture WRAM. Les boutons du démarrage normal atteignent le choix de fichier et son contrôle natif. L’option `--sram-input` exige la taille exacte annoncée par le cœur ; l’inspection bornée `sram` ne sauvegarde pas de dump.

24 essais : six configurations×deux profils×avant/après. Les pertes des slots1/2/3 affichent le bon numéro. Avec une seule copie abîmée, la copie valide est recopiée silencieusement. Quand les deux sont invalides, le jeu efface les deux blocs et annonce la perte. Les six blocs finaux ont signature et deux sommes valides, données nulles ; leurs empreintes sont identiques avant/après. Les entrées synthétiques sont supprimées après l’essai. Les rapports ne contiennent que nombres, empreintes et commandes de lecture, jamais leurs réponses mémoire.

## Réinsertion et affichage

L’original07C973–07C9A8 est préservé intégralement, y compris ses possibles accès intérieurs. Seul le lecteur natif01ED25 change l’adresse immédiate basse et l’octet de banque vers une copie dans3EF600–3EF680. Chaque commande et le formatage du numéro sont identiques. Réserve nulle dans source et produit d’entrée, après flux graphique17 réel, hors sprites et cibles conservatives. Code d’intégrité, signatures, données SRAM, banque25 et sprites ne sont pas modifiés par l’IPS.

51 références de captures :48 de produit formant24 paires, plus3 images de contrôle sur ROM originale.17 PNG uniques,12 paires changent uniquement dans16,144–240,208. Retours et contrôles sans perte sont strictement identiques. Les deux pages françaises et les numéros1/2/3 sont lisibles, sans texte tronqué. Le profil ASCII remplace les accents.

Le fond strié observé pendant le message est **déjà présent dans la ROM originale**, confirmée par son SHA256 source et le même SRAM/boutons. Hors libellés français du menu de fichiers, les trois images originales sont identiques au produit avant cette étape. Ce défaut hérité n’est ni une corruption nouvelle de l’IPS ni un affichage nettoyé par ce correctif ; il reste explicitement signalé.

## Vérifications et suite

12 tests ciblés passent, zéro ignoré. Trois méthodes nouvelles portent le total distinct connu à160, sans répétition générale160. L’ajout incrémental aux IPS be25a9e est exact ; modifications hors adresses autorisées exclues, gardes altérées refusées, compteur/registre/empreintes et comparaisons d’images concordants. Les tests historiques de stages vérifient leur préfixe, car l’IPS continue de s’étendre.

La sauvegarde be25a9e a été téléchargée et restaurée dans le dépôt de base, commit/arbre exacts ; arbre GitHub reconstruit localement et guide relu. Les binaires privés ne sont pas distribués. Poursuivre les candidats avec provenance réelle, les accès calculés et graphiques, puis la relecture globale ; les834 plages de l’ancien inventaire sont des candidats, pas834 textes utilisés ni un volume à traduire.
