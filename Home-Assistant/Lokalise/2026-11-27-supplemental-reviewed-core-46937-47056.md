# Home Assistant Core – radgranskning 46 937–47 056

Datum: 2026-11-27  
Lokalise-projekt: `130246255a974bd3b5e8a1.51616605`  
Core-källrevision: `1d07105b760c73093145526a51758938e87cc658`

## Kompletterande omfattning och verifiering

Denna kompletterande granskning gäller positionerna 46 937–47 056; den ändrar inte den löpande granskningsmarkören. Alla 120 positioner jämfördes med aktuell källtext och tidigare rapporter: 48 direkta Core-strängar, 26 referenser och 46 historiska nycklar utan aktuell källväg. Alla 46 historiska poster fanns i tidigare dokumentation. Samtliga 26 referenser matchade målens engelska källa och svenska text.

- 17 korrigeringar sparades och lästes tillbaka via Lokalise API; övriga direkta strängar behölls efter granskning.
- Platshållare: 120/120; pluralnycklar: 0.
- `svlang skrivregler --enable-interpunktion`: inga skrivregelfel.
- Hunspell hittade två giltiga, tidigare saknade sammansättningar (`växelriktareffekt`, `växelriktartemperatur`). De lades till i båda ordböckerna och regressionstesterna; sviten passerar 19/19. Ingen ytterligare verktygsrelease skapades i dag.
- Inga osäkra översättningar eller olösta referensmål återstår i batchen.

## Historiska nycklar utan aktuell källväg

Följande 46 historiska nycklar saknas i aktuell Core-källrevision. Samtliga var tidigare dokumenterade och markeras som `source-path-follow-up` i TM:

- Position 46962: `component::waterfurnace::issues::deprecated_yaml_import_issue_cannot_connect::description`.
- Position 46963: `component::waterfurnace::issues::deprecated_yaml_import_issue_cannot_connect::title`.
- Position 46964: `component::waterfurnace::issues::deprecated_yaml_import_issue_invalid_auth::description`.
- Position 46965: `component::waterfurnace::issues::deprecated_yaml_import_issue_invalid_auth::title`.
- Position 46966: `component::waterfurnace::issues::deprecated_yaml_import_issue_unknown::description`.
- Position 46967: `component::waterfurnace::issues::deprecated_yaml_import_issue_unknown::title`.
- Position 46973: `component::switch::common::condition_behavior_description`.
- Position 46976: `component::switch::conditions::is_off::fields::behavior::description`.
- Position 46980: `component::switch::conditions::is_on::fields::behavior::description`.
- Position 46983: `component::switch::selector::condition_behavior::options::all`.
- Position 46984: `component::switch::selector::condition_behavior::options::any`.
- Position 46985: `component::lock::common::condition_behavior_description`.
- Position 46988: `component::lock::conditions::is_jammed::fields::behavior::description`.
- Position 46992: `component::lock::conditions::is_locked::fields::behavior::description`.
- Position 46996: `component::lock::conditions::is_open::fields::behavior::description`.
- Position 47000: `component::lock::conditions::is_unlocked::fields::behavior::description`.
- Position 47003: `component::lock::selector::condition_behavior::options::all`.
- Position 47004: `component::lock::selector::condition_behavior::options::any`.
- Position 47006: `component::libre_hardware_monitor::config::abort::reauth_successful`.
- Position 47030: `component::aladdin_connect::config::abort::oauth_implementation_unavailable`.
- Position 47031: `component::august::config::abort::oauth_implementation_unavailable`.
- Position 47032: `component::ekeybionyx::config::abort::oauth_implementation_unavailable`.
- Position 47033: `component::electric_kiwi::config::abort::oauth_implementation_unavailable`.
- Position 47034: `component::fitbit::config::abort::oauth_implementation_unavailable`.
- Position 47035: `component::gentex_homelink::config::abort::oauth_implementation_unavailable`.
- Position 47036: `component::geocaching::config::abort::oauth_implementation_unavailable`.
- Position 47037: `component::google::config::abort::oauth_implementation_unavailable`.
- Position 47038: `component::google_assistant_sdk::config::abort::oauth_implementation_unavailable`.
- Position 47039: `component::google_drive::config::abort::oauth_implementation_unavailable`.
- Position 47040: `component::google_mail::config::abort::oauth_implementation_unavailable`.
- Position 47041: `component::google_photos::config::abort::oauth_implementation_unavailable`.
- Position 47042: `component::google_sheets::config::abort::oauth_implementation_unavailable`.
- Position 47043: `component::google_tasks::config::abort::oauth_implementation_unavailable`.
- Position 47044: `component::home_connect::config::abort::oauth_implementation_unavailable`.
- Position 47045: `component::husqvarna_automower::config::abort::oauth_implementation_unavailable`.
- Position 47046: `component::iotty::config::abort::oauth_implementation_unavailable`.
- Position 47047: `component::lametric::config::abort::oauth_implementation_unavailable`.
- Position 47048: `component::lyric::config::abort::oauth_implementation_unavailable`.
- Position 47049: `component::mcp::config::abort::oauth_implementation_unavailable`.
- Position 47050: `component::microbees::config::abort::oauth_implementation_unavailable`.
- Position 47051: `component::miele::config::abort::oauth_implementation_unavailable`.
- Position 47052: `component::monzo::config::abort::oauth_implementation_unavailable`.
- Position 47053: `component::myuplink::config::abort::oauth_implementation_unavailable`.
- Position 47054: `component::neato::config::abort::oauth_implementation_unavailable`.
- Position 47055: `component::nest::config::abort::oauth_implementation_unavailable`.
- Position 47056: `component::netatmo::config::abort::oauth_implementation_unavailable`.

## Status

Detta är en kompletterande, ur ordning utförd granskning och flyttar inte den löpande markören i `STATUS.md`.

Nästa Lokalise-position: **47 057**. Enligt den löpande positionsräkningen återstår **30 484 positioner**. Core-granskningen fortsätter; inte klar.
