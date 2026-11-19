# Home Assistant Core: aerosmart tekniska termer

Sparat och separat återläst via Lokalises API 2026-11-19. Svenska fält var tomma. Dessa tre tidigare osäkra förslag har omformulerats efter kontroll av [aerosmart-dokumentation för köldbärarkrets](https://www.lebensraumholz.de/files/content/downloads/frischluftheizung-drexel-weiss-aerosmart-s.pdf) och [tillverkarens Modbus-registerbeskrivning](https://www.loxforum.com/filedata/fetch?id=148267), som anger begäran om obalans vid övertemperatur i beredaren. Formuleringen om en deltagare i styrsystemet följer källtextens ospecificerade deltagare.

## `component::aerosmart::entity::binary_sensor::ventilation_stoerung_teilnehmer_nicht_erreichbar::name`

**Engelska:** Controller participant unreachable

**Tidigare svenska:** (tom)

**Sparad svenska:** Det går inte att nå en deltagare i styrsystemet

## `component::aerosmart::entity::binary_sensor::outside_temperature_stoerung_temperaturfuehler_sole_aussenluft::name`

**Engelska:** Outdoor brine temperature sensor fault

**Tidigare svenska:** (tom)

**Sparad svenska:** Fel på temperaturgivaren för uteluftens köldbärarkrets

## `component::aerosmart::entity::binary_sensor::hot_water_ventilation_anforderung_disbalance_boilerueberwaermung::name`

**Engelska:** Boiler overheating imbalance request

**Tidigare svenska:** (tom)

**Sparad svenska:** Begäran om obalans vid överhettning av varmvattenberedaren

