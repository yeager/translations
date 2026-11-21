# Home Assistant Core – Actron Air

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/actron_air/strings.json`, aktuell Lokalise-export.

Status: samtliga 39 aktuella bladsträngar är radgranskade. Fyra tydliga fel har sparats och återlästs.

| Nyckel | Svenska efter granskning | Motivering |
| --- | --- | --- |
| `component::actron_air::config::progress::wait_for_authorization` | För att autentisera öppnar du följande URL och loggar in på Actron Air … Inloggningsförsöket upphör efter `{expires_minutes}` minuter. | Rättar den oidiomatiska konstruktionen ”ta en timeout”, återställer källans radbrytning och bevarar `{verification_uri}`, `{user_code}`, `{expires_minutes}` samt kodblock. Lokalise-ID `738636766`. |
| `component::actron_air::config::step::reauth_confirm::title` | Autentiseringen har löpt ut | Bestämd form och hjälpverb saknades. Lokalise-ID `772876453`. |
| `component::actron_air::exceptions::update_error` | … från Actron Air-API:et: `{error}` | Produktnamnet `Actron Air` ska inte bindestreckas internt; API-sammansättningen är korrekt. Lokalise-ID `780057714`. |
| `component::actron_air::exceptions::setup_connection_error` | Det gick inte att ansluta till Actron Air-API:et | Samma produktnamns- och API-sammansättning. Lokalise-ID `827699053`. |

Övriga konfigurationsflöden, statusetiketter, klimat- och kompressortermer samt undantag har kontrollerats utan ytterligare ändringsförslag. `{error}`-platshållarna och kodblocket i auktoriseringsflödet är intakta.
