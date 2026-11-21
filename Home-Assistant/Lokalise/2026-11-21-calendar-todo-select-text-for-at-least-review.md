# Home Assistant Core – kalender, att göra, val och text: tidsvillkor

Granskad: 2026-11-21  
Omfattning: åtta live-identifierade fält med den engelska etiketten `For at least`.

Fyra fel rättades i Lokalise: kalenderns generella villkor, att-göra-listans
generella villkor, valvillkoret och textvillkoret. De ändrades från
`I åtminstone` till `I minst`, sparades via API och lästes tillbaka. De övriga
fyra fälten var redan korrekta vid live-läsning. Samtliga åtta nycklar har
kontrollerats mot Lokalises live-nyckelresurs (nyckelnamn, engelska källa,
svenskt översättnings-ID och svensk text).

`I minst` fungerar som kort etikett för varaktighet; `I åtminstone` är inte
idiomatisk svenska i detta gränssnitt.

Spårbarhet: `Home-Assistant/2026-11-21-calendar-todo-select-text-for-at-least-verified.json`.
