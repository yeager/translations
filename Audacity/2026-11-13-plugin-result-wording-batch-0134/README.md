# Audacity: resulttexter från Nyquist-effekter

- Datum: 2026-11-13
- Källcommit: `b07c9ed`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 2 svenska PO-poster i grind- och samplingsdataeffekter.

Batchen gör grindfrekvensens feltext konsekvent med parameternamnet och ändrar exportsignaturen till den idiomatiska formuleringen **Skapad med**. Nyquist-markörer och HTML-taggar är oförändrade.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Inga av verktygen träffar någon ändrad post.
