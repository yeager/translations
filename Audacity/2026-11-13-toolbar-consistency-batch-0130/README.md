# Audacity: konsekventa verktygsfält

- Datum: 2026-11-13
- Källcommit: `5b1adc0`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 2 svenska PO-poster i kontroll- och verktygsfälten.

Batchen samordnar **Append Record** med transportmenyns **Fortsätt spela in** och ersätter den avvikande termen *enveloppverktyg* med den etablerade **amplitudkurvverktyg**.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Hunspell-sv känner inte igen den avsiktliga facktermen *amplitudkurvverktyg*; den finns dokumenterad i projektets terminologi. Övriga kontroller träffar ingen ändrad post.
