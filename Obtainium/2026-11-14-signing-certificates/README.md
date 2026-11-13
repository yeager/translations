# Obtainium – verifiering av signeringscertifikat

Datum: 2026-11-14
Komponent: `assets/translations/sv.json`
Källversion: `v1.7.4`, publicerad 2026-11-01

## Granskning

Den här batchen översätter elva säkerhetsnära strängar för verifiering av
signeringscertifikat. Den omfattar förväntade och hämtade hashsummor,
valideringsfel, varningar och hårda installationsblockeringar.

Varnings- och blockeringsvägarna har kontrollerats var för sig i dialogkoden.
Svenskan behåller skillnaden mellan att en installation hoppas över, att den
troligen misslyckas och att den blockeras.

## Kontroller

- JSON-syntax: godkänd
- `l10n-lint`: godkänd
- Hunspell-sv: körd med sänkt prioritet och avslutad; tekniska former granskade
- `svlang`: en känd ordlistevarning för `APK`, inga grammatiska fel
- `git diff --check`: godkänd
- Gitleaks: godkänd
- `msgfmt`: inte tillämpligt på JSON

## Upstream

Ändringarna är inskickade som
[ImranR98/Obtainium#3522](https://github.com/ImranR98/Obtainium/pull/3522).
PR:en är öppen; upstreamgranskning och merge återstår.
