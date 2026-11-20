# Home Assistant Core – Ezviz: återstående aktiva strängar

Datum: 2026-11-20. Alternativ, tjänst och återstående entiteter kontrollerades mot `homeassistant/components/ezviz/strings.json` i Core-commit `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`.

## Tydligt ändringsförslag

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::ezviz::entity::image::last_motion_image::name` | Sista rörliga bilden | Senaste rörelsebilden — **sparad och återläst i Lokalise** | *Motion image* är bilden från den senaste rörelsehändelsen, inte en animerad/rörlig bild. |

## Bedömda utan ändringsförslag

De fyra alternativraderna är korrekta. Den aktiva tjänsten `wake_device` med namn och beskrivning är korrekt. `Detektionskänslighet` är korrekt talvärde och både lamp- och sirenentiteten bevarar sina gemensamma referenser exakt.

## Historiska Lokalise-rader

Den äldre tjänsten `set_alarm_detection_sensibility` med sex följdrader saknas i aktuell Core-källa. Den har därför inte behandlats som en aktiv ändring eller TMX-källa.

## Validering och minneshantering

`svlang skrivregler` och `hunspell -d sv_SE -l` accepterar `Senaste rörelsebilden`. Ändringen sparades och återlästes i Lokalise 2026-11-20 och har förts in i det kanoniska HA-TMX-minnet med statusen `saved-and-read-back`.
