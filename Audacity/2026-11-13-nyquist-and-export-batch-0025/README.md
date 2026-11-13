# Audacity – Nyquist och exportdialoger, batch 26

Granskad rad för rad i Audacity 4.0.2:s svenska UI-katalog.

- 47 PO-poster ändrade i källkontext.
- Nyquist- och Vamp-fel, spektrala effekter, skript och felsökningsutdata har normaliserats.
- Exportdialoger, rådataimport, byteordning, samplingsfrekvens, kanalmappning och klipphantering har fått idiomatisk och konsekvent svenska.
- Källcommit: `a4260ee8aced92bde59bb1162f9d58b5c966a27a`.
- Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759), öppen och inväntar obligatorisk upstreamgranskning vid arkiveringstillfället.

## Kontroller

`msgfmt --check`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll och Gitleaks kördes. Hunspell- och svlang-träffar i batchen består av avsedda formatnamn, mnemonikfragment, kod och tekniska termer; inga nya sakfel hittades.
