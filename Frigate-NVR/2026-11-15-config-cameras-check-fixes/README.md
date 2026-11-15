# Frigate NVR, config-cameras — svensk granskningsbatch 001

- Datum: 2026-11-15
- Källa: Frigate `dev`, `web/public/locales/en/config/cameras.json`
- Målkomponent: Hosted Weblate `frigate-nvr/config-cameras`, svenska
- Omfattning: 2 befintliga svenska kontrollfel
- Status: inskickad och mottagen via Weblates enhets-API.

## Ändringar och verifiering

- `FPS` rättades till tekniskt korrekta `fps`.
- Dubbleringen *som som* togs bort i GenAI-beskrivningen.
- Komponentens kontrollantal minskade från 3 till 1. Återstående `ONVIF-port`
  är en medveten svensk sammansättning och en känd falsk positiv mot
  källtextens mellanslag.

Kontroller: `jq empty`, `l10n-lint`, `git diff --check` och Gitleaks passerade.
