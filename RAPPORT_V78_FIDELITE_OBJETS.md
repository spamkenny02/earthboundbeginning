# V78 — relecture bilingue des objets

153 lignes d’objets qualifiés relues : noms et textes littéraux de leurs152 racines principales d’aide, soit203 plages alphabétiques. Le doublon des champignons est partagé. B8/Débogueur est exclu. Le registre contient les sources anglaises, le français avant correction, les adresses et les limites : `tools/v78/item_fidelity_review.json`. Les auxiliaires imbriqués ne sont pas tous couverts par cette nouvelle passe.

Treize champs français sont corrigés : douze plages d’aide et un nom d’objet. Vitalité (Strength) et Force (Force) sont distinguées dans les deux capsules ; Capsule combat remplace Capsule de cran pour correspondre au menu Comb. Le badge reçoit le sujet manquant (« Gardé parmi tes objets, il… »), les deux maquettes passent au tutoiement, la description du talon suit le nom employé par le pilote ; banane, pomme, poire, herbe secrète, briques de crème/lait perdent leurs accords masculins incorrects. Le nom raccourci mesure68 pixels pour une limite80.

Les frontières de scripts, destinations et commandes natives restent identiques. Banque25 et sprites préservés, données d’objet hors nom inchangées. HP reste cohérent avec l’interface graphique existante : la tentative historique PV de V37 avait révélé des tuiles partagées ; cette relecture ne change pas le HUD.

140 captures,70 paires,28 paires différentes,26 témoins de cas dans les deux profils. Les changements restent entièrement dans la fenêtre d’aide(96,8)–(248,72). Les planches des passages modifiés accents/ASCII ont été relues. Preuve : `tests/emulation_v78_item_fidelity/coverage.json`. Les scripts d’aide sont appelés artificiellement ; noms et descriptions réels sont rendus par le moteur natif, mais ni acquisition naturelle ni effets d’objets ne sont certifiés.

La qualification nouvelle de l’animation6 a identifié TO BE CONTINUED dans20E851, plutôt que THE END. Ses deux sites de création hérités sont09C981 et38ED7E. La fin actuelle observée passe par le rappel téléphonique puis la boucle09C98A, qui saute le site antérieur. L’activation de la branche alternative n’est pas démontrée : aucun graphisme modifié ni source comptée. Voir `tools/v78/ending_animation_qualification.json`. Ne pas traduire ce candidat pour remplir le quota.

Zéro nouvelle traduction distincte dans ce jalon :15 depuisfbd987c,264 historiques dont137 publiées et127 en attente ;297 plages originales. Les corrections françaises de l’exécution passent de15 à28, sans augmenter le compteur de sources. Lot400, relecture complète et achèvement global toujours ouverts. ROM/cœur/états/dumps exclus des preuves publiques.

104 tests V78 passent avec la ROM privée (56,916s), après mise à jour du registre de validation et du contrôle de la nouvelle étape. Les deux IPS sont reconstruits : accents`a5793faf96798bdb47f4c86e8815f52c27a195ea67354280d872ee6b975c0b2b`, ASCII`18e86c2bbe5c10efce4b310355d9c3f55fc027e77a2cc0838c355dc0236a15cb`.
