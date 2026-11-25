# Home Assistant Core: tidigare tomma svenska mål 1–120

- Granskade och sparade: **120/120**. Alla nycklar hade aktuell källmatchning vid granskningen.
- Källrevision: `86a2eabe7e43f526db5821ef068087ce8404ae07`.
- Alla 120 mål skrevs via Lokalise API och verifierades med färsk GET.
- 28 unika levande referensmål kontrollerades. Fem strängar hade totalt sex referensavvikelser; de korrigerades/synkroniserades och återlästes.
- Home Assistant-TMX: **17 247 poster**, validerad.
- `svlang skrivregler`: inga fel. Hunspell flaggade främst kompassförkortningar (`NNO`, `NNV`, `OSO`, `SSO`, `SSV`, `SV`, `VNV`, `VSV`), AEMET/OpenData/Azure/BenQ/DVI-D och vissa ord med produktnamn eller platshållaren `name`; manuellt bedömda som egennamn, tekniska termer, giltiga riktningsförkortningar eller platshållare.
- Fullständiga källor, slutvärden och status per nyckel finns i `../Lokalise/2026-11-25-reviewed-empty-targets-001-120.json`.
- Levande referenssvar sparades i `../Lokalise/2026-11-25-reference-targets-empty-001-120-live.json`; rättelser finns i `../Lokalise/2026-11-25-empty-target-reference-corrections.json`.

## Radgranskning

### `component::abrp::entity::sensor::battery_temperature_max::name`
- Källa: Maximum battery temperature
- Föreslagen och sparad svenska: Högsta batteritemperatur
- Motivering: Vehicle telemetry context: battery/cabin/ambient temperature, HVAC load and gear selector states.
- Lokalise-status: sparad och återläst.

### `component::abrp::entity::sensor::battery_temperature_min::name`
- Källa: Minimum battery temperature
- Föreslagen och sparad svenska: Lägsta batteritemperatur
- Motivering: Vehicle telemetry context: battery/cabin/ambient temperature, HVAC load and gear selector states.
- Lokalise-status: sparad och återläst.

### `component::abrp::entity::sensor::cabin_temperature::name`
- Källa: Cabin temperature
- Föreslagen och sparad svenska: Kupétemperatur
- Motivering: Vehicle telemetry context: battery/cabin/ambient temperature, HVAC load and gear selector states.
- Lokalise-status: sparad och återläst.

### `component::abrp::entity::sensor::driving_state::name`
- Källa: Driving state
- Föreslagen och sparad svenska: Växelläge
- Motivering: Vehicle telemetry context: battery/cabin/ambient temperature, HVAC load and gear selector states.
- Lokalise-status: sparad och återläst.

### `component::abrp::entity::sensor::driving_state::state::drive`
- Källa: Drive
- Föreslagen och sparad svenska: Körläge
- Motivering: Vehicle telemetry context: battery/cabin/ambient temperature, HVAC load and gear selector states.
- Lokalise-status: sparad och återläst.

### `component::abrp::entity::sensor::driving_state::state::neutral`
- Källa: Neutral
- Föreslagen och sparad svenska: Friläge
- Motivering: Vehicle telemetry context: battery/cabin/ambient temperature, HVAC load and gear selector states.
- Lokalise-status: sparad och återläst.

### `component::abrp::entity::sensor::driving_state::state::park`
- Källa: Park
- Föreslagen och sparad svenska: Parkering
- Motivering: Vehicle telemetry context: battery/cabin/ambient temperature, HVAC load and gear selector states.
- Lokalise-status: sparad och återläst.

### `component::abrp::entity::sensor::driving_state::state::reverse`
- Källa: Reverse
- Föreslagen och sparad svenska: Backläge
- Motivering: Vehicle telemetry context: battery/cabin/ambient temperature, HVAC load and gear selector states.
- Lokalise-status: sparad och återläst.

