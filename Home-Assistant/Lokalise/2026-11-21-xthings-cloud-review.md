# Home Assistant Core – Xthings Cloud

Datum: 2026-11-21

Alla 26 Xthings Cloud-strängar har granskats. En återautentiseringsrubrik är korrigerad, sparad och API-återläst.

| Nyckel | Tidigare svenska | Sparad svenska |
| --- | --- | --- |
| `config::step::reauth_confirm::title` | `Autentiseringen har upphört för {name}` | `Autentiseringen har upphört att gälla för {name}` |

Ändringen följer etablerad Core-terminologi för utgången autentisering och bevarar `{name}`. Övriga konto- och feltexter är korrekta.
