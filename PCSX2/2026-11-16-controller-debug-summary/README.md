# PCSX2: handkontroll och felsökningshjälp

Datum: 2026-11-16  
Tjänst: Crowdin, projekt 561203 (PCSX2 Emulator)  
Språk: `sv-SE`

## Ändringar

| Sträng-id | Källa | Svenska |
| --- | --- | --- |
| 10173 | Analog lampa på | `… port {0} / plats {1}` |
| 10175 | Analog lampa av | `… port {0} / plats {1}` |
| 10352 | Sammanfattning av spelinställningar | Tydligare aktiv svensk text |
| 10418 | Debug Settings | `Felsökningsinställningar` och en naturlig varning |

`slot` avser här en fysisk plats vid den angivna handkontrollporten och blir
därför `plats`. Platshållarna `{0}` och `{1}` är bevarade. Felsökningsvarningen
har skrivits om så att den förklarar både prestandapåverkan och användningen av
diskutrymme utan det onaturliga ordet `långsamheter`.

## Kontroller

- Deltafilen är välformad XML och kontrolleras med l10n-lint.
- svlang körs på måltexterna.
- Hunspell-sv körs lågprioriterat på ett begränsat urval och processlistan
  kontrolleras efteråt.
- `msgfmt` gäller PO-filer och är inte tillämpligt på XLIFF.

svlang flaggade tre falska positiva V2-varningar. De två korta
handkontrollmeddelandena har korrekt ordföljd, och i meningen som börjar med
`Med spårlistan och dumpverifiering` står det finita verbet `kan` korrekt på
andra plats.

## Inskick och återläsning

Alla fyra ändringar sparades via Crowdin API och lästes därefter tillbaka:

| Sträng-id | Crowdin-översättning |
| --- | ---: |
| 10173 | 450405 |
| 10175 | 450407 |
| 10352 | 450409 |
| 10418 | 450411 |

Detta är sparade Crowdin-förslag, inte belägg för godkännande eller release
uppströms.
