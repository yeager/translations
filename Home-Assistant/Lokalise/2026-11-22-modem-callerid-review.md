# Modem Caller ID: fullständig svensk granskning

Granskad 22 november 2026 mot aktuell källtext och aktuella svenska
översättningar i Lokalise via API. Samtliga tio strängar i komponenten
`modem_callerid` har lästs från Lokalise.

## Rättning sparad i Lokalise

| Fullständig nyckel | Tidigare text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `component::modem_callerid::entity::button::phone_modem_reject::name` | Telefon modem avvisa | Avvisa samtal | Naturlig svensk åtgärdstext som motsvarar knappen för att avvisa inkommande samtal. |

Ändringen sparades via Lokalise API och lästes tillbaka ordagrant. Den är
inlagd i det validerade HA-minnet (`swedish-tm`, commit `0872cd0`).

## Kontrollerade utan ändring

| Fullständig nyckel | Aktuell svensk text |
| --- | --- |
| `component::modem_callerid::config::abort::already_configured` | Enheten är redan konfigurerad |
| `component::modem_callerid::config::abort::already_in_progress` | Detta konfigureras redan. Slutför den befintliga konfigurationen innan du börjar igen. |
| `component::modem_callerid::config::abort::no_devices_found` | Inga återstående enheter hittades |
| `component::modem_callerid::config::error::cannot_connect` | Det gick inte att ansluta |
| `component::modem_callerid::config::step::usb_confirm::description` | Den här integrationen är avsedd för samtal via fast telefoni med ett CX93001-röstmodem. Den kan hämta information om nummerpresentation och har ett alternativ för att avvisa inkommande samtal. |
| `component::modem_callerid::config::step::user::data::name` | Namn |
| `component::modem_callerid::config::step::user::data::port` | Port |
| `component::modem_callerid::config::step::user::description` | Den här integrationen är avsedd för samtal via fast telefoni med ett CX93001-röstmodem. Den kan hämta information om nummerpresentation och har ett alternativ för att avvisa inkommande samtal. |
| `component::modem_callerid::config::step::user::data::device` | Enhet |

## Verifiering

- Lokalise API: samtliga tio svenska översättningar hämtades direkt vid denna
  granskning; ändringen lästes tillbaka efter skrivning.
- `svlang check`: 10,0/10 för `Avvisa samtal`.
- `hunspell-sv`: inga stavningsavvikelser i den sparade knapptexten.
- Den längre CX93001-beskrivningen förekommer två gånger med identisk käll- och
  måltext och har kontrollerats på båda nycklarna.
- HA-TMX-validatorn: `valid: 3319 entries` efter uppdateringen.

Ingen osäker fråga eller oavslutad referens återstår för komponenten.
