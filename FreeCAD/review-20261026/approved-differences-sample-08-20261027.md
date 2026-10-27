# FreeCAD: åttonde urvalet av godkända avvikelser

Den 27 oktober 2026 granskades 20 godkända avvikelser, sträng-id
176481–6687710, mot XLIFF-kontexten, FreeCADs svenska TS-katalog och den
granskade FreeCAD-terminologin. Inga ändringar eller röster skickades till
Crowdin.

## Bedömning

- Nitton av 20 kandidater är godtagbara i sitt sammanhang.
- `Växlar till perspektiviskt visningsläge` är ett korrekt kommandonamn. Det
  ersätter den svagare befintliga formuleringen `perspektivt visningsläge` i
  den lokala TS-katalogen, men får inte skickas till Crowdin utan kontroll av
  den nu valda måltexten.
- `Länkåtgärder`, `specialåtgärder`, `länkgrupp` och `Ny del` följer
  FreeCADs etablerade gränssnittsterminologi.
- `Python-utmatning`, `Python-fel`, `rapportvyn` och `formatmallen` är
  fackmässiga och begripliga i respektive inställningsdialog.
- Åtkomstnycklarna i `Förhandsgranska &utskrift` och `&Rutmarkering` är
  bevarade. HTML-länken till tilläggshanteraren och dess mål är också
  oförändrade.

## Rättelse att kontrollera i Crowdin

Sträng 6687710, `&Box Selection` i `StdBoxSelection`, är felöversatt som
`&Rutmarkering`. Den granskade FreeCAD-terminologin anger konsekvent
`&Rektangelmarkering` för just den här kommandokontexten. Hunspell saknar
dessutom uppslaget `rutmarkering`. Ingen ändring har skickats, eftersom den
aktuellt valda Crowdin-måltexten först måste jämföras med den rekommenderade
rättelsen.

## Slutsats

Urvalet ger två möjliga rättelser att jämföra med Crowdin: `perspektiviskt
visningsläge` för 176481 och `&Rektangelmarkering` för 6687710. Övriga
poster kräver inga nya Crowdin-förslag.
