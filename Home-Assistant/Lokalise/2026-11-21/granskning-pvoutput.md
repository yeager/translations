# Home Assistant Core – PVOutput

Datum: 2026-11-21  
Status: samtliga 23 aktuella bladnycklar är granskade mot `origin/dev` och Lokalise.

## Osparade förslag

| Nyckel | Källa | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- | --- |
| `component::pvoutput::config::step::reauth_confirm::data_description::api_key` | `[%key:component::pvoutput::config::step::user::data_description::api_key%]` | `API-nyckeln för ditt PVOutput-konto.` | `[%key:component::pvoutput::config::step::user::data_description::api_key%]` | Källans komponentreferens ska bevaras. Nuvarande mål flaggas för referens-/formatmismatch i Lokalise. ID `949163250`. |
| `component::pvoutput::config::step::reconfigure::data_description::api_key` | `[%key:component::pvoutput::config::step::user::data_description::api_key%]` | `API-nyckeln för ditt PVOutput-konto.` | `[%key:component::pvoutput::config::step::user::data_description::api_key%]` | Samma referensmismatch som återautentiseringsflödet. ID `949163251`. |

## Verifierade befintliga värden

- Alla gemensamma konfigurationsreferenser och `{account_url}` är bevarade i aktiva källsträngar.
- Instruktionerna för autentisering, återautentisering och omkonfigurering är språkligt korrekta.
- Sensorerna använder korrekt åtskillnad mellan energi och effekt: `Energiförbrukning`, `Energiproduktion`, `Effektförbrukning` och `Effektproduktion`.
- System-ID, API-nyckelbeskrivning, senaste rapportering och de fyra felmeddelandena är korrekta.
- Lokalise innehåller äldre poster för lyckad omkonfigurering och återautentisering som saknas i aktuell Core-källa; de är inte ändrade.

De två förslagen är inte sparade och ingår inte i TMX-minnet.
