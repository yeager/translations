# Home Assistant Core – Fing

Datum: 2026-11-20. Alla **15** aktuella Fing-strängar lästes i Lokalise och kontrollerades mot `homeassistant/components/fing/strings.json` i Core-commit `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12`.

## Tydligt ändringsförslag

| Fullständig nyckel | Befintlig svenska | Föreslagen svenska | Motivering |
| --- | --- | --- | --- |
| `component::fing::config::step::user::data_description::api_key` | API-nyckel som används för att autentisera med Fing API. | API-nyckel som används för att autentisera med Fing-API:et. | Rättar produktnamnssammansättningen och böjer `API` korrekt. Samma komponent använder redan `Fing-API:et` i portbeskrivningen. |

## Bedömda utan ändringsförslag

De övriga 14 strängarna är korrekta. Samtliga gemensamma konfigurationsreferenser är bevarade och platshållaren `{message}` i HTTP-felet är oförändrad. `Fing-agent`, `Fing-API:et` och meddelandet om den saknade `network_id`-parametern är konsekventa med källtexten.

## Validering och minneshantering

- `svlang skrivregler` gav inga träffar.
- Hunspell markerar produktnamnssammansättningen `Fing-API:et`; den har komponentintern källa men saknar oberoende generell ordbokskälla och läggs därför inte in globalt.
- Ingen Lokalise-skrivning har genomförts; förslaget har inte förts in i HA-TMX-minnet.
