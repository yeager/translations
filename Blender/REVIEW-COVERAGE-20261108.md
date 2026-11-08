# Blender UI – täckning av lokal granskning

## Underlag

- Källfil: `~/Downloads/blender-ui-ui-sv (4).po`.
- Källfilens innehåll: 40 427 översättningsposter (rubrik undantagen).
- Arkiverade granskningsbatcher: 793 filer med namnet
  `blender-ui-sv-reviewed-*-batch-*.po`, plus samlade deltafiler. Mätningen
  använder unionen av de spårbara granskningsfilerna utan att låta fullfiler
  och samlingsfiler räknas som fristående radgranskningar.

## Verifierad basmätning 2026-11-08

Normaliserade identitetsnycklar för `msgctxt` och `msgid` jämfördes med
källfilen. Mätningen räknar inte dubbletter eller skillnader i måltext som
har skapats av senare granskningar.

| Mått | Poster |
| --- | ---: |
| Granskade identiteter som fortfarande finns i källfilen före de riktade restgrupperna | 9 897 |
| Granskningstäckning i den lokala källfilen före de riktade restgrupperna | 24,48 % |
| Återstående för full radvis täckning före de riktade restgrupperna | 30 530 |

## Riktade restgrupper

| Grupp | Granskade | Ändrade | Medvetet oförändrade | Belägg |
| --- | ---: | ---: | ---: | --- |
| glTF: komprimerade WebP/KTX2-texturer och PNG/JPEG-reservtexturer | 14 | 8 | 6 | `blender-ui-sv-reviewed-batch-1218-gltf-compressed-textures.po`, commit `1db265b6` |
| Projekt, startbild/startskärm och samlingsimportör | 27 | 6 | 21 | `blender-ui-sv-reviewed-batch-1219-project-startup-importer.po`, commit `8e5c6188` |
| Armatur, poser och begränsningar | 7 | 2 | 5 | `blender-ui-sv-reviewed-batch-1230-armature-pose-constraints.po`, commit `ad008b13` |
| Skulptering, målning och viktmålning | 14 | 2 | 12 | `blender-ui-sv-reviewed-batch-1231-sculpt-paint-weight-paint.po`, commit `77c97075` |
| Mesh- och UV-redigering | 21 | 4 | 17 | `blender-ui-sv-reviewed-batch-1232-mesh-uv-editing.po`, commit `68fc110b` |
| Filhantering, import/export och externa data | 23 | 6 | 17 | `blender-ui-sv-reviewed-batch-1233-file-browser-external-data.po`, commit `58911c57` |
| Rendering, färghantering och kompositorn | 22 | 4 | 18 | `blender-ui-sv-reviewed-batch-1234-render-color-compositor.po`, commit `a9cf36dd` |
| Arbetsytor, redigerare och layout | 10 | 5 | 5 | `blender-ui-sv-reviewed-batch-1235-workspace-editor-layout.po`, commit `94766888` |
| Animation, tidslinje, Dope Sheet och Graph Editor | 22 | 7 | 15 | `blender-ui-sv-reviewed-batch-1236-animation-timeline-graph.po`, commit `8f56cedd` |
| Nodredigerare och Geometry Nodes | 14 | 7 | 7 | `blender-ui-sv-reviewed-batch-1237-node-editor-geometry-nodes.po`, commit `f19d1549` |

Efter dessa tio grupper har 174 tidigare otäckta strängar granskats. Deltafiler
registrerar de ändrade strängarna; den här loggen registrerar även de
kontrollerade former som rätteligen lämnades kvar. Den jämförbara lokala
täckningen är därmed minst 10 071 av 40 427 strängar, alltså **24,91 %**;
30 356 återstår i basexporten. Korrigeringen i batch 1229 räknas inte som en
ny radgranskning, eftersom den rättar formuleringen av en redan granskad
sekvensrenderingssträng.

## Avgränsning

Detta är en lokal granskningsmätning, inte Blender Weblates
översättningsprocent och inte ett importresultat. Källfilen är äldre än en
del batcher; nya eller ändrade källsträngar i Blender Translate måste jämföras
mot en ny export innan samma procenttal kan användas för serverns aktuella
katalog.
