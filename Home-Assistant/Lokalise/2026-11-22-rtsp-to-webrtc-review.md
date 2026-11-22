# RTSPtoWebRTC: fullständig svensk granskning

Granskad 22 november 2026 mot aktuell källtext och aktuella svenska
översättningar i Lokalise via API. Samtliga 14 strängar i komponenten
`rtsp_to_webrtc` har lästs från Lokalise. Platshållarna `{addon}` och
`{go2rtc}`, URL:en och formatet `(värd:port)` är bevarade exakt.

## Rättning sparad i Lokalise

| Fullständig nyckel | Tidigare text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `component::rtsp_to_webrtc::issues::deprecated::title` | RTSPtoWebRTC-integreringen är utfasad | RTSPtoWebRTC-integrationen är utfasad | `Integration` används genomgående som `integration` i Home Assistant. |

Ändringen lästes tillbaka från Lokalise efter sparning och finns i det
validerade HA-minnet i `swedish-tm`.

## Kontrollerade utan ändring

| Fullständig nyckel | Aktuell svensk text |
| --- | --- |
| `component::rtsp_to_webrtc::config::abort::single_instance_allowed` | Redan konfigurerad. Endast en konfiguration kan göras. |
| `component::rtsp_to_webrtc::config::error::invalid_url` | Måste vara en giltig RTSPtoWebRTC-serveradress, t.ex. https://example.com |
| `component::rtsp_to_webrtc::config::error::server_failure` | RTSPtoWebRTC-servern returnerade ett fel. Kontrollera loggar för mer information. |
| `component::rtsp_to_webrtc::config::error::server_unreachable` | Det går inte att kommunicera med RTSPtoWebRTC-servern. Kontrollera loggar för mer information. |
| `component::rtsp_to_webrtc::config::step::user::data::server_url` | RTSPtoWebRTC-serveradress, t.ex. https://example.com |
| `component::rtsp_to_webrtc::config::step::user::description` | RTSPtoWebRTC-integrationen kräver en server för att översätta RTSP-strömmar till WebRTC. Ange URL:en till RTSPtoWebRTC-servern. |
| `component::rtsp_to_webrtc::config::step::user::title` | Konfigurera RTSPtoWebRTC |
| `component::rtsp_to_webrtc::config::step::hassio_confirm::description` | Vill du konfigurera Home Assistant för att ansluta till RTSPtoWebRTC-servern som tillhandahålls av tillägget {addon}? |
| `component::rtsp_to_webrtc::config::step::hassio_confirm::title` | RTSPtoWebRTC via Home Assistant-tillägget |
| `component::rtsp_to_webrtc::config::abort::server_failure` | RTSPtoWebRTC-servern returnerade ett fel. Kontrollera loggar för mer information. |
| `component::rtsp_to_webrtc::config::abort::server_unreachable` | Det går inte att kommunicera med RTSPtoWebRTC-servern. Kontrollera loggar för mer information. |
| `component::rtsp_to_webrtc::options::step::init::data::stun_server` | Stun serveradress (värd:port) |
| `component::rtsp_to_webrtc::issues::deprecated::description` | RTSPtoWebRTC-integrationen är utfasad och kommer att tas bort. Använd {go2rtc}-integrationen istället, som är aktiverad som standard och ger en bättre upplevelse. Du behöver bara ta bort konfigurationsposten RTSPtoWebRTC. |

## Verifiering

- Lokalise API: alla 14 svenska översättningar hämtades direkt vid denna
  granskning.
- Referenser, produktnamn och tekniska protokollnamn (`RTSP`, `WebRTC`,
  `URL`, `STUN`) har medvetet inte översatts.
- Den dubbla engelska felmallen förekommer i både konfigurations- och
  avbrottsflödet; den svenska översättningen är konsekvent på båda ställena.

Ingen osäker fråga eller oavslutad referens återstår för komponenten.
