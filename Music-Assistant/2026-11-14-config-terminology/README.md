# Music Assistant server — Swedish configuration terminology

Date: 2026-11-14

Repository: `music-assistant/server` (`dev` at `8b1c3fb4e5c2411b5c97a247129876ebbf0f09e9`)

Release freshness: 2.10.11 was published 2026-11-13.

## Reviewed changes

- `AirPlay-specifika inställningar`
- `Aktivera stöd för {0}`
- source-aligned help for flow mode and the shared Music Assistant icon set
- an idiomatic TTS pre-announcement description using `klocksignal`
- corrected loudness terminology: `ljudklippning`, not interrupted audio
- `förinläsning` in the infinite-mix description; the em dash remains because it is present in the source
- `Alla favoritspår`
- `Visning`, `Synkroniserings- och importalternativ` och `Utgångskanalläge`
- consistent `favoritspår` terminology in the infinite-mix variant
- ten missing, context-clear configuration categories, including `Automatisk uppspelning`, `Klickåtgärder`, `Felsökning`, `Källval` and placeholder-preserving protocol support labels
- five further context-checked configuration categories: `Objekt att välja`, `Insticksmoduler`, `Förinställningar`, `Rekommendationer` and `Server`
- `Intelligent blandning` for the recency-aware queue algorithm and `Upptäck` for the recommendation row
- fourteen context-clear configuration labels for network, content, volume and player controls, including `TCP-port`, `Klient-ID`, `Volymstyrning` and `Samplingsfrekvenser som stöds av den här spelaren`
- eleven source-specific library synchronization labels, using `läs in` for track import and `synkronisera` for two-way library operations
- the corresponding eleven source-specific library synchronization descriptions, including the behavior for albums, playlists, deletions and two-way sync
- Swedish network-discovery and stream-server binding settings, with technical terms retained where required: `mDNS`, `UPnP`, `IPv4`, `IPv6` and `Zeroconf`
- Swedish device setup, network-advertised naming and session-authentication settings, retaining the established technical term `token`
- complete Swedish review of flow-mode sample-rate and live-source audio settings, retaining established sound terms such as `WAV`, `PCM`, `bitperfekt` and `samplingsfrekvens`
- complete Swedish review of local-library behavior settings: feed limits, idle shutdown, album playlists, missing `Albumartist` tags and genre inheritance; `Various Artists` is preserved because it is an internal, visible canonical artist name
- Swedish authentication settings for remote servers, device codes, QR codes and browser cookies, retaining canonical names and standards such as `passport.yandex.ru`, `OAuth`, `SSL` and `TLS`
- Swedish review of output-codec choices and their help text, using `kodek`, `förlustfri`, `med förlust`, `bithastighet` and `samplingsfrekvens`, while retaining the format names `AAC`, `FLAC`, `MP3`, `WAV` and `PCM`
- Swedish ICY metadata settings, including the flow-mode behavior and the basic and full metadata profiles; the established protocol name `ICY` is retained
- Swedish AI, image-generation and text-to-speech engine settings. Home Assistant entities and the visible `OpenAI Compatible` integration name remain identifiable while the surrounding UI is Swedish
- Swedish player output-protocol settings, including the experimental variants and the dependency on an underlying protocol; the dynamic `{0}` protocol placeholder is preserved
- Swedish Home Assistant player exposure and plug-in availability settings, plus track-version suffix and audio-synchronization-delay controls. The existing UI label `Anslutna spelare` is used consistently
- Swedish group-playback, announcement-signal URL and preview-warning settings, retaining canonical URLs, formats and command semantics while using Swedish UI wording
- Swedish per-player and per-user scrobbling controls. The established Swedish free-software spelling `scrobbla` is used, and the unofficial-provider notice retains its original scope and legal qualifications
- Swedish help text for all announcement-volume strategies: fixed volume, unchanged volume, percentage increase and relative increase
- Swedish content-type settings for stored music, podcasts, audiobooks and sound effects
- Swedish mute and power-control choices for players, including native, simulated and automatic protocol-controlled behavior; the Home Assistant entity concept is retained
- Swedish help text and availability states for the preferred player output protocol, including automatic selection and setup requirements
- Swedish player-visibility, volume-bound and fixed-content-length help text, preserving the behavioral distinction between hiding and disabling a player
- Swedish supported-sample-rate settings, including bit depths and Swedish numeric typography while retaining the technical sample-rate values
- Swedish server port, exposed-player, log-level and volume-control settings. This completes the source-context review of all currently missing `common.config_entries` strings in the reviewed catalog
- Swedish review of all currently missing `common.player_options` strings: receiver and speaker sound controls, network and sleep options, and canonical audio-mode names such as `DRC`, `DTS`, `Link` and `Pure Direct`
- Swedish completion of all currently missing `common.setup_flow` strings: initial library import, completion state and selection of a child device for setup
- Swedish device-code login page: code copying, expiry, denial and failure states, and the Yandex continuation step. The source em dash is retained only in the manual-copy notice where the English source also uses it
- Swedish review of 20 context-clear common error messages for authentication, connections, permissions, provider identifiers, tokens and invalid values; all `{0}` placeholders are preserved
- Swedish review of 20 further common error messages for user roles, music sources, playlists, players, provider-stream limits and request limits; all `{0}` and `{1}` placeholders are preserved
- Swedish review of 20 common error messages for required fields, roles, music-source ownership and sharing, setup, sign-in expiry and the protected Home Assistant system account; the dynamic `{0}` limit is preserved
- Swedish completion of all currently missing `common.errors` strings, including account, media, feature and system-requirement errors. Technical identifiers such as `AVX2`, `CPU`, `RAM`, `Intel Haswell`, `AMD Zen`, `Proxmox`, `TrueNAS` and the visible CPU type `host` remain identifiable
- Swedish completion of all currently missing `core.music` strings: background tasks for library synchronization and maintenance, remaster handling, library-database reset and the core module metadata. The visible title `Remastered 2009` is intentionally retained
- Swedish review of the first 17 `core.storage` errors: storage folders, absolute export paths, containers, mounts and the security rationale for refusing unsafe network-share mount paths
- Swedish completion of all currently missing `core.storage` strings: network-share discovery, mounting, credentials, protocol versions, Home Assistant ownership and manifest metadata
- Swedish review of 25 player-queue settings for automatic playback and övertoning, including the source-specific explanations, dynamic playlists, similar artists, smart transitions and audio-buffer requirements
- Swedish review of 24 player-queue settings for default click actions on albums, artists, genres, playlists and radio stations, plus global, smart and standard övertoning choices
- Swedish review of 25 further player-queue settings for tracks and default queuing of albums, artists, audiobooks, folders, genres, radio stations and direct inputs. The source em dash is retained in the live-stream explanation
- Swedish review of 20 player-queue settings for playlists, podcasts, podcast episodes and tracks, plus artist playback order and its album, release-year and shuffled-track behaviors
- Swedish review of 16 player-queue settings for choosing album and artist contents and for playing individual tracks from albums and playlists
- Swedish review of 30 player-queue settings for pause timeouts, smart shuffle, repeat spacing, artist recency and smart-overtoning order optimization
- Swedish review of 21 remaining player-queue settings for smart-shuffle song recency, smart-overtoning defaults and EBU-R128 volume normalization
- Swedish completion of all currently missing `core.player_queues` strings: playback-request timeout, module description and the visible module name
- Swedish review of 15 audiobook genres and descriptions in `common.media`, with Swedish library terminology and source-preserving em dashes
- Swedish completion of the remaining six audiobook genres in `common.media`: science, self-help, speakers, sports, technology and travel
- Swedish review of 35 visible media-folder names in `common.media`, including libraries, playlists, radio stations, periods and moods
- Swedish completion of the remaining four visible media-folder names and context review of Afrobeats metadata in `common.media`
- Swedish review of ten `common.media` podcast genres: arts, business, comedy, education, fiction, government, health, history, kids and leisure
- Swedish completion of the remaining nine `common.media` podcast genres: music, news, religion, science, society, sports, technology, true crime and television/film
- Swedish review of 38 visible `common.media` recommendation labels and subtitles for albums, artists, podcasts, playlists, radio and recently or frequently played content
- Swedish context review of the Ambient genre metadata in `common.media`, retaining the established genre and new-age terminology
- Swedish context review of the anime/video-game and Asian-music genre metadata in `common.media`, retaining identifiers such as VGM, PSG, FM synthesis and chiptune
- Swedish context review of the children’s, Christmas and church-music genre metadata in `common.media`
- Swedish context review of the classical-music and chanson metadata in `common.media`, including music-historical terminology
- Swedish review of 23 visible music-genre labels in `common.media`, using Swedish labels where natural and retaining established international genre names
- Swedish review of 27 additional visible music-genre labels in `common.media`, including Middle Eastern music, spoken word, soundtrack and wellness
- Swedish context review of the metal, polka, punk and reggaeton metadata in `common.media`
- Swedish context review of the bluegrass, blues, Brazilian-music and comedy-music metadata in `common.media`
- Swedish context review of the country-music and dance-music metadata in `common.media`
- Swedish context review of the dark-ambient and dark-wave metadata in `common.media`
- Swedish context review of the disco and electronic-music metadata in `common.media`
- Swedish context review of the experimental-music and field-recording metadata in `common.media`
- Swedish context review of the folk-music and funk metadata in `common.media`
- Swedish context review of the gangsta-rap, gospel and hip-hop metadata in `common.media`
- Swedish context review of the Indian-classical and industrial-music metadata in `common.media`
- Swedish context review of the jazz, klezmer and Latin-music metadata in `common.media`
- Swedish context review of the marching-band, Middle-Eastern-music and musical-theatre metadata in `common.media`; the visible genre label was corrected from `Marschmusik` to `Marschorkester`
- Swedish context review of the new-age, poetry and pop-music metadata in `common.media`
- Swedish context review of the psychedelic-music, rhythm-and-blues and ragtime metadata in `common.media`
- Swedish context review of the raï, reggae and rock metadata in `common.media`
- Swedish context review of the salsa, singer-songwriter, ska and soul metadata in `common.media`
- Swedish context review of the trap, waltz and meditation-music metadata in `common.media`
- Swedish completion of all 59 currently missing `common.media` music-genre descriptions: sound effects, soundtrack, spoken word, swing and tango; the visible `Soundtrack` label was corrected to `Filmmusik`
- Swedish context review of all 43 source-identical values: 42 are valid Swedish technical values, UI terms, folder names or established genre names; Flow Mode's sample-rate strategy was translated from `Smart` to `Intelligent`
- Swedish terminology normalization of the Smart Shuffle category from `Smart blandning` to `Intelligent blandning`
- Swedish review of Sendspin's delay setting: `Offset` and `Statisk uppspelningsfördröjning` were clarified as `Förskjutning` and `Fast uppspelningsfördröjning`
- Swedish terminology review of Music's background task `Scan genre mappings`, clarified as `Sök igenom genremappningar`
- Swedish normalization of the queue UI: `Smart shuffle` and `Smart crossfade` are consistently rendered as `Intelligent slumpning` and `Intelligent övertoning`; `smart uttag` remains an established home-automation term
- Swedish completion of 13 current-source keys for the Cache, Dashboard and Discovery modules, including cache clearing, dashboard casting and UPnP/SSDP network discovery
- Swedish completion of all 20 current-source Metadata-module keys: online and local metadata precedence, radio artwork, MusicBrainz linking, preferred language and thumbnail-cache limits
- Swedish completion of all seven current-source Player-module keys: announcement text-to-speech, adaptive volume steps and protocol-compatible group playback
- Swedish completion of all six current-source Statistics and Tasks module keys: listening analytics and bounded concurrent background work
- Swedish completion of the current-source Webserver module: self-registration, internal and external URLs, TLS certificates, reverse-proxy guidance and secure remote access; the changed `base_url` label is `Intern URL`
- Swedish completion of the first Streams-module batch: same-album crossfade, background-analysis concurrency, memory-buffer strategy, published IP address, intelligent-overtoning logging, source selection and quality thresholds
- Swedish completion of the remaining Streams-module keys: radio and track volume-normalization methods, fixed and fallback gain strategies, and the stream-processing module manifest
- Swedish completion of the Local Files provider: folder selection, media-content categories, library import options, overlap handling and storage errors
- Swedish completion of the Audiobookshelf provider: connection and authentication settings, server errors, library navigation and recommendation views
- Swedish completion of the Plex provider: local and account authentication, library selection, collections, stream quality, ratings, discovery and setup flow
- Swedish completion of the AirPlay provider: buffering, pairing, encryption, volume reporting, stream timing and remote-control setup
- Swedish completion of the Spotify configuration batch: stream quality, playback engines, Soloist setup, loudness normalization and listening-progress synchronization
- Swedish completion of the Spotify error-message batch: authentication, account and pairing recovery, API-key validation and Soloist playback failures
- Swedish completion of the Spotify setup flow: account connection, browser authorization, playback approval, pairing and Soloist consent
- Swedish completion of the Deezer configuration batch: ARL authentication, profiles, stream quality, queue continuation and recovery errors
- Swedish completion of the Deezer media batch: Flow, discovery, genres, personal and recommended playlists, and top-list navigation
- Swedish completion of the OpenSubsonic provider: connection and authentication settings, recommendations, raw-stream handling and connection errors
- Swedish completion of the Audible provider: marketplace selection, browser login, redirect handling, catalog and library navigation
- Swedish completion of the Last.fm Recommendations provider: refresh controls, chart configuration and personalized, genre and geographic recommendation views
- Swedish completion of the Bose SoundTouch provider: presets, media search, announcement key configuration and physical-button mapping
- Swedish completion of the gPodder provider: gPodder/opodsync and Nextcloud connection, account setup, authorization and errors
- Swedish completion of the Plex Connect provider: device registration, plex.tv linking, mobile discovery, ports and player exposure
- Swedish completion of the Hue Entertainment provider: Hue Bridge and ZHA setup, pairing, timing, visualization modes and multi-lamp synchronization
- Swedish completion of the Sonic Similarity provider: local audio-signature search, similarity presets, CLAP character index, free-text search and discovery rows
- Swedish completion of the Party provider: guest QR access, queue requests and prioritization, rate limits, karaoke mode, screen protection and playback modes
- Swedish completion of the FastMCP Server provider: MCP configuration, token policies, resources, connection wizard and reverse-proxy security controls
- Swedish completion of the Spotify Connect provider: playback engines, stream quality, volume handling, Soloist API-key setup and download consent
- Swedish completion of the OpenAI TTS provider: cloud and self-hosted speech APIs, models, audio formats, voices and error recovery
- Swedish completion of the AI Radio provider: AI and text-to-speech engines, presentation segments, timezone, weather forecast and audio-level controls
- Swedish completion of the Alexa provider: language selection, Amazon authentication, companion API credentials and Echo-device streaming
- Swedish completion of the OpenAI Compatible provider: API connection, model and image-model selection, local servers and service presets
- Swedish completion of the Music Quiz provider: quiz playback, players, AI-generated answer options, game validation and QR-code participation

