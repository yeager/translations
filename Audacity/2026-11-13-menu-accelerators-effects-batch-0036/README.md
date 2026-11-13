# Audacity: menygenvägar och effektkontroller

59 PO-poster har granskats rad för rad i källkontext. Genomgången flyttar
menygenvägar från å, ä och ö till tillgängliga tangenter, lägger till saknade
menygenvägar och rättar några termer i effekt- och verktygsfältsdialoger.

Viktiga termbeslut:

- `Actual Compression` är `Faktisk komprimering`, inte den falska vännen
  `Aktuell komprimering`.
- `Wah Frequency Offset` är `wahwah-frekvensförskjutning`.
- `Resample` är åtgärden `Sampla om...`.
- `Render` behåller den etablerade Audacity-betydelsen `återge`.

Källcommit: [`230fab2`](https://github.com/yeager/audacity/commit/230fab2524f454aca4ef68cb3fb2ec2a7c7b3db4).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt --check --statistics`, avgränsad Hunspell-sv, `l10n-lint`, `svlang`,
diffkontroll och Gitleaks kördes. `msgfmt`, diffkontroll och Gitleaks
passerade. Hunspell-sv markerar endast det projektspecifika
`wahwah-frekvensförskjutning`, den sammansatta UI-termen
`spektrumsmarkering` och en F10-markör från Nyquist-dialogen. `l10n-lint`
har inga fel; dess 40 kvarvarande varningar är globala kontroller utanför den
här patchen. `svlang` används som triage och har kvar äldre tekniska
false positives i hela PO-filen.

PR:n är öppen och väntar på obligatorisk upstreamgranskning. Den är inte
mergad.
