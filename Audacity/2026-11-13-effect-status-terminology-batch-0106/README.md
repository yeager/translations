# Audacity: status- och intervallterminologi för effekter

- Datum: 2026-11-13
- Källcommit: `2f4ebe4`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 6 svenska PO-poster i effekt- och plug-in-avsnitt.

Batchen skiljer korrekt mellan **faktisk** och **aktuell** komprimering, använder svensk intervallnotation och bevarar utropstecknet i WavPack-felmeddelandet. Statusmeddelandet för tillämpat kommando har också fått idiomatisk svensk ordföljd.

Kontroller: `msgfmt` (4 443 översatta poster), Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Hunspell-sv markerar endast produktnamnskombinationen ”WavPack-filen”. Varken l10n-lint eller svlang träffar någon ändrad sträng.
