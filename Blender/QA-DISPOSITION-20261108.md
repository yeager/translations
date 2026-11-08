# Blender UI – disposition av automatiska QA-träffar

Granskad export: `Downloads/blender-ui-ui-sv (5).po`

SHA-256: `9a4f6b06ee3f64be30f4be80e324f8e0f5059a43ea81b35b8bc3535953fb2d11`
Kontrolldatum: 8 november 2026

`l10n-lint` rapporterar noll fel och 26 varningar. Tabellen avgränsar de
återstående träffarna efter manuell kontextgranskning. Den ersätter inte en
framtida granskning när källsträngen eller användningskontexten ändras.

| Träfftyp | Bedömning | Hantering |
| --- | --- | --- |
| `source-equals-translation` för färgrymder, codecs, API-/formatnamn och matematiska uttryck | Avsiktligt | Produkt-, standard- och formatnamn som `ACES`, `ProRes`, `WebM / VP9`, `Open Shading Language` och uttryck som `A + B` ska behållas. |
| `number-range-dash` för `sRGB IEC 61966-2-1` | Falsk positiv | Bindestrecket ingår i standardidentifieraren, inte i ett svenskt talintervall. |
| `numeric-mismatch` för decimaler och intervall | Falsk positiv | Svensk text använder decimaltecken och mellanrum enligt svensk typografi, till exempel `[0, 1]`; källans maskinella extraktion kan därför inte jämföras bokstavligt. |
| `boundary-character-mismatch` i beskrivningar med parenteser, citat, kod och URI:er | Falsk positiv | Svensk ordföljd och svenska citattecken ändrar strängens första eller sista tecken utan att kod, platshållare eller betydelse går förlorad. |
| `mixed-quotes` i filändelseexemplet | Avsiktligt | Svensk löptext använder typografiska citattecken medan kodexemplet behåller ASCII-citattecken. |
| `punctuation-mismatch` i filnamnsexemplet | Falsk positiv | Källans kolon saknas i löptexten men exempelvärdet `filnamn + .jpg` är bevarat; ingen funktionell interpunktion förloras. |
| `duplicate-words` för Voronoi | Redan åtgärdad lokalt | Den äldre exporten innehåller den tidigare formuleringen. Rättningen finns i batch 1 269 och måste inte dupliceras. |
| `length-ratio` för korta etiketter | Falsk positiv | Svenska sammansättningar och entydiga UI-termer blir ofta längre än korta engelska enordsfält. Varje träff har lästs i sin RNA- eller UI-kontext. |

Följande kontroller passerade för den aktuella exporten: `msgfmt`, l10n-lint,
svlang (enhetlighet, skrivregler och svengelska), Hunspell-sv som
kandidatkontroll och Gitleaks. Hunspell-träffar som gäller kod, formatnamn,
egna namn eller etablerade Blender-fackord är granskningsunderlag och inte
automatiska ändringsförslag.
