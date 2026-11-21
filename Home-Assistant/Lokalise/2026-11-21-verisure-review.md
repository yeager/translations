# Home Assistant Core – Verisure

Datum: 2026-11-21

Alla 30 Verisure-strängar har granskats mot aktuell källa och tidigare sparade ändringar. En inkonsekvent produktbeteckning är rättad, sparad och API-återläst.

| Nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `config::step::reauth_confirm::data::description` | `... Verisure mina sidor-konto` | `... Verisure My Pages-konto` | Anpassar texten till källans och den vanliga inloggningstextens produktnamn. |

Tvåstegsverifieringen och tidigare sparade feltexter är korrekta. Inga platshållare berörs.