## Checks

- JSON parsing passed.
- `l10n-lint` passed.
- Targeted `svlang` review found only known false positives for the product names AirPlay and TTS, and for valid Swedish inversion.
- Targeted `hunspell -d sv_SE -l` ran with `nice -n 10`; technical or product compounds such as `AirPlay` and `streamingtjänsten` are reviewed manually. No Hunspell process remained afterward.
- `git diff --check` and Gitleaks passed.
- Full-catalog checks found no target em dash that is absent from its source and no value with three consecutive identical consonants.
- The remaining source-identical values are verified UI terms, technical values, folder names or established genre names. The only remaining `smart` wording is the established home-automation term `smart uttag`.
- `msgfmt` is not applicable to this JSON catalog.

## Upstream status

Submitted as [music-assistant/server#7640](https://github.com/music-assistant/server/pull/7640), branch `yeager:l10n/sv-config-terminology-20261114`, latest commit `56958b8ac16f8aff3410d703a6f2f11812ae666e`.

The PR is open. Its checklist truthfully leaves the project's full pre-commit and pytest checks unchecked: the sparse review checkout lacks the repository runner and its Python 3.14 environment. Repository CI performs its checks separately. The PR has not received maintainer review or been merged.

All recorded batches have been pushed to the PR branch. The replacement CI run was requested by the latest push; it is not maintainer reviewed or merged.

The local Swedish export predates the current English source snapshot: it contains 1,034 keys while the current source contains 3,173. The current-source gaps are being added in reviewed batches; do not infer a fully current Swedish catalog from the older export's non-empty-value count.
