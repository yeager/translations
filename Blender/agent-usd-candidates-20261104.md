# Kandidater från oberoende USD-granskning

Källa: `exports/2026-11-04/blender-manual-manual-sv.po`  
Område: `files/import_export/usd.rst`, raderna 176–449.  
Status: kandidater för huvudgranskning; inte ändrade i råexporten.

Nedan följer 15 säkra förslag. Kodidentifierare, RST-roller och URL:er ska
bevaras bytekorrekt när en deltafil byggs.

| Källa (`msgid`, förkortad för läsbarhet) | Föreslagen `msgstr` | Motivering |
| --- | --- | --- |
| `Import ``UsdGeomBasisCurves`` primitives as :doc:`Curves ...` | `Importera ``UsdGeomBasisCurves``-primitiver som :doc:`kurvor </modeling/curves_new/index>` och ``UsdGeomNurbsCurves`` som Blender-nät.` | Rätt backticks, bindestreck och svenska facktermer. |
| `Import ``UsdGeomMesh`` primitives as :doc:`Mesh Objects ...`` | `Importera ``UsdGeomMesh``-primitiver som :doc:`meshobjekt </modeling/meshes/index>`.` | Rätt markeringssyntax och naturlig sammansättning. |
| `Import ``UsdVolVolume`` OpenVDB assets as :doc:`Volume Objects ...`` | `Importera ``UsdVolVolume``-OpenVDB-tillgångar som :doc:`volymobjekt </modeling/volumes/index>`.` | Bevarar identifierare och gör terminologin konsekvent. |
| `Import ``UsdGeomPoints`` primitives as :doc:`Point Cloud Objects ...`` | `Importera ``UsdGeomPoints``-primitiver som :doc:`punktmolnsobjekt </modeling/point_cloud/index>`.` | Följer *punktmoln* i övriga USD-avsnitt. |
| `USD Shapes` | `USD-former` | Svensk versalisering och sammansättning. |
| `Display Purpose` | `Visningssyfte` | `Visa syfte` är verbfras och inte en rubrik. |
| `Material Purpose` | `Materialsyfte` | Rätt svensk sammansättning. |
| `Attempt to import ``allPurpose`` materials.` | `Försök att importera ``allPurpose``-material.` | Kodvärdet ska behållas men bindas korrekt till substantivet. |
| `Attempt to import ``preview`` materials. Load ``allPurpose`` materials as a fallback.` | `Försök att importera ``preview``-material. Läs in ``allPurpose``-material som reserv.` | Tar bort engelskt blandord och bevarar kodvärden. |
| `Import USD blend shapes as Blender's :doc:`/animation/shape_keys/index`.` | `Importera USD-blandningsformer som Blenders :doc:`/animation/shape_keys/index`.` | Rätt apostrof/svenskt genitiv; granska samtidigt om länken kan få synlig texten *formnycklar*. |
| `Import USD Preview` | `Importera USD-förhandsgranskning` | Rätt svensk sammansättning och versalisering. |
| `Convert USD Preview Surface shaders to Principled BSDF shader networks.` | `Konvertera USD Preview Surface-shadrar till Principled BSDF-shadernätverk.` | Rättar engelska pluralformer; termen *shader* är projektets etablerade. |
| `Don't import textures. Note that, with this option, material textures may fail to be resolved in Blender.` | `Importera inte texturer. Observera att materialtexturer kanske inte kan hittas i Blender med det här alternativet.` | `lösas upp` ändrar innebörden av *resolved*. |
| `Textures Directory` | `Texturkatalog` | Naturlig, kort UI-rubrik. |
| `File Name Collision` / `Use Existing` | `Filnamnskollision` / `Använd befintlig` | Korrigerar felaktiga särskrivningar och uttrycket `Användning Befintlig`. |

## Ytterligare säkra rättelser att bedöma i samma sammanhang

- `Shot from ...` bör behålla den aktuella käll-URL:en och översättas med
  `Bild från ... som har exporterats till USD och öppnats i USDView.`
- `Root Prim` ska konsekvent vara `Rotprim`, enligt den redan arkiverade
  USD-tillgänglighetsgranskningen.
- `Exported USDZ package ... zip archive` bör använda `ZIP-arkiv`.
- `Author USD custom attributes ...` måste börja med `Skapa`, inte engelska
  `Author`.
- `Exports parent hair strands are exported ...` har ett faktiskt dubblerat
  verb och behöver omformuleras till `Exporterar föräldrahårstrån som ett
  kurvsystem. Hårstrånas färger exporteras inte.`
- `The corresponding USD schema type ...` kan bli `Motsvarande USD-
  schematyp som används vid export motsvarar typen som läses vid import.`

## Risker att bevaka

- Bevara ``UsdGeom*``, ``allPurpose``, ``preview``, ``full``, `prims`,
  `Scope`, `USDZ` och RST-roller/URL:er exakt.
- `mesh` är ett Blender-fackord; växla inte godtyckligt mellan *mesh*,
  *nät* och *mask* utan att kontrollera den aktuella UI-terminologin.
- `Blend Shapes` har ett etablerat samband med *formnycklar*, men den
  exakta synliga länktexten måste kontrolleras mot RST-stilen före ändring.

## Huvudgranskning

Rapporten är mottagen och kontrollerad som kandidatunderlag. Förslagen
kräver radvis jämförelse med råexporten när nästa USD-delta byggs;
rapporten är inte i sig en godkänd översättningsfil. Kodidentifierare,
RST-roller och gällande UI-terminologi ska kontrolleras då.
