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
- `Smart blandning` for the recency-aware queue algorithm and `Upptäck` for the recommendation row
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

## Checks

- JSON parsing passed.
- `l10n-lint` passed.
- Targeted `svlang` review found only known false positives for the product names AirPlay and TTS, and for valid Swedish inversion.
- Targeted `hunspell -d sv_SE -l` ran with `nice -n 10`; it flagged only AirPlay. No Hunspell process remained afterward.
- `git diff --check` and Gitleaks passed.
- `msgfmt` is not applicable to this JSON catalog.

## Upstream status

Submitted as [music-assistant/server#7640](https://github.com/music-assistant/server/pull/7640), branch `yeager:l10n/sv-config-terminology-20261114`, latest commit `949b1903dac8a650cee5e791ce73e720f338ed36`.

The PR is open. Its checklist truthfully leaves the project's full pre-commit and pytest checks unchecked: the sparse review checkout lacks the repository runner and its Python 3.14 environment. Repository CI performs its checks separately. The PR has not received maintainer review or been merged.
