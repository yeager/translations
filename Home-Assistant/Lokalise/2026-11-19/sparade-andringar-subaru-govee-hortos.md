# Home Assistant Core: Subaru, Govee, Reolink och HortOS

Kontrollerat mot aktuell Lokalise-källa och sparat/återläst via API 2026-11-19. Samtliga 13 förslag från den [tidigare granskningsrapporten](../2026-11-19-granskning/granskning-13561-13680.md) matchade fortfarande den äldre svenska texten. Platshållarna `{probe_id}` och `{error}` bevarades.

## `component::subaru::entity::binary_sensor::mil_vdc::name`

**Engelska:** Vehicle dynamics control warning

**Tidigare svenska:** Varning för fordonsdynamik kontroll

**Sparad svenska:** Varning för stabilitetskontroll

## `component::subaru::entity::binary_sensor::mil_srs::name`

**Engelska:** Airbag warning

**Tidigare svenska:** Airbag-varning

**Sparad svenska:** Krockkuddevarning

## `component::subaru::entity::binary_sensor::mil_iss::name`

**Engelska:** Idle stop & start warning

**Tidigare svenska:** Varning för tomgångsstopp och start

**Sparad svenska:** Varning för start-stopp-systemet

## `component::subaru::entity::binary_sensor::mil_ess::name`

**Engelska:** EyeSight warning

**Tidigare svenska:** Varning för ögonsyn

**Sparad svenska:** Varning för EyeSight

## `component::subaru::entity::binary_sensor::ev_is_plugged_in::name`

**Engelska:** EV plug

**Tidigare svenska:** EV-uttag

**Sparad svenska:** Laddkontakt

## `component::teslemetry::entity::cover::tonneau::name`

**Engelska:** Tonneau

**Tidigare svenska:** Flaket

**Sparad svenska:** Flakskydd

## `component::govee_ble::entity::sensor::temperature_probe::name`

**Engelska:** Temperature probe {probe_id}

**Tidigare svenska:** Temperatur sond {probe_id}

**Sparad svenska:** Temperaturgivare {probe_id}

## `component::govee_ble::entity::sensor::temperature_alarm_probe::name`

**Engelska:** Temperature alarm probe {probe_id}

**Tidigare svenska:** Temperatur larm sond {probe_id}

**Sparad svenska:** Temperaturlarm för givare {probe_id}

## `component::govee_ble::entity::sensor::low_temperature_alarm_probe::name`

**Engelska:** Low temperature alarm probe {probe_id}

**Tidigare svenska:** Larm sond för låg temperatur {probe_id}

**Sparad svenska:** Larm för låg temperatur på givare {probe_id}

## `component::reolink::entity::select::anti_flicker::name`

**Engelska:** Anti-flicker

**Tidigare svenska:** Anti-flimmer

**Sparad svenska:** Flimmerreducering

## `component::hortimax::exceptions::no_devices::message`

**Engelska:** The HortOS API reported no controllers for this API key

**Tidigare svenska:** HortOS API rapporterade inga styrenheter för denna API-nyckel

**Sparad svenska:** HortOS-API:et rapporterade inga styrenheter för den här API-nyckeln

## `component::hortimax::exceptions::invalid_auth::message`

**Engelska:** The HortOS API rejected the API key

**Tidigare svenska:** HortOS API avvisade API-nyckeln

**Sparad svenska:** HortOS-API:et avvisade API-nyckeln

## `component::hortimax::exceptions::cannot_connect::message`

**Engelska:** Error talking to the HortOS API: {error}

**Tidigare svenska:** Fel vid kommunikation med HortOS API: {error}

**Sparad svenska:** Fel vid kommunikation med HortOS-API:et: {error}

