# Home Assistant Core – Crownstone

Datum: 2026-11-21

Alla 33 aktuella strängar jämfördes med Core `2fdaa177` och direkt återlästes från Lokalise. USB-konfiguration, kontoflöden, felmeddelanden och Markdown-länken med `{entries}` kontrollerades.

| Nyckel | Befintlig text | Sparad text | Motivering |
| --- | --- | --- | --- |
| `component::crownstone::config::abort::usb_setup_complete` | `Crownstone USB-installationen är klar.` | `Crownstone USB-konfigurationen är klar.` | `setup` syftar på integrationskonfigurationen, inte programvaruinstallation. |
| `component::crownstone::config::abort::usb_setup_unsuccessful` | `Crownstone USB-installationen misslyckades.` | `Crownstone USB-konfigurationen misslyckades.` | Samma kontext och terminologi. |

Ändringarna PUT-sparades och direkt återlästes. Det verifierade Core-TMX-minnet validerades efter uppdateringen till 2 017 poster.
