# Audacity: Fördröjning och efterklang

En aktiv post i effektmenyn har granskats i sin källkontext.
`Delay and Reverb` använder nu samma svenska termer som de enskilda
effekterna: `Fördröjning och efterklang`.

Källcommit: [`e8d6c49`](https://github.com/yeager/audacity/commit/e8d6c4917683566612a4cee658e378442ae4cecb).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och
Gitleaks kördes. `msgfmt`, diffkontroll och Gitleaks passerade. `l10n-lint`
har inga fel; de 40 kvarvarande varningarna gäller andra delar av katalogen.
PR:n är öppen och väntar på obligatorisk upstreamgranskning. Den är inte
mergad.
