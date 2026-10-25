# FreeSWITCH Swedish Anton script review draft

This branch stores the current in-progress, unapproved Swedish manuscript candidate set for a FreeSWITCH sound pack using ElevenLabs voice Anton - Warm, Confident & Friendly.

- `scripts.tsv` contains all 290 candidate prompts mapped to their FreeSWITCH paths. Every row remains marked for review. The Jakob ASR column is machine-generated, unverified, and only a comparison aid.
- Swedish `ascii/` candidates use letter names; the phonetic alphabet remains in `phonetic-ascii/`. The user clarified that standalone letter name G must have a hard /ɡ/ onset (/ɡeː/), distinct from the soft /j/ in the word `ge`. The review archives select `candidate-hard-g-1` at all four rates; the ordinary soft-j `ge` take is only a comparison. The wider package still needs human review.
- Nine voicemail candidates have meaning or idiom edits. All 290 entries remain drafts and need semantic and pronunciation review.
- Local Anton technical pilot: 57 of 290 prompts generated, with 228 WAV files across 48, 32, 16, and 8 kHz. Separate 57-prompt smoke archives were checked.
- A local review-only distribution now covers all 290 references with four 290-WAV archives at 8, 16, 32, and 48 kHz. It combines pilot masters with unapproved candidates and is not copied into this translation branch or approved for release. Its G asset uses the user-selected hard-/ɡ/ `candidate-hard-g-1` recording.
- Current package QA: all 290 prompts have at least one generated audio candidate, but all scripts still need human review and most audio candidates remain unapproved. All 290 selected source hashes and 1,160 SoX rate conversions were checked against the staged package (maximum sample difference: 2 PCM units from independent dithering), and all 1,160 archive members match the staged files byte for byte. The archives also passed path, mono PCM16 format, rate, checksum, silence, and clipping checks; live FreeSWITCH calls have not been tested.
- ElevenLabs’ current EEA terms grant paid-plan commercial use of generated Output, but its Prohibited Use Policy also bars making Output available to third parties on terms more permissive than ElevenLabs’. Because a FreeSWITCH sound package redistributes isolated files under an open license, written confirmation for that use is still needed. Lisa’s Lessac-derived voice/output rights are a separate unresolved issue.
- Local text QA checked 290 entries with `l10n-lint` (0 errors, 0 warnings) and `svlang skrivregler` (no findings). Hunspell flagged nine spoken names/short forms (`Qvintus`, `eff`, `ell`, `em`, `err`, `ji`, `ku`, `kå`, `pe`), which still need pronunciation review.
- Still required: human script approval and audio listening review, written redistribution clearance, live FreeSWITCH testing, and upstream packaging/CI validation. As checked on 2026-10-25, PR #3242 and #3243 are open, non-draft, and marked mergeable. GitHub returned no combined status checks, reviews, or inline review threads for either head.

`glossary.tsv` records the package terms used for linting: `voicemail` → `röstbrevlåda`, `extension` → `anknytning`, `inbox` → `inkorg`, and `email` → `e-post`.

Related FreeSWITCH changes remain open: [PR #3242](https://github.com/signalwire/freeswitch/pull/3242) and [PR #3243](https://github.com/signalwire/freeswitch/pull/3243).
