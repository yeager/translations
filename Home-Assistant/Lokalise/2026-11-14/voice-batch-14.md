# Home Assistant Core, Lokalise, svenska: Voice-batch 14

Datum: 2026-11-14

Feltexten gäller en protokollversionskonflikt mellan Voice-appen och den
aktuella Home Assistant-installationen. Produktnamnet behålls och åtgärden
uttrycks med etablerade svenska former. Strängen sparades direkt i Lokalise och
lästes sedan om i redigeraren:

- `component::voice_support::config::abort::unsupported_version`
  - Voice-appen använder en protokollversion som den här Home Assistant-installationen inte stöder. Uppdatera appen eller Home Assistant.

Kontroller: diffkontroll och Gitleaks för arkivändringen. Resursfilbaserade
kontroller kräver en exporterad lokaliseringsfil och är därför inte tillämpliga
på denna direkt sparade Lokalise-batch.

Status: sparad och verifierad upstream i Lokalise. Detta är en avgränsad batch,
inte en fullständig genomgång av projektet.
