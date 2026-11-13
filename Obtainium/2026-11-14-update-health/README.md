# Obtainium – uppdateringsstatus

Datum: 2026-11-14
Komponent: `assets/translations/sv.json`
Källversion: `v1.7.4`, publicerad 2026-11-01

## Granskning

Den här batchen översätter 21 etiketter och meddelanden i sidan för
uppdateringsstatus. Den omfattar trösklar för identifiering, ignorerade appar,
orsaker till varningar samt inställningar per app. Varje sträng är kontrollerad
mot sin användning i Flutter-vyn och den underliggande kontrollogiken.

## Kontroller

- JSON-syntax: godkänd
- `l10n-lint`: godkänd
- Hunspell-sv: projektspecifika böjningar och sammansättningar granskade manuellt
- `svlang`: godkänd
- `git diff --check`: godkänd
- Gitleaks: godkänd
- `msgfmt`: inte tillämpligt på JSON

## Upstream

Ändringarna är inskickade som
[ImranR98/Obtainium#3519](https://github.com/ImranR98/Obtainium/pull/3519).
PR:en är öppen; upstreamgranskning och merge återstår.
