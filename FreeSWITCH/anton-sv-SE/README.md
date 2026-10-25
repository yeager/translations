# FreeSWITCH Swedish Anton script review draft

This folder contains an in-progress, unapproved Swedish manuscript candidate set for a FreeSWITCH sound pack using ElevenLabs voice Anton - Warm, Confident & Friendly.

- `scripts.tsv` has 290 candidate prompts mapped to FreeSWITCH paths.
- All entries are marked for review. The Jakob ASR column is machine-generated and unverified; it is only a comparison aid.
- 116 rows are prioritized for review because the reference ASR is empty or has low confidence.
- Local audio pilot: 7 of 290 prompts generated. Each has a lossless 48 kHz master and an 8 kHz version. A 2026-10-25 date sequence was assembled at both rates following the `mod_say_sv` file order. Whisper small agrees with most individual prompts but mishears the short `tjugo` prompt; listening review remains necessary.
- The audio files and sequence demo are in the local deliverable, not this repository branch. The complete sound pack, human script approval, listening review, full distribution builds, live FreeSWITCH test, and redistribution-rights review remain incomplete.
- Local QA: `l10n-lint` checked 290 entries with no typo/terminology findings; `svlang skrivregler` reported no writing-rule findings; Hunspell flagged only `Qvintus`, a proper name requiring pronunciation review.

Related upstream FreeSWITCH changes remain open: [PR #3242](https://github.com/signalwire/freeswitch/pull/3242) and [PR #3243](https://github.com/signalwire/freeswitch/pull/3243).