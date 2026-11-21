# Home Assistant Core – Venstar

Datum: 2026-11-21

Alla 28 Venstar-strängar är granskade mot aktuell källa och tidigare sparat arbete. Fyra sensorbenämningar är korrigerade, sparade och API-återlästa.

| Nyckel | Sparad svenska | Motivering |
| --- | --- | --- |
| `entity::sensor::active_stage::name` | `Aktivt steg` | Etablerad teknisk term i stället för `skede`. |
| `entity::sensor::active_stage::state::first_stage` | `Första steget` | Samma terminologi och korrekt bestämd form. |
| `entity::sensor::active_stage::state::second_stage` | `Andra steget` | Samma terminologi och korrekt bestämd form. |
| `entity::sensor::schedule_part::name` | `Schemaperiod` | Ersätter den felaktiga särskrivningen `Schema del`. |

Tidigare sparade YAML-migreringstexter är oförändrade och korrekta. Platshållarna `{integration_title}` och `{domain}` har kontrollerats.
