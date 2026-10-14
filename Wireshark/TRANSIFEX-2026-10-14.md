# Wireshark: Transifex import, 14 October 2026

`wireshark_sv-transifex-ready.ts` is a complete Qt TS import catalog based on
the current local Swedish Wireshark export. It completes 90 visible unfinished
strings, completes one empty internal Qt unit, and replaces four Swedish em
dashes with colons where the source does not use an em dash.

Validation completed:

- XML: `xmllint --noout`
- required translations and placeholders: `l10n-lint`
- Swedish dash check: no target-only em dashes
- secret scan: Gitleaks found no leaks

Upload this file to the Wireshark Swedish resource in Transifex. Read the
resource back after import before treating the upload as accepted.
