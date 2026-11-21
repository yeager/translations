# Home Assistant Core — Shelly: kompletterade svenska mål

Datum: 2026-11-21  
Plattform: Lokalise API  
Språk: `sv`

## Sparade och återlästa ändringar

| Fullständig nyckel | Engelska | Sparad svenska |
| --- | --- | --- |
| `component::shelly::exceptions::command_http_error::message` | Command {command} failed for {device} with HTTP status {status} | Kommandot {command} misslyckades för {device} med HTTP-status {status} |
| `component::shelly::exceptions::command_invalid_params::message` | Command parameters for {device} must be text, number or boolean values | Kommandoparametrarna för {device} måste vara text-, tal- eller booleska värden |
| `component::shelly::exceptions::command_not_allowed::message` | Command {command} is not allowed for {device} | Kommandot {command} är inte tillåtet för {device} |
| `component::shelly::exceptions::command_rpc_error::message` | Command {command} failed for {device} with error {code}: {message} | Kommandot {command} misslyckades för {device} med felet {code}: {message} |
| `component::shelly::exceptions::command_sleeping_device::message` | {device} is a sleeping device and does not support commands | {device} är en sovande enhet och har inte stöd för kommandon |
| `component::shelly::services::command::description` | Sends a command to a Shelly device and returns the device response. | Skickar ett kommando till en Shelly-enhet och returnerar enhetens svar. |
| `component::shelly::services::command::fields::command::description` | The RPC method for generation 2 and newer devices, for example `Switch.Set`, or the HTTP endpoint for generation 1 devices, for example `relay/0`. | RPC-metoden för generation 2 och nyare enheter, till exempel `Switch.Set`, eller HTTP-slutpunkten för generation 1-enheter, till exempel `relay/0`. |
| `component::shelly::services::command::fields::command::name` | Command | Kommando |
| `component::shelly::services::command::fields::device_id::description` | The ID of the Shelly device to send the command to. | ID:t för Shelly-enheten som kommandot ska skickas till. |
| `component::shelly::services::command::fields::device_id::name` | Device | Enhet |
| `component::shelly::services::command::fields::params::description` | Optional parameters of the command in the format of key value pairs. | Valfria kommandoparametrar i formatet nyckel-värde-par. |
| `component::shelly::services::command::fields::params::name` | Parameters | Parametrar |
| `component::shelly::services::command::name` | Send command | Skicka kommando |
| `component::shelly::entity::number::display_brightness::name` | Display brightness | Skärmens ljusstyrka |
| `component::shelly::entity::number::min_auto_display_brightness::name` | Minimum auto display brightness | Minsta automatiska skärmljusstyrka |
| `component::shelly::entity::switch::auto_brightness::name` | Auto display brightness | Automatisk skärmljusstyrka |

## Verifiering

- Samtliga 16 mål var tomma vid den färska sidindelade Lokalise-hämtningen och har nu sparats samt lästs tillbaka via respektive svenska Lokalise-översättnings-ID.
- Platshållarna `{command}`, `{device}`, `{status}`, `{code}` och `{message}` är bevarade exakt.
- Kodfragmenten `` `Switch.Set` `` och `` `relay/0` `` är bevarade exakt.
- Åtta samtidiga tomma poster har tom engelska källtext och är strukturella objektbehållare, inte synliga översättningsmål; de lämnades oförändrade.
