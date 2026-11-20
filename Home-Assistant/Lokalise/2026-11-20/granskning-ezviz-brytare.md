# Home Assistant Core – Ezviz: brytare

Datum: 2026-11-20. Lokalise lästes i skrivskyddat läge och alla tolv aktuella brytarsträngar kontrollerades mot `homeassistant/components/ezviz/strings.json` i Core-commit `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`.

## Tydligt ändringsförslag

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::ezviz::entity::switch::pir_motion_activated_light::name` | PIR rörelseaktiverat ljus | PIR-rörelseaktiverat ljus — **sparad och återläst i Lokalise** | Initialförkortningen är förled i en svensk sammansättning och ska därför följas av bindestreck. |

## Bedömda utan ändringsförslag

`Sabotagelarm`, `Statuslampa`, `Viloläge`, `Integritet`, `Rörelsespårning`, `IR-ljus`, `Följ rörelse`, `Blinka ljus vid rörelse`, `Automatiskt viloläge`, `Ljud` och `Videoinspelning hela dygnet` återger respektive aktiv Core-källtext korrekt.

## Validering och minneshantering

- `svlang skrivregler` gav inga träffar för förslaget.
- `hunspell -d sv_SE -l` gav inga felstavningsträffar.
- Ändringen sparades och återlästes i Lokalise 2026-11-20 och har förts in i det kanoniska HA-TMX-minnet.
