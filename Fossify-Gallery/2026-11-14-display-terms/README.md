# Fossify Gallery — Swedish display terms, 2026-11-14

The work was added to the existing upstream pull request rather than creating
a competing translation pull request.

## Reviewed changes

- `Deep zoomable images` → `Bilder med djupzoom`.
- `Show a notch if available` → `Visa skärmutskärning om tillgänglig`.
- `Show file count in brackets` → `Visa filantal i parenteser`.
- The FAQ now uses the same `Bilder med djupzoom` label as the setting.

## Validation

- `xmllint --noout`: passed.
- `l10n-lint`: passed.
- Targeted Hunspell-sv was run at low CPU priority; the four reviewed terms
  were accepted and no Hunspell process remained afterwards.
- `git diff --check`: passed.
- Gitleaks: passed.
- Android resource processing could not run locally because this machine has
  no Java runtime. The pushed commit was subsequently verified by upstream CI:
  Android lint, tests, Detekt, wrapper validation, and the CI gate all passed.

## Upstream status

The commit `3af7b88d5fc7bb5abf5f0a83e3e846c6b3eb2e88` was pushed to the
existing branch for [FossifyOrg/Gallery PR #1223](https://github.com/FossifyOrg/Gallery/pull/1223).
The pull request remains open; it has not been upstream reviewed or merged.
