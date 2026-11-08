# Blender UI – bedömda scannerträffar

Följande prioriterade träffar från `l10n-lint` i den lokala UI-exporten har
granskats rad för rad och lämnas avsiktligt oförändrade.

| Källsträng | Regel | Bedömning |
| --- | --- | --- |
| `The bf-translation repository` | versalisering | `bf-translation` är ett projektnamn och ska inte framtvingas till versal initial. |
| `sRGB IEC 61966-2-1 compound (piece-wise) encoding` | talintervall | `IEC 61966-2-1` är en standardidentifierare, inte ett svenskt talintervall. |
| `This data-block is not an independent one ...` | skiljetecken | Svenskan återger innehållet korrekt; varningen bygger på en förenklad skiljeteckenkontroll. |
| `Noise algorithm - Voronoi Crackle ...` | upprepat ord | Den första förekomsten är algoritmnamnet och den andra beskriver Voronoi-tessellering. |
| `The solver does not reiterate, not even on first frame ...` | upprepat ord | ”itererar inte, inte ens” är korrekt och följer källans betydelse. |

Inga ändringar gjordes för dessa träffar. Automatiska varningar används som
granskningsunderlag, inte som ett automatiskt facit.
