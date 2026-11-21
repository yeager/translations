# Home Assistant – Mullvad: svensk radgranskning

Datum: 2026-11-21  
Komponent: `mullvad`  
Omfattning: 4/4 aktuella källsträngar

| Fullständig nyckel | Engelsk källtext | Befintlig svensk text | Föreslagen text | Åtgärd/motivering |
| --- | --- | --- | --- | --- |
| `component::mullvad::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Oförändrad | Korrekt; Lokalise returnerar den upplösta gemensamma källtexten. |
| `component::mullvad::config::error::unknown` | Unexpected error | Oväntat fel | Oförändrad | Korrekt; Lokalise returnerar den upplösta gemensamma källtexten. |
| `component::mullvad::config::step::user::description` | Set up the Mullvad VPN integration? | Konfigurera Mullvad VPN-integrationen? | Oförändrad | Korrekt och konsekvent terminologi. |
| `component::mullvad::entity::binary_sensor::exit_ip::name` | Exit IP | Utgångs-IP | Utgående IP-adress | Sparad i Lokalise. Ersätter en onaturlig sammansättning med ett tydligt tekniskt sensornamn. |

## Verifiering

- Aktuell källa och svenska värden hämtades via Lokalise API; den ändrade raden lästes tillbaka efter sparning.
- `l10n-lint`, `hunspell-sv` och `svlang`: inga problem.
- Inga platshållare, pluralformer eller formateringsmarkörer förekommer.
