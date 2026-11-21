# Home Assistant Core – Update: duration label

En senare kontroll mot den aktuella Lokalise-nyckelresursen visade att två
tidigare angivna ID:n i den lokala exporten i själva verket tillhörde
`temperature`, inte `update`. De två felkopplade raderna har därför tagits bort
från TMX-manifestet och det kanoniska minnet. De återstående fyra
automationsfälten har separat spårbarhet. 

Spårbarhet finns i
`tools/swedish-tm/Home-Assistant/2026-11-21-update-for-at-least-verified.json`.
