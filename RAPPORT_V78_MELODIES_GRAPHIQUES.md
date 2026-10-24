# V78 — les légendes de l’Ocarina

Suite du même travail interne, après le checkpoint71f6b84. Quatre nouvelles sources graphiques distinctes :

| Source | Français visible | Icône |
|---|---|---|
| Doll | POUPÉE / POUPEE | 0 |
| Canary | CANARI | 1 |
| Monkey | SINGE | 2 |
| Grave Stone | PIERRE / TOMBALE, sur deux lignes | 7 |

Piano, Dragon, Cactus et EVE sont préservés et ne servent pas au quota. Les quatre légendes portent le compteur de cette exécution à15 sources depuisfbd987c ; total historique264, dont137 publiées et127 en attente. Les249 sources littérales et297 plages littérales ne changent pas. Le seuil400 n’est pas atteint ; aucune release ni complétude globale n’est annoncée.

## Accès réellement exécuté

Objet79, Ocarina, action native0102. Une fixture privée accorde l’objet, prépare explicitement les drapeaux00B6..00BD et une arrivée parwarp2 àPodunk. La suite utilise les touches ordinaires : Objets, sélectionOcarina, utilisation et lecture des mélodies. Le testeur n’appelle ni le script d’utilisation ni l’écran cible directement ; il n’écrit pas laWRAM. L’acquisition naturelle de l’objet et des mélodies, ainsi que le parcours initial, ne sont pas prouvés.

La première lecture courte ne montrait pas Doll : l’icône active utilise son image sans légende. L’essai conservé laisse la lecture se poursuivre, jusqu’à voir aussi cette légende et les huit icônes. Les fichiers publics sont dans `tests/emulation_v78_melody_labels` :64 captures,32 paires,312 correspondances de motifs d’icônes ; les huit icônes sont observées avant et après dans les deux profils. Les32 différences de frames sont limitées aux rectangles des légendes concernées. Les étapes d’inventaire précédant l’écran ne changent pas.

## Intégration bornée et relecture

Le lecteur natif4ACF0 charge le bloc20B16D et copie2C00 octets décomprimés. Le nouveau flux reste dans son conteneur existant20B16D..20CE2F :7228 octets compressés pour une capacité7362. Le lecteur, la palette et les octets hors conteneur restent identiques. Le flux est décompressé indépendamment et comparé aux pixels attendus.

Seuls les anciens pixels des lettres, leur ombre voisine et les nouvelles lettres/ombres sont possédés. Le fond à l’intérieur des anciennes lettres est reconstruit à partir de l’image native sans texte avec une correspondance majoritaire d’indices gris ; il ne faut pas présenter cette reconstruction comme une récupération certaine des pixels originellement cachés par l’anglais. Tous les pixels hors masque sont identiques. Les autres icônes et toutes les images d’animation sans légende, à partir de la ligne64 du canevas décomprimé, sont identiques.

Relecture des quatre noms communs : accents, singulier, fidélité au sens, absence de troncature et séparation en deux lignes pour Pierre tombale. Les deux profils ont été affichés. Aucun nom propre n’est traduit pour augmenter le volume. Les94 tests V78 passent avec laROM privée (suite complète,92,137s), dont les vérifications de pixels, conteneur, chemin préparé, empreintes des captures et motifs réellement affichés.

IPS accents : `92e60279f04c406665da87a9ebb72b66acc1d14f977037fb8fca0147aa6586fd` ; cible privée `903a355e611e718d168529b679258bcb8a84128531d9065f4a16ddd3ccef6e5f`.

IPS ASCII : `3d44022dde31635a06d0d7192ac739a5e4dd03f4ea9b8e10207a8ad6102caf1e` ; cible privée `3950da20591ef5d1c7dbae74f48c84b24a961293f9b988a411203d0dfe9e3f5c`.

## Suite concrète

Les circonflexes du décor dePodunk restent ouverts : les512 indices autorisés sont tous référencés ; aucune paire exacte, même avec retournement horizontal/vertical et conservation des deux couches, n’a fourni d’emplacement supplémentaire sûr dans l’analyse de cette étape. Ne pas répéter cette recherche identique sans nouvelle piste ni dépasser la borne photo sans validation de son lecteur.

Les légendes de carte et les groupes436/213 restent non qualifiés comme décrit dans le rapport des panneaux. Reprendre les autres courts champs et assemblages non couverts par la relecture796 amorces/615 continuations, puis compléter les accès calculés, fins et relecture globale. Aucun inventaire global certifiant moins de400 restes n’est disponible. ROM, cœur, états et dumps ne sont pas distribués.
