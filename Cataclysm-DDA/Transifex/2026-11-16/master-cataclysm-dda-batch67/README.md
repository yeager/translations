# Cataclysm-DDA, svenska: batch 67

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De gäller bränslenivå, energiproduktion och
olika sätt som bionik stängs av.

Källkontexten kontrollerades i `src/bionics.cpp`. Formuleringarna utelämnar
onödiga possessiva pronomen före platsmarkörer med okänt grammatiskt genus.
Taggarna `<npcname>` förekommer bara i källor vars svenska mål kan uttryckas
korrekt utan ett personnamn.

## Kontroller före API-inskick

- Platsmarkörer och XML-liknande taggar ska stämma mellan källa och mål.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för sammansättningar och
  projektspecifika termer.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio översättningar via Transifex API.
En oberoende GET-återläsning jämförde därefter varje målsträng med batchens
underlag: 10 av 10 stämde exakt.

`l10n-lint` passerade utan varningar eller fel. Hunspell-SV och svlang
rapporterade inga avvikelser.
