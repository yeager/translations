# Home Assistant Core – Lokalise-granskning, sida 610

Datum: 2026-11-20  
Omfattning: Lokalise API, 20 Core-strängar (`foscam`, `freebox`, `fritz`, `fully_kiosk`).

## Sparade ändringar

| Nyckel | Sparad svensk text | Motivering |
|---|---|---|
| `component::foscam::services::ptz_preset::fields::preset_name::description` | `Namnet på förinställningen som kameran ska flyttas till. Förinställningar kan skapas i de officiella Foscam-apparna.` | Rätt svensk satsstruktur och preposition. |
| `component::fritz::services::set_guest_wifi_password::description` | `Ställer in ett nytt lösenord för gäst-Wi-Fi. Lösenordet måste vara mellan 8 och 63 tecken långt. Om ingen ytterligare parameter anges genereras lösenordet automatiskt med en längd på 12 tecken.` | Imperativ konsekvent med tjänsttexten. |
| `component::fritz::services::set_guest_wifi_password::fields::device_id::name` | `FRITZ!Box-enhet` | Bevarar officiell märkesskrivning. |
| `component::fritz::services::set_guest_wifi_password::fields::password::description` | `Nytt lösenord för gäst-Wi-Fi.` | Konsekvent Wi-Fi-skrivning. |
| `component::fritz::services::set_guest_wifi_password::name` | `Ange lösenord för gäst-Wi-Fi` | Konsekvent Wi-Fi-skrivning. |

## Verifiering

Alla fem ändringar skickades med Lokalise API och återlästes. Referensen för lösenordsfältet är giltig; övriga strängar behöver ingen ändring.

Status: sparat och återläst i Lokalise.
