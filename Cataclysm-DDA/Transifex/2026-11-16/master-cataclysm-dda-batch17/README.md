# Cataclysm-DDA: aktiviteter och dörrar, batch 17

Batchen omfattar 25 sammanhängande strängar från `src/activity_actor.cpp`.
Den översätter patronantal, arbetsuppgifter och zoner, mörker- och
slaktvarningar samt öppning och stängning av dörrar och andra objekt.

## Terminologi och kontroll

- **round** är **patron**, enligt projektets terminologilista.
- **task** är **uppgift**, **zone** är **zon** och en spelruta är **ruta**.
- Formuleringar med ett okänt objekt använder omskrivningar som fungerar för
  både en- och ett-ord, utan att skapa felaktigt genus kring `%s`.
- Samtliga 25 `%s`-, `%d`- och positionsplatshållare är identiska med källan.
- Ingen ny em dash har införts.
- `l10n-lint` har 0 fel och 0 varningar; ett informationsfynd för en inledande
  platshållare är avsiktligt.
- Hunspell-SV, svlang, `git diff --check` och Gitleaks har körts. svlangs fem
  V2-träffar är falska positiva i korrekta satser med platshållare, bisats
  eller modalverb.

## Uppladdning och API-återläsning

Samtliga 25 måltexter skickades via Transifex API. Varje sparad översättning
lästes sedan tillbaka med en separat `GET`-begäran: 25 av 25 överensstämmer
exakt med batchens måltext.

Projektet har fortfarande många oöversatta svenska strängar. Den fulla
resultatsidan är fortsatt fylld med 150 poster och har en nästa sida, så den
här batchen anges som inskickad och verifierad, inte som en komplett svensk
katalog.

Efter en kontroll mot källkoden för `activity_actor.cpp` förtydligades sex
fordonsdelstexter. Deras `%s`-värden saknar artikel i källkoden; måltexterna
använder därför **fordonets** och lägesfraser som är fria från genusfel. De
sex rättningarna återlästes via API utan avvikelse.
