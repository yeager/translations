# Home Assistant Core – Vera

Datum: 2026-11-21

Samtliga tio Vera-strängar har granskats. Tre termer är korrigerade, sparade och API-återlästa.

| Nyckel | Sparad svenska | Motivering |
| --- | --- | --- |
| `config::abort::cannot_connect` | `Det gick inte att ansluta till styrenheten med URL:en {base_url}` | Naturlig felsats och korrekt term. |
| `config::step::user::data::vera_controller_url` | `Styrenhetens URL` | Ersätter engelskinfluerade `Controller-URL`. |
| `options::step::init::title` | `Alternativ för Vera-styrenheten` | Konsekvent svensk fackterm. |

Övriga strängar är korrekta. Platshållarna `{base_url}`, `{documentation_url}` och `{sample_ip}` är bevarade.
