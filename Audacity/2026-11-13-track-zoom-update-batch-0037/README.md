# Audacity: spår, zoom och uppdateringar

Sju PO-poster har granskats rad för rad i källkontexten för spårhantering,
zoom, uppdateringsdialoger och verktygsfält.

- `Grabber` är `draghandtag`, eftersom kontrollen är en greppyta som används
  för att dra ett verktygsfält eller spår.
- Zoominstruktionerna är skrivna som naturliga svenska uppmaningar.
- Uppdateringsdialogen använder `ansluta till` i stället för det krystade
  `koppla upp mot`.

Källcommit: [`7ea2417`](https://github.com/yeager/audacity/commit/7ea2417e0dadfbf308e15831ee204d265f2126bb).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt --check --statistics`, avgränsad Hunspell-sv, `l10n-lint`, `svlang`,
diffkontroll och Gitleaks kördes. `msgfmt`, diffkontroll och Gitleaks
passerade. Hunspell-sv markerar bara produktnamnet `Audacitys`. `l10n-lint`
har inga fel; dess 40 kvarvarande varningar är globala kontroller utanför den
här patchen. `svlang` används som triage och har kvar äldre tekniska
false positives i hela PO-filen.

PR:n är öppen och väntar på obligatorisk upstreamgranskning. Den är inte
mergad.
