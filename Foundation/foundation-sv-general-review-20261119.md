# Foundation – allmänna resurser och eftertexter, svensk granskningsbatch 2026-11-19

Elva oöversatta svenska strängar i `general.json` har granskats via Crowdin API. Förslagen är utkast och har inte sparats i Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 26642 | Paint a {1} zone from a {2} | — | Måla en zon för {1} från {2} |
| 26644 | Tavern Drink | — | Krogsdryck |
| 26646 | Military Resource | — | Militär resurs |
| 26648 | Artwork | — | Illustrationer |
| 26650 | Monastic Resource | — | Klosterresurs |
| 26652 | Luxurious Goods | — | Lyxvaror |
| 26654 | Project Manager | — | Projektledare |
| 26656 | Graphics Programmer | — | Grafikprogrammerare |
| 26658 | Additional 3D Artists | — | Ytterligare 3D-grafiker |
| 26660 | Additional UI/UX | — | Ytterligare UI/UX |
| 26662 | DOKI DOKI | — | DOKI DOKI |

## Kontroller

- Foundation's TM kontrollerades via Crowdin concordance. Ett separat lokalt verktyg med namnet `swedish-tm` finns inte installerat.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` markerar UI, UX och DOKI DOKI; de är etablerade förkortningar respektive egennamn.
- Platshållarna `{1}` och `{2}` är bevarade exakt.
