# Rust Coreutils, Swedish Weblate component batch 01

Whole current component files were reviewed against the English Fluent reference at
`uutils/coreutils-l10n` commit `a981da82eaf5328028c781333e8cc285d3221d09`
(2026-11-02).  Weblate's public API was rate-limited during status collection, so
the files are prepared as separate component uploads rather than a bulk import.

| Component | Added Swedish messages | Validation | SHA-256 |
| --- | ---: | --- | --- |
| `join` | 1 | Fluent lint and `svlang` pass | `4edc3abe4a41d7fae1f7dc02e1da9384a0f23fbc46780beda76d3ca94e843e41` |
| `tr` | 2 | Fluent lint and `svlang` pass | `75e1566b5075874a08444340e203e092093634f46956046ebfe672d51f96724f` |
| `fmt` | 1 | Fluent lint and `svlang` pass | `b1a764b23d24ce6df01b5f778a70a940bf140467e3ce561190cf712b70f7eb90` |
| `ln` | 1 | Fluent lint and `svlang` pass | `ad256c0de3863f0bc231657ef8e3a9c0d513fcc06196cddb1a9cc90230ece5a3` |
| `sort` | 2 | Fluent lint and `svlang` pass | `669ffd7e601c4916888a1d5bbe951ccebdc07de37ca1a5176457c760a82ed67b` |

`hunspell-sv` flags command syntax (`-n`) and technical identifiers
(`sträng2`, `tabbstopp`); these were reviewed in context and retained.

The five `.ftl` files were instead rebased onto current upstream and submitted
directly as [uutils/coreutils-l10n PR #96](https://github.com/uutils/coreutils-l10n/pull/96)
on 2026-11-02. The PR is the upstream submission; Weblate import remains
unnecessary for this batch.
