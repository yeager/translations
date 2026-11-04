# Blender UI – granskningsbatch 1, 2026-11-04

Kandidatfil: `blender-ui-sv-review-batch-20261104-01.po`.

Den här batchen bygger på den aktuella exporterade UI-katalogen och omfattar
fyra manuellt verifierade rättelser. Den råa exporten under
`exports/2026-11-04/` har inte ändrats.

| Källsträng | Tidigare svensk text | Ny svensk text | Skäl |
| --- | --- | --- | --- |
| `Custom Shader Group Node for Python nodes` | Tidigare svensk sammansättning med tre *g* | Anpassad shadergruppnod för Python-noder | *Shader* är etablerad Blender-term och ska inte snävas in till *skugga*. |
| `Hit Color` | Tidigare svensk sammansättning med tre *f* | Träffärg | Svensk sammansättning utan tre lika konsonanter i följd. |
| `Popover panel for adding extra options …` | Tidigare poppupp-sammansättning | Utfällningspanel … | Den närliggande Blender-katalogen använder *utfällningspanel* för *popover panel*. |
| `3D View Tool: Paint Grease Pencil, Trim (fallback)` | Mappning för punktsamplning med pipett för färggradient | 3D-vyverktyg: måla Grease Pencil, trimma (reserv) | Den tidigare måltexten hör till en annan funktion. *Reserv* följer övriga WindowManager-fallbackar. |

## Verifiering

- `msgfmt --check`: passerar utan fel.
- `l10n-lint --language sv`: inga träffar.
- `svlang skrivregler`: inga träffar.
- Hunspell-träffarna är endast Blender-/API-namn och facktermen
  `shadergruppnod`; de är granskade manuellt.
- Gitleaks: inga hemligheter hittades.
