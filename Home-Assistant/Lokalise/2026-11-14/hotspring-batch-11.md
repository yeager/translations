# Home Assistant Core, Lokalise, svenska: Hot Spring-batch 11

Datum: 2026-11-14

API är ett synligt och etablerat tekniskt namn i Hot Spring-integrationen. Den
svenska texten använder den naturliga formen för ett överskridet tidsvärde och
bevarar produktnamnet. Strängen sparades direkt i Lokalise och lästes sedan om
i redigeraren:

- `component::hotspring::exceptions::timeout::message`
  - Tidsgränsen överskreds vid kommunikation med Hot Spring-API:t.

Kontroller: diffkontroll och Gitleaks för arkivändringen. Resursfilbaserade
kontroller kräver en exporterad lokaliseringsfil och är därför inte tillämpliga
på denna direkt sparade Lokalise-batch.

Status: sparad och verifierad upstream i Lokalise. Detta är en avgränsad batch,
inte en fullständig genomgång av projektet.
