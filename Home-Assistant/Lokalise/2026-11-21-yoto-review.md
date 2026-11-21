# Home Assistant Core: Yoto — sparade platshållarrättningar

Fyra feltexter i `component::yoto` innehöll den extra platshållaren `{error}` i svensk text, men den saknas i respektive aktuell engelsk källa. Platshållaren togs bort och varje värde API-återlästes:

- `exceptions::command_failed::message`: `Yoto-kommandot misslyckades: {error}` → `Yoto-kommandot misslyckades.`
- `exceptions::update_error::message`: `Fel vid kommunikation med Yoto: {error}` → `Fel vid kommunikation med Yoto.`
- `exceptions::play_failed::message`: `Det gick inte att spela upp Yoto-mediefilen: {error}` → `Det gick inte att spela upp Yoto-mediefilen.`
- `exceptions::config_update_failed::message`: `Det gick inte att uppdatera inställningarna för Yoto-spelaren: {error}` → `Det gick inte att uppdatera inställningarna för Yoto-spelaren.`

TMX-manifest: `Home-Assistant/2026-11-21-yoto-verified.json`; validerad TMX: 2 474 poster.
