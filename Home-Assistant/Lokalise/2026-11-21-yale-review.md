# Home Assistant Core – Yale

Datum: 2026-11-21

Alla 24 Yale-strängar har granskats mot aktuell källa och tidigare sparade ändringar. Ett entitetsnamn är korrigerat, sparat och API-återläst.

| Nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `entity::binary_sensor::image_capture::name` | `Fånga bild` | `Bildtagning` | Entitetsnamnet ska vara ett substantiv, inte en uppmaning. |

OAuth-, autentiserings- och dörrklockstexterna är i övrigt korrekta. Platshållarna `{error}` och `{docs_url}` har kontrollerats.
