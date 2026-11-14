# Hermes Agent Swedish core locale — batch 01

Date: 2026-11-14
Source: upstream `main` at `abeeef4d491cba7ea6126a2f54d81c879da5059f`

## Scope

This locally reviewed delta contains 46 current core-locale entries for
approval, denial, timeout, prompt rewind and context-window feedback. It is
not an upstream submission.

The earlier Swedish core YAML contains 371 keys, of which 370 still match the
current English catalog. The current English catalog has 3,550 leaf keys, so
3,180 are absent from the old Swedish file. Hermes validates bundled TUI packs
against full key parity; publishing the obsolete partial catalog would be
incorrect. The Swedish catalog is therefore being rebuilt from the current
source in reviewed deltas before a complete YAML file and upstream change are
prepared.

## Checks

- JSON parse: passed.
- Placeholder parity against current `locales/en.yaml`: 46/46 passed.
- Hunspell-sv: only identifiers, placeholders, commands and product names.
- `l10n-lint`: one false positive for repeated `Esc` in a keyboard instruction.
- `svlang`: its file-mode analysis includes JSON keys, revision hash and
  placeholders; reported V2 cases are grammatical Swedish or imperative UI
  text and require no change.
- `git diff --no-index --check`: passed.
- `gitleaks detect --no-git --source … --redact`: passed; no leaks found.

`msgfmt` is not applicable: this is a JSON delta for a YAML catalog.

## Batch 02: billing and payment authorization

`core-billing-batch02.json` adds 65 current core-locale entries for cards,
balance top-ups, automatic reload, Remote Spending, role requirements and
payment failures. JSON syntax and 65/65 placeholder parity against the
current English catalog pass. `l10n-lint`, diff check and Gitleaks pass.
Hunspell and svlang only flag identifiers, placeholders, `3DS`, product names
or grammatical V2 false positives; no wording change is required.

## Upstream state

The web localization PR [#148618](https://github.com/NousResearch/hermes-agent/pull/148618)
and desktop localization PR [#101116](https://github.com/NousResearch/hermes-agent/pull/101116)
remain open as checked on 2026-11-14. Neither has a review decision or a
reported check run. This delta has not been uploaded because it is only one
reviewed portion of a catalog that must retain full key parity.
