# Wagtail, svenska på Transifex

- Version: Wagtail 8.1, publicerad 2026-11-02.
- Omfattning: 13 tidigare oöversatta UI-strängar.
- Resurser: `wagtailadmin` (9), `wagtaildocs` (2), `wagtailtypedtableblock` (1) och `wagtailadminjs` (1 pluralpost).
- Status: uppladdat och återläst via Transifex API. Samtliga fyra resurser har 0 oöversatta svenska strängar efter uppladdningen. Formell upstream-granskning är inte verifierad.

## Terminologi

- `page metadata`: sidmetadata
- `meta tags`: metataggar
- `workflow action`: arbetsflödesåtgärd
- `typed table block`: typat tabellblock i Wagtail

## Kontroller

- Platshållare, HTML-markup och pluralformer: bevarade och kontrollerade.
- `l10n-lint`: inga fel.
- `svlang`: inga anglicismer; återstående stilträffar uppkommer av sammanfogade UI-fragment och HTML-attribut.
- `hunspell-sv`: endast metadata-termer och markup.
- `git diff --check` och Gitleaks: godkända.
- `msgfmt`: ej tillämpligt; API-underlaget är JSON.
