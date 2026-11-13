# Dwarf Fortress Steam, Swedish, batch 37

- Date: 13 November 2026
- Component: `hardcoded_steam`
- Scope: 13 untranslated strings with sufficient in-game or narrative context.
- Local checks: JSON parsing, `l10n-lint`, Hunspell Swedish word check, `gitleaks detect --no-git --redact`, and whitespace diff check passed. Hunspell listed `-och-en-halv`; this is an intentional hyphenated fragment corresponding to the source fragment.
- PO check: `msgfmt --check` passed for the downloaded PO export. Its incomplete metadata headers produced the known warnings for `Project-Id-Version`, `PO-Revision-Date`, and `MIME-Version`.
- Upstream: uploaded as one Transifex bulk API request; API response contained 13 imported records.
- Verification: direct API readback matched all 13 translations.
- State: saved upstream. Review, finalization and release state have not been verified.
