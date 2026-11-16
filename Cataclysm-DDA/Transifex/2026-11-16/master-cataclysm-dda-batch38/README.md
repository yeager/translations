# Cataclysm-DDA, svenska: batch 38

Tio aktuella oöversatta strängar ur `master-cataclysm-dda`, hämtade från
Transifex den 16 november 2026. De hör till avancerat inventarium och dess
sortering, tabellhuvuden och flytt av föremål.

Källkontexten kontrollerades i `src/advanced_inv.cpp`. `charges` är ett
generellt antal enheter, så den svenska kolumnrubriken är `Namn (enheter)`.
De täta tabellrubrikerna förkortas på samma sätt som källtexten: `ant` för
antal och `vol` för volym. När ett fyllt kärl inte kan flyttas uttrycker
frågan att dess innehåll först måste förvaras.

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

svlang markerade endast den förväntade V2-träffen när separata
tabellrubriker granskades som löptext, samt den avsiktliga förkortningen
`vol`. Hunspell-SV markerade endast de avsiktliga UI-förkortningarna
`ant` och `vol` samt den avstavade sammansättningen `ammunitions-/enhetstyp`.