### `component::abrp::entity::sensor::external_temperature::name`
- Källa: External temperature
- Föreslagen och sparad svenska: Utomhustemperatur
- Motivering: Vehicle telemetry context: battery/cabin/ambient temperature, HVAC load and gear selector states.
- Lokalise-status: sparad och återläst.

### `component::abrp::entity::sensor::hvac_power::name`
- Källa: HVAC power
- Föreslagen och sparad svenska: Klimatanläggningens effekt
- Motivering: Vehicle telemetry context: battery/cabin/ambient temperature, HVAC load and gear selector states.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::precipitation::state_attributes::type::name`
- Källa: Precipitation type
- Föreslagen och sparad svenska: Nederbördstyp
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::precipitation::state_attributes::type::state::ice`
- Källa: Ice
- Föreslagen och sparad svenska: Is
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::precipitation::state_attributes::type::state::mixed`
- Källa: Mixed
- Föreslagen och sparad svenska: Blandat
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::precipitation::state_attributes::type::state::rain`
- Källa: Rain
- Föreslagen och sparad svenska: Regn
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::precipitation::state_attributes::type::state::snow`
- Källa: Snow
- Föreslagen och sparad svenska: Snö
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_day::state_attributes::direction::name`
- Källa: Direction
- Föreslagen och sparad svenska: Vindriktning
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_day::state_attributes::direction::state::e`
- Källa: E
- Föreslagen och sparad svenska: O
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_day::state_attributes::direction::state::ene`
- Källa: ENE
- Föreslagen och sparad svenska: ONO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_day::state_attributes::direction::state::ese`
- Källa: ESE
- Föreslagen och sparad svenska: OSO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_day::state_attributes::direction::state::n`
- Källa: N
- Föreslagen och sparad svenska: N
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_day::state_attributes::direction::state::ne`
- Källa: NE
- Föreslagen och sparad svenska: NO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_day::state_attributes::direction::state::nne`
- Källa: NNE
- Föreslagen och sparad svenska: NNO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_day::state_attributes::direction::state::nnw`
- Källa: NNW
- Föreslagen och sparad svenska: NNV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_day::state_attributes::direction::state::nw`
- Källa: NW
- Föreslagen och sparad svenska: NV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_day::state_attributes::direction::state::s`
- Källa: S
- Föreslagen och sparad svenska: S
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_day::state_attributes::direction::state::se`
- Källa: SE
- Föreslagen och sparad svenska: SO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_day::state_attributes::direction::state::sse`
- Källa: SSE
- Föreslagen och sparad svenska: SSO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_day::state_attributes::direction::state::ssw`
- Källa: SSW
- Föreslagen och sparad svenska: SSV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_day::state_attributes::direction::state::sw`
- Källa: SW
- Föreslagen och sparad svenska: SV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_day::state_attributes::direction::state::w`
- Källa: W
- Föreslagen och sparad svenska: V
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_day::state_attributes::direction::state::wnw`
- Källa: WNW
- Föreslagen och sparad svenska: VNV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_day::state_attributes::direction::state::wsw`
- Källa: WSW
- Föreslagen och sparad svenska: VSV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_night::state_attributes::direction::name`
- Källa: Direction
- Föreslagen och sparad svenska: Vindriktning
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_night::state_attributes::direction::state::e`
- Källa: E
- Föreslagen och sparad svenska: O
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_night::state_attributes::direction::state::ene`
- Källa: ENE
- Föreslagen och sparad svenska: ONO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_night::state_attributes::direction::state::ese`
- Källa: ESE
- Föreslagen och sparad svenska: OSO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_night::state_attributes::direction::state::n`
- Källa: N
- Föreslagen och sparad svenska: N
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_night::state_attributes::direction::state::ne`
- Källa: NE
- Föreslagen och sparad svenska: NO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_night::state_attributes::direction::state::nne`
- Källa: NNE
- Föreslagen och sparad svenska: NNO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_night::state_attributes::direction::state::nnw`
- Källa: NNW
- Föreslagen och sparad svenska: NNV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_night::state_attributes::direction::state::nw`
- Källa: NW
- Föreslagen och sparad svenska: NV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_night::state_attributes::direction::state::s`
- Källa: S
- Föreslagen och sparad svenska: S
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_night::state_attributes::direction::state::se`
- Källa: SE
- Föreslagen och sparad svenska: SO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_night::state_attributes::direction::state::sse`
- Källa: SSE
- Föreslagen och sparad svenska: SSO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_night::state_attributes::direction::state::ssw`
- Källa: SSW
- Föreslagen och sparad svenska: SSV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_night::state_attributes::direction::state::sw`
- Källa: SW
- Föreslagen och sparad svenska: SV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_night::state_attributes::direction::state::w`
- Källa: W
- Föreslagen och sparad svenska: V
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_night::state_attributes::direction::state::wnw`
- Källa: WNW
- Föreslagen och sparad svenska: VNV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_gust_speed_night::state_attributes::direction::state::wsw`
- Källa: WSW
- Föreslagen och sparad svenska: VSV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_day::state_attributes::direction::name`
- Källa: Direction
- Föreslagen och sparad svenska: Vindriktning
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_day::state_attributes::direction::state::e`
- Källa: E
- Föreslagen och sparad svenska: O
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_day::state_attributes::direction::state::ene`
- Källa: ENE
- Föreslagen och sparad svenska: ONO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_day::state_attributes::direction::state::ese`
- Källa: ESE
- Föreslagen och sparad svenska: OSO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_day::state_attributes::direction::state::n`
- Källa: N
- Föreslagen och sparad svenska: N
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_day::state_attributes::direction::state::ne`
- Källa: NE
- Föreslagen och sparad svenska: NO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_day::state_attributes::direction::state::nne`
- Källa: NNE
- Föreslagen och sparad svenska: NNO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_day::state_attributes::direction::state::nnw`
- Källa: NNW
- Föreslagen och sparad svenska: NNV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_day::state_attributes::direction::state::nw`
- Källa: NW
- Föreslagen och sparad svenska: NV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_day::state_attributes::direction::state::s`
- Källa: S
- Föreslagen och sparad svenska: S
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_day::state_attributes::direction::state::se`
- Källa: SE
- Föreslagen och sparad svenska: SO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_day::state_attributes::direction::state::sse`
- Källa: SSE
- Föreslagen och sparad svenska: SSO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_day::state_attributes::direction::state::ssw`
- Källa: SSW
- Föreslagen och sparad svenska: SSV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_day::state_attributes::direction::state::sw`
- Källa: SW
- Föreslagen och sparad svenska: SV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_day::state_attributes::direction::state::w`
- Källa: W
- Föreslagen och sparad svenska: V
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_day::state_attributes::direction::state::wnw`
- Källa: WNW
- Föreslagen och sparad svenska: VNV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_day::state_attributes::direction::state::wsw`
- Källa: WSW
- Föreslagen och sparad svenska: VSV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_night::state_attributes::direction::name`
- Källa: Direction
- Föreslagen och sparad svenska: Vindriktning
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_night::state_attributes::direction::state::e`
- Källa: E
- Föreslagen och sparad svenska: O
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_night::state_attributes::direction::state::ene`
- Källa: ENE
- Föreslagen och sparad svenska: ONO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_night::state_attributes::direction::state::ese`
- Källa: ESE
- Föreslagen och sparad svenska: OSO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_night::state_attributes::direction::state::n`
- Källa: N
- Föreslagen och sparad svenska: N
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_night::state_attributes::direction::state::ne`
- Källa: NE
- Föreslagen och sparad svenska: NO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_night::state_attributes::direction::state::nne`
- Källa: NNE
- Föreslagen och sparad svenska: NNO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_night::state_attributes::direction::state::nnw`
- Källa: NNW
- Föreslagen och sparad svenska: NNV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_night::state_attributes::direction::state::nw`
- Källa: NW
- Föreslagen och sparad svenska: NV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_night::state_attributes::direction::state::s`
- Källa: S
- Föreslagen och sparad svenska: S
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_night::state_attributes::direction::state::se`
- Källa: SE
- Föreslagen och sparad svenska: SO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_night::state_attributes::direction::state::sse`
- Källa: SSE
- Föreslagen och sparad svenska: SSO
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_night::state_attributes::direction::state::ssw`
- Källa: SSW
- Föreslagen och sparad svenska: SSV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_night::state_attributes::direction::state::sw`
- Källa: SW
- Föreslagen och sparad svenska: SV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_night::state_attributes::direction::state::w`
- Källa: W
- Föreslagen och sparad svenska: V
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_night::state_attributes::direction::state::wnw`
- Källa: WNW
- Föreslagen och sparad svenska: VNV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::accuweather::entity::sensor::wind_speed_night::state_attributes::direction::state::wsw`
- Källa: WSW
- Föreslagen och sparad svenska: VSV
- Motivering: Weather forecast enum. AccuWeather Swedish UI uses Is/Blandat; English compass points converted to Swedish nautical abbreviations. Referenced night values use identical day targets.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::aemet::config::error::town_not_found`
- Källa: No AEMET town found near this location. AEMET OpenData only covers Spain.
- Föreslagen och sparad svenska: Ingen AEMET-ort hittades i närheten av den här platsen. AEMET OpenData omfattar endast Spanien.
- Motivering: Spanish AEMET OpenData setup and weather forecast context.
- Lokalise-status: sparad och återläst.

