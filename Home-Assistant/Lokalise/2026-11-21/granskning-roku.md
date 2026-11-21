# Home Assistant Core – Roku

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/roku/strings.json`  
Status: samtliga 23 aktuella strängar granskade mot Lokalise och källtext.

Referenser och platshållare är korrekta. Följande texter behöver korrigeras:

| Nyckel | Befintlig text | Föreslagen text |
| --- | --- | --- |
| `component::roku::options::step::init::data::play_media_app_id` | `Spela Media Roku Applikations-ID` | `Roku-applikations-ID för medieuppspelning` |
| `component::roku::entity::binary_sensor::supports_find_remote::name` | `Stöder hitta fjärrkontroll` | `Stöder funktionen Hitta fjärrkontroll` |
| `component::roku::entity::binary_sensor::supports_ethernet::name` | `Stöder ethernet` | `Stöder Ethernet` |
| `component::roku::config::step::user::description` | `Ange din Roku-information .` | `Ange din Roku-information.` |

De två första korrigeringarna är sparade och återlästa i Lokalise 2026-11-21.
Ethernet-raden är sparad och verifierad via Lokalise API 2026-11-21 med
översättnings-ID `2958065190`. Informationsraden var redan korrekt i den
aktuella API-katalogen. TMX-synkning kan göras med verifierade API-ID:n.
