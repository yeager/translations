# Obtainium – käll- och utgåvestatus

Datum: 2026-11-14
Komponent: `assets/translations/sv.json`
Källversion: `v1.7.4`, publicerad 2026-11-01

## Granskning

Den här batchen översätter tolv texter för källor och utgåvor. Den täcker bland
annat flyttade förråd, hantering av utgåvedatum, val av utgåvor och fel när
ingen matchande utgåva finns. Källkodens dialoger och kontrollogik har lästs
innan översättningarna fastställdes.

## Kontroller

- JSON-syntax: godkänd
- `l10n-lint`: godkänd
- Hunspell-sv: körd med sänkt prioritet på endast batchens texter och avslutad
- `svlang`: godkänd
- `git diff --check`: godkänd
- Gitleaks: godkänd
- `msgfmt`: inte tillämpligt på JSON

## Upstream

Ändringarna är inskickade som
[ImranR98/Obtainium#3521](https://github.com/ImranR98/Obtainium/pull/3521).
PR:en är öppen; upstreamgranskning och merge återstår.
