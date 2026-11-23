# Home Assistant Core – Keymitt BLE

Datum: 2026-11-23

Hela komponenten (22 aktuella strängar) lästes från Lokalise API och jämfördes
med Core-exporten. Alla poster var redan korrekta och behövde därför ingen
ändring; nedan är den fullständiga, liveverifierade nyckeluppsättningen.

| Nyckel | Svenska | Resultat |
| --- | --- | --- |
| `component::keymitt_ble::config::abort::already_configured_device` | Enheten är redan konfigurerad | Korrekt. |
| `component::keymitt_ble::config::abort::cannot_connect` | Det gick inte att ansluta | Korrekt. |
| `component::keymitt_ble::config::abort::unknown` | Oväntat fel | Korrekt. |
| `component::keymitt_ble::config::error::linking` | Det gick inte att koppla ihop, försök igen. Är MicroBot i parkopplingsläge? | Korrekt. |
| `component::keymitt_ble::config::flow_title` | `{name}` | Platshållaren är oförändrad. |
| `component::keymitt_ble::config::step::init::data::address` | Enhetsadress | Korrekt. |
| `component::keymitt_ble::config::step::init::data::name` | Namn | Korrekt. |
| `component::keymitt_ble::config::step::init::title` | Konfigurera MicroBot-enhet | Korrekt. |
| `component::keymitt_ble::config::step::link::description` | Tryck på knappen på MicroBot Push när lysdioden lyser med fast rosa eller grönt sken för att registrera den i Home Assistant. | Korrekt. |
| `component::keymitt_ble::config::step::link::title` | Parkoppling | Korrekt. |
| `component::keymitt_ble::config::abort::no_devices_found` | Inga enheter hittades i nätverket | Korrekt. |
| `component::keymitt_ble::services::calibrate::description` | Ställer in djup, tryck- eller släpptid och driftläge. Varning - detta skickar ett tryckkommando till enheten. | Korrekt. |
| `component::keymitt_ble::services::calibrate::fields::depth::description` | Hur långt tryckarmen ska sträckas ut. | Korrekt. |
| `component::keymitt_ble::services::calibrate::fields::depth::name` | Djup | Korrekt. |
| `component::keymitt_ble::services::calibrate::fields::duration::description` | Hur länge man ska trycka eller släppa. | Korrekt. |
| `component::keymitt_ble::services::calibrate::fields::duration::name` | Varaktighet | Korrekt. |
| `component::keymitt_ble::services::calibrate::fields::entity_id::description` | Namn på entitet som ska kalibreras. | Korrekt. |
| `component::keymitt_ble::services::calibrate::fields::entity_id::name` | Entitet | Korrekt. |
| `component::keymitt_ble::services::calibrate::fields::mode::description` | Armens driftläge. | Korrekt. |
| `component::keymitt_ble::services::calibrate::fields::mode::name` | Läge | Korrekt. |
| `component::keymitt_ble::services::calibrate::name` | Kalibrera | Korrekt. |
| `component::keymitt_ble::entity::switch::push::name` | Tryck | Korrekt i switch-kontext. |

Hunspell har endast produktnamn och den domänspecifika sammansättningen
`tryckarmen` som okända ord. svlang hittade inga anglifieringar eller
skrivregelfel; dess V2-varningar gäller fristående UI-fragment och ändrar
inte bedömningen. Inga pluraler eller referenser förekommer. Det validerade
TMX-minnet har uppdaterats med en Lokalise-återläst manifestfil.
