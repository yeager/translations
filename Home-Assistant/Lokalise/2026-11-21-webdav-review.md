# Home Assistant Core – WebDAV

Datum: 2026-11-21

Alla 24 WebDAV-strängar har granskats mot aktuell källa. Tre fel är rättade, sparade och API-återlästa.

| Nyckel | Sparad svenska | Motivering |
| --- | --- | --- |
| `exceptions::cannot_access_or_create_backup_path::message` | `Det går inte att komma åt eller skapa sökvägen för säkerhetskopior.` | Ersätter den grammatiskt felaktiga formen `en säkerhetskopians filsökväg`. |
| `config::error::access_denied` | `Åtkomst till sökvägen för säkerhetskopior nekades ...` | Rätt objekt: sökvägen, inte själva säkerhetskopian. |
| `config::step::reauth_confirm::title` | `Autentiseringen har upphört att gälla för {name}` | Etablerad, fullständig formulering med bevarad platshållare. |

Övriga URL-, SSL- och serversträngar är korrekta.