### `component::aemet::config::step::reauth_confirm::data_description::api_key`
- Källa: The API key from your AEMET OpenData account. It is free, but you need to register to get one.
- Föreslagen och sparad svenska: API-nyckeln från ditt AEMET OpenData-konto. Den är gratis, men du måste registrera dig för att få en.
- Motivering: Spanish AEMET OpenData setup and weather forecast context.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::aemet::config::step::reconfigure::data_description::api_key`
- Källa: The API key from your AEMET OpenData account. It is free, but you need to register to get one.
- Föreslagen och sparad svenska: API-nyckeln från ditt AEMET OpenData-konto. Den är gratis, men du måste registrera dig för att få en.
- Motivering: Spanish AEMET OpenData setup and weather forecast context.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::aemet::config::step::user::data_description::api_key`
- Källa: The API key from your AEMET OpenData account. It is free, but you need to register to get one.
- Föreslagen och sparad svenska: API-nyckeln från ditt AEMET OpenData-konto. Den är gratis, men du måste registrera dig för att få en.
- Motivering: Spanish AEMET OpenData setup and weather forecast context.
- Lokalise-status: sparad och återläst.

### `component::aemet::config::step::user::data_description::location`
- Källa: The location used for the weather forecast and sensors. AEMET OpenData only covers Spain.
- Föreslagen och sparad svenska: Platsen som används för väderprognosen och sensorerna. AEMET OpenData omfattar endast Spanien.
- Motivering: Spanish AEMET OpenData setup and weather forecast context.
- Lokalise-status: sparad och återläst.

