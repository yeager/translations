# Music Assistant Server - Swedish live batch 01

Date: 2026-11-14

Channel: Music Assistant Server, Lokalise project `264744796a2c5fd1b48fb5.28236063`.

## Saved translations

| Key | English | Swedish |
| --- | --- | --- |
| `provider.cbc_listen.media.folder.radio_shows.name` | Radio Shows | Radioprogram |
| `provider.cbc_listen.manifest.description` | Listen to live radio stations, podcasts, and on-demand radio shows from CBC Listen, the audio service of the Canadian public broadcaster CBC. | Lyssna på direktsända radiostationer, poddar och radioprogram på begäran från CBC Listen, den kanadensiska public service-kanalen CBC:s ljudtjänst. |
| `core.player_queues.config_entries.default_enqueue_select_artist.options.library_album_tracks` | All tracks of the artist's albums in your library | Alla spår från artistens album i ditt bibliotek |
| `core.player_queues.errors.play_request_timeout` | Loading what you asked to play took longer than {0} seconds and was cancelled. | Det tog längre än {0} sekunder att läsa in det du ville spela och åtgärden avbröts. |
| `provider.hue_entertainment.setup_flow.abort.no_zigbee_lights` | No Hue lamps that support light sync were found in ZHA. | Inga Hue-lampor som stöder ljussynkronisering hittades i ZHA. |

## Verification

Each value was saved in Lokalise and immediately read back in the server editor on 2026-11-14. The `{0}` placeholder in the timeout message was preserved. The existing untranslated `LightSync` term was corrected to the source-aligned Swedish `ljussynkronisering` and read back after replacement.

`msgfmt`, l10n-lint, svlang and Hunspell are not applicable to this browser-only batch because no local resource export was produced. Archive diff control and Gitleaks were run before the archive commit.

## Upstream status

The five values are verified saved in Music Assistant's established Lokalise channel. Lokalise review, repository synchronization and a released server build are not verified by this readback.
