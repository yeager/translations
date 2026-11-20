# Home Assistant Core – Ezviz: sensorer

Datum: 2026-11-20. Lokalise lästes i skrivskyddat läge och jämfördes med `homeassistant/components/ezviz/strings.json` i Core-commit `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`.

## Tydliga ändringsförslag

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::ezviz::entity::sensor::seconds_last_trigger::name` | Sekunder sedan senaste trigger | Sekunder sedan senaste utlösning — **sparad och återläst i Lokalise** | Undviker oöversatt engelskt substantiv och beskriver sensorhändelsen idiomatiskt. |
| `component::ezviz::entity::sensor::last_alarm_type_name::name` | Senaste larm typ namn | Namn på senaste larmtyp — **sparad och återläst i Lokalise** | Rättar särskrivningen *larm typ* och naturlig svensk ordföljd. |
| `component::ezviz::entity::sensor::last_alarm_type_code::name` | Senaste larm typ kod | Kod för senaste larmtyp | Rättar särskrivningen och naturlig svensk ordföljd. |
| `component::ezviz::entity::sensor::last_alarm_time::name` | Senaste larm tid | Tid för senaste larm | Rättar särskrivningen och gör etiketten idiomatisk. |

## Bedömda utan ändringsförslag

De fem andra aktuella sensorsraderna—`WAN-IP`, `Kanaler som stöds`, `PIR-status`, `Lokal IP` och `Ljudnivå för larm`—är korrekta.

## Historiska Lokalise-rader

`record_mode`, `power_status`, `online_status`, `battery_camera_work_mode` och `last_alarm_pic` syns i Lokalise men saknas i aktuell Core-källa. De bedöms därför inte som aktiva ändringsförslag och får inte användas som underlag för ett uppdaterat TMX-minne.

## Validering och minneshantering

- `svlang skrivregler` gav inga träffar för alla fyra förslag.
- `hunspell -d sv_SE -l` gav inga felstavningsträffar.
- Ingen Lokalise-skrivning har genomförts; förslagen har inte förts in i HA-TMX-minnet.
