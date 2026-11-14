# Home Assistant Core – Tuya, batch 34

Datum: 2026-11-14

Tre korta namn för Tuya-binärsensorer sparades direkt i Lokalise och återlästes:

- `component::tuya::entity::binary_sensor::short_circuit::name`: **Kortslutning**
- `component::tuya::entity::binary_sensor::self_test::name`: **Självtest**
- `component::tuya::entity::binary_sensor::fire::name`: **Brand**

Källsträngarna är statusnamn i Home Assistants enhetsgränssnitt. De svenska
termerna är etablerade inom el- och säkerhetsområdet. Inga platshållare, URL:er
eller em dash förekommer.

## Kontroller

- Sparade värden återlästa i Lokalise.
- `msgfmt`, l10n-lint, svlang och hunspell-sv är inte tillämpliga på den här
  webbläsarbaserade redigeringen utan en lokal export.
- Diffkontroll och Gitleaks körs före arkivering.

## Upstreamstatus

Alla tre värden är sparade i Lokalise. Lokalise-granskning, kodsynkronisering
och release är inte verifierade.
