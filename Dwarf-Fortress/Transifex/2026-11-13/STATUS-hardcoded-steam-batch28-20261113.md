# Dwarf Fortress Steam — hardcoded_steam — Swedish batch 28

- Date: 2026-11-13
- Scope: 33 context-safe untranslated strings, including freight terminology normalized to the project glossary: `Track Stop` = `spårstopp`, `Stockpile` = `förråd`, and `Minecart` = `gruvvagn`.
- Source: Transifex `dwarf-fortress-translation / dwarf-fortress-steam / hardcoded_steam`.
- Local validation: JSON syntax (`jq`), markup-tag parity, `l10n-lint`, Hunspell-Swedish, `gitleaks detect --no-git --redact`, and `git diff --no-index --check` passed. `msgfmt --check` passed against the local PO export, with its known non-fatal incomplete-header warnings.
- Submission: bulk PATCH accepted 33 translations.
- Verification: direct Transifex API readback matched 33/33 submitted translations exactly.
- Upstream state: received by Transifex; upstream review, finalization, and released-game publication remain unverified upstream states.
