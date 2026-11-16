# Home Assistant Swedish LIFX Worldly batch 121

This batch contains all 146 Swedish translations that were still empty on 16 November 2026 and whose English source begins with `Worldly >`.

The wording is taken from the already reviewed Worldly entries in the local Home Assistant archive. It retains the UI label as `Världsligt >` and uses established Swedish country and region names.

## Verification

- Candidate count, JSON structure and placeholder parity: passed (146 entries)
- `l10n-lint`: passed
- `svlang`: inspected; its sentence-level warnings are structural false positives caused by treating the 146 short labels as one text block. Its only lexical flags are expected names and the UI label.
- `hunspell-sv`: inspected; `Eswatini` is an expected proper name absent from the dictionary.
- `git diff --check`: passed
- `gitleaks`: passed
- `msgfmt`: not applicable; this is a Lokalise JSON/API batch.

## Upstream result

All 146 entries were saved through the Lokalise API with `is_unverified: false` and each entry was immediately read back by its translation ID. A fresh scan of every currently untranslated Swedish record then found **zero** remaining sources beginning with `Worldly >` (2,281 unrelated untranslated records remain).
