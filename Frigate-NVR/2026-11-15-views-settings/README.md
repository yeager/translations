# Frigate NVR, views-settings — svensk granskningsbatch 001

- Datum: 2026-11-15
- Källa: Frigate `dev`, `web/public/locales/en/views/settings.json`
- Målkomponent: Hosted Weblate `frigate-nvr/views-settings`, svenska
- Omfattning: två fuzzy-strängar som granskats mot aktuell källtext
- Status: inskickad och mottagen i Hosted Weblate.

## Ändringar och verifiering

Kameraguidens beskrivning saknade översättningen av “features”. Meddelandet om
web push-aviseringar innehöll föråldrad markup som inte längre finns i
källsträngen. Båda korrigerades direkt i Weblate och lästes därefter tillbaka
via API:t: komponenten har 0 fuzzy-strängar.

Kontroller: JSON-validering, `l10n-lint`, tekniktokenjämförelse,
`git diff --check` och Gitleaks.
