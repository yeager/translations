# Audacity: tids- och efterklangseffekter

- Datum: 2026-11-13
- Källcommit: `919ed18`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 9 svenska PO-poster i Paulstretch, Phaser, Reparera, Upprepa, Efterklang och Trunkera tystnad.

Batchen rättar bestämd form och synliga kontrollnamn i Paulstretch, använder **startfas** och **toppamplitud**, samt gör beskrivningarna av efterklang och tystnadsförkortning idiomatiska.

Kontroller: `msgfmt` (4 443 översatta poster), Hunspell-sv, l10n-lint, svlang, diffkontroll och Gitleaks. l10n-lint rapporterar 28 befintliga varningar utanför batchen.
