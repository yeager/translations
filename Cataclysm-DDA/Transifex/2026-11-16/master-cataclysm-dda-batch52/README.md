# Cataclysm-DDA, svenska: batch 52

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De är status- och smärtmeddelanden för
karaktären och kroppsdelar.

Källkontexten kontrollerades i `src/avatar.cpp` och i anropsplatserna för
menyn om vad som ska göras med ett föremål. De fyra smärtnivåerna skiljs åt
som olidlig, fruktansvärd, vanlig smärta och värk. I kroppsdelstexterna
utelämnas possessivt pronomen före `%s`, eftersom kroppsdelsnamnets genus
annars inte är känt i översättningen.

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

svlang rapporterade inga språkvarningar. Hunspell-SV rapporterade inga
stavningsfel; analysutmatningen innehöll bara vanliga böjningsuppslag.
