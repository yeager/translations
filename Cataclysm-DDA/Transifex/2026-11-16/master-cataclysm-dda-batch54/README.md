# Cataclysm-DDA, svenska: batch 54

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De gäller förflyttning, automatiska rörelser,
attack och effekter som begränsar spelarens val.

Källkontexten kontrollerades i `src/avatar_action.cpp`. ”Automatisk
förflyttning” används konsekvent för *auto move*. Samtliga platsmarkörer i
säkert-läge-meddelandet bevaras. Källans riktiga utelämningstecken bevaras,
men ingen em dash har tillförts i den svenska texten.

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

svlang rapporterade en naturlighetspoäng på 10 av 10 utan språkvarningar.
Hunspell-SV gav endast normal analysutmatning och inga stavningsfel.
