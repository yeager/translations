# Swedish review status

This copy is a reviewed working catalogue. It is not a direct export from CrowdIn and must be reconciled with the current upstream source before upload.

## Verified 2026-10-16

- 32,976 translated messages; `msgfmt --check --statistics` passes.
- 1,010 translations differ from the saved upstream baseline; no active message keys were added or removed.
- `l10n-lint` reports 0 errors and 188 warnings.
- `svlang skrivregler` reports 45 signals. They come from URLs, version and percentage values, markup syntax, code examples, machine-formatted dots, or the literal source string `—`.
- Gitleaks reports no secrets in the catalogue.
- No visible Crowdin context prefix has leaked into a translation. The remaining `|` characters are source syntax in notification text or regular expressions.
- No en dash or em dash remains in a Swedish translation, except the literal source string `—`.
- Direct Swedish imperatives are used in place of `Vänligen` and `Var god`; `ej` does not occur; and no comma directly precedes `och`.
- UI ellipses use `…` where they are prose rather than URLs, code patterns, or fixed-width formatting.

## Remaining lint warnings

The remaining warnings are review signals, not compilation errors. They are mainly:

- Swedish nouns with identical singular and plural forms, such as `projekt`, `fel`, and `år`.
- Product names, protocols, commands, placeholders, URLs, regular expressions, and version values that must remain unchanged.
- Context-dependent translations that intentionally differ between components.
- Heuristic length and punctuation signals around markup tags.

Each future upstream import should be checked again against the then-current source catalogue.
