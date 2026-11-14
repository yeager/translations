# Home Assistant Core, Lokalise, svenska: Voice-batch 16

Datum: 2026-11-14

Tre konkreta feltexter för installation, start och hämtning av appinformation
har översatts med samma korta felstil som övriga Home Assistant-dialoger. De
sparades direkt i Lokalise och lästes sedan om i redigeraren:

- `component::voice_support::config::abort::app_start_failed`
  - Det gick inte att starta Voice-appen.
- `component::voice_support::config::abort::app_install_failed`
  - Det gick inte att installera Voice-appen.
- `component::voice_support::config::abort::app_info_failed`
  - Det gick inte att hämta information om Voice-appen.

Kontroller: diffkontroll och Gitleaks för arkivändringen. Resursfilbaserade
kontroller kräver en exporterad lokaliseringsfil och är därför inte tillämpliga
på denna direkt sparade Lokalise-batch.

Status: sparad och verifierad upstream i Lokalise. Detta är en avgränsad batch,
inte en fullständig genomgång av projektet.
