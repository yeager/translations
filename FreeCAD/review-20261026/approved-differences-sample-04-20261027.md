# FreeCAD: fjärde urvalet av godkända avvikelser

Den 27 oktober 2026 granskades ytterligare 20 godkända avvikelser i den
arkiverade kandidatfilen: sträng-id 6607681–175632. Resursnamn och, när det
behövdes, aktuell källkod kontrollerades. Inga ändringar eller röster
skickades till Crowdin.

## Fynd

- Sträng-id `6683762` är felöversatt som `Plats`. Den förekommer som etikett
  i `Gui::Dialog::DlgAuthorization`, före användarnamn och lösenord, och
  dess värde visas som `%1 at %2`. I denna nätverkskontext betyder `Site`
  `Webbplats`, inte en fysisk plats. Rättelsen bör skickas individuellt till
  Crowdin efter kontroll av den valda översättningen.
- Snäppkommandona använder konsekvent etablerad CAD-terminologi: `Snäpp till
  rutnät`, `Snäpp till skärningspunkt`, `Snäpp till ändpunkt` och `Snäpp till
  arbetsplan`. Översättningsminnet använder samma verbform för snapping.
- `B-spline`, `Avrundning`, `ytbindare`, `hörnpunkter`, `verktygsfält` och
  `inställningspaket` är korrekta och konsekventa i sammanhanget.
- Kodnamnen `Part Compounds`, `App::Link`, `True`, `False`, `Axis`, `Center`
  och `Label Type` ska behållas eftersom de är klasser, värden eller
  egenskapsnamn som användaren möter exakt så i programmet.
- Åtkomsttangenten i `&OK` är avsiktlig och behöver inte ändras.

## Slutsats

Nitton av tjugo poster är godtagbara i sin givna kontext. Endast `Site` i
autentiseringsdialogen kräver en riktad Crowdin-rättning: `Webbplats`.
Massändring eller massröstning är inte lämplig.
