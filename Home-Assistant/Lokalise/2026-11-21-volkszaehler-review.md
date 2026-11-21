# Home Assistant Core – Volkszaehler

Datum: 2026-11-21

Alla 31 Volkszaehler-strängar har granskats. Ett felaktigt ordval är korrigerat, sparat och API-återläst.

| Nyckel | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `config::abort::reconfigure_successful` | `Omkonstruktionen lyckades.` | `Omkonfigurationen lyckades.` | *Reconfiguration* avser ändrad inställning, inte fysisk omkonstruktion. |

YAML-migreringstexterna, UUID, servernamn och referenser till Home Assistants användargränssnitt är i övrigt korrekta.
