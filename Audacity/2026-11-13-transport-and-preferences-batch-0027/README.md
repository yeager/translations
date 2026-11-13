# Audacity – transport och inställningar, batch 28

Granskad rad för rad i Audacity 4.0.2:s svenska UI-katalog.

- 35 PO-poster ändrade i källkontext.
- Transport- och loopkommandon, uppspelningsövervakning, ljudinställningar, kataloger, effekter och utökad import har rättats.
- Flera sakfel i dB-intervall för PCM-samplingar har korrigerats.
- Källcommit: `631d723fae211ba79a89598ca24d8ab07faa105b`.
- Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759), öppen och inväntar obligatorisk upstreamgranskning vid arkiveringstillfället.

## Kontroller

`msgfmt --check`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll och Gitleaks kördes. Kvarvarande träffar i dessa kontroller är redan kända tekniska termer, tangentbordsmarkörer och formattext utanför batchens ändrade poster.
