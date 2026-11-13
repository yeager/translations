# Audacity: amplitudkurvor och kommandostatus

- Datum: 2026-11-13
- Källcommit: `72fc5d1`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 7 svenska PO-poster.

`Envelope` är normaliserat till **amplitudkurva** i kommandon, historik och hjälptext. Batchen gör också felstatusen för `FAIL` idiomatisk och använder liten bokstav efter kolon i ett parametermeddelande.

Kontroller: `msgfmt` (4 443 översatta poster), Hunspell-sv, l10n-lint, svlang, diffkontroll och Gitleaks. l10n-lint rapporterar 28 befintliga varningar utanför batchen.
