# Home Assistant Core – ChirpStack

Datum: 2026-11-21

Källa: Home Assistant Core `2fdaa177`, `homeassistant/components/chirpstack/strings.json`, tidigare sparad granskningsdokumentation och direkt återläsning via Lokalise API.

Alla 26 aktuella ChirpStack-strängar lästes direkt från Lokalise och jämfördes med aktuell källtext. Tidigare sparad ändring för anslutningsfelet finns kvar. En ytterligare säker korrigering gjordes och lästes tillbaka.

| Fullständig nyckel | Befintlig svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::chirpstack::config::error::invalid_auth` | API-nyckeln avvisades eller kan inte komma åt denna klientorganisation | API-nyckeln avvisades eller saknar åtkomst till denna klientorganisation | Nyckeln är subjektet och saknar behörighet; den kan inte själv ”komma åt” klientorganisationen. |

API-nyckel, HTTP/HTTPS, HTTP/2, TLS, gRPC, UUID och produktnamnet ChirpStack har behållits exakt. Det verifierade språkparet är tillagt i Home Assistant-TMX; valideraren godkände 1 959 poster efter uppdateringen.
