# Sparad ändring för UniFi Protect

Sparad och återläst i Lokalise 2026-11-19 efter kontroll mot tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::unifiprotect::config::step::api_key::description` | Connect using only an API key, without a local user. Features the public Integration API does not offer yet are unavailable. For more information: {api_key_documentation_url} | Anslut enbart med hjälp av en API-nyckel, utan lokal användare. Läget ”endast API-nyckel” erbjuder för närvarande en begränsad uppsättning enheter: larmhanteraren, kameror (strömmar och stillbilder) samt belysning. Allt annat kräver en lokal användare. För mer information: {api_key_documentation_url} | Anslut med enbart en API-nyckel, utan lokal användare. Funktioner som det offentliga integrations-API:t ännu inte erbjuder är inte tillgängliga. Mer information: {api_key_documentation_url} |

En föråldrad detaljuppräkning ersätts med den aktuella källans begränsning; platshållaren är bevarad. Närliggande API-nyckeltexter i tidigare rapport återstår.

## Upptäckt med API-nyckel

Sparad och återläst i Lokalise efter jämförelse med tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::unifiprotect::config::step::discovery_api_key::description` | Connect to {name} ({ip_address}) using only an API key. Features the public Integration API does not offer yet are unavailable. For more information: {api_key_documentation_url} | Anslut till {name} ({ip_address}) enbart med hjälp av en API-nyckel. Läget där endast API-nyckel används erbjuder för närvarande en begränsad uppsättning enheter: larmhanteraren, kameror (strömmar och ögonblicksbilder) samt belysning. Allt annat kräver en lokal användare. För mer information: {api_key_documentation_url} | Anslut till {name} ({ip_address}) med enbart en API-nyckel. Funktioner som det offentliga integrations-API:t ännu inte erbjuder är inte tillgängliga. Mer information: {api_key_documentation_url} |

Den äldre uppräkningen ersätts med aktuell källtext och de tre platshållarna är bevarade.

## Omkonfigurering till API-nyckel

Sparad och återläst i Lokalise efter jämförelse med tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::unifiprotect::config::step::reconfigure_api_key::description` | Switch to (or update) API-key-only mode. Stored local user credentials are kept, so you can switch back at any time. Features the public Integration API does not offer yet are unavailable. For more information: {api_key_documentation_url} | Växla till (eller uppdatera) API-nyckel-läge. Lagrade lokala användaruppgifter behålls, så att du kan växla tillbaka när som helst. API-nyckel-läget tillhandahåller för närvarande en begränsad uppsättning enheter: larmhanteraren, kameror (strömmar och ögonblicksbilder) och belysning. Allt annat kräver en lokal användare. För mer information: {api_key_documentation_url} | Växla till eller uppdatera läget med enbart API-nyckel. Sparade inloggningsuppgifter för den lokala användaren behålls, så att du kan växla tillbaka när som helst. Funktioner som det offentliga integrations-API:t ännu inte erbjuder är inte tillgängliga. Mer information: {api_key_documentation_url} |

Den äldre uppräkningen ersätts med aktuell källtext; uppgiften om återgång och platshållaren bevaras.

## Lokal användare

Sparade och återlästa i Lokalise efter jämförelse med tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::unifiprotect::exceptions::public_only_no_actions::message` | This action requires a local user; the entry is set up with an API key only. | Denna åtgärd kräver fullständig åtkomst (lokal användare); inställningen konfigureras enbart med en API-nyckel. | Den här åtgärden kräver en lokal användare. Posten är konfigurerad med enbart en API-nyckel. |
| `component::unifiprotect::config::step::full::data_description::username` | Username for your local (not cloud) user account. | Användarnamn för ditt lokala (inte moln-) användarkonto. | Användarnamn för ditt lokala användarkonto, inte ditt molnkonto. |

Kravet och tidsformen följer källtexten. Tre separata användarnamnsreferenser kontrollerades på båda språken och pekar på den ändrade texten.

## Beskrivning av API-nyckelfältet

Sparad och återläst i Lokalise efter jämförelse med tidigare granskningsrapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::unifiprotect::config::step::api_key::data_description::api_key` | API key from your UniFi OS Console. Only the public Integration API is used; some entities that require a local user are unavailable in this mode. | API-nyckel från din UniFi OS-konsol. Endast det offentliga integrations-API:et används; vissa funktioner som kräver en lokal användare är inte tillgängliga i det här läget. | API-nyckel från din UniFi OS-konsol. Endast det offentliga integrations-API:t används. Vissa entiteter som kräver en lokal användare är inte tillgängliga i det här läget. |

Entiteter motsvarar källans entities. Tre separata API-nyckelreferenser kontrollerades på båda språken och pekar på den ändrade texten.

## Föråldrade sensorinställningar

Sparade och återlästa i Lokalise 2026-11-19. Mellanslag och syftning rättades; platshållare och kodmarkeringar bevarades. `<br>` i tabellen återger radbrytningar.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::unifiprotect::issues::sense_setting_mirror_deprecated_no_replacement::title` | Read-only sensor setting entity deprecated | Skrivskyddad sensorinställningsenhet föråldrad | Skrivskyddad entitet för sensorinställning är föråldrad |
| `component::unifiprotect::issues::sense_setting_mirror_deprecated::title` | Read-only sensor setting entity deprecated | Skrivskyddad sensorinställningsenhet föråldrad | Skrivskyddad entitet för sensorinställning är föråldrad |
| `component::unifiprotect::issues::sense_setting_mirror_deprecated_no_replacement::description` | The read-only entity `{entity_id}` is deprecated and will be removed in a future release. The sensor does not support this setting, so there is no replacement.<br><br>Update the following automations and scripts:<br>{items} | Den skrivskyddade entiteten `{entity_id}`är föråldrad och kommer att tas bort i en framtida version. Sensorn stöder inte den här inställningen, så det finns ingen ersättning.<br><br>Uppdatera följande automatiseringar och skript:<br>{items} | Den skrivskyddade entiteten `{entity_id}` är föråldrad och kommer att tas bort i en framtida version. Sensorn stöder inte den här inställningen, så det finns ingen ersättning.<br><br>Uppdatera följande automatiseringar och skript:<br>{items} |
| `component::unifiprotect::issues::sense_setting_mirror_deprecated::description` | The read-only entity `{entity_id}` is deprecated and will be removed in a future release; use `{replacement}` instead, which holds the same state and can also change it.<br><br>Update the following automations and scripts:<br>{items} | Den skrivskyddade entiteten `{entity_id}`är föråldrad och kommer att tas bort i en framtida version; använd `{replacement}`istället, vilket håller samma tillstånd och även kan ändra det.<br><br>Uppdatera följande automatiseringar och skript:<br>{items} | Den skrivskyddade entiteten `{entity_id}` är föråldrad och kommer att tas bort i en framtida version. Använd `{replacement}` i stället: den har samma tillstånd och kan även ändra det.<br><br>Uppdatera följande automatiseringar och skript:<br>{items} |

