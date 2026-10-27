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
- två fristående `Split`-poster och texten om en dold måldelpost: arkivets
  `split` respektive `Destinations-spliten` är inte konsekvent svenska och
  behöver en separat termgranskning.

Kontroller av 59-postersdeltat: `msgfmt --check --check-format`, l10n-lint,
svlang med verktygets egen virtuella miljö, hunspell-sv, Gitleaks och
`git diff --check`. l10n-lint rapporterar 0 fel och 0 varningar. Filen är
inte uppladdad eller mergeverifierad.
