# Blender Manual: svensk granskningsbatch 34

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`.

## Omfattning

Åtta Outliner-poster i `editors/outliner/usage.rst` har granskats:

- flyttning och länkning till samlingar;
- överordnade relationer, även mellan samlingar;
- den exakta API-referensen `bpy.types.Object.parent`;
- drag-och-släpp-operationernas räckvidd för urvalet.

Termerna följer UI-katalogen: `Move` → *Flytta*, `Link` som operatör →
*Länka*, `Set Parent To` → *Sätt överordnad till*, och `Clear Parent` →
*Rensa överordnad*. RST-rollerna och kortkommandona är oförändrade.

UI-kontrollen den 5 november visar att `Parent` varierar med sammanhanget:
den fristående egenskapen använder *Förälder*, men objekt- och
samlingshierarkin använder *överordnad*. Batchens åtgärdsrubriker följer
därför hierarkisammanhanget medan förklarande text använder
*föräldrarelation* när själva relationstypen avses.

## Kontroller

- `msgfmt --check --statistics`: 8 översatta meddelanden, godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 8/8 träffar.
- Hunspell `sv_SE`: endast PO-huvudets tekniska fält, RST-roller,
  kortkommandot `Shift` och API-identifieraren `bpy.types.Object.parent`.
- `git diff --check`: godkänd.
- Gitleaks: inga hemligheter hittades.

Råexporten är orörd. Deltafilen arkiveras för en kommande, samlad
uppladdning efter fortsatt oberoende granskning.
