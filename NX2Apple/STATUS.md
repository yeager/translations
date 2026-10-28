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

Arbetsgrenen `l10n/swedish` är klar lokalt. En upstream-PR återstår att skapa.
