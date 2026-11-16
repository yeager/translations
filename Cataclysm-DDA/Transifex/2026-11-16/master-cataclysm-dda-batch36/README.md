# Cataclysm-DDA, svenska: batch 36

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De gäller aktivitetsavbrott och kompass- samt
positionsetiketter i avancerat inventarium.

Källkontexten kontrollerades i `src/activity_type.cpp` och
`src/advanced_inv.cpp`. Svenska kompassförkortningar används: `Ö` för öster
och `NV` för nordväst. Etiketten `DU` betecknar rutan direkt under spelaren;
den engelska tvåteckensetiketten `DN` hade ingen naturlig svensk motsvarighet.
`IN` blir `INV` för inventarium, konsekvent med menyns andra förkortningar.

## Kontroller före API-inskick

- Platsmarkörer ska stämma mellan källa och mål.
- `l10n-lint --language sv --json-format auto` ska passera utan varningar eller fel.
- Hunspell-SV och svlang ska granskas manuellt för sammansättningar,
  platshållare och projektspecifika termer.
- Ingen otillåten em dash får tillföras. `msgfmt` är inte tillämpligt eftersom
  Transifex API tar enskilda JSON-översättningar, inte en PO-katalog.

## Inskick och återläsning

Den 16 november 2026 sparades samtliga tio översättningar via Transifex API.
En ny, oberoende GET-återläsning jämförde sedan varje målsträng med denna
batch. Alla 10 av 10 stämde exakt.

svlang rapporterade inga språkvarningar. Hunspell-SV markerade endast den
avsiktliga UI-förkortningen `INV`.
