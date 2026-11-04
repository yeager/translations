# Oberoende motgranskning: Blender Manual – armaturer, del 1

Datum: 2026-11-04  
Underlag: `agent-manual-large-candidates-20261104.md`, råexporten av Blender
Manual och Blender UI-katalogen.

Omfattning: Kandidat 1–18, från `bone_roll.rst` till
`duplicate_rename.rst:26`. Ingen PO-fil har ändrats.

## Resultat

| Kandidat | Beslut | Motivering |
| --- | --- | --- |
| 1–5 | Godkänn | `benrullning`, `viloposition`, axelbeteckningarna och `3D-markören` har stöd i UI-katalogen; RST-markeringarna är intakta. |
| 6 | Ändra | Källtexten är en uppmaning. Skriv `Ändra resultatet med 180°.` i stället för indikativformen `Ändrar`. |
| 7–14 | Godkänn | Åtgärdsnamn, menyväg, dupliceringsförlopp och API-målet är innehållstroget återgivna. `Rensa rullning` och `Duplicera och byt namn` är direkt belagda i UI-katalogen. |
| 15 | Ändra | `parenting` bör beskrivas som föräldrarelation, inte som överordning. Använd formuleringen i nästa stycke. |
| 16–18 | Godkänn | Markering, omplacering, `riggar` och riktningssuffix återger källans UI- och domänbetydelse. Literalvärdena i nästa kandidat lämnas separat orörda. |

## Terminologibelägg

UI-katalogen använder bland annat `Benrullning` för *Bone Roll*,
`Rensa rullning` för *Clear Roll* och `Duplicera och byt namn` för *Duplicate
and Rename*. Den använder dessutom *Parents* → `Föräldrar` och
*parenting* → `föräldraskap` eller `föräldrarelation`, vilket motiverar
ändringen i kandidat 15.

Kandidat 15 ska ha följande `msgstr`:

```po
msgstr "Den här operatorn fungerar på liknande sätt som :ref:`bpy.ops.armature.duplicate_move` och bevarar, när det är möjligt, föräldra- och anslutningsrelationer mellan duplicerade ben."
```

## Slutsats

16 av 18 kandidater kan användas oförändrade. Kandidat 6 och 15 ska använda
de kompletta ersättningarna ovan. Inga RST-mål, API-identifierare, siffror
eller UI-formella namn ska ändras ytterligare i denna del.
