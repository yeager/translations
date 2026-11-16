# Cataclysm-DDA, svenska: batch 66

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De gäller inaktivering av bionik samt
förutsättningar för kalori- och bränsledrivna funktioner.

Källkontexten kontrollerades i `src/bionics.cpp`. Svenska formuleringar
undviker könsberoende pronomen och okänt grammatiskt genus för
platsmarkörernas bioniknamn. Taggen `<npcname>` är bevarad där den behövs.

## Kontroller före API-inskick

- Platsmarkörer och XML-liknande taggar ska stämma mellan källa och mål.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för sammansättningar och
  projektspecifika termer.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio översättningar via Transifex API.
En ny, oberoende GET-återläsning jämförde sedan varje målsträng med denna
batch. Alla 10 av 10 stämde exakt.

svlangs enda V2-varning gäller en korrekt platsmarkörsfras följd av en bisats
och är en falsk positiv. Hunspell-SV rapporterade inga stavningsfel.
