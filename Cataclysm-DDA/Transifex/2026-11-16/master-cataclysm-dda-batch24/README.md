# Cataclysm-DDA, svenska: batch 24

15 aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De gäller hopfällbara fordon, motorstart,
uppvärmning och eld i `src/activity_actor.cpp`.

Källkontexten kontrollerades mot aktuell upstream-källkod. Fordon är
`körklara`, motorer beskrivs utan genusbunden fordonsböjning och `tinder`
översätts som `tändmaterial` i eldstartskontexten.

Kontroller före API-inskick:

- 15 av 15 platsmarkörer stämmer mellan källa och mål. Motorsträngarna har
  kontrollerade singular- och pluralformer.
- `l10n-lint --language sv --json-format auto` passerar utan varningar eller fel.
- Hunspell-SV träffar endast fackordet `tändmaterial`.
- svlang rapporterar två falska V2-varningar i korrekta svenska huvudsatser.
- Ingen otillåten em dash tillfördes. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga 15 översättningar via Transifex API.
API:t krävde korrekt både singular- och pluralform för de tre motorsträngarna;
batchunderlaget kompletterades innan den slutliga inskickningen. En oberoende
GET-återläsning jämförde därefter alla 15 sparade värden, inklusive de tre
pluralparen: 15 av 15 stämde exakt.
