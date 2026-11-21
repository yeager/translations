# Home Assistant – GeoNet NZ Quakes: svensk radgranskning

Datum: 2026-11-21  
Komponent: `geonetnz_quakes`  
Omfattning: 4/4 aktuella källsträngar

| Fullständig nyckel | Engelsk källtext | Befintlig svensk text | Föreslagen text | Åtgärd/motivering |
| --- | --- | --- | --- | --- |
| `component::geonetnz_quakes::config::abort::already_configured` | Service is already configured | Tjänsten är redan konfigurerad | Oförändrad | Korrekt; den lokala nyckeln refererar en gemensam text och Lokalise visar den upplösta källtexten. |
| `component::geonetnz_quakes::config::step::user::data::mmi` | MMI | MMI | Oförändrad | Korrekt vedertagen förkortning för Modified Mercalli Intensity. |
| `component::geonetnz_quakes::config::step::user::data::radius` | Radius | Radie | Oförändrad | Korrekt fackterm. |
| `component::geonetnz_quakes::config::step::user::title` | Fill in your filter details. | Fyll i dina filterdetaljer. | Ange filterinställningarna. | Sparad i Lokalise; konsekvent med motsvarande GeoNet NZ Volcano-flöde. |

## Verifiering

- Aktuell källa och svenska värden hämtades via Lokalise API; den ändrade raden lästes tillbaka efter sparning.
- `l10n-lint`: inga problem.
- `hunspell-sv`: inga stavningsanmärkningar.
- `svlang`: 10,0/10; MMI markeras som sällsynt förkortning men är korrekt i sammanhanget.
- Inga platshållare, pluralformer eller formateringsmarkörer förekommer.
