# NX2Apple: svensk lokalisering

Datum: 2026-10-28

## Omfattning

- 616 av 616 källsträngar har en svensk översättning.
- SwiftUI-programmet väljer svenska när systemets förstahandsspråk börjar med `sv`.
- Språkvalet har ett explicit alternativ för svenska och Qt-klienten använder samma katalog.

## Arkiverade filer

- `Localization.swift`: Swift-katalogen och den svenska överlagringen.
- `qt-i18n.py` och `qt-localization.py`: motsvarande Qt-stöd och genererad katalog.
- `sv.json`: platt export av samtliga svenska poster för granskning.

## Verifiering

- `swift test --package-path frontend`: 251 tester passerade, 7 visuella capture-tester hoppades över eftersom deras explicita miljövariabler saknades.
- `python3 frontend-qt/gen_localization.py` och `py_compile`: passerade.
- Platshållarjämförelse mot engelska: 0 avvikelser.
- `l10n-lint` på den exporterade JSON-katalogen: inga anmärkningar.
- `svlang skrivregler`: inga anmärkningar.
- Avgränsad Gitleaks-kontroll: inga fynd.

## Upstream

Arbetsgrenen `l10n/swedish` rebasedes mot uppströms `main` och skickades som
[PR #168](https://github.com/LNPANDY/NX2Apple/pull/168). PR-huvudet är
`10ef7a292f1fd33a463db5d9f1f89528a01379d6`. GitHub har ännu inte slutfört sin
mergebarhetsberäkning och visar därför `UNSTABLE`; den lokala rebasen och hela
testsviten är verifierade mot samma huvudcommit.
