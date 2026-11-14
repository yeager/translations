# Home Assistant Core, Lokalise, svenska: Tuya-batch 25

Datum: 2026-11-14

Följande Tuya-texter beskriver valet av tillstånd efter påslagning. De
sparades direkt i Lokalise och lästes sedan om i redigeraren:

- `component::tuya::entity::select::power_on_behavior::state::last`
  - Föregående läge
- `component::tuya::entity::select::power_on_behavior::name`
  - Beteende vid påslagning

De övriga närliggande tillstånden lämnades oförändrade eftersom de är delade
Lokalise-referenser till allmänna på- och av-etiketter.

Kontroller: diffkontroll och Gitleaks för arkivändringen. Resursfilbaserade
kontroller kräver en exporterad lokaliseringsfil och är därför inte tillämpliga
på denna direkt sparade Lokalise-batch.

Status: sparad och verifierad upstream i Lokalise. Detta är en avgränsad batch,
inte en fullständig genomgång av projektet.
