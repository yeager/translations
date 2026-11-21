# Home Assistant Core – Qbus

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/qbus/strings.json`  
Status: samtliga 15 aktuella källsträngar är radgranskade mot Lokalise.

## Sparade förslag

| Nyckel | Källa | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- | --- |
| `component::qbus::config::abort::not_supported` | Configuration for QBUS happens through MQTT discovery. If your controller is not automatically discovered, check the prerequisites and troubleshooting section of the documentation. | Konfiguration för QBUS sker genom MQTT-upptäckt. Om din handkontroll inte upptäcks automatiskt så kan du läsa mer i avsnitten om förutsättningar och felsökning i dokumentationen. | Konfiguration av QBUS sker genom MQTT-upptäckt. Om styrenheten inte upptäcks automatiskt, kontrollera avsnittet om förutsättningar och felsökning i dokumentationen. | `controller` är en Qbus-styrenhet, inte en handkontroll. Förslaget följer också källans uppmaning att kontrollera ett avsnitt. Lokalise-ID `593003945`. |
| `component::qbus::entity::sensor::light_south::name` | Illuminance south | Belysningsstyrka mot söder | Belysningsstyrka i söder | Samordnar väderstrecksformen med de verifierade öst- och västetiketterna. Lokalise-ID `689695406`. |

## Verifierade befintliga värden

- Konfigurationsavbrotten för redan konfigurerad styrenhet och pågående identifiering, felet för saknad styrenhet, flödestiteln och båda bekräftelsetexterna är korrekta.
- De sex entitetsnamnen – `Regnar`, `Skymning`, `Dagsljus` samt belysningsstyrka i öster, väster och söder – är kontrollerade. Endast söderposten har förslag ovan.
- Båda undantagstexterna är idiomatiska och bevarar respektive platshållare: `{option}` och `{options}`, respektive `{preset}` och `{options}`.
- `QBUS` och `MQTT` behålls som produkt- och tekniknamn. Källan innehåller inte `Home Assistant` i denna komponent.

Lokalise-sökningen visade exakt 15 Qbus-poster; inga historiska extrarader förekom. De två förslagen är sparade och API-återlästa 2026-11-21 med översättnings-ID `5107640383` och `6288413801` och ingår i verifierad TMX.
