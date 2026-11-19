# Sparade svenska översättningar: Axle, Tuya, PeBlär, WAQI, Zonneplan och MCP

Datum: 2026-11-19

Alla poster nedan har sparats via Lokalise API och lästs tillbaka efter uppdateringen.

## Ändringar

### `component::axle_energy::config::step::reauth_confirm::description`

- Engelska: Your Axle API key is no longer accepted. Open the [Home Assistant page in your Axle account]({token_url}) and copy your Home Assistant token. If **Generate Token** is available, select it first. Enter the token in **API key**. If the token is still rejected, contact Axle support.
- Tidigare svenska: Din Axle API-nyckel accepteras inte längre. Öppna [Home Assistant-sidan i ditt Axle-konto]({token_url}) och kopiera din Home Assistant-token. Om alternativet **Generera token** finns väljer du det först. Ange token i **API-nyckel**. Om token fortfarande avvisas kontaktar du Axles support.
- Sparad svenska: Din Axle-API-nyckel accepteras inte längre. Öppna [Home Assistant-sidan i ditt Axle-konto]({token_url}) och kopiera din Home Assistant-token. Om alternativet **Generera token** finns väljer du det först. Ange token i **API-nyckel**. Om token fortfarande avvisas kontaktar du Axles support.

### `component::tuya::entity::sensor::indexed_reactive_power::name`

- Engelska: Reactive power channel {index}
- Tidigare svenska: Reaktiv effekt kanal {index}
- Sparad svenska: Reaktiv effekt för kanal {index}

### `component::tuya::entity::sensor::indexed_power_factor::name`

- Engelska: Power factor channel {index}
- Tidigare svenska: Effektfaktor kanal {index}
- Sparad svenska: Effektfaktor för kanal {index}

### `component::tuya::entity::sensor::indexed_apparent_power::name`

- Engelska: Apparent power channel {index}
- Tidigare svenska: Skeneffekt kanal {index}
- Sparad svenska: Skenbar effekt för kanal {index}

### `component::peblar::entity::event::session_authorization::state_attributes::event_type::state::session_authorized`

- Engelska: Session authorized
- Tidigare svenska: Session autentiserad
- Sparad svenska: Session auktoriserad

### `component::peblar::entity::event::session_authorization::name`

- Engelska: Session authorization
- Tidigare svenska: Sessionsautentisering
- Sparad svenska: Sessionsauktorisering

### `component::waqi::issues::station_not_found::fix_flow::step::confirm::description`

- Engelska: The measuring station "{name}" can no longer be found by the World Air Quality Index API. This usually means the station has been permanently taken offline. A different station may report different metrics, so it is not automatically substituted.

Select **Submit** to remove this measuring station. You can add a replacement station afterwards.
- Tidigare svenska: Mätstationen "{name}" kan inte längre hittas via World Air Quality Index API. Detta betyder vanligtvis att stationen har tagits ur drift permanent. En annan station kan rapportera andra mätvärden och ersätts därför inte automatiskt.

Välj **Skicka** för att ta bort mätstationen. Du kan lägga till en ersättningsstation efteråt.
- Sparad svenska: Mätstationen "{name}" kan inte längre hittas via World Air Quality Index-API:t. Detta betyder vanligtvis att stationen har tagits ur drift permanent. En annan station kan rapportera andra mätvärden, så den ersätts inte automatiskt.

Välj **Skicka** för att ta bort mätstationen. Du kan lägga till en ersättningsstation efteråt.

### `component::zonneplan::exceptions::rate_limited::message`

- Engelska: The Zonneplan API rate limit was reached
- Tidigare svenska: Gränsen för antal begäranden till Zonneplan API har nåtts
- Sparad svenska: Gränsen för antal begäranden till Zonneplan-API:t har nåtts

### `component::zonneplan::exceptions::api_error::message`

- Engelska: Unexpected error from the Zonneplan API
- Tidigare svenska: Oväntat fel från Zonneplan API
- Sparad svenska: Oväntat fel från Zonneplan-API:t

### `component::zonneplan::config::error::rate_limited`

- Engelska: Too many requests to the Zonneplan API. Wait a minute and try again.
- Tidigare svenska: För många begäranden till Zonneplan API. Vänta en minut och försök igen.
- Sparad svenska: För många begäranden till Zonneplan-API:t. Vänta en minut och försök igen.

### `component::mcp_server::options::step::init::data_description::all_llm_apis`

- Engelska: Also exposes sets of tools that integrations add later.
- Tidigare svenska: Exponera alla LLM-API:er, även de som läggs till senare.
- Sparad svenska: Exponerar även verktygsuppsättningar som integreringar lägger till senare.

### `component::mcp_server::options::step::init::data::all_llm_apis`

- Engelska: Expose all AI tools
- Tidigare svenska: Exponera alla LLM-API:er
- Sparad svenska: Exponera alla AI-verktyg

### `component::mcp_server::config::create_entry::default`

- Engelska: The Model Context Protocol server is active. To change which tools its main URL exposes, select **Configure** on the integration.
- Tidigare svenska: Model Context Protocol-servern är aktiv. Om du bara vill exponera vissa LLM-API:er väljer du **Konfigurera** på integreringen.
- Sparad svenska: Model Context Protocol-servern är aktiv. Om du vill ändra vilka verktyg som exponeras via dess huvudadress väljer du **Konfigurera** på integreringen.
