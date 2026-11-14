# Home Assistant Core, Lokalise, svenska: Hot Spring-batch 9

Datum: 2026-11-14

Hot Spring-integrationen använder en Home Network Adapter (HNA) för
hemnätverksanslutningen. Produktnamnet och förkortningen har bevarats, medan
meningens svenska form har anpassats till felmeddelandets UI-kontext. Strängen
sparades direkt i Lokalise och lästes sedan om i redigeraren:

- `component::hotspring::exceptions::spa_not_connected::message`
  - Spabadet är inte anslutet till sin Hot Spring-hemnätverksadapter (HNA).

Kontroller: diffkontroll och Gitleaks för arkivändringen. Resursfilbaserade
kontroller kräver en exporterad lokaliseringsfil och är därför inte tillämpliga
på denna direkt sparade Lokalise-batch.

Status: sparad och verifierad upstream i Lokalise. Detta är en avgränsad batch,
inte en fullständig genomgång av projektet.
