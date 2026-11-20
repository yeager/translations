# Home Assistant Core – Evohome: undantag

Datum: 2026-11-20. Lokalise lästes i skrivskyddat läge och jämfördes med `homeassistant/components/evohome/strings.json` i Core-commit `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`.

## Tydligt ändringsförslag

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::evohome::exceptions::api_rate_limited::message` | Hastighetsgränsen för leverantörens API har överskridits. Försök igen senare | Gränsen för antalet anrop till leverantörens API har överskridits. Försök igen senare. | Sparad och återläst i Lokalise. API-*rate limit* begränsar anropsfrekvens, inte hastighet. |

## Aktuella källnycklar utan ytterligare ändringsförslag

Elva aktuella undantag har kontrollerats och är korrekta: `api_connection_failed`, `api_request_failed`, `api_request_rejected`, `api_server_error`, `controller_only_service`, `invalid_system_mode`, `mode_cant_be_temporary`, `mode_cant_have_duration`, `mode_cant_have_period`, `mode_not_supported` och `zone_only_service`. Kodvärdena `Duration`, `Period` och platshållarna `{mode}`, `{service}` och `{error}` är bevarade exakt.

`component::evohome::exceptions::api_credentials_invalid::message` är en aktuell men tom Lokalise-rad. Förslaget `Leverantörens API avvisade användarnamnet eller lösenordet` finns redan i [rapporten om nya tomma strängar](granskning-nya-tomma-strangar-hotspring.md) och dupliceras därför inte här.

## Historiska Lokalise-nycklar

`component::evohome::exceptions::api_call_failed::message` och `component::evohome::exceptions::entity_not_found::message` finns i Lokalise men saknas i den aktuella Core-källan. De är språkligt godtagbara respektive innehåller korrekt `{error}`/`{entity_id}`-platshållare, men de behandlas inte som aktiva förslag eller TMX-underlag.

## Validering och minneshantering

- `svlang skrivregler` gav inga träffar för förslaget.
- `hunspell -d sv_SE -l` gav inga felstavningsträffar.
- Anropsgränsvärdet är sparat, återläst och infört i det kanoniska HA-TMX-minnet.
  Det redan dokumenterade tomma värdet förs inte in förrän det har sparats och återlästs.

## Uppdatering och avvecklingsmeddelande

De två aktiva `refresh_system`-strängarna och de två aktuella raderna i `deprecated_refresh_system_service` är kontrollerade mot Core-källan utan ändringsförslag. `Uppdatera systemet` och dess beskrivning är korrekta. Issue-raderna bevarar `{breaks_in_ha_version}`, ``refresh_system`` och ``homeassistant.update_entity`` exakt och översätter korrekt målentiteten till *styrenhetens klimatentitet*.
