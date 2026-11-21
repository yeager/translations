# Home Assistant Core – Pushbullet

Datum: 2026-11-21  
Status: samtliga 19 aktuella bladnycklar är granskade mot `origin/dev` och Lokalise.

## Osparade förslag

| Nyckel | Källa | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- | --- |
| `component::pushbullet::config::step::reauth_confirm::title` | `[%key:common::config_flow::title::reauth%]` | `Autentiseringen har upphört för {name}` | `[%key:common::config_flow::title::reauth%]` | Måltexten innehåller den odefinierade platshållaren `{name}` och avviker från den obligatoriska gemensamma referensen. Lokalise-ID `952263599`. |
| `component::pushbullet::config::step::reauth_confirm::data::api_key` | `[%key:common::config_flow::data::api_key%]` | `API-nyckel` | `[%key:common::config_flow::data::api_key%]` | Källans referens ska bevaras för konsekvens och för att undanröja Lokalises referens-/formatvarning. Lokalise-ID `952263597`. |

## Verifierade befintliga värden

- Återautentiseringsbeskrivningen är korrekt: `Pushbullet API-nyckeln är inte längre giltig. Ange en ny API-nyckel.` (ID `952263598`).
- Kontofelet `API-nyckeln hör till ett annat Pushbullet-konto än det konfigurerade.` och undantaget `Ogiltig API-nyckel för Pushbullet` är korrekta (ID `952263596`, `951175406`).
- Sensorerna för applikationsnamn, meddelande, aviseringens ID och tagg, paketnamn, avsändare/mottagare, avsändarens enhets-ID, rubrik och typ är korrekta (ID `347197488`–`347197497`).
- Övriga aktiva konfigurationsreferenser är bevarade. En äldre Lokalise-rad för användarens `name` finns utanför den aktuella Core-källan och har inte ändrats.

De två förslagen är inte sparade i Lokalise och ingår därför inte i TMX-minnet.
