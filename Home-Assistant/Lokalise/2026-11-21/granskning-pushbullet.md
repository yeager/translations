# Home Assistant Core – Pushbullet

Datum: 2026-11-21  
Status: samtliga 19 aktuella bladnycklar är granskade mot `origin/dev` och Lokalise.

## Referensuppföljning

| Nyckel | Källa | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- | --- |
| `component::pushbullet::config::step::reauth_confirm::title` | `[%key:common::config_flow::title::reauth%]` | `Autentiseringen har upphört för {name}` | Ingen ändring | Aktuell API-export löser referensen till en platshållarkorrekt text. Behåll som uppföljning tills referenslagring kan verifieras separat. |
| `component::pushbullet::config::step::reauth_confirm::data::api_key` | `[%key:common::config_flow::data::api_key%]` | `API-nyckel` | Ingen ändring | Aktuell API-export löser referensen till dess korrekta svenska måltext. Behåll som uppföljning tills referenslagring kan verifieras separat. |

## Verifierade befintliga värden

- Återautentiseringsbeskrivningen är korrekt: `Pushbullet API-nyckeln är inte längre giltig. Ange en ny API-nyckel.` (ID `952263598`).
- Kontofelet `API-nyckeln hör till ett annat Pushbullet-konto än det konfigurerade.` och undantaget `Ogiltig API-nyckel för Pushbullet` är korrekta (ID `952263596`, `951175406`).
- Sensorerna för applikationsnamn, meddelande, aviseringens ID och tagg, paketnamn, avsändare/mottagare, avsändarens enhets-ID, rubrik och typ är korrekta (ID `347197488`–`347197497`).
- Övriga aktiva konfigurationsreferenser är bevarade. En äldre Lokalise-rad för användarens `name` finns utanför den aktuella Core-källan och har inte ändrats.

De två raderna är inte språkfel i den aktuella API-exporten och ingår därför
inte som nya poster i TMX-minnet. Referensrepresentationen behöver en separat
Lokalise-kontroll.
