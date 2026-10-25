# FreeSWITCH Swedish Anton script review draft

This folder contains an in-progress, unapproved Swedish manuscript candidate set for a FreeSWITCH sound pack using ElevenLabs voice Anton - Warm, Confident & Friendly.

- `scripts.tsv` has 290 candidate prompts mapped to FreeSWITCH paths.
- All entries are marked for review. The Jakob ASR column is machine-generated and unverified; it is only a comparison aid.
- 116 rows are prioritized for review because the reference ASR is empty or has low confidence.
- The only generated Anton audio currently is one 8 kHz technical pilot. The 290-file pack, listening review, full-rate builds, live FreeSWITCH test, and redistribution-rights review remain incomplete.
- Local QA: `l10n-lint` checked 290 entries with no typo/terminology findings; `svlang skrivregler` reported no writing-rule findings; Hunspell flagged only `Qvintus`, a proper name requiring pronunciation review.

Related upstream FreeSWITCH changes remain open: [PR #3242](https://github.com/signalwire/freeswitch/pull/3242) and [PR #3243](https://github.com/signalwire/freeswitch/pull/3243).