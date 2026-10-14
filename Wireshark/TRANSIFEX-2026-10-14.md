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

One l10n-lint warning remains. It concerns an intentional leading blank in a UI fragment and is not a Swedish prose defect.

Upload this file to the Wireshark Swedish resource in Transifex. Read the
resource back after import before treating the upload as accepted.
