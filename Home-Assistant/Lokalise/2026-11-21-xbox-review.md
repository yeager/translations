# Home Assistant Core: Xbox — sparade ändringar

Tidigare Xbox-rapporter i backupen kontrollerades mot aktuell export. Följande redan dokumenterade förslag sparades via Lokalise API och återlästes:

- `component::xbox::exceptions::timeout_exception::message`: `Misslyckades med att ansluta till Xbox Nätverket på grund av timeout för anslutningen.` → `Det gick inte att ansluta till Xbox Network eftersom anslutningen tog för lång tid.`
- `component::xbox::config::step::oauth_discovery::title`: `Upptäckt Xbox enhet` → `Upptäckt Xbox-enhet`.
- `component::xbox::config_subentries::friend::step::user::description`: `Håll koll på online-statusen för en Xbox Network-vän.` → `Håll koll på onlinestatusen för en Xbox Network-vän.`
- `component::xbox::config_subentries::friend::step::user::title`: `Väns online-status` → `Väns onlinestatus`.
- `component::xbox::entity::sensor::free_storage::name`: `Ledigt utrymme - {name}` → `Ledigt utrymme – {name}`. Platshållaren är oförändrad.

De fullständiga verifieringsposterna finns i `swedish-tm`-manifesten `Home-Assistant/2026-11-21-xbox-verified.json` och `Home-Assistant/2026-11-21-xbox-storage-verified.json`; den kanoniska TMX-filen validerades efter uppdateringen (2 448 poster).
