# Audacity: Återgivning och importdiagnostik

Sju aktiva PO-poster har granskats rad för rad i källkontext. Batchen
normaliserar `Render` till `återge`, rättar filtypssammansättningar och
förenklar två importdiagnostiska meddelanden.

Källcommit: [`30d8c71`](https://github.com/yeager/audacity/commit/30d8c71a670ba5e8792ee80a2269ff2c0b1d18fc).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv, `l10n-lint`, `svlang`, diffkontroll och
Gitleaks kördes. `msgfmt`, diffkontroll och Gitleaks passerade. `l10n-lint`
har inga fel; de 40 kvarvarande varningarna gäller andra delar av katalogen.
PR:n är öppen och väntar på obligatorisk upstreamgranskning. Den är inte
mergad.
