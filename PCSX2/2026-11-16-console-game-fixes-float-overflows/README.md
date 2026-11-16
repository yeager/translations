# PCSX2: konsol, spelfixar och flyttal

Datum: 2026-11-16  
Tjänst: Crowdin, projekt 561203 (PCSX2 Emulator)  
Språk: `sv-SE`

## Ändringar

| Sträng-id | Källa | Svenska |
| --- | --- | --- |
| 8489 | Hjälptext om `framebuffer fetch` | `bildbuffertshämtning` |
| 8587 | `System Console` | `Systemkonsol` |
| 8695 | Varning om Game Fixes | `Spelfixar` och en naturlig svensk varning |
| 8715 | Hoppa över videor | `… hänger sig eller fryser.` |
| 8763 | Kontroll av float-overflow | `flyttalsöverflöden` |

`Systemkonsoll` rättas till `Systemkonsol`. Den förra texten om
`float overflows` använde felaktigt `flottörer`; här avses överflöden i
flyttal, inte flytande objekt. `FMV:er` behåller kolon eftersom det är korrekt
svensk böjning av en förkortning; QA-varningen om mellanrum efter kolon är
därför en falsk positiv.

## Kontroller

- Deltafilen är välformad XML och kontrolleras med l10n-lint.
- svlang används på måltexterna.
- Hunspell-sv körs lågprioriterat för ett begränsat ordurval och processlistan
  kontrolleras efteråt.
- `bildbuffertshämtning`, `spelfixar` och `flyttalsöverflöden` lades även till
  i hunspell-sv tillsammans med tester. Hela testsviten passerade.
- `msgfmt` gäller PO-filer och är inte tillämpligt på XLIFF.

svlang markerade bara de nya facktermerna och förkortningen `FMV` som ovanliga
i sin frekvenslista. Det är inte stavnings- eller grammatikfel.

## Inskick och återläsning

Alla fem ändringar sparades via Crowdin API och lästes därefter tillbaka:

| Sträng-id | Crowdin-översättning |
| --- | ---: |
| 8489 | 450383 |
| 8587 | 450385 |
| 8695 | 450387 |
| 8715 | 450389 |
| 8763 | 450391 |

Detta är sparade Crowdin-förslag, inte belägg för godkännande eller release
uppströms.
