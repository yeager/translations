# Home Assistant Core, Lokalise, svenska: Voice-batch 5

Datum: 2026-11-14

Två ytterligare Voice-strängar har granskats i Lokalise, sparats direkt
upstream och återlästs i redigeraren:

- `component::voice_support::config::step::zeroconf_confirm::title`
  - Voice-app hittades
- `component::voice_support::config::step::zeroconf_confirm::description`
  - Vill du ansluta till { name } på { host }?

Platshållarna bevarades oförändrade i anslutningsfrågan.

Kontroller: diffkontroll och Gitleaks för arkivändringen. Resursfilbaserade
kontroller kräver en exporterad lokaliseringsfil och är därför inte tillämpliga
på denna direkt sparade Lokalise-batch.

Status: sparad och verifierad upstream i Lokalise. Detta är en avgränsad batch,
inte en fullständig genomgång av projektet.
