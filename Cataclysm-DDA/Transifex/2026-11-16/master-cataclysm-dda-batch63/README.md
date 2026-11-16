# Cataclysm-DDA, svenska: batch 63

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De gäller bioniska funktioner, fukt och
förflyttning.

Källkontexten kontrollerades i `src/bionics.cpp`. De mekaniska termerna har
svenska sammansättningar: ”torsionsspärrar” och ”ledservomotorer”.
Platsmarkörerna och ljudeffekten är bevarade exakt.

## Kontroller före API-inskick

- Platsmarkörer och ljudeffekter ska stämma mellan källa och mål.
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
l10n-lints enda varning är den avsiktliga ljudeffekten `VRRRRMP!` som finns
oförändrad i både källan och målet. Hunspell-SV saknar den tekniska
sammansättningen ”ledservomotorer”, men rapporterade inga andra stavningsfel.
