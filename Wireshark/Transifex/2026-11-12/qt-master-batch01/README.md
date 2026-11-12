# Wireshark Qt master, svenska: batch 01

- Omfattning: 25 strängar i DistributionDialog och DistributionModel.
- Kontext: fältfördelningar, visningsfilter, I/O-diagram och paketstatistik.
- Status: uppladdade i ett Transifex API-anrop och återlästa. Kvar i Qt-master efter batchen: 398 oöversatta strängar.

## Terminologi

- `display filter`: visningsfilter
- `I/O Graph`: I/O-diagram
- `distribution`: fördelning
- `field`: fält

## Kontroller

- Källkodskontext kontrollerad i Wiresharks Qt-dialog.
- Platshållare och fältidentifierare bevarade.
- `l10n-lint`: en kontextuell varning för uttrycket `i I/O-diagram`.
- `svlang`, Hunspell, diffkontroll och Gitleaks körda; återstående träffar gäller UI-fragment och tekniska fältnamn.
- `msgfmt`: ej tillämpligt på Transifex JSON-batchen; källresursen är Qt TS.
