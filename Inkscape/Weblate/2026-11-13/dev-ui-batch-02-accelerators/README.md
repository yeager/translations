# Inkscape Weblate: utvecklingsgrenen, batch 02

- Källa: `inkscape/master/inkscape`, svenska.
- Omfattning: tre nordiska tangentbordsacceleratorer som l10n-lint markerade som fel.
- Ändringar: acceleratortecknen flyttades till `x` respektive `w`, utan att den svenska UI-texten ändrades i sak.
- Kontroller: `msgfmt --check`, l10n-lint (0 fel), diffkontroll och Gitleaks passerade.
- Första Weblate-importen: 0 accepterade och 3 hoppade över, eftersom de var befintliga översättningar.
- Slutlig Weblate-import med uttryckligt ersättningsläge: 3 accepterade, 0 hoppade över, 0 saknade.
- Efterkontroll: råexporten visar de tre avsedda acceleratorerna och l10n-lint rapporterar 0 fel i hela katalogen.

`first-upload-receipt.json` är det förväntade skyddsutfallet. `upload-receipt.json` är den verifierade slutliga importen.
