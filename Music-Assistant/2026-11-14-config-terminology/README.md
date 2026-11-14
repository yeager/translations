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

## Checks

- JSON parsing passed.
- `l10n-lint` passed.
- Targeted `svlang` review found only known false positives for the product names AirPlay and TTS, and for valid Swedish inversion.
- Targeted `hunspell -d sv_SE -l` ran with `nice -n 10`; it flagged only AirPlay. No Hunspell process remained afterward.
- `git diff --check` and Gitleaks passed.
- `msgfmt` is not applicable to this JSON catalog.

## Upstream status

Submitted as [music-assistant/server#7640](https://github.com/music-assistant/server/pull/7640), branch `yeager:l10n/sv-config-terminology-20261114`, latest commit `12c927e7e3e02ba2a704315f636a3d99edcc1093`.

The PR is open. Its initial repository verification requests the project's full pre-commit and pytest checklist. Those commands are unavailable in the sparse review checkout, which lacks both the repository runner and its Python 3.14 environment; the PR body records that limitation rather than claiming checks that did not run. Repository lint passed; its three pytest jobs are still pending. It has not received maintainer review or been merged.
