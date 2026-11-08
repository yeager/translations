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
| Bildredigerare, bildhantering och texturer | 15 | 6 | 9 | `blender-ui-sv-reviewed-batch-1238-image-editor-textures.po`, commit `d54408ba` |
| Fysik och simuleringar | 18 | 7 | 11 | `blender-ui-sv-reviewed-batch-1239-physics-simulations.po`, commit `2ca643b5` |
| Import/export och armaturdata | 12 | 1 | 11 | `blender-ui-sv-reviewed-batch-1240-import-export-armature.po`, commit `6e161836` |
| Spreadsheet Editor och Geometry Bundle-visning | 15 | 1 | 14 | `blender-ui-sv-reviewed-batch-1241-spreadsheet-input-output.po`, commit `42f962ed` |
| Övre fältet och statusfältet | 19 | 2 | 17 | `blender-ui-sv-reviewed-batch-1242-top-status-bar-descriptions.po`, commit `d9b7fd2a` |
| Enhetsinställningar: fysisk area | 1 | 1 | 0 | `blender-ui-sv-reviewed-batch-1243-unit-area.po` |
| Geometry Nodes: ytattributdiagnostik | 1 | 1 | 0 | `blender-ui-sv-reviewed-batch-1244-geometry-nodes-surface-attribute.po` |
| PLY-importör: fel utan hörnpunkter | 1 | 1 | 0 | `blender-ui-sv-reviewed-batch-1245-ply-importer-error.po`, commit `78c5c1cb` |
| PLY- och SPZ-importdiagnostik | 13 | 13 | 0 | `blender-ui-sv-reviewed-batch-1246-ply-spz-import-diagnostics.po`, commit `4f6cc6aa` |
| USD: formnyckel- och morfmålsdiagnostik | 4 | 4 | 0 | `blender-ui-sv-reviewed-batch-1247-usd-blendshape-diagnostics.po`, commit `2f515f34` |
| SPZ: rubrik- och byteordningsdiagnostik | 2 | 2 | 0 | `blender-ui-sv-reviewed-batch-1248-spz-header-diagnostics.po`, commit `458a1420` |
| USD: tillgångar, skelett och kurvdiagnostik | 70 | 3 | 67 | `blender-ui-sv-reviewed-batch-1249-usd-assets-skeleton.po` |
| Alembic: import- och exportdiagnostik | 20 | 0 | 20 | `REVIEW-ALEMBIC-DIAGNOSTICS-20261108.md` |
| SPZ: läs- och dekomprimeringsdiagnostik | 15 | 0 | 15 | `REVIEW-SPZ-READ-DIAGNOSTICS-20261108.md` |
| OTIO, PLY, OBJ och STL: import- och exportdiagnostik | 24 | 0 | 24 | `REVIEW-FORMAT-IO-DIAGNOSTICS-20261108.md` |
| Sammansättningar, fjärrresurser och nedladdningscache | 13 | 13 | 0 | `blender-ui-sv-reviewed-batch-1250-compounds-cache.po` |
| Omfångspaneler och märkta kanter | 2 | 2 | 0 | `blender-ui-sv-reviewed-batch-1251-scope-marked-edges.po` |
| Action-datatyp: konsekvent böjning i animeringskontext | 4 | 4 | 0 | `blender-ui-sv-reviewed-batch-1252-action-datablock-consistency.po`; terminologirättelse efter tidigare Action-granskning, ej inräknad som ny täckning |
| Bake Action: menyetikett för Action-datatyp | 1 | 1 | 0 | `blender-ui-sv-reviewed-batch-1253-bake-action-label.po`; terminologirättelse efter tidigare Action-granskning, ej inräknad som ny täckning |
| Python Console: navigering, urklipp och körningskontext | 15 | 0 | 15 | `REVIEW-CONSOLE-20261108.md`; kontrollgruppen saknar deltafil och är inte inräknad i den äldre basmätningen |

Efter dessa tjugosju grupper har 419 tidigare otäckta strängar granskats. Deltafiler
registrerar de ändrade strängarna; den här loggen registrerar även de
kontrollerade former som rätteligen lämnades kvar. Den jämförbara lokala
täckningen är därmed minst 10 316 av 40 427 strängar, alltså **25,52 %**;
30 111 återstår i basexporten. Korrigeringen i batch 1229 räknas inte som en
ny radgranskning, eftersom den rättar formuleringen av en redan granskad
sekvensrenderingssträng.

## Avgränsning

Detta är en lokal granskningsmätning, inte Blender Weblates
översättningsprocent och inte ett importresultat. Källfilen är äldre än en
del batcher; nya eller ändrade källsträngar i Blender Translate måste jämföras
mot en ny export innan samma procenttal kan användas för serverns aktuella
katalog.
