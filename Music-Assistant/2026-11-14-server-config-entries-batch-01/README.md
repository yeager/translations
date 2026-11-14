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
- `common.config_entries.announce_volume.label`: *Volume for Announcements* →
  *Volym för meddelanden*; befintlig översättning bevarad.
- `common.config_entries.announce_volume.description`: *The percentual,
  relative or absolute volume level, used with the strategy for
  announcements.* → *Den procentuella, relativa eller absoluta volymnivån som
  används med strategin för meddelanden.*; befintlig översättning bevarad.
- `common.config_entries.announce_volume_max.description`: *The volume
  (adjustment) of announcements should not go above this level.* → *Volymen
  (justeringen) för meddelanden bör inte överstiga denna nivå.*; befintlig
  översättning bevarad.
- `common.config_entries.announce_volume_max.label`: *Maximum Volume level
  for Announcements* → *Maximal volymnivå för meddelanden*; befintlig
  översättning bevarad.
- `common.config_entries.announce_volume_min.description`: *The volume
  (adjustment) of announcements should not go below this level.* →
  *Volymjusteringen för meddelanden bör inte understiga denna nivå.*;
  översättningen förtydligad.
- `common.config_entries.announce_volume_min.label`: *Minimum Volume level
  for Announcements* → *Lägsta volymnivå för meddelanden*; befintlig
  översättning bevarad.
- `common.config_entries.announce_volume_strategy.label`: *Volume strategy for
  Announcements* → *Volymstrategi för meddelanden*; befintlig översättning
  bevarad.
- `common.config_entries.announce_volume_strategy.description`: *When an
  announcement is being broadcast to this player, how should the volume be
  adjusted temporarily (use in combination with the volume value below)?* →
  *När ett meddelande sänds till den här spelaren, hur ska volymen justeras
  tillfälligt (använd i kombination med volymvärdet nedan).*; befintlig
  översättning bevarad.
- `common.config_entries.announce_volume_strategy.options.none`: *Do not
  adjust volume* → *Justera inte volymen*; befintlig översättning bevarad.
- `common.config_entries.announce_volume_strategy.option_descriptions.none`:
  *Leave the volume unchanged; play the announcement at the player's current
  volume.* → *Lämna volymen oförändrad; spela upp meddelandet med spelarens
  aktuella volym.*; saknad översättning tillagd och återläst.
- `common.config_entries.auth_cookies.description`: *Authenticate using browser
  cookies from passport.yandex.ru.* → *Autentisera med webbläsarkakor från
  passport.yandex.ru.*; saknad översättning tillagd och återläst.
- `common.config_entries.auth_cookies.action_label`: *Login with Cookies* →
  *Logga in med kakor*; saknad översättning tillagd och återläst.
- `common.config_entries.auto_play.label`: *Automatically play (resume on
  power on)* → *Automatisk uppspelning (återupptas när strömmen slås på)*;
  befintlig översättning bevarad.
- `common.config_entries.auto_play.description`: *When this player is turned
  ON, automatically start playing (if there are items in the queue).* → *När
  spelaren är påslagen startar uppspelningen automatiskt (om det finns objekt
  i kön).*; befintlig översättning bevarad.
- `common.config_entries.crossfade_duration.label`: *Crossfade duration* →
  *Varaktighet för övertoning*; befintlig översättning bevarad.
- `common.config_entries.crossfade_duration.description`: *Duration in seconds
  of the crossfade between tracks (if enabled)* → *Varaktighet i sekunder för
  övertoning mellan spår (om aktiverad)*; befintlig översättning bevarad.
- `common.config_entries.default_enqueue_option_album.label`: *Default enqueue
  option for Album item(s).* → *Standardalternativ för att köa album.*;
  översättningen förtydligad och återläst.
- `common.config_entries.default_enqueue_option_artist.label`: *Default enqueue
  option for Artist item(s).* → *Standardalternativ för att köa artister.*;
  översättningen förtydligad och återläst.

## Upstreamstatus

`common.config_entries.ai_engine.description` översattes och återlästes i MA
Server på Lokalise 2026-11-14. Lokalise-granskning, kodsynkronisering och
release är inte verifierade.
`common.config_entries.ai_engine.label` översattes och återlästes i MA Server
på Lokalise 2026-11-14.
`common.config_entries.ai_engine_unavailable.label` översattes och återlästes
i MA Server på Lokalise 2026-11-14.
`common.config_entries.announce_volume.label` kontrollerades i MA Server på
Lokalise 2026-11-14. Ingen ändring behövdes.
`common.config_entries.announce_volume.description` kontrollerades i MA Server
på Lokalise 2026-11-14. Ingen ändring behövdes.
`common.config_entries.announce_volume_max.description` kontrollerades i MA
Server på Lokalise 2026-11-14. Ingen ändring behövdes.
`common.config_entries.announce_volume_max.label` kontrollerades i MA Server
på Lokalise 2026-11-14. Ingen ändring behövdes.
`common.config_entries.announce_volume_min.description` förtydligades och
återlästes i MA Server på Lokalise 2026-11-14.
`common.config_entries.announce_volume_min.label` kontrollerades i MA Server
på Lokalise 2026-11-14. Ingen ändring behövdes.
`common.config_entries.announce_volume_strategy.label` och
`common.config_entries.announce_volume_strategy.description` kontrollerades i
MA Server på Lokalise 2026-11-14. Ingen ändring behövdes.
`common.config_entries.announce_volume_strategy.options.none` kontrollerades
och dess saknade förklaring lades till och återlästes i MA Server på Lokalise
2026-11-14.
`common.config_entries.announce_volume_strategy.options.absolute`
kontrollerades och dess saknade förklaring lades till och återlästes i MA
Server på Lokalise 2026-11-14.
`common.config_entries.announce_volume_strategy.options.relative`
kontrollerades och dess saknade förklaring lades till och återlästes i MA
Server på Lokalise 2026-11-14.
`common.config_entries.announce_volume_strategy.options.percentual`
kontrollerades och dess saknade förklaring lades till och återlästes i MA
Server på Lokalise 2026-11-14.
`common.config_entries.auth_cookies.label` översattes och återlästes i MA
Server på Lokalise 2026-11-14.
`common.config_entries.auth_cookies.description` översattes och återlästes i
MA Server på Lokalise 2026-11-14.
`common.config_entries.auth_cookies.action_label` översattes och återlästes i
MA Server på Lokalise 2026-11-14.
`common.config_entries.auto_play.label` och
`common.config_entries.auto_play.description` kontrollerades i MA Server på
Lokalise 2026-11-14. Ingen ändring behövdes.
`common.config_entries.crossfade_duration.label` och
`common.config_entries.crossfade_duration.description` kontrollerades i MA
Server på Lokalise 2026-11-14. Ingen ändring behövdes.
`common.config_entries.default_enqueue_option_album.label` och
`common.config_entries.default_enqueue_option_artist.label` förtydligades och
återlästes i MA Server på Lokalise 2026-11-14.

`msgfmt` är inte tillämpligt eftersom katalogen är JSON.
