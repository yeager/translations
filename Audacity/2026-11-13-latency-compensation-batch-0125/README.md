# Audacity: fördröjningskompensation

- Datum: 2026-11-13
- Källcommit: `c59a741`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 1 delad svensk PO-post i VST, VST3 och LV2.

Batchen normaliserar `Latency Compensation` till **fördröjningskompensation** i alla tre insticksmodulsgränssnitt. Det följer projektets terminologilista och skiljer funktionen från generell nätverkslatens.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Inga av verktygen träffar den ändrade posten.
