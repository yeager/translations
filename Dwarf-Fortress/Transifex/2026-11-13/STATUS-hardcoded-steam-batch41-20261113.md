# Dwarf Fortress Steam, Swedish, batch 41

- Date: 13 November 2026
- Component: `hardcoded_steam`
- Scope: 23 context-safe interface, narrative, state and descriptive strings.
- Local checks: JSON parsing, `l10n-lint`, Hunspell Swedish word check, `gitleaks detect --no-git --redact`, and whitespace diff check passed. Hunspell listed `Mellan-` and `VILDSKAP`; both deliberately preserve the source's fragment or all-caps form.
- PO check: `msgfmt --check` passed for the downloaded PO export. Its incomplete metadata headers produced the known warnings for `Project-Id-Version`, `PO-Revision-Date`, and `MIME-Version`.
- Upstream: uploaded as one Transifex bulk API request; API response contained 23 imported records.
- Verification: direct API readback matched all 23 translations.
- State: saved upstream. Review, finalization and release state have not been verified.
