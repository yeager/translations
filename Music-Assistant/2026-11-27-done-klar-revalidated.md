# Music Assistant: “Done” → “Klar”

Datum: 2026-11-27

Fyra aktiva nycklar med exakt källtext `Done` i MA Frontend, MA Mobile App och MA Server lästes om från Lokalise API. Alla har fortfarande svenska `Klar`, med rätt nyckel- och översättnings-ID. MA Desktop App hade ingen aktiv exakt `Done`-nyckel vid den föregående fullständiga projektsökningen.

Ingen ny Lokalise-textändring behövdes: de fyra värdena hade redan sparats som `Klar`. TMX-posterna återverifieras med dagens datum och samma svenska måltext.

| Projekt | Nyckel | English | Svenska | Lokalise-ID |
|---|---|---|---|---|
| MA Frontend | `settings::setup_flow::done` | `Done` | `Klar` | `9208725279` |
| MA Frontend | `done` | `Done` | `Klar` | `9743304767` |
| MA Mobile App | `common_done` | `Done` | `Klar` | `10318685278` |
| MA Server | `common.setup_flow.finish_silent.title` | `Done` | `Klar` | `9561764417` |
