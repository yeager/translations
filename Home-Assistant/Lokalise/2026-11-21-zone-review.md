# Home Assistant Core: Zone — sparade ändringar

Tidigare rapport kontrollerades mot aktuell export. Följande sparades via Lokalise API och återlästes:

- `component::zone::triggers::entered::name`: `Ankommit zon` → `Gått in i zon`.
- `component::zone::triggers::left::name`: `Lämnat zon` → `Lämnat zonen`.
- `component::zone::triggers::occupancy_cleared::description`: belagd/obelagd → `går från att ha närvaro till att vara tomma`.
- Tio fullständiga `For at least`-nycklar under `component::zone` ändrades konsekvent från `I åtminstone` till `I minst`; samtliga finns i TMX-manifestet `Home-Assistant/2026-11-21-zone-verified.json`.

TMX validerades efter sparning: 2 470 poster.