### `component::aemet::options::step::init::data_description::radar_updates`
- Källa: Download the AEMET weather radar image and create an image entity for it.
- Föreslagen och sparad svenska: Hämta AEMET:s väderradarbild och skapa en bildentitet för den.
- Motivering: Spanish AEMET OpenData setup and weather forecast context.
- Lokalise-status: sparad och återläst.

### `component::aemet::options::step::init::data_description::station_updates`
- Källa: Get current observations from the nearest AEMET weather station, in addition to the town forecast.
- Föreslagen och sparad svenska: Hämta aktuella observationer från närmaste AEMET-väderstation utöver ortsprognosen.
- Motivering: Spanish AEMET OpenData setup and weather forecast context.
- Lokalise-status: sparad och återläst.

### `component::anova::config::step::reauth_confirm::data::password`
- Källa: Password
- Föreslagen och sparad svenska: Lösenord
- Motivering: Bedömd mot aktuell Home Assistant Core-komponent och funktion.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::anova::config::step::reauth_confirm::data_description::password`
- Källa: The password of your Anova account.
- Föreslagen och sparad svenska: Lösenordet för ditt Anova-konto.
- Motivering: Bedömd mot aktuell Home Assistant Core-komponent och funktion.
- Lokalise-status: sparad och återläst.

### `component::anova::config::step::reauth_confirm::description`
- Källa: The password for {username} is no longer valid. Enter the current password.
- Föreslagen och sparad svenska: Lösenordet för {username} är inte längre giltigt. Ange det aktuella lösenordet.
- Motivering: Bedömd mot aktuell Home Assistant Core-komponent och funktion.
- Lokalise-status: sparad och återläst.

### `component::anova::config::step::reauth_confirm::title`
- Källa: Authentication expired for {name}
- Föreslagen och sparad svenska: Autentiseringen har upphört att gälla för {name}
- Motivering: Exact shared reauthentication title; follows common::config_flow::title::reauth.
- Referens: Live referenced target fetched and synchronized.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::azure_data_explorer::config::step::reauth_confirm::data::authority_id`
- Källa: Authority ID
- Föreslagen och sparad svenska: Klientorganisations-ID
- Motivering: Azure source description identifies this as the directory/tenant ID; synchronize with the shared target.
- Referens: Live referenced target fetched and synchronized.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::azure_data_explorer::config::step::reauth_confirm::data::client_id`
- Källa: Client ID
- Föreslagen och sparad svenska: Klient-ID
- Motivering: Microsoft identity terminology; Authority ID is identified by source description as directory/tenant ID.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::azure_data_explorer::config::step::reauth_confirm::data::client_secret`
- Källa: Client secret
- Föreslagen och sparad svenska: Klienthemlighet
- Motivering: Microsoft identity terminology; Authority ID is identified by source description as directory/tenant ID.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::azure_data_explorer::config::step::reauth_confirm::data_description::authority_id`
- Källa: In Azure portal this is also known as Directory (tenant) ID
- Föreslagen och sparad svenska: I Azure-portalen kallas detta även för katalog-ID (klientorganisations-ID)
- Motivering: Synchronize the exact duplicate with the referenced Azure description; adds idiomatic “för” and follows source punctuation.
- Referens: Live referenced target fetched and synchronized.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::azure_data_explorer::config::step::reauth_confirm::description`
- Källa: The app registration credentials for Azure Data Explorer are no longer valid. Enter new credentials.
- Föreslagen och sparad svenska: Autentiseringsuppgifterna för appregistreringen i Azure Data Explorer är inte längre giltiga. Ange nya autentiseringsuppgifter.
- Motivering: Microsoft identity terminology; Authority ID is identified by source description as directory/tenant ID.
- Lokalise-status: sparad och återläst.

