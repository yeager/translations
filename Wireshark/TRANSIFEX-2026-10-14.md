# Wireshark: Transifex import, 14 October 2026

`wireshark_sv-transifex-ready.ts` is a complete Qt TS import catalog based on
the current local Swedish Wireshark export. It completes 90 visible unfinished
strings, completes one empty internal Qt unit and makes 106 source-key changes
in total. This includes 4 replacements of Swedish em dashes with colons where
the source does not use an em dash.

Validation completed:

- XML: `xmllint --noout`
- 4,445 live messages: l10n-lint reports 0 errors
- Changed Swedish text: svlang has no writing-rule findings
- Hunspell findings were reviewed as product names, protocols, identifiers and
  technical terms
- secret scan: Gitleaks found no leaks

l10n-lint reports 0 errors and 0 warnings with l10n-lint 1.23.6.

Upload this file to the Wireshark Swedish resource in Transifex. Read the
resource back after import before treating the upload as accepted.
