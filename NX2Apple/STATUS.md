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
- Qt-testsviten: 132 tester passerade, 9 hoppades över.
- Riktat test av språkcykeln kinesiska → engelska → svenska → kinesiska: passerade.
- Platshållarjämförelse mot engelska: 0 avvikelser.
- `l10n-lint` på den exporterade JSON-katalogen: inga anmärkningar.
- `svlang skrivregler`: inga anmärkningar.
- Avgränsad Gitleaks-kontroll: inga fynd.

## Upstream

Arbetsgrenen `l10n/swedish` är rebased mot uppströms `main` (`3384be8c`) och
skickad som [PR #168](https://github.com/LNPANDY/NX2Apple/pull/168). PR-huvudet
är `5a2a96780a791dac0c3bc7bb1fa11a6399100597`. GitHubs API bekräftade före
rebasen att PR:en är mergebar. GitHub-granskningen upptäckte att språkknappen
inte kunde välja svenska; rättningen är med och skyddas av ett test. Efter
rebasen passerar Qt-sviten (132 tester, 9 avsiktliga hopp) och Swift-sviten.
PR:en saknar CI-kontroller och väntar därför på underhållargranskning.
