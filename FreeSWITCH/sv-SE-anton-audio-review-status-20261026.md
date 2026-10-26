# FreeSWITCH Swedish Anton audio review status

This is a manuscript and review copy, not an audio package. All historical Anton package audio remains rejected after the user's report that recordings say the wrong words. No audio is approved or assigned to the package.

The current catalog has 296 active resources and two proposed voicemail resources requiring a source patch. Seven new 48 kHz mono PCM16 candidates have individual, hash-bound review controls: two are rejected (`ascii/100.wav`, `ascii/101.wav`) and five await human listening. The other 290 active references lack new recordings. The two proposed resources have no audio. Current candidate hashes, ASR triage and decisions are recorded in `sv-SE-current-audio-candidates-20261026.tsv`; ASR is not human approval.

The source review found a byte-encoding gate for `ä`, `å` and `ö` in `mod_say_sv.c:say_spell`: CP437 byte IDs map to legacy resources 132, 134 and 148, while UTF-8 produces different bytewise paths. The available checkout lacks a runtime test that establishes the actual caller encoding, so these three scripts remain drafts.

In PR #3242, the Swedish `voicemail_greeting_selected` macro still uses message-number and “marked” resources where the English macro selects a greeting. Two Swedish scripts and a focused XML patch are proposed; neither source change nor audio is integrated. PR #3243 changes the one-before-million resource to `digits/u-1`; it has no runtime confirmation. Both PRs remain open and review-required, with no checks or reviews reported at the latest check.
