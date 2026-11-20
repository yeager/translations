# Home Assistant Core – Tankerkoenig, del 1

Datum: 2026-11-20  
Källa: Home Assistant Core `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`,
`homeassistant/components/tankerkoenig/strings.json`  
Lokalise: läsning av `component::tankerkoenig`; inga skrivningar har gjorts.

## Omfattning

Den första och andra synliga delen omfattar **minst 38 av 72** aktuella Lokalise-nycklar,
inklusive tjänsten `get_opening_times`, undantag, gemensamma datafält och de
första sensorattributen. De resterande 44 nycklarna är inte markerade som
färdiggranskade.

Följande värden och referenser är korrekta i denna del: stations-, plats-,
radie- och kartbeskrivningarna, sensorattributen `city`, `fuel_type`,
`house_number`, `latitude`, `longitude`, `postcode`, `station_name` och
`street`, samt de återanvända referenserna som redan är identiska med källan.

## Lokala, ännu osparade förslag

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::tankerkoenig::services::get_opening_times::name` | Tom | `Hämta öppettider` | Ny tjänstetikett; tydlig imperativform. |
| `component::tankerkoenig::services::get_opening_times::description` | Tom | `Hämtar en bensinstations öppettider och tillfälliga ändringar.` | Återger både öppettider och temporära ändringar. |
| `component::tankerkoenig::options::abort::cannot_connect` | `Det gick inte att ansluta` | `[%key:common::config_flow::error::cannot_connect%]` | Återställer den obligatoriska referensen från aktuell Core-källa. |
| `component::tankerkoenig::config::error::cannot_connect` | `Det gick inte att ansluta` | `[%key:common::config_flow::error::cannot_connect%]` | Återställer den obligatoriska referensen från aktuell Core-källa. |
| `component::tankerkoenig::exceptions::connection_error::message` | `Misslyckades med att ansluta till  Tankerkoenig  API. Kontrollera din nätverksanslutning.` | `Det gick inte att ansluta till Tankerkoenig-API:t. Kontrollera din nätverksanslutning.` | Korrigerar sammansättning och blanksteg samt ger naturlig svensk formulering. |
| `component::tankerkoenig::exceptions::rate_limit_reached::message` | `Du har nått begränsningen för  Tankerkoenig-API :et. Försök att öka  avfrågningsintervallet  och minska antalet förfrågningar.` | `Du har nått begränsningen för Tankerkoenig-API:t. Försök att öka avfrågningsintervallet och minska antalet förfrågningar.` | Korrigerar böjning av sammansättningen och överflödiga blanksteg. |
| `component::tankerkoenig::exceptions::invalid_api_key::message` | `Den angivna  API-nyckeln  är ogiltig. Kontrollera din API-nyckel.` | `Den angivna API-nyckeln är ogiltig. Kontrollera din API-nyckel.` | Tar bort överflödiga blanksteg. |
| `component::tankerkoenig::common::data_description_api_key` | `Tankerkoenig API-nyckeln  som ska användas.` | `Den Tankerkoenig-API-nyckel som ska användas.` | Svensk sammansättning och fullständig bestämning. |
| `component::tankerkoenig::options::error::invalid_auth` | `[%key:common::config_flow::error::invalid_auth%]` | `[%key:component::tankerkoenig::config::error::invalid_auth%]` | Återställer den komponentreferens som finns i den aktuella Core-källan. |
| `component::tankerkoenig::entity::sensor::e10::name` | `Super  E10` | `Super E10` | Tar bort dubbelblanksteg i bränslebeteckningen. |

## Verktygsstatus

Förslagen följer den befintliga svenska Core-terminologin för `API-nyckel`,
`avfrågningsintervall` och `bensinstation`. De ska inte läggas till i
Home Assistant-TMX:en förrän eventuella Lokalise-värden har sparats och lästs
tillbaka. Den tidigare dokumenterade API-sparningen för tre Tankerkoenig-rader
ersätts inte av denna delgranskning.
