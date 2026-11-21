# Home Assistant Core – DuckDNS

Datum: 2026-11-21

Alla 26 aktuella strängar kontrollerades mot Core och Lokalise. Sex fel- och YAML-texter rättades och direktåterlästes via API.

| Nyckel | Sparad text | Motivering |
| --- | --- | --- |
| `config::error::update_failed` | `Det gick inte att uppdatera Duck DNS.` | Idiomatisk feltext. |
| `exceptions::entry_not_selected::message` | `Ingen Duck DNS-integrationspost har valts.` | Fullständig svensk sats. |
| `issues::deprecated_yaml_import_issue_error::*` | Förtydligad YAML-formulering för Duck DNS. | Naturlig ordföljd och konsekvent produktnamn. |
| `exceptions::{connection_error,update_failed}::message` | `Det gick inte att uppdatera …` | Konsekvent och läsbar felrapportering. |
