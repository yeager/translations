# PCSX2: svenska grafiktermer

Datum: 2026-11-16  
Tjänst: Crowdin, projekt 561203 (PCSX2 Emulator)  
Språk: `sv-SE`

## Ändringar

| Sträng-id | Källa | Svenska |
| --- | --- | --- |
| 8255 | `Bilinear Filtering` | `Bilinjär filtrering` |
| 8257 | Hjälptext för bilinjär filtrering | `… när texturer återges.` |
| 8259 | `Trilinear Filtering` | `Trilinjär filtrering` |
| 8261 | Hjälptext för trilinjär filtrering | `… när texturer återges.` |
| 8271 | `Blending Accuracy` | `Blandningsnoggrannhet` |
| 8345 | Hjälptext om texturcache | `bildbuffert` och `inmatningstextur` |

`Bilinear` och `Trilinear` ersätts av svenska former i löpande UI-text.
`Dithering` ligger nära i gränssnittet, men lämnas orörd eftersom det fungerar
som en etablerad grafikteknisk term. `Frame buffer` blir `bildbuffert` i den
förklarande hjälptexten.

## Kontroller

- Deltafilen är välformad XML och kontrolleras med l10n-lint.
- svlang körs på måltexterna.
- De berörda svenska orden kontrolleras med Hunspell-sv, med låg prioritet och
  ett begränsat ordurval. Processlistan kontrolleras efteråt.
- `msgfmt` gäller PO-filer och är inte tillämpligt på XLIFF.

svlang markerade bisatsen `var programmet använder …` som en möjlig
V2-avvikelse. Det är en falsk positiv: huvudsatsen har korrekt ordföljd
(`Här väljer du`) och bisatsen har korrekt bisatsordföljd.

## Inskick och återläsning

Alla ändringar sparades via Crowdin API och lästes därefter tillbaka:

| Sträng-id | Crowdin-översättning |
| --- | ---: |
| 8255 | 450371 |
| 8257 | 450373 |
| 8259 | 450375 |
| 8261 | 450377 |
| 8271 | 450379 |
| 8345 | 450381 |

Detta är sparade Crowdin-förslag, inte belägg för godkännande eller release
uppströms.
