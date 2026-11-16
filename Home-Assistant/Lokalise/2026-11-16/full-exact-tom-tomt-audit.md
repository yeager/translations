# Home Assistant Core – full granskning av “Tom” och “Tomt”

Datum: 2026-11-16

## Omfattning

Lokalise API användes för en sidvis genomgång av samtliga 74 606 svenska
översättningar i projektet. Sökningen avsåg exakta, fristående värden `Tom`
och `Tomt`, inte förekomster inuti längre texter.

## Resultat

Första genomgången hittade 58 värden.

- 8 värden hade en avsiktligt tom engelsk källa och återställdes från “Tom”
  till tom svensk text i batch 120.
- 40 `state::off`-värden hade engelska *Clear* och felaktigt “Tom” eller
  “Tomt”. De är uppdaterade till **Klar** i batch 121.
- 10 värden har engelska *Empty* i konkret kontext: Whirlpools tankstatus,
  LG ThinQ-batteri, Litter-Robots behållare, SwitchBots vattennivå,
  Roborocks tvättmedel och sköljmedel, gemensamt tomtillstånd samt Tuya
  matnivå. De behåller **Tom**, eftersom det är korrekt svenska i respektive
  UI-kontext.

Efter ändringarna lästes batcherna tillbaka från API:t. En ny full sökning
fann exakt de tio kontextuellt korrekta *Empty → Tom*-värdena och inga
felaktiga värden med tom källa eller *Clear*.

Kontrollen upprepades direkt mot Lokalise API senare samma dag. Den sidvisa
hämtningen täckte åter samtliga 74 606 svenska översättningar på 150 sidor.
Den fann tio exakta värden `Tom` och inget `Tomt`; källtext och nyckelkontext
lästes därefter separat för samtliga tio. Resultatet var oförändrat: alla är
konkreta tomma tillstånd, inte en svensk återgivning av en annan betydelse av
engelskans *empty*.

## Status

Ändringarna är sparade i Lokalise, Home Assistants etablerade
översättningskanal. Det här bekräftar inte upstream-granskning, publicering
eller en Home Assistant-release.
