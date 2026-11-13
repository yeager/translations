# Audacity: molnsynk och Om-dialogen

Fjorton aktiva PO-poster har granskats rad för rad. Batchen rättar språk i
molnuppladdning och synkronisering, använder ”läs in” i rätt UI-kontext och
förtydligar bygg-, format- och funktionsinformation i Om-dialogen.

Källcommit: [`d3f5843`](https://github.com/yeager/audacity/commit/d3f5843).
Ändringen är pushad till [audacity/audacity#12759](https://github.com/audacity/audacity/pull/12759).

`msgfmt`, avgränsad Hunspell-sv-kontroll, l10n-lint, svlang, diffkontroll och
Gitleaks passerade. Hunspell markerar format- och domännamn, bland annat
`FFmpeg` och `audio.com`. l10n-lint har inga fel och 29 befintliga varningar
utanför batchen. PR:n är öppen och inväntar obligatorisk upstreamgranskning;
den är inte mergad.
