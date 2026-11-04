# Blender Manual: svensk granskningsbatch 39

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`.

## Omfattning

Åtta poster för Resursbibliotek har granskats: tillagda kopior, beroenden,
packning av länkade resurser samt relativa sökvägar.

*Mesh* behålls som Blenders etablerade datatyp i just beroendeförteckningen.
`Drivers` följer UI-katalogen som *drivrutiner*. Termerna *resursbibliotek*,
*länkad* och *tillagd* används konsekvent med de föregående batcherna.

## Kontroller

- `msgfmt --check --statistics`: 8 översatta meddelanden, godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 8/8 träffar.
- Hunspell `sv_SE`: endast PO-huvudets fält och etablerade projekttermer
  `mesh` och `nodgrupper`.
- `git diff --check`: godkänd.
- Gitleaks: inga hemligheter hittades.

Råexporten är orörd. Deltafilen arkiveras för en senare samlad uppladdning.
