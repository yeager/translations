# Home Assistant – Chacon DIO: svensk radgranskning

Datum: 2026-11-21  
Komponent: `chacon_dio`  
Omfattning: 6/6 aktuella källsträngar

| Fullständig nyckel | Engelsk källtext | Befintlig svensk text | Föreslagen text | Bedömning |
| --- | --- | --- | --- | --- |
| `component::chacon_dio::config::abort::already_configured` | Device is already configured | Enheten är redan konfigurerad | Oförändrad | Korrekt. |
| `component::chacon_dio::config::error::cannot_connect` | Failed to connect | Det gick inte att ansluta | Oförändrad | Korrekt. |
| `component::chacon_dio::config::error::invalid_auth` | Invalid authentication | Ogiltig autentisering | Oförändrad | Korrekt. |
| `component::chacon_dio::config::error::unknown` | Unexpected error | Oväntat fel | Oförändrad | Korrekt. |
| `component::chacon_dio::config::step::user::data::password` | Password | Lösenord | Oförändrad | Korrekt. |
| `component::chacon_dio::config::step::user::data::username` | Username | Användarnamn | Oförändrad | Korrekt. |

## Verifiering

- Alla lokala källnycklar refererar gemensamma texter; Lokalise API returnerade respektive upplöst engelsk källtext och aktuell svensk måltext.
- `l10n-lint`, `hunspell-sv` och `svlang`: inga problem.
- Inga platshållare, pluralformer eller formateringsmarkörer förekommer.
- Ingen ändring skickades, eftersom de sparade översättningarna redan är korrekta.
