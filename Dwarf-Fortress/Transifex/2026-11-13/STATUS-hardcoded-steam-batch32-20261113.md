# Dwarf Fortress Steam — hardcoded_steam — Swedish batch 32

- Date: 2026-11-13
- Scope: 38 context-safe untranslated strings.
- Source: Transifex `dwarf-fortress-translation / dwarf-fortress-steam / hardcoded_steam`.
- Local validation: JSON syntax (`jq`), `l10n-lint`, Hunspell-Swedish, `gitleaks detect --no-git --redact`, and `git diff --no-index --check` passed. `msgfmt --check` passed against the local PO export, with its known non-fatal incomplete-header warnings.
- Submission: an initial bulk PATCH was rejected before import because Transifex returned an invalid 31-hex-character translation identifier for `A poetry competition`; it was omitted from this delta. The retry bulk PATCH accepted 38 translations.
- Verification: direct Transifex API readback matched 38/38 submitted translations exactly.
- Remaining upstream defect: the malformed identifier must be corrected server-side before that one string can be submitted through the API.
- Upstream state: the 38 accepted translations are received by Transifex; upstream review, finalization, and released-game publication remain unverified upstream states.
