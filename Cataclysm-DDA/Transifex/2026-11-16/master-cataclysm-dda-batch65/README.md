# Cataclysm-DDA, svenska: batch 65

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De gäller kabelansluten kraftförsörjning och
avaktivering av bionik.

Källkontexten kontrollerades i `src/bionics.cpp`. ”Bioniskt implantat”
används för CBM och ”inventarium” för spelinventariet. Platshållarna bevaras
utan possessiva pronomen där grammatiskt genus annars är okänt.

## Kontroller före API-inskick

- Platsmarkörer ska stämma mellan källa och mål.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för sammansättningar och
  projektspecifika termer.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio översättningar via Transifex API.
En ny, oberoende GET-återläsning jämförde sedan varje målsträng med denna
batch. Alla 10 av 10 stämde exakt.

svlangs enda V2-varning gällde en korrekt bisats och är en falsk positiv.
Hunspell-SV saknar den etablerade projektspecifika termen ”bionisk”, men
rapporterade inga andra stavningsfel.
