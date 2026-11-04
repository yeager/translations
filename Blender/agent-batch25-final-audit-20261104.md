# Slutgranskning: Blender Manual batch 25

Granskad fil: `blender-manual-sv-review-batch-20261104-25.po`.
Underlag: råexporten `blender-manual-manual-sv.po`, Blender UI-katalogen,
`TERMINOLOGY.md` samt den dubbelgranskade införandeplanen för
`animation/actions.rst`.

| Källa | Bedömning | Skäl |
| --- | --- | --- |
| `Action Slots` | Godkänd | `Åtgärdsslotar` följer projektets termbeslut; `slott` skulle ha fel betydelse. |
| Actions och slotar, rad 32 | Godkänd | Förklaringen återger relationen mellan åtgärd, slot och animerat objekt utan engelsk syntax. |
| Sammanfattning, rad 37 | Godkänd | Fetmarkering och innebörden för åtgärds- respektive slotnamn är bevarade. |
| Animeringsdata, rad 39 | Godkänd | `datablock`, `åtgärd` och `slot` används konsekvent och korrekt. |
| Väljare, rad 45 | Godkänd | Den svenska UI-beskrivningen är sakligt korrekt. |
| F-kurvor, rad 131 | Godkänd | RST-destinationen är exakt bevarad; `F-kurva` och `nyckelbild` är etablerade Blender-termer. |
| Grafredigeraren, rad 138 | Godkänd | Synlig länktext är lokaliserad, men destinationssökvägen är orörd. |
| Dopebladet, rad 148 | Godkänd | Följer UI-katalogens `Dope Sheet` → `Dopeblad`; RST-målet är bevarat. |
| Manuell tilldelning, rad 194 | Godkänd | Förklarar korrekt att den första nyckelbilden skapar en tom slot. |
| Högtalarens panel, rad 221 | Godkänd | RST-identifieraren är oförändrad och svensk possessivform fungerar i en rubrik. |
| Filmklippets panel, rad 222 | Godkänd | Korrekt svensk sammansättning och intakt RST-mål. |
| Nodgruppens panel, rad 224 | Godkänd | Korrekt svensk sammansättning och intakt RST-mål. |

## Verktygskontroll

- `msgfmt --check`: godkänd.
- `l10n-lint`: inga fel eller varningar.
- `svlang skrivregler`: inga skrivregelfel i batchens svenska måltexter.
- Hunspell återrapporterar förväntade kod-, RST- och Blenderidentifierare;
  inga oavsedda svenska stavfel hittades.
- Gitleaks: inga träffar.
- `git diff --check -- Blender`: inga fel.

## Slutsats

Samtliga 12 poster är godkända för den samlade, ännu ej uppladdade
manualbatchen. Ingen råexport har ändrats.
