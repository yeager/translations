# Home Assistant Core, Lokalise, svenska: TTS, VeSync och Tuya-batch 23

Datum: 2026-11-14

Följande texter är kontrollerade mot Home Assistants aktuella
integrationskällor. De sparades direkt i Lokalise och lästes sedan om i
redigeraren. Det oöversatta filtret minskade samtidigt från 2 873 till 2 868
nycklar.

- `component::tts::services::clear_cache::fields::days::name`
  - Oanvända dagar
- `component::tts::services::clear_cache::fields::days::description`
  - Tar endast bort filer som inte har använts på så här många dagar. Lämna tomt
    för att ta bort alla filer.
- `component::vesync::exceptions::nightlight_command_failed::message`
  - Det gick inte att styra nattlampan.
- `component::vesync::entity::light::nightlight::name`
  - Nattlampa
- `component::tuya::entity::sensor::leakage_current::name`
  - Läckström

Kontroller: diffkontroll och Gitleaks för arkivändringen. Resursfilbaserade
kontroller kräver en exporterad lokaliseringsfil och är därför inte tillämpliga
på denna direkt sparade Lokalise-batch.

Status: sparad och verifierad upstream i Lokalise. Detta är en avgränsad batch,
inte en fullständig genomgång av projektet.
