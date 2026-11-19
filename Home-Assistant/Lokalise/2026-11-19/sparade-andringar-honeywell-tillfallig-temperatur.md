# Home Assistant Core: Honeywell tillfällig temperatur

Sparat och separat återläst via Lokalises API 2026-11-19. Samtliga svenska fält var tomma och engelska källtexter stämde med [tidigare granskningsförslag](../2026-11-19-granskning/forslag-0181-0240.md). Variablerna för läge och temperaturintervall bevarades.

## `component::honeywell::services::set_hold_until::name`

**Engelska:** Set hold until

**Tidigare svenska:** (tom)

**Sparad svenska:** Ställ in tillfällig temperatur till och med

## `component::honeywell::services::set_hold_until::fields::until::name`

**Engelska:** Until

**Tidigare svenska:** (tom)

**Sparad svenska:** Till och med

## `component::honeywell::services::set_hold_until::fields::until::description`

**Engelska:** Time of day on the thermostat's clock at which the hold ends. Must be on a quarter hour.

**Tidigare svenska:** (tom)

**Sparad svenska:** Klockslaget enligt termostatens klocka då den tillfälliga inställningen upphör. Måste anges i hela kvartar.

## `component::honeywell::services::set_hold_until::fields::temperature::name`

**Engelska:** Temperature

**Tidigare svenska:** (tom)

**Sparad svenska:** Temperatur

## `component::honeywell::services::set_hold_until::fields::temperature::description`

**Engelska:** Target temperature during the hold. If omitted, the current target temperature is kept. Cannot be used while the system mode is auto.

**Tidigare svenska:** (tom)

**Sparad svenska:** Måltemperatur under den tillfälliga inställningen. Om den utelämnas behålls den aktuella måltemperaturen. Kan inte användas när systemet är i automatiskt läge.

## `component::honeywell::services::set_hold_until::description`

**Engelska:** Sets a temporary hold that ends at a given time.

**Tidigare svenska:** (tom)

**Sparad svenska:** Ställer in en tillfällig temperatur som gäller till ett angivet klockslag.

## `component::honeywell::exceptions::set_hold_until_failed::message`

**Engelska:** Honeywell could not set temporary hold

**Tidigare svenska:** (tom)

**Sparad svenska:** Honeywell kunde inte ställa in den tillfälliga temperaturen

## `component::honeywell::exceptions::hold_until_temperature_mode::message`

**Engelska:** Honeywell cannot set a temporary hold temperature while the system mode is {mode}

**Tidigare svenska:** (tom)

**Sparad svenska:** Honeywell kan inte ställa in en tillfällig temperatur när systemläget är {mode}

## `component::honeywell::exceptions::hold_until_invalid_time::message`

**Engelska:** Honeywell temporary hold must end on a quarter hour

**Tidigare svenska:** (tom)

**Sparad svenska:** Den tillfälliga temperaturinställningen i Honeywell måste upphöra vid en hel kvart

## `component::honeywell::exceptions::hold_until_invalid_temperature::message`

**Engelska:** Honeywell temporary hold temperature {temperature} is not valid. Accepted range is {min_temp} to {max_temp}.

**Tidigare svenska:** (tom)

**Sparad svenska:** Den tillfälliga temperaturen {temperature} i Honeywell är ogiltig. Tillåtet intervall är {min_temp} till {max_temp}.

## `component::honeywell::exceptions::hold_until_invalid_mode::message`

**Engelska:** Honeywell cannot set a temporary hold while the system mode is {mode}

**Tidigare svenska:** (tom)

**Sparad svenska:** Honeywell kan inte ställa in en tillfällig temperatur när systemläget är {mode}

