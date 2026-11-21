# Home Assistant Core – qBittorrent

Datum: 2026-11-21  
Källa: aktuell Core `2fdaa177`, `homeassistant/components/qbittorrent/strings.json`  
Status: samtliga 48 aktuella källsträngar är radgranskade mot Lokalise.

## Osparade förslag

| Nyckel | Källa | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- | --- |
| `component::qbittorrent::services::get_torrents::description` | Gets a list of current torrents | Visar en lista över aktuella torrenter | Hämtar en lista över aktuella torrenter | Källans åtgärd är hämtning, inte visning. Lokalise-ID `469339370`. |
| `component::qbittorrent::services::get_torrents::fields::torrent_filter::description` | What kind of torrents you want to return, such as All or Active. | Vilken typ av torrents du vill returnera, till exempel Alla eller Aktiva. | Vilken typ av torrenter som ska returneras, till exempel Alla eller Aktiva. | Rättar både pluralformen och satskonstruktionen. Lokalise-ID `469339373`. |
| `component::qbittorrent::services::get_all_torrents::fields::torrent_filter::description` | What kind of torrents you want to return, such as All or Active. | Vilken typ av torrents du vill returnera, till exempel Alla eller Aktiva. | Vilken typ av torrenter som ska returneras, till exempel Alla eller Aktiva. | Samma källtext och rättning som den andra filterbeskrivningen. Lokalise-ID `469339367`. |

## Verifierade befintliga värden

- De sju konfigurationsposterna använder korrekta gemensamma referenser för lösenord, URL, användarnamn, SSL, anslutning, autentisering och redan konfigurerad enhet.
- Samtliga sensor- och reglageetiketter, statusvärden och måttenheter är korrekta. Referenserna mellan torrentmåtten och de gemensamma anslutnings-/vilolägesvärdena är intakta.
- Torrentterminologi som `torrenter`, `Seedar`, `Laddar ner`, `Upp/ner`, `Begränsad av brandvägg` samt upp- och nedladdningshastighet är konsekvent och korrekt i sammanhanget.
- Alla fyra undantagstexter är korrekta; `{device_id}` bevaras i båda relevanta meddelandena.
- qBittorrent behåller sin officiella stavning, inklusive inledande gemen `q`.

Lokalise-sökningarna omfattade exakt de aktuella konfigurations-, entitets-, tjänst- och undantagsdelarna. De tre förslagen ovan är inte sparade och förs inte in i TMX före Lokalise-sparning och återläsning.
