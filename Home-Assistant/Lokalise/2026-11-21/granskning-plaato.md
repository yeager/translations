# Home Assistant Core – Plaato

Datum: 2026-11-21

## Fullständig radgranskning

| Nyckel | Källa | Svenska | Bedömning |
| --- | --- | --- | --- |
| `component::plaato::config::step::api_method::description` | To be able to query the API an 'auth token' is required which can be obtained by following [these instructions]({auth_token_url})… | För att kunna göra förfrågningar till API:et krävs en autentiseringstoken. Den får du genom att följa [dessa instruktioner]({auth_token_url})… | Verifierad i Lokalise (ID `74499923`). Båda platshållarna, länken och Markdown-formatet är bevarade. |
| `component::plaato::config::step::webhook::description` | To send events to Home Assistant, you will need to set up the webhook feature in Plaato Airlock… | För att skicka händelser till Home Assistant måste du konfigurera webhookfunktionen i Plaato Airlock… | Verifierad i Lokalise (ID `74499927`). Båda platshållarna, kodformateringen och listan är bevarade. |
| `component::plaato::config::create_entry::default` | Your Plaato {device_type} with name **{device_name}** was successfully set up! | Din Plaato {device_type} med namn **{device_name}** är färdig att användas! | Verifierad i Lokalise (ID `23517552`); båda platshållarna och fetstilen är bevarade. |
| `component::plaato::config::error::invalid_webhook_device` | You have selected a device that does not support sending data to a webhook. It is only available for the Airlock | Du har valt en enhet som inte stöder att skicka data till en webhook. Den är endast tillgänglig för Airlock | Verifierad i Lokalise (ID `74499918`). |
| `component::plaato::config::error::no_api_method` | You need to add an auth token or select webhook | Du måste lägga till en autentiseringstoken eller välja webhook | Verifierad i Lokalise (ID `74499919`). |

De återstående direkta strängarna är radgranskade mot aktuell Core-källa och Lokalise-exporten utan ändringsförslag: flödestitlarna och etiketterna är idiomatiska, `Home Assistant` och `Home Assistant Cloud` bevaras som produktnamn, och alla webhook-URL:er, fetstil och radbrytningar är intakta. `webhook_not_internet_accessible`, `no_options` och `scan_interval` är källreferenser eller kompatibilitetsposter där den upplösta svenska Lokalise-texten är korrekt.

