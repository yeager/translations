# Home Assistant Core, Lokalise, svenska: Tuya-batch 18

Datum: 2026-11-14

Statusarna gäller en automatmatare: foder som fastnat, en blockerad matning och
låg fodernivå. De sparades direkt i Lokalise och lästes sedan om i redigeraren:

- `component::tuya::entity::binary_sensor::food_stuck::name`
  - Foder har fastnat
- `component::tuya::entity::binary_sensor::feed_blocked::name`
  - Matningen är blockerad
- `component::tuya::entity::sensor::food_level::state::less`
  - Låg

Kontroller: diffkontroll och Gitleaks för arkivändringen. Resursfilbaserade
kontroller kräver en exporterad lokaliseringsfil och är därför inte tillämpliga
på denna direkt sparade Lokalise-batch.

Status: sparad och verifierad upstream i Lokalise. Detta är en avgränsad batch,
inte en fullständig genomgång av projektet.