## Dörrklockans text

Sparad och återläst i Lokalise den 19 november 2026 efter jämförelse med tidigare rapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::unifiprotect::entity::select::doorbell_text::name` | Doorbell text | Dörrklocka text | Dörrklockans text |

Genitivformen rättar sammansättningen. `component::unifiprotect::entity::sensor::doorbell_text::name` hänvisar på båda språken till den ändrade nyckeln; referensen behölls.

## Uppspelning av signaler

Sparade och återlästa i Lokalise den 19 november 2026 efter jämförelse med tidigare rapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::unifiprotect::entity::button::play_chime::name` | Play chime | Spela upp klocka | Spela upp ringsignal |
| `component::unifiprotect::entity::button::play_buzzer::name` | Play buzzer | Spela upp summer | Spela upp summersignal |

Benämningarna anger ljuden som spelas upp.

## Ringningens varaktighet

Sparad och återläst i Lokalise den 19 november 2026 efter jämförelse med tidigare rapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::unifiprotect::entity::number::chime_duration::name` | Chime duration | Varaktighet för klocka | Ringningens varaktighet |

Ljussensorns brytare har en svensk referens till `component::unifiprotect::entity::binary_sensor::light_sensor::name`, vars engelska och svenska text kontrollerades som ”Light sensor” respektive ”Ljussensor”. Referensen behölls.

## Tid till automatisk låsning

Sparad och återläst i Lokalise den 19 november 2026 efter jämförelse med tidigare rapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::unifiprotect::entity::number::auto_lock_timeout::name` | Auto-lock timeout | Timeout för automatisk låsning | Tid till automatisk låsning |

Tidsangivelsen uttrycks på svenska.

## Tid till automatisk avstängning

Sparad och återläst i Lokalise den 19 november 2026 efter jämförelse med tidigare rapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::unifiprotect::entity::number::auto_shutoff_duration::name` | Auto-shutoff duration | Varaktighet för automatisk avstängning | Tid till automatisk avstängning |

[Home Assistants kod](https://github.com/home-assistant/core/blob/dev/homeassistant/components/unifiprotect/number.py) kopplar inställningen till ljusenhetens rörelsesensor och en varaktighet i sekunder. Tidsangivelsen förtydligas som tid till avstängning.

## Infrarött luxgränsvärde

Sparad och återläst i Lokalise den 19 november 2026 efter jämförelse med tidigare rapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::unifiprotect::entity::number::infrared_custom_lux_trigger::name` | Infrared custom lux trigger | Infraröd anpassad lux-utlösare | Anpassat luxgränsvärde för infrarött ljus |

[Home Assistants kod](https://github.com/home-assistant/core/blob/dev/homeassistant/components/unifiprotect/number.py) kopplar värdet till kameror med infraröd LED och inställningen `icr_lux`; ljusgränsvärde är en tolkning av källans ”lux trigger”.

## Lägga till enhet

Sparad och återläst i Lokalise den 19 november 2026 efter jämförelse med tidigare rapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::unifiprotect::entity::button::adopt_device::name` | Adopt device | Adoptera enhet | Lägg till enhet i UniFi Protect |

[Ubiquitis dokumentation](https://help.ui.com/hc/en-us/articles/27878858632599-Getting-Started-with-UniFi-Protect) beskriver adoption som att lägga till kameror i UniFi Protect. [Home Assistants kod](https://github.com/home-assistant/core/blob/dev/homeassistant/components/unifiprotect/button.py) kopplar knappen till `adopt`. Den relaterade borttagningsknappen återstår att kontrollera.

## Ta bort enhet

Sparad och återläst i Lokalise den 19 november 2026 efter jämförelse med tidigare rapport.

| Fullständig nyckel | Engelska | Tidigare svenska | Sparad svenska |
|---|---|---|---|
| `component::unifiprotect::entity::button::unadopt_device::name` | Unadopt device | Avadoptera enhet | Ta bort enhet från UniFi Protect |

[Home Assistants kod](https://github.com/home-assistant/core/blob/dev/homeassistant/components/unifiprotect/button.py) kopplar knappen till `unadopt` med raderingsbehörighet. [Ubiquitis dokumentation](https://help.ui.com/hc/en-us/articles/26301104828439-Third-Party-Cameras-in-UniFi-Protect) beskriver att en kamera kan tas bort och läggas till på nytt i Protect. Formuleringen kompletterar knappnamnet för att lägga till en enhet.
