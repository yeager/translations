# Andra motgranskning: Blender Manual — USD-datatyper

Granskad mot råexporten `blender-manual-manual-sv.po`, den första
motgranskningen och Blender-UI-katalogen (`blender-ui-ui-sv.po`). Inga
råexporter eller deltafiler har ändrats.

| Källa | Bedömning | Fastställd svensk måltext |
| --- | --- | --- |
| `Floating point :term:\`Quaternion\` rotation.` | Godkänd | `:term:\`Kvaternionsrotation <Quaternion>\` med flyttal.` UI-katalogen har samma synliga term i *Floating point quaternion rotation*. |
| USD Primvars begränsningar | Godkänd | `Blender har inte stöd för USD-primvars som använder 64-bitars heltalsvärden (``int64``), osignerade typer (``uint``) eller 64-bitars flyttal med dubbel precision eller 16-bitars flyttal med halv precision. Det omfattar exempelvis ``matrix4d`` (4×4-matris med flyttal med dubbel precision) och ``quath`` (kvaternion med halv precision).` Samtliga typidentifierare och dubbelbacktick-markeringar bevaras. |
| USD `float4`-begränsning | Godkänd med rättelse | `Datatypen USD ``float4`` har ingen direkt motsvarighet i Blender och behandlas inte som en Blender-``Color`` eller ``Quaternion``.` Formuleringen beskriver en Blender-datatyp utan den missvisande genitiven *Blenders*. |

## Kontrollpunkter

- `Quaternion` är `Kvaternion` i Blender-UI:t och är korrekt länkad som
  `:term:` med oförändrat mål `Quaternion`.
- `Primvar`, `int64`, `uint`, `matrix4d`, `quath`, `float4`, `Color` och
  `Quaternion` behandlas som USD-/API-identifierare och lämnas exakta.
- `4×4-matris`, `flyttal med dubbel precision` och `flyttal med halv
  precision` är idiomatisk och tekniskt korrekt svensk fackprosa.
