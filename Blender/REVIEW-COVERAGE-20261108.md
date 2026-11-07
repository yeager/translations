# Blender UI – täckning av lokal granskning

## Underlag

- Källfil: `~/Downloads/blender-ui-ui-sv (4).po`
- Källfilens innehåll: 40 427 översättningsposter (rubriken undantagen).
- Arkiverade granskningsbatcher: 766 filer med namnet
  `blender-ui-sv-reviewed-*-batch-*.po`, plus samlade deltafiler. Mätningen
  använder unionen av samtliga 1 513 arkiverade filer med namnet
  `blender-ui-sv-reviewed-*.po` så att en granskad post räknas även när den
  endast finns i en samlad, spårbar importfil.

## Mätning 2026-11-08

Alla arkiverade granskningsfiler slogs ihop med `msgcat --use-first`. Därefter
jämfördes normaliserade identitetsnycklar för `msgctxt` och `msgid` med
källfilen. Mätningen räknar därför inte dubbletter eller skillnader i själva
måltexten som skapas av senare granskningar.

| Mått | Poster |
| --- | ---: |
| Unika identiteter i alla arkiverade granskningsfiler | 10 120 |
| Granskade identiteter som fortfarande finns i källfilen | 9 792 |
| Granskningstäckning i den lokala källfilen | 24,30 % |
| Återstående för full radvis täckning | 30 510 |

## Tolkning

Detta är en lokal granskningsmätning, inte Blender Weblates
översättningsprocent och inte ett importresultat. Källfilen är äldre än en
del batcher; 328 arkiverade identiteter kan därför inte matchas i just denna
nedladdning. De behöver inte vara fel eller saknas i Weblate.

Den samlade manuella deltafilen `pending-batches-811-923.po` innehåller endast
de nyaste lokalt granskade ändringarna och är avsiktligt mycket mindre än hela
arkivet. Fortsatt granskning ska prioritera poster som inte ingår i den
uppmätta skärningen.
