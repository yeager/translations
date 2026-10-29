# GnuCash: aktuell upstreamjämförelse 2026-10-27

Programkatalogen i arkivet jämfördes med `po/sv.po` på `stable` i
`Gnucash/gnucash`. Den hämtade upstreamfilen har SHA-256
`f334e684c6442a26f938d774eb63e3c59213e7d71d4311181d031db1a79a172e`.
Den senaste GitHub-releasen är 5.17 från 2026-09-27 och uppfyller därmed
48-månaderskravet.

Katalogerna har samma 5 749 översatta poster, men 64 svenska måltexter skiljer
sig. Den kompakta filen `gnucash-program-sv-reviewed-delta-20261027.po`
innehåller 59 redan granskade rättningar: svensk bokföringsterminologi,
format-/radbrytningsrättningar och tangentbordsgenvägar utan å, ä eller ö som
acceleratortecken.

Fem poster är medvetet utelämnade ur deltat:

- `Date Opened`: den arkiverade lydelsen `Öppnad datum` är felaktig; upstreams
  `Öppningsdatum` behålls;
- `Open`: upstreams `Öppna` är korrekt som åtgärd;
- två fristående `Split`-poster och texten om en dold måldelpost: de är
  utelämnade ur deltat i avvaktan på den separata termgranskningen
  `SPLIT-TERM-REVIEW-20261027.md`.

Kontroller av 59-postersdeltat: `msgfmt --check --check-format`, l10n-lint,
svlang med verktygets egen virtuella miljö, hunspell-sv, Gitleaks och
`git diff --check`. l10n-lint rapporterar 0 fel och 0 varningar. Filen är
inte uppladdad eller mergeverifierad.

## Ny jämförelse 2026-10-29

Aktuell `stable`-revision `fec5643` har jämförts post för post med deltat.
Alla 59 nycklar finns kvar i `po/sv.po`; ingen måltext är identisk med
deltats förslag. Deltat är alltså fortfarande relevant i sin helhet.

En direkt `msgcat`-sammanslagning ska inte användas för att skapa PR-filen:
den normaliserar Weblate-huvudet och flyttar poster, vilket skulle ge onödig
metadata- och formateringsdiff. Nästa steg är en radbevarande tillämpning av
de 59 redan granskade posterna och därefter full kontrollkedja mot `stable`.
