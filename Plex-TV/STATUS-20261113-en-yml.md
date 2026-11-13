# Plex TV, Swedish `en.yml` status

Checked and submitted on 2026-11-13 through the Transifex API.

The resource `o:plex-1:p:plex_tv:r:enyml` had one untranslated Swedish
string, added at 2026-11-13T18:15:27Z:

| Key | Source | Swedish |
| --- | --- | --- |
| `activerecord.errors.models.profile.invalid_clear_logos_visibility` | `invalid value for clear logos visibility` | `Ogiltigt värde för visning av titellogotyper` |

Plex documents Clear Logos as title art on content-detail pages. The Swedish
target uses *titellogotyper*, which describes that UI concept rather than
leaving an unexplained English feature label.

## Validation

- Ruby YAML parser: passed.
- Hunspell-SV: passed with no unknown target words.
- `git diff --check`: passed.
- Gitleaks: passed for the candidate file.
- `l10n-lint`: unavailable for YAML input; it reports the format as
  unsupported.
- `svlang`: its YAML-key and English-comment findings are false positives;
  the target sentence was reviewed directly.

## Upstream readback

The Transifex PATCH response and subsequent direct GET show the exact target
text with origin `API` at `2026-11-13T19:08:06Z`. A filtered API query then
returned 0 untranslated strings. Current resource statistics are
**1,712/1,712 translated**, 0 untranslated, and 0 formally reviewed.

This confirms submission and visibility in Transifex, not project review,
release, or merge.
