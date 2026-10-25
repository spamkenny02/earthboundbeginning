# Avertissements Util. et PP du menu principal

Deux messages réellement déclenchés par les menus ordinaires sont traduits : « The Lance-pierre is one of the items that can be equipped. » devient « Lance-pierre : à équiper. » ; « Not enough PP! » devient « PP insuffisants ! ». Chaque source complète compte une fois, même lorsque le refus est répété. Les deux textes correspondent à trois plages sources ; aucun nom d’objet ni contrôle n’est compté comme nouvelle traduction.

La préparation donne le Lance-pierre, ou porte Ninten au niveau99 puis vide/remplit ses PP par commandes natives. L’état privé initial et la ROM de préparation restent privés. Les choix Util. et PSI sont ensuite pilotés à la manette : aucun appel direct des avertissements ni des pouvoirs, aucune écriture directe de mémoire vive.

Trois chemins, accents et ASCII, avant/après :72 références de captures,36 paires,23 PNG uniques. Six paires changent uniquement dans les fenêtres de texte ; les30 autres sont identiques. Le refus de PP est rencontré deux fois par exécution et conserve0 PP. Le contrôle avec assez de PP lance PV+ α, fait passer les PP visibles de257 à252 (coût5) et conserve le message français « PV au max ! ». L’activation de la télépathie à l’auberge a aussi été observée séparément en français ; elle n’est pas recomptée et ne prouve pas les autres refus de déplacement.

Le message d’équipement est raccourci dans ses31 octets originaux. Celui des PP utilise19 octets du remplissage original vide3EFCE0–3EFCFD, hors sprites, graphismes, cibles de pointeurs et auxiliaire privé3EFC50–3EFCD0. Un saut à l’ancienne entrée08FAAA conserve le lecteur natif. Les commandes du texte, les conditions aux lecteurs01B033/01B6F9, le coût du pouvoir, les sprites et la banque25 restent identiques.

Quinze tests ciblés réussissent, dont trois nouveaux :143 tests distincts connus après la suite140 et son retest documenté, sans répétition d’une suite globale143. La reconstruction incrémentale gardée depuis le commit78ffca5 reproduit exactement les deux IPS. Le relevé borné HP reste à3896 racines, sans HP résiduel ni erreur ; il ne couvre pas le jeu entier.

Compteurs du même lot :116 nouvelles sources depuisfbd987c ;365 historiques,504 unités/plages sources,137 publiées et228 en attente. Les59 corrections françaises restent hors quota. Aucun400, aucun inventaire global sous400, aucun100% certifié. Les autres refus hérités doivent encore être qualifiés avant traduction.
