# PCSX2: svenska filteretiketter

Datum: 2026-11-16  
Tjänst: Crowdin, projekt 561203 (PCSX2 Emulator)  
Språk: `sv-SE`

## Ändringar

| Sträng-id | Källa | Svenska |
| --- | --- | --- |
| 9155 | `Bilinear (Forced excluding sprite)` | `Bilinjär (tvingad, utom sprite)` |
| 9157 | `Off (None)` | `Av (ingen)` |
| 9273 | `Scanline Filter` | `Bildradsfilter` |

`Bilinjär` gör etiketten konsekvent med de övriga svenska grafiktermerna.
`Bildradsfilter` är en svensk sammansättning och ligger tillsammans med
`Diagonalt filter`, `Triangulärt filter` och `Vågfilter` i samma inställning.
`sprite` är en etablerad grafikteknisk term och lämnas medvetet på engelska.

## Kontroller

- Deltafilen är välformad XML och kontrolleras med l10n-lint.
- svlang körs på måltexterna.
- Hunspell-sv körs lågprioriterat för ett begränsat urval. `Bildradsfilter`
  läggs till i ordlistan med testfall; `sprite` lämnas som teknisk term.
- `msgfmt` gäller PO-filer och är inte tillämpligt på XLIFF.

svlang markerade `Bilinjär (tvingad, utom sprite)` som ett möjligt
ordföljdsfel, eftersom etiketten inte är en fullständig sats. Det är en falsk
positiv. Verktyget markerade även `bildradsfilter` och `sprite` som ovanliga
ord; det första har lagts till i Hunspell-sv och det andra är en avsiktligt
bevarad grafikteknisk term.

## Inskick och återläsning

Alla tre ändringar sparades via Crowdin API och lästes därefter tillbaka:

| Sträng-id | Crowdin-översättning |
| --- | ---: |
| 9155 | 450393 |
| 9157 | 450395 |
| 9273 | 450397 |

Detta är sparade Crowdin-förslag, inte belägg för godkännande eller release
uppströms.
