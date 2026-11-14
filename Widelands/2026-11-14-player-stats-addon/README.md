# Widelands Add-Ons: Player Statistics

Projektet har en aktuell release, Widelands 1.3.1 från 2026-02-22. Den nya
Transifex-resursen `player_stats.wad.pot` granskades i sin spelkontext.

- Resurs: `o:widelands:p:widelands-addons:r:player-stats-wad`
- Språk: svenska (`sv`)
- Omfattning: 35 av 35 poster
- Inskick: Transifex REST API, 2026-11-14
- Verifiering: 35 uppdateringar och 35 exakta återläsningar, utan avvikelser

Kontroller före inskick: `msgfmt`, diffkontroll, `l10n-lint`, `svlang`,
Hunspell-sv och Gitleaks. `l10n-lint` godkände katalogen utan varningar.
Hunspell-sv markerade endast `02d` i den oförändrade tidsformatsträngen
`%1$d:%2$02d:%3$02d`; formatet får inte översättas.

Detta är ett verifierat upstream-inskick. Det är inte samma sak som extern
granskning eller införlivande i en Widelands-utgåva.
