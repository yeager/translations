# Home Assistant Core, Lokalise, svenska: Tuya-batch 19

Datum: 2026-11-14

Följande tillstånd och etikett hör till samma fodernivåsensor för en
automatmatare. De sparades direkt i Lokalise och lästes sedan om i redigeraren:

- `component::tuya::entity::sensor::food_level::state::lack`
  - Tom
- `component::tuya::entity::sensor::food_level::state::full`
  - Full
- `component::tuya::entity::sensor::food_level::name`
  - Fodernivå

Kontroller: diffkontroll och Gitleaks för arkivändringen. Resursfilbaserade
kontroller kräver en exporterad lokaliseringsfil och är därför inte tillämpliga
på denna direkt sparade Lokalise-batch.

Status: sparad och verifierad upstream i Lokalise. Detta är en avgränsad batch,
inte en fullständig genomgång av projektet.
