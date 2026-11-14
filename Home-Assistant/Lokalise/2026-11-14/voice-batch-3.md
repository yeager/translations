# Home Assistant Core, Lokalise, svenska: Voice-batch 3

Datum: 2026-11-14

Tre ytterligare Voice-strängar har granskats i Lokalise, sparats direkt
upstream och återlästs i redigeraren:

- `component::voice_support::config::step::on_supervisor::data_description::use_app`
  - Home Assistant installerar och startar appen vid behov.
- `component::voice_support::config::step::on_supervisor::data::use_app`
  - Använd den officiella Voice-appen
- `component::voice_support::config::step::manual::title`
  - Anslut till Voice-appen

Kontroller: diffkontroll och Gitleaks för arkivändringen. Resursfilbaserade
kontroller kräver en exporterad lokaliseringsfil och är därför inte tillämpliga
på denna direkt sparade Lokalise-batch.

Status: sparad och verifierad upstream i Lokalise. Detta är en avgränsad batch,
inte en fullständig genomgång av projektet.
