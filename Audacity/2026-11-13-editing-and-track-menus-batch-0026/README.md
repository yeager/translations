# Audacity – redigerings- och spårmenyer, batch 27

Granskad rad för rad i Audacity 4.0.2:s svenska UI-katalog.

- 45 PO-poster ändrade i källkontext.
- Klipp-, redigerings-, fil-, hjälp-, etikett-, insticksmoduls- och spårmenyer har rättats.
- Svenska menyverb, mnemoniker, klippterminologi, säkerhetskopiering, realtidseffekter och återgivning har normaliserats.
- Källcommit: `1b46705bcc28d4f0108bff12ab6b2067b814123f`.
- Upstream: [Audacity PR #12759](https://github.com/audacity/audacity/pull/12759), öppen och inväntar obligatorisk upstreamgranskning vid arkiveringstillfället.

## Kontroller

`msgfmt --check`, avgränsad Hunspell-sv-kontroll, `l10n-lint`, `svlang`, diffkontroll och Gitleaks kördes. De verktygsrapporter som berör batchen gäller avsedda mnemoniker, facktermer och formattext; inga nya sakfel hittades.
