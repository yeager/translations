# Dwarf Fortress Steam, Swedish, batch 42

- Date: 13 November 2026
- Component: `hardcoded_steam`
- Scope: 38 context-safe interface, gameplay, descriptive and narrative strings.
- Local checks: JSON parsing, `l10n-lint`, Hunspell Swedish word check, `gitleaks detect --no-git --redact`, and whitespace diff check passed.
- PO check: `msgfmt --check` passed for the downloaded PO export. Its incomplete metadata headers produced the known warnings for `Project-Id-Version`, `PO-Revision-Date`, and `MIME-Version`.
- Upstream: uploaded as one Transifex bulk API request; API response contained 38 imported records.
- Verification: direct API readback matched all 38 translations.
- State: saved upstream. Review, finalization and release state have not been verified.
