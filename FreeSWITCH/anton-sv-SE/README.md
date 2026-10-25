# FreeSWITCH Swedish Anton script review draft

This branch stores the current in-progress, unapproved Swedish manuscript candidate set for a FreeSWITCH sound pack using ElevenLabs voice Anton - Warm, Confident & Friendly.

- `scripts.tsv` contains all 290 candidate prompts mapped to their FreeSWITCH paths. Every row remains marked for review. The Jakob ASR column is machine-generated, unverified, and only a comparison aid.
- Swedish `ascii/` candidates use letter names; the phonetic alphabet remains in `phonetic-ascii/`. The letter G has a pronunciation exception: use a hard /ɡ/ (/ɡeː/), not the soft-j sound in the plain-spelling word `ge`. The IPA candidate is still awaiting human listening approval.
- Nine voicemail candidates have meaning or idiom edits. All 290 entries remain drafts and need semantic and pronunciation review.
- Local Anton technical pilot: 57 of 290 prompts generated, with 228 WAV files across 48, 32, 16, and 8 kHz. The separate distribution archives are smoke builds with 57 prompts each, not release packages.
- The local pilot and pronunciation candidates are not copied into this branch. No candidate audio is approved for the complete package.
- Local text QA checked 290 entries with `l10n-lint` (0 errors, 0 warnings) and `svlang skrivregler` (no findings). Hunspell flagged nine spoken names/short forms (`Qvintus`, `eff`, `ell`, `em`, `err`, `ji`, `ku`, `kå`, `pe`), which still need pronunciation review.
- Still required: human script approval, full audio generation and listening review, complete distribution builds, redistribution-rights review, live FreeSWITCH testing, and release CI validation.

`glossary.tsv` records the package terms used for linting: `voicemail` → `röstbrevlåda`, `extension` → `anknytning`, `inbox` → `inkorg`, and `email` → `e-post`.

Related FreeSWITCH changes remain open: [PR #3242](https://github.com/signalwire/freeswitch/pull/3242) and [PR #3243](https://github.com/signalwire/freeswitch/pull/3243).
