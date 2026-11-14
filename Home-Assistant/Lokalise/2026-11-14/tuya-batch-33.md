# Home Assistant Core – Tuya, batch 33

Datum: 2026-11-14

Två svenska felindikeringar för Tuya sparades direkt i Lokalise och återlästes:

- `component::tuya::entity::binary_sensor::overvoltage::name`: **Överspänning**
- `component::tuya::entity::binary_sensor::overcurrent::name`: **Överström**

Källsträngarna är korta sensornamn i Home Assistants enhetsgränssnitt. Termerna följer etablerad svensk elektroterminologi. Inga platshållare, URL:er eller em dash förekommer.

## Kontroller

- Sparade värden återlästa i Lokalise.
- `msgfmt`, l10n-lint, svlang och hunspell-sv är inte tillämpliga på den här webbläsarbaserade redigeringen utan en lokal export.
- Diffkontroll och Gitleaks körs före arkivering.

## Upstreamstatus

Båda värdena är sparade i Lokalise. Lokalise-granskning, kodsynkronisering och release är inte verifierade.
