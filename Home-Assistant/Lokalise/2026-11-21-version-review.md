# Home Assistant Core – Version

Datum: 2026-11-21

Alla 12 Version-strängar är granskade mot aktuell källa. Två konfigurationsbeskrivningar är förenklade, sparade och API-återlästa.

| Nyckel | Sparad svenska | Motivering |
| --- | --- | --- |
| `config::step::user::description` | `Välj den källa vars versioner du vill spåra` | Tydliggör relationen mellan källa och versioner. |
| `config::step::version_source::description` | `Konfigurera versionsspårning för {version_source}` | Naturlig ordföljd; platshållaren är bevarad. |

Övriga strängar är korrekta. Variablerna `{version_source}`, `{board}` och `{title}` är kontrollerade.
