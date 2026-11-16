# Cataclysm-DDA, svenska: batch 28

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De omfattar vila, väder, följeslagare och
sortering av föremål.

Källkontexten kontrollerades i `src/activity_actor.cpp`. För sorteringsflödet
har `source` återgivits som `ursprungsplatsen`, eftersom koden uttryckligen
försöker återställa ett föremål där det hämtades. Den enda ellipsen bevaras
eftersom den finns i källtexten.

## Kontroller före API-inskick

- Platsmarkörer, inklusive `%s` och `%d`, ska stämma mellan källa och mål.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för sammansättningar,
  platshållare och projektspecifika termer.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio översättningar via Transifex API.
En ny, oberoende GET-återläsning jämförde sedan varje målsträng med denna
batch. Alla 10 av 10 stämde exakt.

svlang markerade en förväntad falsk V2-träff i en korrekt `för att`-bisats.
Hunspell-SV rapporterade inga avvikelser.