### `component::azure_data_explorer::config::step::reauth_confirm::title`
- Källa: Authentication expired for {name}
- Föreslagen och sparad svenska: Autentiseringen har upphört att gälla för {name}
- Motivering: Exact shared reauthentication title; follows common::config_flow::title::reauth.
- Referens: Live referenced target fetched and synchronized.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::benq_projector_infrared::config::abort::already_configured`
- Källa: A BenQ projector has already been configured with this infrared emitter.
- Föreslagen och sparad svenska: En BenQ-projektor har redan konfigurerats med den här infraröda sändaren.
- Motivering: Infrared projector setup and projector input-source context; standard source acronyms and port names preserved.
- Lokalise-status: sparad och återläst.

### `component::benq_projector_infrared::config::abort::no_infrared_emitters`
- Källa: No infrared emitter entities found. Please set up an infrared device first.
- Föreslagen och sparad svenska: Inga entiteter för infraröda sändare hittades. Konfigurera först en infraröd enhet.
- Motivering: Infrared projector setup and projector input-source context; standard source acronyms and port names preserved.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::benq_projector_infrared::config::step::user::data::infrared_entity_id`
- Källa: Infrared emitter
- Föreslagen och sparad svenska: Infraröd sändare
- Motivering: Infrared projector setup and projector input-source context; standard source acronyms and port names preserved.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::benq_projector_infrared::config::step::user::data::infrared_receiver_entity_id`
- Källa: Infrared receiver
- Föreslagen och sparad svenska: Infraröd mottagare
- Motivering: Infrared projector setup and projector input-source context; standard source acronyms and port names preserved.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::benq_projector_infrared::config::step::user::data_description::infrared_entity_id`
- Källa: The infrared emitter entity to use for sending commands.
- Föreslagen och sparad svenska: Sändarentiteten som ska användas för att skicka infraröda kommandon.
- Motivering: Synchronize with the exact shared infrared entity description.
- Referens: Live referenced target fetched and synchronized.
- Referensmål hämtat från Lokalise live och jämfört/synkroniserat.
- Lokalise-status: sparad och återläst.

