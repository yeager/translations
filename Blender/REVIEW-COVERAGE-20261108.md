# Blender UI: granskningslogg 8 november 2026

Den här loggen kompletterar deltafilerna. En post som har granskats och
medvetet lämnats oförändrad ska inte räknas som ogranskad bara för att den
inte behöver en importfil.

## Underlag

- Basexport: `blender-ui-ui-sv.po`, hämtad 4 november 2026.
- Basens omfattning: 40 427 aktiva strängar.
- Arkiverade deltafiler täckte 40 299 unika käll-/kontextnycklar före den här
  dagens riktade restgranskning.

## Riktade restgrupper

| Grupp | Granskade | Ändrade | Medvetet oförändrade | Belägg |
| --- | ---: | ---: | ---: | --- |
| glTF: komprimerade WebP/KTX2-texturer och PNG/JPEG-reservtexturer | 14 | 8 | 6 | `blender-ui-sv-reviewed-batch-1218-gltf-compressed-textures.po`, commit `1db265b6` |
| Projekt, startbild/startskärm och samlingsimportör | 27 | 6 | 21 | `blender-ui-sv-reviewed-batch-1219-project-startup-importer.po`, commit `8e5c6188` |

Efter dessa två grupper har 41 tidigare otäckta strängar granskats. Deltafiler
registrerar de 14 ändrade strängarna; denna logg registrerar även de 27
kontrollerade former som rätteligen lämnades kvar.

## Avgränsning

Täckningssiffran är knuten till basexporten från 4 november. Nya eller ändrade
källsträngar i Blender Translate måste jämföras mot en ny export innan samma
procenttal kan användas för serverns aktuella katalog.
