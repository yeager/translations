# Home Assistant Core – Climate: duration label

Datum: 2026-11-21  
Omfattning: 20 klimatnycklar för automationsutlösare och -villkor.

## Sparade ändringar

Alla berörda nycklar har källtexten `For at least` och hade den felaktiga
svenska texten `I åtminstone`. Den rättades till `I minst`. Det är den
idiomatiska svenska etiketten för en minsta varaktighet och fungerar i både
utlösar- och villkorsfält.

Ändringarna sparades via Lokalise API och varje post lästes tillbaka via API.
Fullständiga nycklar, Lokalise-id:n och den verifierade måltexten finns i
`tools/swedish-tm/Home-Assistant/2026-11-21-climate-for-at-least-verified.json`.

## Terminologiminne

De 20 API-verifierade posterna har förts in i det kanoniska Home Assistant-TMX
med källnyckel, Lokalise-id, verifieringsmetod och datum. TMX-valideraren
godkände minnet efter uppdateringen (2 530 poster).

## Verktygsresultat

`append_verified_home_assistant_tmx.py` rättades så att den accepterar både
JSON-tal och JSON-strängar för Lokalise-id:n. Den validerar fortfarande att
värdena består av decimala siffror innan de skrivs till TMX.
