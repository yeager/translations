# Portainer och IMAP: språkfel i tidigare förslag

Ändringarna nedan har sparats och lästs tillbaka via Lokalise API den 24 november 2026. Källtexterna kontrollerades mot aktuell Home Assistant Core `strings.json`.

| Fullständig nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::portainer::config::step::reauth_confirm::data_description::api_token` | `Den nya API åtkomsttoken för autentisering med Portainer` | `Den nya API-åtkomsttoken för autentisering mot Portainer` | Korrigerad sammansättning och naturligare preposition. |
| `component::imap::services::fetch_part::name` | `Hämta meddelande del` | `Hämta meddelandedel` | Korrigerad sammansättning. |
| `component::imap::services::fetch_part::fields::part::description` | `Meddelande delens index.` | `Meddelandedelens index.` | Korrigerad sammansättning. |
| `component::imap::exceptions::invalid_part_index::message` | `Ogiltigt del index.` | `Ogiltigt delindex.` | Korrigerad sammansättning. |
| `component::portainer::config::step::user::data_description::url` | `URL:en, inklusive porten, för din Portainer instans` | `URL:en, inklusive porten, för din Portainer-instans` | Korrigerad sammansättning. |
| `component::portainer::config::step::user::data_description::api_token` | `API åtkomsttoken för autentisering med Portainer` | `API-åtkomsttoken för autentisering mot Portainer` | Korrigerad sammansättning och naturligare preposition. |
| `component::portainer::config::step::user::data_description::verify_ssl` | `Huruvida SSL certifikat ska verifieras. Inaktivera endast om du har ett självsignerat certifikat.` | `Om SSL-certifikat ska verifieras. Inaktivera endast om du har ett självsignerat certifikat.` | Korrigerad sammansättning och idiomatisk inledning. |

Samtliga sju poster är märkta `saved-and-read-back` i Home Assistant-minnets snapshot, PO och TMX.