### `component::benq_projector_infrared::config::step::user::data_description::infrared_receiver_entity_id`
- Källa: Optional. Keeps the state up to date when the projector's own remote is used.
- Föreslagen och sparad svenska: Valfritt. Håller statusen uppdaterad när projektorns egen fjärrkontroll används.
- Motivering: Infrared projector setup and projector input-source context; standard source acronyms and port names preserved.
- Lokalise-status: sparad och återläst.

### `component::benq_projector_infrared::config::step::user::description`
- Källa: Select the infrared emitter to use for controlling your BenQ projector. Optionally select a receiver to follow commands sent by the projector's own remote.
- Föreslagen och sparad svenska: Välj den infraröda sändare som ska användas för att styra BenQ-projektorn. Du kan även välja en mottagare som håller statusen uppdaterad när projektorns egen fjärrkontroll används.
- Motivering: Infrared projector setup and projector input-source context; standard source acronyms and port names preserved.
- Lokalise-status: sparad och återläst.

### `component::benq_projector_infrared::config::step::user::title`
- Källa: Set up BenQ projector
- Föreslagen och sparad svenska: Konfigurera BenQ-projektor
- Motivering: Infrared projector setup and projector input-source context; standard source acronyms and port names preserved.
- Lokalise-status: sparad och återläst.

### `component::benq_projector_infrared::entity::media_player::projector::state_attributes::source::state::component_1`
- Källa: Component 1
- Föreslagen och sparad svenska: Komponent 1
- Motivering: Infrared projector setup and projector input-source context; standard source acronyms and port names preserved.
- Lokalise-status: sparad och återläst.

### `component::benq_projector_infrared::entity::media_player::projector::state_attributes::source::state::component_2`
- Källa: Component 2
- Föreslagen och sparad svenska: Komponent 2
- Motivering: Infrared projector setup and projector input-source context; standard source acronyms and port names preserved.
- Lokalise-status: sparad och återläst.

### `component::benq_projector_infrared::entity::media_player::projector::state_attributes::source::state::dvi_d`
- Källa: DVI-D
- Föreslagen och sparad svenska: DVI-D
- Motivering: Infrared projector setup and projector input-source context; standard source acronyms and port names preserved.
- Lokalise-status: sparad och återläst.

### `component::benq_projector_infrared::entity::media_player::projector::state_attributes::source::state::hdmi_1`
- Källa: HDMI 1
- Föreslagen och sparad svenska: HDMI 1
- Motivering: Infrared projector setup and projector input-source context; standard source acronyms and port names preserved.
- Lokalise-status: sparad och återläst.

### `component::benq_projector_infrared::entity::media_player::projector::state_attributes::source::state::hdmi_2`
- Källa: HDMI 2
- Föreslagen och sparad svenska: HDMI 2
- Motivering: Infrared projector setup and projector input-source context; standard source acronyms and port names preserved.
- Lokalise-status: sparad och återläst.

