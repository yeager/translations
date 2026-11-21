# Home Assistant – GeoNet NZ Volcano: svensk radgranskning

Datum: 2026-11-21  
Komponent: `geonetnz_volcano`  
Omfattning: 3/3 aktuella källsträngar

| Fullständig nyckel | Engelsk källtext | Befintlig svensk text | Föreslagen text | Åtgärd/motivering |
| --- | --- | --- | --- | --- |
| `component::geonetnz_volcano::config::error::already_configured` | Location is already configured | Platsen är redan konfigurerad | Oförändrad | Korrekt. Den lokala källan refererar en gemensam sträng; Lokalise gav den upplösta källtexten. |
| `component::geonetnz_volcano::config::step::user::data::radius` | Radius | Radie | Oförändrad | Korrekt fackterm. |
| `component::geonetnz_volcano::config::step::user::title` | Fill in your filter details. | Fyll i dina filterdetaljer. | Ange filterinställningarna. | Sparad i Lokalise. Undviker direktöversättningen ”filterdetaljer” och blir tydligare i ett inställningsflöde. |

## Verifiering

- Aktuell källa och svenska värden hämtades via Lokalise API; den ändrade strängen lästes tillbaka efter sparning.
- `l10n-lint`: inga problem.
- `hunspell-sv`: inga stavningsanmärkningar.
- `svlang`: 10,0/10; inga relevanta anmärkningar för denna komponent.
- Inga platshållare, pluralformer eller formateringsmarkörer förekommer.
