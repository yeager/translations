# PrusaSlicer – kontroll av den svenska wxWidgets-katalogen

Datum: 2026-11-14

Kontrollerad sökväg: `resources/localization/wx_locale/sv.po`
Källversion: PrusaSlicer 2.9.7, publicerad 2026-11-02

## Bedömning

PrusaSlicer använder den svenska wxWidgets-katalogen som en genererad eller
synkroniserad beroenderesurs. Projektets egen lokaliseringsguide säger uttryckligen
att poster utan en filreferens som innehåller `Slic3r` inte ska ändras, eftersom
de skrivs över vid nästa synkning.

Katalogen har 1 672 översatta poster, 123 oöversatta och 96 osäkra poster.
Samtliga oöversatta och osäkra poster har wxWidgets-referenser; inga har en
`Slic3r`-referens. De är alltså inte säkra PrusaSlicer-strängar att ändra i detta
arkiv. Ingen upstreamändring eller PR skapades.

## Kontroller

- Senaste stabila release: 2.9.7 från 2026-11-02.
- `msgfmt --check --statistics`: 1 672 översatta, 96 osäkra och 123 oöversatta.
- Referenskontroll: 0 `Slic3r`-referenser bland oöversatta respektive osäkra poster.
- Gitleaks: godkänd.

## Status

Lokalt kontrollerat och arkiverat. En framtida PrusaSlicer-granskning ska börja i
projektets egna extraherade strängar, inte i den synkroniserade wxWidgets-filen.
