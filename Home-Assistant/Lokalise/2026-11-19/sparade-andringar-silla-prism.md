# Sparade ändringar för Silla Prism

Sparade och återlästa i Lokalise 2026-11-19 efter jämförelse med tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::silla_prism::entity::sensor::session_start::name` | Session start | Session start | Sessionsstart |
| `component::silla_prism::entity::sensor::session_energy::name` | Session energy | Session energi | Energi för sessionen |

Sammansättningen och relationen till sessionen görs tydligare på svenska.

## MQTT-konfigurationsfel

Sparade och återlästa i Lokalise efter jämförelse med tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::silla_prism::config::error::no_device` | No Prism messages were received on this base topic. Check that the topic matches the one configured in the Silla app and that Prism is online. | Inga Prism-meddelanden mottogs om detta bas-topic. Kontrollera att topic matchar det som konfigurerats i Silla-appen och att Prism är online. | Inga Prism-meddelanden togs emot på detta bastopic. Kontrollera att topicet stämmer med det som konfigurerats i Silla-appen och att Prism är online. |
| `component::silla_prism::config::error::invalid_base_topic` | This is not a valid MQTT topic. Enter the plain topic prefix from the Silla app, without wildcards. | Detta är inte ett giltigt MQTT-topic. Ange det vanliga topic-prefixet från Silla-appen, utan wildcards. | Det här är inte ett giltigt MQTT-topic. Ange topicprefixet från Silla-appen utan jokertecken. |

Projektordlistans topic används och wildcards översätts till jokertecken.
