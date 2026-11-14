# Home Assistant Core, Lokalise, svenska: WattWächter och RainMachine-batch 26

Datum: 2026-11-14

Följande integrationsspecifika feltexter är kontrollerade mot Home Assistants
aktuella källor. De sparades direkt i Lokalise och lästes sedan om i
redigeraren:

- `component::wattwaechter::config::abort::already_configured_mqtt`
  - Den här enheten är redan konfigurerad i Home Assistant via MQTT. Lägg till
    den manuellt om du även vill konfigurera den med den här integrationen.
- `component::rainmachine::exceptions::action_failed::message`
  - Ett fel uppstod när RainMachine-åtgärden {action} kördes.

Lokalise visar en stavnings- eller grammatikvarning för RainMachine-posten.
Platshållaren matchar dock källan och varningen avser produktnamnet eller den
sammansatta facktermen, inte ett sakfel i översättningen.

Kontroller: diffkontroll och Gitleaks för arkivändringen. Resursfilbaserade
kontroller kräver en exporterad lokaliseringsfil och är därför inte tillämpliga
på denna direkt sparade Lokalise-batch.

Status: sparad och verifierad upstream i Lokalise. Detta är en avgränsad batch,
inte en fullständig genomgång av projektet.
