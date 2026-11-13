# Obtainium – kategori- och appåtgärder

Datum: 2026-11-14
Komponent: `assets/translations/sv.json`
Källversion: `v1.7.4`, publicerad 2026-11-01

## Granskning

Den här batchen översätter 16 svenska etiketter och åtgärder för kategorier,
applistan och appstatus. Källkodens användning har kontrollerats i listvyn,
kategoriredigeraren, appvyn och inställningarna.

"Svepåtgärder" och "applistan" är medvetna UI-sammansättningar. Hunspell-sv
och svlang saknar dem i sina generella ordlistor, men de är korrekta i
Obtainiums kontext.

## Kontroller

- JSON-syntax: godkänd
- `l10n-lint`: godkänd
- Hunspell-sv: projekttermer granskade manuellt
- `svlang`: inga grammatiska fel; två kända ordlistevarningar
- `git diff --check`: godkänd
- Gitleaks: godkänd
- `msgfmt`: inte tillämpligt på JSON

## Upstream

Ändringarna är inskickade som
[ImranR98/Obtainium#3518](https://github.com/ImranR98/Obtainium/pull/3518).
PR:en är öppen; upstreamgranskning och merge återstår.
