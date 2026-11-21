# Home Assistant Core: vattenvärmare — sparad granskning

Granskning mot Lokalise-exporten 2026-11-21, tidigare rapporter i `2026-11-19-granskning` och HA-minnet. Samtliga 142 nycklar i `component::water_heater` har lästs i sin grupp; 30 tydliga språk- och konsekvensrättningar sparades via Lokalise API och återlästes med GET. De övriga 112 bedömdes korrekta i sammanhanget.

Den fullständiga, maskinläsbara listan med varje nyckel, engelska, sparad svenska samt Lokalise-ID finns i `swedish-tm`-manifestet `Home-Assistant/2026-11-21-water-heater-verified.json` (commit `ad40cc6`).

## Sparade ändringar

- `component::water_heater::common::trigger_behavior_description`, `triggers::target_temperature_crossed_threshold::fields::behavior::description`, `triggers::turned_off::fields::behavior::description`, `triggers::turned_on::fields::behavior::description` och `triggers::operation_mode_changed::fields::behavior::description`: `Det beteende som ska trigga för valda varmvattenberedare.` → `Vilket beteende hos de valda varmvattenberedarna som ska utlösa automatiseringen.`
- `component::water_heater::common::condition_behavior_description`, `conditions::is_off::fields::behavior::description`, `conditions::is_on::fields::behavior::description`, `conditions::is_operation_mode::fields::behavior::description` och `conditions::is_target_temperature::fields::behavior::description`: `Hur tillståndet ska matcha valda varmvattenberedare.` → `Hur tillståndet för de valda varmvattenberedarna ska uppfylla villkoret.`
- `component::water_heater::conditions::is_target_temperature::description`: `Testar temperaturinställningen för en eller flera varmvattenberedare.` → `Kontrollerar måltemperaturen för en eller flera varmvattenberedare.`
- `component::water_heater::common::trigger_threshold_changed_description` och `triggers::target_temperature_changed::fields::threshold::description`: `Vilka ändringar som ska utlösa samt tröskelvärden.` → `Vilka ändringar som ska utlösa automatiseringen och vilka tröskelvärden som ska användas.`
- `component::water_heater::common::trigger_threshold_crossed_description` och `triggers::target_temperature_crossed_threshold::fields::threshold::description`: `Vilken tröskelövergång som ska utlösa samt tröskelvärden.` → `Vilken passage av tröskelvärdet som ska utlösa automatiseringen och vilka tröskelvärden som ska användas.`
- `component::water_heater::common::condition_threshold_description` och `conditions::is_target_temperature::fields::threshold::description`: `Vad man ska testa för och tröskelvärden.` → `Vad som ska kontrolleras och vilka tröskelvärden som ska användas.`
- `component::water_heater::triggers::operation_mode_changed::fields::operation_mode::description`: `De driftlägen att utlösa på.` → `De driftlägen som ska utlösa automatiseringen.`
- `component::water_heater::triggers::target_temperature_changed::fields::unit::description`: `Alla värden kommer att konverteras till denna enhet när triggern utvärderas.` → `Alla värden konverteras till denna enhet när utlösaren utvärderas.`
- `component::water_heater::selector::number_or_entity::choices::number`: `Nummer` → `Tal`.
- `component::water_heater::common::trigger_for_name`, `triggers::operation_mode_changed::fields::for::name`, `triggers::target_temperature_crossed_threshold::fields::for::name`, `triggers::turned_off::fields::for::name`, `triggers::turned_on::fields::for::name`, `common::condition_for_name`, `conditions::is_off::fields::for::name`, `conditions::is_on::fields::for::name`, `conditions::is_operation_mode::fields::for::name` och `conditions::is_target_temperature::fields::for::name`: `I åtminstone` → `I minst`.

## Verifiering

- API PUT följt av GET för var och en av 30 översättningar.
- TMX uppdaterad och validerad: 2 440 poster, 231 äldre poster med källnyckel och 2 209 Lokalise-ID-poster.
- Inga platshållare eller referensmarkörer ändrades.
