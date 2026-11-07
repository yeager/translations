# Blender UI – täckning av lokal granskning

## Underlag

- Källfil: `~/Downloads/blender-ui-ui-sv (4).po`
- Källfilens innehåll: 40 427 översättningsposter (rubriken undantagen).
- Arkiverade granskningsbatcher: 676 filer med namnet
  `blender-ui-sv-reviewed-*-batch-*.po`.

## Mätning 2026-11-08

Alla batcher slogs ihop med `msgcat --use-first` och jämfördes därefter med
källfilen med `msgcomm --more-than=1`. Jämförelsen använder gettexts
identitet för sammanhang och källsträng, och räknar därför inte dubbletter
eller ändringar som inte längre finns i den nedladdade filen.

| Mått | Poster |
| --- | ---: |
| Unika poster i alla arkiverade batcher | 7 454 |
| Batchposter som fortfarande finns i källfilen | 7 269 |
| Granskningstäckning i den lokala källfilen | 17,98 % |
| Återstående för full radvis täckning | 33 158 |

## Tolkning

Detta är en lokal granskningsmätning, inte Blender Weblates
översättningsprocent och inte ett importresultat. Källfilen är äldre än en
del batcher; 185 arkiverade ändringar kan därför inte matchas i just denna
nedladdning. De behöver inte vara fel eller saknas i Weblate.

Den samlade manuella deltafilen `pending-batches-811-841.po` innehåller endast
de nyaste lokalt granskade ändringarna och är avsiktligt mycket mindre än hela
arkivet. Fortsatt granskning ska prioritera poster som inte ingår i den
uppmätta skärningen.
