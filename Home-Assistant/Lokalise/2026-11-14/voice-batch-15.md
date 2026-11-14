# Home Assistant Core, Lokalise, svenska: Voice-batch 15

Datum: 2026-11-14

Strängen förklarar att en förhandsfunktion behöver aktiveras före anslutning av
Voice-appen. Den sparades direkt i Lokalise och verifierades genom omladdning:

- `component::voice_support::config::abort::preview_feature_disabled`
  - Aktivera först förhandsfunktionen Nästa generations röst i Home Assistant Labs.

Kontroller: diffkontroll och Gitleaks för arkivändringen. Resursfilbaserade
kontroller kräver en exporterad lokaliseringsfil och är därför inte tillämpliga
på denna direkt sparade Lokalise-batch.

Status: sparad och verifierad upstream i Lokalise. Detta är en avgränsad batch,
inte en fullständig genomgång av projektet.
