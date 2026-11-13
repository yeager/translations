# Audacity: navigeringskommandon

- Datum: 2026-11-13
- Källcommit: `b15489b`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 6 svenska PO-poster i navigeringsmenyn.

Batchen beskriver korrekt att kommandona växlar mellan aktiva fönster och växlar markeringen av det aktuella spåret. Kommandona som flyttar fokus med markering anger nu också vilket spår som markeras.

Kontroller: `msgfmt` (4 443 översatta poster), Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. l10n-lint rapporterar 28 befintliga varningar utanför batchen.
