# Home Assistant Core: aerosmart styrning och larm

Sparat och separat återläst via Lokalises API 2026-11-19. Svenska fält var tomma och engelska källtexter stämde med [tidigare granskningsförslag](../2026-11-19-granskning/forslag-0121-0180.md). Tillverkarens [tekniska dokumentation](https://www.lebensraumholz.de/files/content/downloads/frischluftheizung-drexel-weiss-aerosmart-s.pdf) skiljer på uteluftens temperaturgivare och köldbärarkretsens givare. De tidigare markerade osäkra fallen 128, 143 och 149 återstår att kontrollera mer specifikt mot aktuell nyckel och enhet.

## `component::aerosmart::entity::binary_sensor::ventilation_anforderung_st3_ext::name`

**Engelska:** External fan level 3 request

**Tidigare svenska:** (tom)

**Sparad svenska:** Extern begäran om fläktnivå 3

## `component::aerosmart::entity::binary_sensor::utility_lockout_evu_vorhanden::name`

**Engelska:** Utility control installed

**Tidigare svenska:** (tom)

**Sparad svenska:** Elbolagsstyrning installerad

## `component::aerosmart::entity::binary_sensor::utility_lockout_evu_sperre_raumheizung_aktiv::name`

**Engelska:** Space heating utility lockout

**Tidigare svenska:** (tom)

**Sparad svenska:** Elbolagsspärr för rumsuppvärmning

## `component::aerosmart::entity::binary_sensor::utility_lockout_evu_sperre_elektroheizstab_aktiv::name`

**Engelska:** Electric heater utility lockout

**Tidigare svenska:** (tom)

**Sparad svenska:** Elbolagsspärr för elvärmare

## `component::aerosmart::entity::binary_sensor::utility_lockout_evu_sperre_brauchwasser_aktiv::name`

**Engelska:** Hot water utility lockout

**Tidigare svenska:** (tom)

**Sparad svenska:** Elbolagsspärr för varmvatten

## `component::aerosmart::entity::binary_sensor::summer_bypass_function_sommerautomatik::name`

**Engelska:** Summer bypass

**Tidigare svenska:** (tom)

**Sparad svenska:** Sommarbypass

## `component::aerosmart::entity::binary_sensor::summer_bypass_anforderung_sommerautomatik::name`

**Engelska:** Summer bypass request

**Tidigare svenska:** (tom)

**Sparad svenska:** Begäran om sommarbypass

## `component::aerosmart::entity::binary_sensor::room_temperature_timeout_temp_fuehler_raum::name`

**Engelska:** Room temperature sensor timeout

**Tidigare svenska:** (tom)

**Sparad svenska:** Tidsgränsen överskreds för rumstemperaturgivaren

## `component::aerosmart::entity::binary_sensor::room_temperature_timeout_soll_temp_raum::name`

**Engelska:** Room target temperature timeout

**Tidigare svenska:** (tom)

**Sparad svenska:** Tidsgränsen överskreds för rummets måltemperatur

## `component::aerosmart::entity::binary_sensor::hot_water_ventilation_anforderung_brauchwasserheizung_waermepumpe::name`

**Engelska:** Hot water heat pump request

**Tidigare svenska:** (tom)

**Sparad svenska:** Begäran om varmvatten från värmepumpen

## `component::aerosmart::entity::binary_sensor::hot_water_ventilation_anforderung_brauchwasserheizung_elektroheizstab::name`

**Engelska:** Hot water electric heater request

**Tidigare svenska:** (tom)

**Sparad svenska:** Begäran om varmvatten från elvärmaren

## `component::aerosmart::entity::binary_sensor::heat_pump_wp_relaiskontakt_ext::name`

**Engelska:** External heat pump relay contact

**Tidigare svenska:** (tom)

**Sparad svenska:** Extern reläkontakt för värmepumpen

## `component::aerosmart::entity::binary_sensor::heat_pump_wp_kontakt_evu::name`

**Engelska:** Utility contact

**Tidigare svenska:** (tom)

**Sparad svenska:** Elbolagskontakt

## `component::aerosmart::entity::binary_sensor::fans_anforderung_ventilatoren_durch_zonenregelung::name`

**Engelska:** Fan request from zone control

**Tidigare svenska:** (tom)

**Sparad svenska:** Fläktbegäran från zonstyrningen

## `component::aerosmart::entity::binary_sensor::fans_anforderung_ventilatoren_durch_waermepumpe::name`

**Engelska:** Fan request from heat pump

**Tidigare svenska:** (tom)

**Sparad svenska:** Fläktbegäran från värmepumpen

## `component::aerosmart::entity::binary_sensor::aggregate_fault_stoerung_summenstoerung2::name`

**Engelska:** Aggregate fault 2

**Tidigare svenska:** (tom)

**Sparad svenska:** Samlingsfel 2

## `component::aerosmart::entity::binary_sensor::aggregate_fault_stoerung_summenstoerung::name`

**Engelska:** Aggregate fault

**Tidigare svenska:** (tom)

**Sparad svenska:** Samlingsfel

