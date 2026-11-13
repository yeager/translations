# Audacity: verktyg och spårinställningar

- Datum: 2026-11-13
- Källcommit: `b40f2cb`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 6 svenska PO-poster för teman, spårinställningar och etikettspår.

Batchen använder **temaanpassning**, tydliggör den cykliska spårfokusinställningen, och normaliserar verktygs- och typsnittstermer. **Amplitude envelope** följer Audacitys etablerade svenska term **amplitudkurva**.

Kontroller: `msgfmt` (4 443 översatta poster), Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Hunspell-sv markerar endast den korrekta sammansättningen **amplitudkurvverktyg**. l10n-lint rapporterar 28 befintliga varningar utanför batchen.
