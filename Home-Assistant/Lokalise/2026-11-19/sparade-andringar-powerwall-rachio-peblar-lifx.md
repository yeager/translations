# Sparade svenska översättningar: Powerwall, Rachio, PeBlär, LIFX och systemmeddelanden

Datum: 2026-11-19

Alla poster nedan har sparats via Lokalise API och lästs tillbaka efter uppdateringen.

## Ändringar

### `component::powerwall::exceptions::api_changed::message`

- Engelska: The Powerwall API has changed
- Tidigare svenska: Powerwall API har ändrats
- Sparad svenska: Powerwall-API:t har ändrats

### `component::rachio::exceptions::authentication_failed::message`

- Engelska: Authentication with the Rachio API failed
- Tidigare svenska: Autentisering med Rachio API misslyckades
- Sparad svenska: Autentisering med Rachio-API:t misslyckades

### `component::mystrom::exceptions::unsupported_device_type::message`

- Engelska: Unsupported myStrom device type: {device_type}
- Tidigare svenska: Enhetstypen myStrom stöds inte: {device_type}
- Sparad svenska: Enhetstypen för myStrom stöds inte: {device_type}

### `component::luci::issues::legacy_known_devices::description`

- Engelska: OpenWrt (luci) now creates its own device tracker entities, but the following entries left over from the old YAML setup still exist in `{path}` for devices tracked by the router at `{host}`:

{devices}

Because these legacy trackers claim the same entity IDs, the new entities are dropped at startup and stop updating.

Please remove these entries from `{path}` and restart Home Assistant.
- Tidigare svenska: OpenWrt (luci) skapar nu egna enheter för enhetsspårning, men följande poster från den gamla YAML-konfigurationen finns fortfarande i `{path}` för enheter som spåras av routern på `{host}`:

{devices}

Eftersom dessa äldre spårare använder samma entitets-ID:n ignoreras de nya entiteterna vid start och slutar uppdateras.

Ta bort posterna från `{path}` och starta om Home Assistant.
- Sparad svenska: OpenWrt (luci) skapar nu egna entiteter för enhetsspårning, men följande poster från den gamla YAML-konfigurationen finns fortfarande i `{path}` för enheter som spåras av routern på `{host}`:

{devices}

Eftersom dessa äldre spårare använder samma entitets-ID:n ignoreras de nya entiteterna vid start och slutar uppdateras.

Ta bort posterna från `{path}` och starta om Home Assistant.

### `component::peblar::entity::switch::solar_charging_custom_always_charge::name`

- Engelska: Custom solar always charge
- Tidigare svenska: Ladda alltid med anpassad solenergi
- Sparad svenska: Anpassad solladdning: ladda alltid

### `component::peblar::entity::number::solar_charging_custom_power_target::name`

- Engelska: Custom solar grid target
- Tidigare svenska: Anpassat målvärde för solnät
- Sparad svenska: Anpassat målvärde för elnätet vid solladdning

### `component::keyboard_remote::options::step::init::data_description::emulate_key_hold_delay`

- Engelska: Delay before key hold emulation starts.
- Tidigare svenska: Fördröjning före emulering av nedtryckt tangent startar.
- Sparad svenska: Fördröjning innan emulering av nedtryckt tangent startar.

### `component::rainbird::entity::sensor::program_next_run::name`

- Engelska: {program} next run
- Tidigare svenska: {program} nästa körning
- Sparad svenska: Nästa körning för {program}

### `component::melcloud::exceptions::rate_limit_exceeded::message`

- Engelska: MELCloud rate limit exceeded. Your account may be temporarily blocked.
- Tidigare svenska: MELClouds hastighetsgräns har överskridits. Ditt konto kan vara tillfälligt blockerat.
- Sparad svenska: Gränsen för antalet MELCloud-anrop har överskridits. Ditt konto kan vara tillfälligt blockerat.

### `component::lifx::services::effect_sky::fields::duration::description`

- Engelska: How long the effect runs. 0 runs it until it is stopped.
- Tidigare svenska: Hur länge effekten körs. 0 kör den tills den stoppas.
- Sparad svenska: Hur länge effekten körs. Med 0 körs den tills den stoppas.

### `component::lifx::services::effect_colorsweep::fields::speed::description`

- Engelska: How long one sweep takes. 0 sweeps once across the duration, which then has to be set.
- Tidigare svenska: Hur lång tid ett svep tar. 0 sveper en gång under varaktigheten, som då måste anges.
- Sparad svenska: Hur lång tid ett svep tar. Med 0 sker ett svep under den angivna varaktigheten, som då måste anges.

### `component::lifx::services::effect_colorsweep::fields::duration::description`

- Engelska: How long the effect runs. 0 runs it until it is stopped.
- Tidigare svenska: Hur länge effekten körs. 0 kör den tills den stoppas.
- Sparad svenska: Hur länge effekten körs. Med 0 körs den tills den stoppas.

### `component::logger::issues::renamed_loggers::description`

- Engelska: Home Assistant now uses httpx2 instead of httpx. The `logger` configuration in your `configuration.yaml` file sets a level or filter for loggers that no longer receive log messages:

{loggers}

Rename them as shown in your `logger` configuration and restart Home Assistant to fix this issue.
- Tidigare svenska: Home Assistant använder nu httpx2 i stället för httpx. Konfigurationen för `logger` i din `configuration.yaml` anger en nivå eller ett filter för loggare som inte längre tar emot loggmeddelanden:

{loggers}

Byt namn på dem enligt din `logger`-konfiguration och starta om Home Assistant för att lösa problemet.
- Sparad svenska: Home Assistant använder nu httpx2 i stället för httpx. Konfigurationen för `logger` i din `configuration.yaml` anger en nivå eller ett filter för loggare som inte längre tar emot loggmeddelanden:

{loggers}

Byt namn på dem enligt anvisningarna i din `logger`-konfiguration och starta om Home Assistant för att lösa problemet.
