# Foundation — svensk granskningsrapport

Datum: 2026-11-20  
Komponent: `military.release.json` (del 14)

| Engelsk källsträng | Tidigare svensk text | Föreslagen/sparad svensk text | Lint och stavning |
|---|---|---|---|
| Your King demands you prepare for war! | Er kung kräver att ni förbereder er för krig! | Din kung kräver att du förbereder dig för krig! | Inga anmärkningar. |
| Beast Begone | Försvinn odjur | Bort med odjuren | Inga anmärkningar. |
| Garrison Gig | Garnisonsjobb | Garnisonsuppdrag | Inga anmärkningar. |
| The First Constable has a shortage of guards for outposts near your village. She promises fair compensation to any fighters willing to lend a hand for a time. | Den förste konstapeln har brist på vakter till utposter nära er by. Hon lovar rättvis ersättning till alla krigare som är villiga att hjälpa till under en tid. | Den förste konstapeln har brist på vakter till utposter nära din by. Hon lovar rättvis ersättning till alla krigare som är villiga att hjälpa till under en tid. | Inga anmärkningar. |
| Convoy Escort | Eskort för konvoj | Konvojeskort | Inga anmärkningar. |
| Royal Army scouts have spotted well-armed enemy companies near our lands. Anyone who defeats them can claim the enemy's weapons for themselves. | Kungliga arméns spejare har upptäckt välbeväpnade fiendekompanier nära vårt land. Den som besegrar dem kan göra anspråk på fiendens vapen för egen del. | Kungliga arméns spejare har upptäckt välbeväpnade fiendekompanier nära våra marker. Den som besegrar dem kan göra anspråk på fiendens vapen för egen del. | Inga anmärkningar. |

Den första formuleringen av `Beast Begone` hade ett tillagt utropstecken, vilket l10n-lint markerade som en informationsnotis. Det togs bort innan slutlig publicering. Den slutliga PO-filen godkändes av `l10n-lint --language sv`, och `hunspell-sv` fann inga stavningsanmärkningar. Ändringarna skapades i Crowdin via API (HTTP 201). Hunspell gav endast Gettext-varningen om PO-huvudets teckenuppsättning; den gäller inte översättningarna.