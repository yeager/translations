# Audacity: svenska roll- och samplingsord

- Datum: 2026-11-13
- Källcommit: `41c01af`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 7 svenska PO-poster i krediter, benchmarkdiagnostik och spårinställningar.

Batchen ersätter onödiga engelska lån: **formgivare** och **användarstöd** används i krediterna, medan det kontextspecifika tekniska begreppet **samplingsvärde** används för ett enskilt digitalt ljudvärde eller dess index.

Kontroller: `msgfmt` (4 443 översatta poster), Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Hunspell-sv markerar endast formatplatshållaren `lld`. svlang ger en isolerad träff på det korrekta begreppet ”samplingsvärde”; l10n-lint träffar ingen ändrad sträng.
