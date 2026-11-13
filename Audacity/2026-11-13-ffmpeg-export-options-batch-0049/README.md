# Audacity: FFmpeg-exportalternativ

Tio aktiva PO-poster har granskats rad för rad i FFmpeg-exportens inställningar.
Batchen normaliserar `Sampla om`, nivåbenämningar, XML, sökfraser och svenska
bestämda former.

Källcommit: [`66d432e`](https://github.com/yeager/audacity/commit/66d432e928eea9ecd0a5d5a7df0eefd795cd0efe).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, l10n-lint, diffkontroll och Gitleaks passerade. l10n-lint har
inga fel; 40 äldre varningar återstår utanför batchen. PR:n är öppen och
väntar på obligatorisk upstreamgranskning. Den är inte mergad.
