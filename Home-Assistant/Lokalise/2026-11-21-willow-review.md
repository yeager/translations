# Home Assistant Core – Willow

Datum: 2026-11-21

Alla 18 Willow-strängar har granskats. En återautentiseringsrubrik är korrigerad, sparad och API-återläst.

| Nyckel | Tidigare svenska | Sparad svenska |
| --- | --- | --- |
| `config::step::reauth_confirm::title` | `Autentiseringen har upphört för {name}` | `Autentiseringen har upphört att gälla för {name}` |

Den sparade formen följer etablerad Core-terminologi och bevarar `{name}`. OAuth- och kontolänkningssträngarna är i övrigt korrekta.
