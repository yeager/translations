# Blender UI – täckning av lokal granskning

## Underlag

- Källfil: `~/Downloads/blender-ui-ui-sv (4).po`
- Källfilens innehåll: 40 427 översättningsposter (rubriken undantagen).
- Arkiverade granskningsbatcher: 760 filer med namnet
  `blender-ui-sv-reviewed-*-batch-*.po`, plus samlade deltafiler. Mätningen
  använder unionen av samtliga 1 501 arkiverade filer med namnet
  `blender-ui-sv-reviewed-*.po` så att en granskad post räknas även när den
  endast finns i en samlad, spårbar importfil.

## Mätning 2026-11-08

Alla arkiverade granskningsfiler slogs ihop med `msgcat --use-first` och
jämfördes därefter med källfilen med `msgcomm --unique`. Jämförelsen använder
gettexts identitet för sammanhang och källsträng, och räknar därför inte
dubbletter eller ändringar som inte längre finns i den nedladdade filen.

| Mått | Poster |
| --- | ---: |
| Unika poster i alla arkiverade granskningsfiler | 10 095 |
| Poster som fortfarande finns i källfilen | 9 427 |
| Granskningstäckning i den lokala källfilen | 23,32 % |
| Återstående för full radvis täckning | 31 000 |

## Tolkning

Detta är en lokal granskningsmätning, inte Blender Weblates
översättningsprocent och inte ett importresultat. Källfilen är äldre än en
del batcher; 668 arkiverade ändringar kan därför inte matchas i just denna
nedladdning. De behöver inte vara fel eller saknas i Weblate.

Den samlade manuella deltafilen `pending-batches-811-917.po` innehåller endast
de nyaste lokalt granskade ändringarna och är avsiktligt mycket mindre än hela
arkivet. Fortsatt granskning ska prioritera poster som inte ingår i den
uppmätta skärningen.
