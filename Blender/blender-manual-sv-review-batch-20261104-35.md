# Blender Manual: svensk granskningsbatch 35

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`.

## Omfattning

Fyra Outliner-poster har korrigerats:

- `Apply` har rättats från det semantiskt felaktiga *lägga till* till
  *tillämpa*.
- Kontextmenyn, dubblett och länkad dubblett har svensk synlig text.
- `3D Viewport` följer Blender UI-katalogens term *3D-vyport*.
- Båda RST-destinationerna och avskiljaren `--` har bevarats exakt.

## Kontroller

- `msgfmt --check --statistics`: 4 översatta meddelanden, godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 4/4 träffar.
- Hunspell `sv_SE`: endast PO-huvudets tekniska fält, RST-rollen,
  produktnamnet `Outliner` och termen `3D-vyporten`.
- `git diff --check`: godkänd.
- Gitleaks: inga hemligheter hittades.

Råexporten är oförändrad. Deltafilen arkiveras för den samlade uppladdning
som sker när fler självständigt granskade poster har lagts till.
