# Home Assistant Core, Lokalise, svenska: Voice-batch 6

Datum: 2026-11-14

Två ytterligare Voice-inställningssträngar har granskats i Lokalise, sparats
direkt upstream och återlästs i redigeraren:

- `component::voice_support::config::step::on_supervisor::description`
  - Vill du använda den officiella Voice-appen?

    Om du redan kör Voice-appen i en egen behållare, direkt på systemet eller på annat sätt ska du inte välja detta alternativ.
- `component::voice_support::config::step::manual::data_description::port`
  - Porten som Voice-appen lyssnar på.

Kontroller: diffkontroll och Gitleaks för arkivändringen. Resursfilbaserade
kontroller kräver en exporterad lokaliseringsfil och är därför inte tillämpliga
på denna direkt sparade Lokalise-batch.

Status: sparad och verifierad upstream i Lokalise. Detta är en avgränsad batch,
inte en fullständig genomgång av projektet.
