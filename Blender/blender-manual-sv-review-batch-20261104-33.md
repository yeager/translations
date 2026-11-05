# Blender Manual: svensk granskningsbatch 33

Datum: 4 november 2026

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`.

## Omfattning

Fem tidigare oöversatta strängar från Outliner-dokumentationen:

- packning av externa filer och datablockstyper;
- det aktiva objektets rullning och utfällning;
- översikten över omorganisering, länkning och överordnade relationer.

`Outliner` behålls som ett synligt Blender-namn i manualen. I den löpande
beskrivningen blir *parented* "göras underordnade". Det uttrycker resultatet
av hierarkirelationen utan att blanda ihop den med egenskapen `Parent`, som i
Blenders gränssnitt heter `Förälder`.

En språklig eftergranskning den 5 november gjorde tre instruktioner mer
naturliga: *scroll into view* blir "rulla fram i vyn", och *parented* blir
"göras underordnade". Därmed behålls samma relation mellan objekten utan den
otydliga formuleringen "få en överordnad".

## Kontroller

- `msgfmt --check --statistics`: 5 översatta meddelanden, godkänd syntax.
- Radvis jämförelse av `(msgctxt, msgid)` mot råexporten: 5/5 träffar.
- Hunspell `sv_SE`: endast kataloghuvudets tekniska fält, produktnamnet
  `Outliner` och den etablerade sammansättningen `datablockstyper`.
- `git diff --check`: godkänd.
- Gitleaks: inga hemligheter hittades.

Råexporten är inte ändrad. Deltafilen är en separat kandidat för senare
uppladdning tillsammans med ytterligare självständigt granskade poster.
