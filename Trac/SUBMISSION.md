# Trac Swedish update, 2026-10-15

Submit `trac-sv-review-20261015.patch` as an attachment to the existing
[Swedish translation coordination ticket #5487](https://trac.edgewall.org/ticket/5487).

The patch updates the current `sv` catalogs:

- `messages.po`
- `messages-js.po`
- `tracini.po`

Validation completed before creating the patch:

- `msgfmt --check --statistics` for all three catalogs
- Trac's catalog checks have no translation errors from `l10n-lint`
- no untranslated active strings
- `git apply --check` against a clean current checkout
- Gitleaks scan of the catalog directory

Suggested ticket comment:

> Updated Swedish `sv` catalogs for the current source tree. The attached patch
> covers `messages.po`, `messages-js.po` and `tracini.po`; all active strings
> are translated. I validated it with `msgfmt --check`, applied it cleanly to a
> fresh checkout, and checked placeholders and markup.
