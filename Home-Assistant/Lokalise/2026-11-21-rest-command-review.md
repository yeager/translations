# Home Assistant – REST Command: svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `rest_command`

## Underlag

Samtliga fem strängar jämfördes mot aktuell `homeassistant/components/rest_command/strings.json` och Lokalise API. `svlang`, `hunspell-sv`, `swedish-foss-terminology` och `swedish-tm` användes som stöd. Hunspell gav inga relevanta stavningsträffar. Svlang markerade endast platshållaren `request_url`, vilket är en teknisk identifierare och ska bevaras.

## Radvis resultat

| Fullständig nyckel | Engelska | Befintlig svenska | Resultat |
| --- | --- | --- | --- |
| `component::rest_command::exceptions::client_error::message` | Client error occurred when calling resource "{request_url}" | Klientfel inträffade vid anrop av resurs "{request_url}" | Sparad som **Ett klientfel uppstod vid anrop av resursen "{request_url}"**. Naturligare svensk formulering och bestämd form, platshållaren är oförändrad. |
| `component::rest_command::exceptions::decoding_error::message` | The response of "{request_url}" could not be decoded as {decoding_type} | Svaret från "{request_url}" kunde inte avkodas som {decoding_type} | Behåll. Båda platshållarna bevaras och formuleringen är korrekt. |
| `component::rest_command::exceptions::timeout::message` | Timeout when calling resource "{request_url}" | Timeout vid anrop av resurs "{request_url}" | Sparad som **Tidsgränsen överskreds vid anrop av resursen "{request_url}"**. Följer Home Assistants etablerade svenska felmeddelandeterminologi. |
| `component::rest_command::services::reload::description` | Reloads RESTful commands from the YAML-configuration. | Laddar om RESTful-kommandon från YAML-konfigurationen. | Behåll. |
| `component::rest_command::services::reload::name` | Reload | Ladda om | Behåll. Delad referens med korrekt upplöst måltext. |

## Verifiering

De två ändringarna skickades via Lokalise API och lästes tillbaka efter sparandet. Inga referenser, platshållare eller formatmarkörer förändrades.