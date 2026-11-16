# Cataclysm-DDA, svenska: batch 55

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De gäller förflyttning, simning och meddelanden
om hinder och miljöeffekter.

Källkontexten kontrollerades i `src/avatar_action.cpp`. De två korta
strängarna ”to go back” och ”to move anyway” visas efter en tangentbeskrivning;
översättningen bevarar därför deras inledande infinitivfras. Platsmarkören i
luftvarningen och i meddelandet om riddjuret är bevarad.

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

svlangs tre V2-varningar gällde korrekta huvudsatser och bedömdes som falska
positiva. Hunspell-SV gav endast normal analysutmatning och inga stavningsfel.
