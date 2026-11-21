# Home Assistant – iPerf3: svensk radgranskning

Datum: 2026-11-21  
Komponent: `iperf3`  
Omfattning: 4/4 aktuella källsträngar

| Fullständig nyckel | Engelsk källtext | Befintlig svensk text | Föreslagen text | Åtgärd/motivering |
| --- | --- | --- | --- | --- |
| `component::iperf3::services::speedtest::description` | Immediately executes a speed test with iperf3. | Utför omedelbart ett hastighetstest med iperf3. | Oförändrad | Korrekt. |
| `component::iperf3::services::speedtest::fields::host::description` | The host name of the iperf3 server (already configured) to run a test with. | Värdnamnet på den iperf3-server (redan konfigurerad) som testet ska köras mot. | Värdnamnet för den redan konfigurerade iperf3-server som testet ska köras mot. | Sparad i Lokalise. Den tidigare parentesen syftade grammatiskt på fel ord. |
| `component::iperf3::services::speedtest::fields::host::name` | Host | Värd | Oförändrad | Korrekt. Den lokala nyckeln refererar en gemensam text och Lokalise visar den upplösta källtexten. |
| `component::iperf3::services::speedtest::name` | Speedtest | Hastighetstest | Oförändrad | Korrekt. |

## Verifiering

- Aktuell källa och svenska värden hämtades via Lokalise API; den ändrade raden lästes tillbaka efter sparning.
- `l10n-lint`: inga problem.
- `hunspell-sv`: `iperf3` är en förväntad teknisk beteckning.
- `svlang`: varnar för V2-ordföljd i den relativa satsen ”som testet ska köras mot”; det är en felträff. Formuleringen är grammatisk.
- Inga platshållare, pluralformer eller formateringsmarkörer förekommer.
