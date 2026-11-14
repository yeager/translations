# Home Assistant Core, Lokalise, svenska: VeSync-batch 12

Datum: 2026-11-14

VeSync-integrationen exponerar den här växeln för fläktar och luftrenare som
stödjer ljudavstängning. Etiketten beskriver därför åtgärden kort och naturligt
i gränssnittet. Strängen sparades direkt i Lokalise och lästes sedan om i
redigeraren:

- `component::vesync::entity::switch::mute::name`
  - Ljud av

Kontroller: diffkontroll och Gitleaks för arkivändringen. Resursfilbaserade
kontroller kräver en exporterad lokaliseringsfil och är därför inte tillämpliga
på denna direkt sparade Lokalise-batch.

Status: sparad och verifierad upstream i Lokalise. Detta är en avgränsad batch,
inte en fullständig genomgång av projektet.
