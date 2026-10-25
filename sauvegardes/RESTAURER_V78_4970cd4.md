# Checkpoint V78 — PV et retrait préparé

Ce jalon protège le même lot de400 encore ouvert :102 nouvelles sources depuisfbd987c,351 historiques,137 publiées/214 en attente. Il n'ajoute aucune nouvelle source au quota. La jauge graphique passe de HP à PV,26 fragments français sont harmonisés, et le combat préparé de Giygas est suivi jusqu'au retrait et au retour sur la carte.119 tests passent sans erreur ni test ignoré. Ni arrivée naturelle au boss, ni callback de mort, ni parcours de fin/générique ne sont certifiés par ces essais.

- Commit local : `4970cd47612ac7f2b3b60e48df7cbc90e7a34e99`
- Arbre local : `bf4bc2c0072423baf2594c5595b46add485e3802`
- Ref : `refs/heads/checkpoint/v78-pv-retreat-validated`
- Prérequis : `1eff8062f85bdca7153bdc567ca7699eff6c0452`
- Bundle : `EarthBound_FR_V78_4970cd4.bundle`,2912569 octets
- SHA256 : `dc83fd1044f08965369cc428224af338d04fb9f00d759841d8767349591dbb3e`

Restaurer d'abord la chaîne indiquée dans `RESTAURER_V78_1eff806.md`, puis :

```sh
git bundle verify EarthBound_FR_V78_4970cd4.bundle
git fetch EarthBound_FR_V78_4970cd4.bundle refs/heads/checkpoint/v78-pv-retreat-validated:refs/heads/restored-pv-retreat
git rev-parse restored-pv-retreat restored-pv-retreat^{tree}
```

La restauration dans un dépôt distinct a reproduit le commit et l'arbre exacts. Les captures et rapports publics sont inclus ; ROM, cœur, états et dumps mémoire restent privés. Lire `RAPPORT_V78_PV_RETRAIT.md`, `REPRISE_TRADUCTION.md` et les fixtures pour les limites et la suite. Main et releases ne sont pas modifiés à ce jalon de protection.
