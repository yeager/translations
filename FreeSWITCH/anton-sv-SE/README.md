# FreeSWITCH Swedish Anton script review draft

This branch stores the current in-progress, unapproved Swedish manuscript candidate set for a FreeSWITCH sound pack using ElevenLabs voice Anton - Warm, Confident & Friendly.

- `scripts.tsv` contains all 290 candidate prompts mapped to their FreeSWITCH paths. Every row remains marked for review. The Jakob ASR column is machine-generated, unverified, and only a comparison aid.
- Swedish `ascii/` candidates use letter names; the phonetic alphabet remains in `phonetic-ascii/`. The letter G has a pronunciation exception: use a hard /ɡ/ (/ɡeː/), clearly distinct from the soft /j/ in the word `ge` (/jeː/). Four G candidates are available locally, including a tight-crop alternate that reduces carry-over from the preceding vowel. The three-way comparison preview and all G takes still await human listening approval.
- Nine voicemail candidates have meaning or idiom edits. All 290 entries remain drafts and need semantic and pronunciation review.
- Local Anton technical pilot: 57 of 290 prompts generated, with 228 WAV files across 48, 32, 16, and 8 kHz. Separate 57-prompt smoke archives were checked.
- A local review-only distribution now covers all 290 references with four 290-WAV archives at 8, 16, 32, and 48 kHz. It combines pilot masters with unapproved candidates and is not copied into this translation branch or approved for release. The selected G asset in those archives is the original inline-IPA hard-/ɡ/ crop, pending human listening; the newer tight-crop alternate has not been promoted into them.
- Current package QA: all 290 prompts have at least one generated audio candidate, but all scripts still need human review and most audio candidates remain unapproved. The review archives passed path, mono PCM16 format, rate, checksum, silence, and clipping checks; live FreeSWITCH calls have not been tested.
- ElevenLabs’ current EEA terms grant paid-plan commercial use of generated Output, but its Prohibited Use Policy also bars making Output available to third parties on terms more permissive than ElevenLabs’. Because a FreeSWITCH sound package redistributes isolated files under an open license, written confirmation for that use is still needed. Lisa’s Lessac-derived voice/output rights are a separate unresolved issue.
- Local text QA checked 290 entries with `l10n-lint` (0 errors, 0 warnings) and `svlang skrivregler` (no findings). Hunspell flagged nine spoken names/short forms (`Qvintus`, `eff`, `ell`, `em`, `err`, `ji`, `ku`, `kå`, `pe`), which still need pronunciation review.
- Still required: human script approval and audio listening review, written redistribution clearance, live FreeSWITCH testing, and upstream packaging/CI validation. PR #3242 and #3243 remain open, `REVIEW_REQUIRED`, and blocked for merge; GitHub returned no review records or status checks on 2026-10-25.

`glossary.tsv` records the package terms used for linting: `voicemail` → `röstbrevlåda`, `extension` → `anknytning`, `inbox` → `inkorg`, and `email` → `e-post`.

Related FreeSWITCH changes remain open: [PR #3242](https://github.com/signalwire/freeswitch/pull/3242) and [PR #3243](https://github.com/signalwire/freeswitch/pull/3243).
