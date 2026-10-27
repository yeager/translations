# FreeCAD: tolfte urvalet av godkända avvikelser

Den 27 oktober 2026 granskades 20 godkända avvikelser, sträng-id
176828–6594067, mot XLIFF-kontexten, FEM-källkoden och den granskade
FreeCAD-terminologin. Inga ändringar eller röster skickades till Crowdin.

## Bedömning

- Nitton av 20 kandidater är godtagbara i sitt sammanhang.
- `Randvillkor för fluid`, `kontaktvillkor`, `värmeflödesbelastning`,
  `efterbehandlingskedja`, `fästförskjutning`, `slavyta`, `strömtäthet` och
  `spänning` är korrekta FEM-termer i projektet.
- HTML-radbrytningar, kodnamnen CCX_Results, MPI, OpenMP, ElmerSolver,
  Mystran och z88r samt sifferformatet i Elmer-instruktionen är bevarade.
- `Körbar Mystran-fil` är korrekt i rubriken. Det gemena filnamnet `mystran`
  behålls i den efterföljande instruktionen, eftersom den hänvisar till den
  körbara filen.

## Rättelse att kontrollera i Crowdin

Sträng 6677454 `Plane Multi-Point Constraint` ska vara
`Flerpunktsvillkor för plan`, inte `Plant flerpunktsvillkor`. Den förra
formen är den fastställda projekttermen för just kommandokontexten.

## Slutsats

Rättelsen ska först jämföras med Crowdins aktuellt valda måltext. Övriga 19
poster kräver inga nya Crowdin-förslag.
