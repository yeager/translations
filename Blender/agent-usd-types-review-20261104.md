# Motgranskning: Blender Manual — USD-datatyper

Datum: 2026-11-04  
Underlag: `agent-usd-types-candidates-20261104.md`, råexport och
`blender-ui-ui-sv.po`.

| Källa | Bedömning | Godkänd måltext eller korrigering |
| --- | --- | --- |
| `Floating point :term:\`Quaternion\` rotation.` | Godkänd | `:term:\`Kvaternionsrotation <Quaternion>\` med flyttal.` Blender-UI:t använder exakt denna synliga term. |
| USD Primvars begränsningar | Godkänd | Kandidatens text bevarar samtliga kodidentifierare och använder etablerade formerna *flyttal med dubbel precision* och *flyttal med halv precision*. |
| `float4`-begränsning | Korrigera | Använd `Datatypen USD ``float4`` har ingen direkt motsvarighet i Blender och behandlas inte som en Blender-``Color`` eller ``Quaternion``.` Källan avser en *Blender Color*-datatyp, inte något som ägs av Blender; undvik därför den felaktiga genitiven `Blenders`. |

## Avgränsning

De delade posterna `float`, `2D Vector`, `color4f` och `Byte Color` lämnas
utanför även fortsättningsvis. De tre granskade kandidaterna kan införas i
en separat deltafil med den angivna följdrättelsen för `float4`.
