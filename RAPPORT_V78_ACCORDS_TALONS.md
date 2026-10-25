# V78 — accords autour du suffixe des talons

Relecture nouvelle des courts fragments et assemblages, après le checkpoint584e8b6. Zéro nouvelle source anglaise comptée : le compteur reste15 depuisfbd987c et264 historiques (137 publiées/127 en attente),297 plages littérales.

Dix champs français corrigés : huit fragments dans32FA20, la réplique du reçu373C57 et le nom d’objet4D. Le message affichait notamment « 3 ticket(s) usagé(s)s », « le tickets usagé » et « Talon de billets ». Le suffixe natif pluriel373F15 reste identique ; son appel est déplacé entre « talon » et « de billet » dans le conteneur autorisé. Le libellé de retour devient « À rendre : talons de billet, s’il te plaît. » avec singulier au besoin ; tutoiement harmonisé. Le nom devient « Talon », ce qui permet « Reçu : Talon » ou « Talons ». La consigne utilise « Avec dix talons, monte dans le char ! ». Les espaces libérés sont reportés en fin de la ligne de rire, pour éviter un grand blanc au milieu de la phrase.

Les commandes et destinations restent identiques dans32FA20 et373C34. L’entrée et le terminal de32FA20, ainsi que l’entrée embarquée373CD8, restent aux mêmes adresses. Le nom garde son champ25 octets, un terminateur nul et les données d’objet suivantes intactes. Seuls trois enregistrements IPS sont ajoutés. Aucune allocation ni modification de sprites, banque25, helper partagé ou données financières.

## Observation et limites

Deux quantités,1 et3, dans les deux profils ;24 appels isolés,80 captures et40 paires avant/après. Les32 différences restent dans la fenêtre de texte104/8/248/100. Les huit paires de la branche protégée sont identiques. Singulier/pluriel et retours à la ligne des passages corrigés ont été relus.

Préparation : don natif de1 ou3 objets4D, comptage natif1A104D (le même lecteur que l’entrée du PNJ210), échanges/copies des registres textuels puis appel direct des branches. Le premier essai n’avait initialisé que le registre de travail : le nombre imprimé restait1 ; il a été rejeté comme preuve de quantité3. L’essai retenu initialise les deux registres par les commandes natives et affiche réellement1/3. Aucune écriture WRAM directe, aucun dump enregistré ou distribué.

Ces appels ne constituent ni achat, vol, sélection de tarif ni remboursement naturel. Les valeurs financières de l’état isolé ne sont pas préparées comme une vraie vente : aucun montant ou effet de remboursement n’est certifié. La préservation des commandes et des zones hors texte, ainsi que les paires, bornent la correction de langue.

Les97 tests V78 passent avec la ROM privée (suite complète,56,073s). Les preuves sont dans `tests/emulation_v78_stub_plural` ; outils et transformations : `stub_plural_review_stage.py`, `probe_stub_plural_review.py`, `verify_stub_plural_review.py`.

## Branche encore ouverte

La copie25D1C0 affiche encore « 3 talon de billets » avec une quantité3 préparée. Le contrôle a détecté son chevauchement avec des images de sprites réservées25D1C0..25D4C0 ; aucune écriture n’y est appliquée. Il n’existe plus de réserve sûre retournée par l’allocateur, ni d’intervalle originalement nul, actuellement nul dans les deux profils, non référencé et hors sprites d’au moins32 octets dans328A70..330FC0. Ne pas répéter ces recherches identiques ni relâcher le garde-fou. Une copie autorisée ou une réorganisation explicitement prouvée sera nécessaire pour ce chemin, avec ses appelants protégés de banque25 conservés.

## Nouvel inventaire des courts fragments

`short_literal_inventory_snapshot.json` conserve76 plages alphabétiques inchangées de moins de8 caractères, dans3405 racines typées de PNJ placés, sans erreur de décodage et hors PNJ86 comme graine. C’est le snapshot d’entrée de cette correction, non un audit présenté comme refait sur chaque build. Les relectures796 amorces/615 continuations restent historiques et ne sont pas répétées. La plupart des76 plages sont interjections, vocalisations, syllabes chantées ou nom propre ; aucune ne sert artificiellement au quota. Les articles a/an/some/the sont ceux du formateur original, déjà neutralisé chez les appelants qualifiés antérieurs ; la provenance restante passe par la copie non qualifiée du PNJ598. Le suffixe38D9AF et ses arguments restent à qualifier.

La recherche suivante porte sur les graphismes hors enseignes de services déjà traitées. Une bannière WELCOME TO/SNOWMAN a été observée après arrivée native préparée ; cette représentation de WELCOME TO manque encore, mais la source a déjà été comptée àSpookane et ne doit pas être recomptée. Les enseignes détectées PI sont des PIZZA, cognat conservé. Aucun400, aucun100% ni reste global inférieur à400 n’est établi.
