# Home Assistant: retroaktiv terminologikorrigering för GeoFence

Fyra Lokalise-texter uppdaterades och återlästes den 26 november 2026 efter kontroll mot Husqvarnas svenska dokumentation. Dokumentationen använder produktnamnet GeoFence och beskriver funktionen som ett GPS-baserat stöldskyddssystem/virtuellt staket. De tidigare formuleringarna ”geostaketet” ersattes därför med produktnamnet i feltexten och den officiella funktionsbeskrivningen i utanför-meddelandet.

Källa: [Husqvarna – GeoFence och GPS-spårning](https://www.husqvarna.com/se/support/husqvarna-self-service/sa-har-aktiverar-du-geo-fence-och-gps-sparning-pa-automower-robotgrasklipparen-ka-01568/). Den relaterade felmeddelandesidan namnger också larmet ”Utanför stöldskyddsområde”.

## Lokalise-ändringar

- `component::husqvarna_automower::entity::sensor::error::state::alarm_outside_geofence` — `Larm! Gräsklipparen är utanför geostaketet.` → `Larm! Utanför stöldskyddsområdet.`; sparad och återläst.
- `component::husqvarna_automower::entity::event::message::state_attributes::event_type::state::alarm_outside_geofence` — `Larm! Gräsklipparen är utanför geostaketet.` → `Larm! Utanför stöldskyddsområdet.`; sparad och återläst.
- `component::husqvarna_automower::entity::sensor::error::state::geofence_problem` — `Problem med geostaketet.` → `Problem med GeoFence.`; sparad och återläst.
- `component::husqvarna_automower::entity::event::message::state_attributes::event_type::state::geofence_problem` — `Problem med geostaketet.` → `Problem med GeoFence.`; sparad och återläst.

Ändringarna skrivs retroaktivt över i HA Core-TM och registreras som separat korrektionsmanifest.
