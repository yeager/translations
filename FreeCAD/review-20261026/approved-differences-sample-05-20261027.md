# FreeCAD: femte urvalet av godkända avvikelser

Den 27 oktober 2026 granskades 20 ytterligare godkända avvikelser: sträng-id
175647–176044. Kandidaterna kontrollerades mot resursnamn och berörd
källkod. Inga ändringar eller röster skickades till Crowdin.

## Bedömning

- Samtliga 20 kandidater är godtagbara i sin givna kontext.
- `Verktygsrad` i dialogen för egna verktygsrader är inte en inkonsekvens:
  samma dialog använder redan `Ny verktygsrad` och `Namn på verktygsraden`.
  `Byt namn på verktygsraden` ska därför behållas där, även om andra delar av
  gränssnittet använder `verktygsfält`.
- `Datum` i `Datum size` är FreeCADs CAD-term för referensobjekt. Översättningen
  `Storlek på referensobjekt` förklarar innebörden utan att blanda ihop termen
  med kalenderdatum.
- `B&W`-relaterad åtkomsttangent, filändelsen `.FCbak`, platshållaren `%1`,
  samt produktnamnet `Qt Assistant` är korrekt bevarade.
- Snäppning, begränsningsruta, stereoprojektioner, säkerhetskopior och
  makrokörning är konsekvent återgivna.

## Slutsats

Urvalet kräver inga nya förslag. Dokumentationen skiljer uttryckligen mellan
detta kontextgranskade resultat och en massändring i Crowdin.
