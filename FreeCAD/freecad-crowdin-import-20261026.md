# FreeCAD: Crowdin-import 2026-10-26

Filen `freecad-sv-crowdin-submitted-20261026.xliff` är den exakta fil som skickades till FreeCAD på Crowdin. Crowdin rapporterade 827 tillagda översättningar, 0 godkända och 627 överhoppade av 1 454 poster. Rapporten identifierar inte de överhoppade posterna; åtkomst till tjänsteloggen nekades. Filen är därför ett arkiv över det inskickade underlaget, inte en förteckning över exakt vilka poster som importerades.

## Uppföljning av vald översättning

En ny export från Crowdin den 26 oktober jämfördes med det inskickade underlaget per sträng-id och källtext. Samtliga 1 454 källtexter matchade. För 575 poster var den valda översättningen identisk med den inskickade; för 879 skilde den sig. Exporten visar endast den valda översättningen och kan inte identifiera vilka alternativa förslag som importerats eller hoppats över.

Två stickprov i Crowdin visade att inskickade alternativ fanns trots att äldre, godkända översättningar valdes: id 6585476, ”Exportera stilar till JSON-fil”, och id 6679412, ”Måttdetaljer”. I båda fallen hade det godkända alternativet och det nya förslaget 0 poäng. Stickproven bevisar inte status för övriga poster.

## API-kontroll av förslag

En kontroll av alla 1 454 inskickade poster mot svenska förslag i Crowdin fann 1 438 exakta textmatchningar. Sexton poster saknade exakt matchning. Tolv av dem är oförändrade från källtexten; fyra har en annan måltext. Dessa fyra sträng-id (194951, 176822, 177244 och 2593990) var alla dolda enligt API:t vid kontrollen. Dold status är en sannolik förklaring till att de inte importerades, men importloggen var inte tillgänglig för att bekräfta orsaken. JSON-filen `freecad-crowdin-presence-20261026.json` innehåller resultat per sträng-id. Förekomst betyder inte att översättningen är vald eller godkänd.
