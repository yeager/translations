# Audacity: Benchmark, beroenden och frekvensanalys

- Datum: 2026-11-13
- Källcommit: `77c377b`
- PR: [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759)
- Omfattning: 6 svenska PO-poster i Benchmark, brusprofilinstruktionen, beroendehantering och frekvensanalys.

Batchen skiljer ett **godkänt** riktighetstest från ett test som enbart har slutförts, gör brusprofilens två steg till direkta markeringar och återger `Removing Dependencies` som beroendehantering i stället för att felaktigt påstå att externa filer tas bort. Frekvensanalysens `Peak` är ett **topp**värde; terminologilistan har kompletterats för den UI-etiketten.

Kontroller: `msgfmt` (4 443 översatta poster), avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och Gitleaks. Varken Hunspell-sv, l10n-lint eller svlang träffar någon ändrad sträng.
