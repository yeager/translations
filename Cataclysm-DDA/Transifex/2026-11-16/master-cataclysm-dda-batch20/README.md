# Cataclysm-DDA, svenska: batch 20

25 aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De hör till möbel- och föremålshantering,
omladdning och djurhantering i `src/activity_actor.cpp`.

Källkontexten kontrollerades mot aktuell upstream-källkod. `wield` är här
spelhandlingen att ta ett föremål i handen, medan `reload` avser både att fylla
en vattentät behållare och att ladda ett vapen. Därför används `fylla på` för
behållare men `ladda` för vapen. Spelnamnen i `%s` kan ha okänt genus, så
formuleringarna undviker genusberoende artiklar.

Kontroller före API-inskick:

- 25 av 25 platsmarkörer, inklusive `%s`, `%i`, `%dx` och `%1$s`–`%3$s`,
  stämmer mellan källa och mål.
- `l10n-lint --language sv --json-format auto` passerar utan varningar eller fel.
- Hunspell-SV träffar endast formatuttrycket `dx` i `%dx`.
- svlang markerar tre falska V2-varningar: alla beror på innehållsord i en
  enkel svensk huvudsats eller på en inledande platsmarkör; faktisk ordföljd är korrekt.
- Ingen otillåten em dash tillfördes. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga 25 översättningar via Transifex API.
Varje enskilt API-svar innehöll en målöversättning, och en ny oberoende
GET-återläsning jämförde sedan samtliga 25 sparade målvärden med denna batch:
25 av 25 stämde exakt.
