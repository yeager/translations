# Home Assistant Core, Lokalise, svenska: Voice-batch 17

Datum: 2026-11-14

Statusmeddelandet gäller en Voice-app som redan kör men ännu inte har annonserat
sin tillgänglighet för Home Assistant. Strängen sparades direkt i Lokalise och
lästes sedan om i redigeraren:

- `component::voice_support::config::abort::app_get_discovery_info_failed`
  - Voice-appen körs men har ännu inte meddelat sig till Home Assistant.

Kontroller: diffkontroll och Gitleaks för arkivändringen. Resursfilbaserade
kontroller kräver en exporterad lokaliseringsfil och är därför inte tillämpliga
på denna direkt sparade Lokalise-batch.

Status: sparad och verifierad upstream i Lokalise. Detta är en avgränsad batch,
inte en fullständig genomgång av projektet.
