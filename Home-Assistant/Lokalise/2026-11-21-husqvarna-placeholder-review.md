# Home Assistant Core: Husqvarna Automower — platshållarrättning

Två sensoretiketter innehöll den extra platshållaren `{work_area}`, trots att den saknas i engelska källor.

- `work_area_last_time_completed::name`: `{work_area} slutfördes senast` → `Senast slutförd`.
- `work_area_progress::name`: `{work_area} förlopp` → `Förlopp`.

Båda sparades via Lokalise API och återlästes. TMX-manifest: `Home-Assistant/2026-11-21-husqvarna-placeholder-verified.json`; validerad TMX: 2 487 poster.
