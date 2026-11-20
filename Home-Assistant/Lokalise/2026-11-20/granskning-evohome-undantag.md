# Home Assistant Core – Evohome: undantag

Datum: 2026-11-20. Lokalise lästes i skrivskyddat läge och jämfördes med `homeassistant/components/evohome/strings.json` i Core-commit `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`.

## Tydligt ändringsförslag

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::evohome::exceptions::api_rate_limited::message` | Hastighetsgränsen för leverantörens API har överskridits. Försök igen senare | Gränsen för antalet anrop till leverantörens API har överskridits. Försök igen senare. | API-*rate limit* begränsar anropsfrekvens, inte hastighet. Home Assistant-minnet stöder exempelvis *Anropsgränsen har överskridits* och *Gränsen för antalet anrop … har överskridits*. Punkt avslutar också den första satsen korrekt. |

## Aktuella källnycklar utan ytterligare ändringsförslag

Elva aktuella undantag har kontrollerats och är korrekta: `api_connection_failed`, `api_request_failed`, `api_request_rejected`, `api_server_error`, `controller_only_service`, `invalid_system_mode`, `mode_cant_be_temporary`, `mode_cant_have_duration`, `mode_cant_have_period`, `mode_not_supported` och `zone_only_service`. Kodvärdena `Duration`, `Period` och platshållarna `{mode}`, `{service}` och `{error}` är bevarade exakt.

`component::evohome::exceptions::api_credentials_invalid::message` är en aktuell men tom Lokalise-rad. Förslaget `Leverantörens API avvisade användarnamnet eller lösenordet` finns redan i [rapporten om nya tomma strängar](granskning-nya-tomma-strangar-hotspring.md) och dupliceras därför inte här.

## Historiska Lokalise-nycklar

`component::evohome::exceptions::api_call_failed::message` och `component::evohome::exceptions::entity_not_found::message` finns i Lokalise men saknas i den aktuella Core-källan. De är språkligt godtagbara respektive innehåller korrekt `{error}`/`{entity_id}`-platshållare, men de behandlas inte som aktiva förslag eller TMX-underlag.

## Validering och minneshantering

- `svlang skrivregler` gav inga träffar för förslaget.
- `hunspell -d sv_SE -l` gav inga felstavningsträffar.
- Ingen Lokalise-skrivning har genomförts. Varken detta förslag eller det redan dokumenterade tomma värdet får föras in i det kanoniska HA-TMX-minnet förrän de sparats och återlästs.
