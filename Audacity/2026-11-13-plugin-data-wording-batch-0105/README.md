# Audacity: statusrubriker och samplingsfält i plug-in-avsnittet

- Datum: 2026-11-13
- Källcommit: `c5a3efd`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 5 svenska PO-poster i Nyquist-insticksmoduler.

Batchen gör statusrubrikerna idiomatiska, förtydligar att datautmatning avses och ersätter det krystade "Samplenr" med **Samplingsnummer**.

Kontroller: `msgfmt` (4 443 översatta poster), Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. l10n-lint rapporterar 28 befintliga varningar utanför batchen; varken l10n-lint eller svlang träffar någon ändrad sträng.