### `component::benq_projector_infrared::entity::media_player::projector::state_attributes::source::state::pc_1`
- Källa: PC 1
- Föreslagen och sparad svenska: PC 1
- Motivering: Infrared projector setup and projector input-source context; standard source acronyms and port names preserved.
- Lokalise-status: sparad och återläst.

### `component::benq_projector_infrared::entity::media_player::projector::state_attributes::source::state::pc_2`
- Källa: PC 2
- Föreslagen och sparad svenska: PC 2
- Motivering: Infrared projector setup and projector input-source context; standard source acronyms and port names preserved.
- Lokalise-status: sparad och återläst.

### `component::benq_projector_infrared::entity::media_player::projector::state_attributes::source::state::s_video_1`
- Källa: S-Video 1
- Föreslagen och sparad svenska: S-Video 1
- Motivering: Infrared projector setup and projector input-source context; standard source acronyms and port names preserved.
- Lokalise-status: sparad och återläst.

### `component::benq_projector_infrared::entity::media_player::projector::state_attributes::source::state::s_video_2`
- Källa: S-Video 2
- Föreslagen och sparad svenska: S-Video 2
- Motivering: Infrared projector setup and projector input-source context; standard source acronyms and port names preserved.
- Lokalise-status: sparad och återläst.

### `component::benq_projector_infrared::entity::media_player::projector::state_attributes::source::state::usb_reader`
- Källa: USB reader
- Föreslagen och sparad svenska: USB-läsare
- Motivering: Infrared projector setup and projector input-source context; standard source acronyms and port names preserved.
- Lokalise-status: sparad och återläst.

### `component::benq_projector_infrared::entity::media_player::projector::state_attributes::source::state::video_1`
- Källa: Video 1
- Föreslagen och sparad svenska: Video 1
- Motivering: Infrared projector setup and projector input-source context; standard source acronyms and port names preserved.
- Lokalise-status: sparad och återläst.

### `component::benq_projector_infrared::entity::media_player::projector::state_attributes::source::state::video_2`
- Källa: Video 2
- Föreslagen och sparad svenska: Video 2
- Motivering: Infrared projector setup and projector input-source context; standard source acronyms and port names preserved.
- Lokalise-status: sparad och återläst.

## Referenskorrigeringar

- `component::anova::config::step::reauth_confirm::title` → **Autentiseringen har upphört att gälla för {name}** — Exact shared reauthentication title; follows common::config_flow::title::reauth. Status: sparad i Lokalise och återläst.
- `component::azure_data_explorer::config::step::reauth_confirm::title` → **Autentiseringen har upphört att gälla för {name}** — Exact shared reauthentication title; follows common::config_flow::title::reauth. Status: sparad i Lokalise och återläst.
- `component::azure_data_explorer::config::step::user::data::authority_id` → **Klientorganisations-ID** — Azure source description identifies this as the directory/tenant ID; synchronize the shared target and its reauthentication reference. Status: sparad i Lokalise och återläst.
- `component::azure_data_explorer::config::step::reauth_confirm::data::authority_id` → **Klientorganisations-ID** — Azure source description identifies this as the directory/tenant ID; synchronize with the shared target. Status: sparad i Lokalise och återläst.
- `component::azure_data_explorer::config::step::reauth_confirm::data_description::authority_id` → **I Azure-portalen kallas detta även för katalog-ID (klientorganisations-ID)** — Synchronize the exact duplicate with the referenced Azure description; adds idiomatic “för” and follows source punctuation. Status: sparad i Lokalise och återläst.
- `component::benq_projector_infrared::config::step::user::data_description::infrared_entity_id` → **Sändarentiteten som ska användas för att skicka infraröda kommandon.** — Synchronize with the exact shared infrared entity description. Status: sparad i Lokalise och återläst.

## Kvarvarande arbete

HA Core-granskningen fortsätter. Aktuell inventering: 521 befintliga Lokalise-nycklar med tom svenska och 203 aktuella Core-nycklar som saknas i Lokalise. Ingen fullständighetsbedömning görs ännu.
