# Audacity – spår- och klippkontroller, batch 31

Granskad rad för rad i Audacity 4.0.2:s svenska UI-katalog.

- 54 PO-poster ändrade i källkontext.
- Fästning, taktarter, etikettspår, MIDI-notspår, klippgränser, tonhöjd, hastighet och tidsutsträckning har rättats.
- De två följdändringarna ersätter sammansättningar med tre identiska konsonanter med idiomatisk formulering.
- Källcommitar: `04763945d3de1f4f106e753766e42559f5143c7f` och `4874e02d10f433c41a84679164c0e4a58322e608`.
- Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759), öppen och inväntar obligatorisk upstreamgranskning vid arkiveringstillfället.

## Kontroller

`msgfmt --check`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll och Gitleaks kördes. Efter följdändringen finns inga nya träffar på tre identiska konsonanter i de ändrade etiketthandlingarna.
