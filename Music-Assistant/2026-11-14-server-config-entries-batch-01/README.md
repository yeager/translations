# Music Assistant Server – konfigurationsposter, batch 1

Datum: 2026-11-14

Komponent: `music-assistant/server`, Lokalise-projektet **MA Server**.

Den här loggen dokumenterar radgranskning av konfigurationsposter mot engelsk
källa och den faktiska svenska Lokalise-strängen.

## Granskade rader

- `common.config_entries.ai_engine.description`: *The AI engine used for this
  feature.* → *AI-motorn som används för den här funktionen.*; saknad
  översättning tillagd och återläst.
- `common.config_entries.ai_engine.label`: *AI engine* → *AI-motor*; saknad
  översättning tillagd och återläst.
- `common.config_entries.ai_engine_unavailable.label`: *No AI engine is
  available. Set up a plugin that provides AI, for example the Home Assistant
  plugin with an AI task entity.* → *Ingen AI-motor är tillgänglig.
  Konfigurera en insticksmodul som tillhandahåller AI, till exempel Home
  Assistant-insticksmodulen med en AI-uppgiftsentitet.*; saknad översättning
  tillagd och återläst.

## Upstreamstatus

`common.config_entries.ai_engine.description` översattes och återlästes i MA
Server på Lokalise 2026-11-14. Lokalise-granskning, kodsynkronisering och
release är inte verifierade.
`common.config_entries.ai_engine.label` översattes och återlästes i MA Server
på Lokalise 2026-11-14.
`common.config_entries.ai_engine_unavailable.label` översattes och återlästes
i MA Server på Lokalise 2026-11-14.

`msgfmt` är inte tillämpligt eftersom katalogen är JSON.
