# Home Assistant Core – PVOutput

Datum: 2026-11-21  
Status: samtliga 23 aktuella bladnycklar är granskade mot `origin/dev` och Lokalise.

## Referensuppföljning

| Nyckel | Källa | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- | --- |
| `component::pvoutput::config::step::reauth_confirm::data_description::api_key` | `[%key:component::pvoutput::config::step::user::data_description::api_key%]` | `API-nyckeln för ditt PVOutput-konto.` | Ingen ändring | Aktuell API-export löser referensen till korrekt svensk måltext. Referenslagringen följs upp separat. |
| `component::pvoutput::config::step::reconfigure::data_description::api_key` | `[%key:component::pvoutput::config::step::user::data_description::api_key%]` | `API-nyckeln för ditt PVOutput-konto.` | Ingen ändring | Aktuell API-export löser referensen till korrekt svensk måltext. Referenslagringen följs upp separat. |

## Verifierade befintliga värden

- Alla gemensamma konfigurationsreferenser och `{account_url}` är bevarade i aktiva källsträngar.
- Instruktionerna för autentisering, återautentisering och omkonfigurering är språkligt korrekta.
- Sensorerna använder korrekt åtskillnad mellan energi och effekt: `Energiförbrukning`, `Energiproduktion`, `Effektförbrukning` och `Effektproduktion`.
- System-ID, API-nyckelbeskrivning, senaste rapportering och de fyra felmeddelandena är korrekta.
- Lokalise innehåller äldre poster för lyckad omkonfigurering och återautentisering som saknas i aktuell Core-källa; de är inte ändrade.

Raderna är inte språkfel i den aktuella API-exporten och förs därför inte in
som nya TMX-poster. Referensrepresentationen följs upp separat.
