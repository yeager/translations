# Audacity – spektrogram och verktygsfält, batch 30

Granskad rad för rad i Audacity 4.0.2:s svenska UI-katalog.

- 29 PO-poster ändrade i källkontext.
- Spektrogramparametrar, nollutfyllnad, frekvensförstärkning, vågformsvisning, ljudinställningar, statusfält och verktygsfält har rättats.
- Källcommit: `b11fe2fe75c531c1e336469acd6eecfab521d642`.
- Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759), öppen och inväntar obligatorisk upstreamgranskning vid arkiveringstillfället.

## Kontroller

`msgfmt --check`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll och Gitleaks kördes. Kvarvarande träffar rör avsedda tekniska termer, formatnamn och redan existerande katalogposter.
