# QGIS: etikettplacering och hinder 141

Datum: 10 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar etikettplacering, hinder, maskning och skalgränser. HTML,
radbrytningar och synliga QGIS-etiketter bevaras i de berörda texterna.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Maximum angle between curved characters` | `Maxvinkel mellan vridna bokstäver` | `Största vinkel mellan böjda tecken` |
| `Labels will not show if smaller than this on screen` | `Etiketter kommer inte visas om de är mindre än detta på skärmen` | `Etiketter visas inte om de är mindre än detta på skärmen` |
| `Labels will not show if larger than this on screen` | `Etiketter kommer inte visas om de är större än detta på skärmen` | `Etiketter visas inte om de är större än detta på skärmen` |
| `Label z-index` | `Etikettera z-index` | `Etiketternas z-index` |
| `Controls how labels are drawn on top of each other. Labels with a higher z-index are drawn above labels and diagrams with a lower z-index.` | `Kontrollerar hur etiketter skrivs ovanpå varandra. Etiketter med ett högre z-index skrivs ovanpå etiketter och diagram med ett lägre z-index.` | `Styr hur etiketter ritas ovanpå varandra. Etiketter med högre z-index ritas ovanför etiketter och diagram med lägre z-index.` |
| `Show upside-down labels` | `Visa upp- och nervända etiketter` | `Visa uppochnedvända etiketter` |
| `Merge connected lines to avoid duplicate labels` | `Slå ihop linjer med kontakt för att undvika duplicering av texter` | `Slå ihop sammanhängande linjer för att undvika dubblettetiketter` |
| `Number of features sent to labeling engine, though not all may be labeled` | `Antal objekt sända till etikettmotorn, dock etikettsätts kanske inte alla` | `Antal objekt som skickas till etikettmotorn; alla får inte nödvändigtvis etiketter` |
| `Limit number of features to be labeled to` | `Begränsa antalet objekt som ska textsättas till` | `Begränsa antalet objekt som ska etiketteras till` |
| `Suppress labeling of features smaller than` | `Visa inte texter på objekt mindre än` | `Undertryck etiketter för objekt mindre än` |
| `Only draw labels which fit completely within feature` | `Rita enbart ut etiketter som helt passar innanför objekt` | `Rita bara etiketter som ryms helt inom objektet` |
| `Enable kerning` | `Aktivera kerning (anpassning av avstånd mellan tecken)` | `Aktivera kerning` |
| `If enabled, a subset of HTML formatting tags can be used to style text` | `Om aktiverad, kan en delmängd av formateringstaggar i HTML användas för att stilsätta text` | `När alternativet är aktiverat kan en delmängd av HTML-formateringstaggar användas för att formge text` |
| `This mask shape should then be selected as a <span style=" font-style:italic;">mask source</span> in the Masks properties of a layer in order to enable masking.` | `Denna form ska sedan väljas som <span style=" font-style:italic;">mask-källa</span> i egenskaperna för mask i ett lager för att aktivera maskning.` | `<html><head/><body><p>Denna maskform ska sedan väljas som <span style=" font-style:italic;">maskkälla</span> i ett lagers maskegenskaper för att aktivera maskning.</p></body></html>` |
| `Setting a repeat distance allows labels to be repeated multiple times over the length of the feature. This distance is treated as a hint for label placement only, and the exact distance between repeating labels may vary depending on the shape of the feature and arrangement of nearby labels.` | `Att ställa in ett avstånd gör upprepning tillåter etiketter att upprepas flera gånger längs objektets sträckning. Avståndet betraktas bara som ett förslag, och det exakta avståndet mellan upprepade etiketter kan variera beroende på objektets form och närliggande etiketters placering.` | `Med ett upprepningsavstånd kan etiketter upprepas flera gånger längs objektets längd. Avståndet är bara en riktlinje för etikettplaceringen och det exakta avståndet mellan upprepade etiketter kan variera beroende på objektets form och närliggande etiketter.` |
| `Label Overrun` | `Överskridande etiketter` | `Etikettöverskridning` |
| `The overrun distance allows labels which extend past the start or end of line features. Increasing this distance can allow for labels to be shown for shorter line features.` | `Avståndet för överskridning tillåter etiketter som sträcker sig förbi starten eller slutet av linjeobjekt. Att öka avståndet kan tillåta att etiketter visas för kortare linjeobjekt.` | `Etikettöverskridningsavståndet tillåter etiketter att sträcka sig förbi början eller slutet av linjeobjekt. Ett större avstånd kan göra att etiketter visas för kortare linjeobjekt.` |
| `Label Anchoring` | `Etikettinsättning` | `Etikettförankring` |
| `When activated, features acting as obstacles discourage labels and diagrams from covering them.` | `När aktiverad, försöker objekten hindra att etiketter eller diagram täcker dem.` | `När alternativet är aktiverat motverkar objekt som fungerar som hinder att etiketter och diagram täcker dem.` |
| `Allow inferior fallback placements` | `Tillåt sämre placeringar att falla tillbaka på` | `Tillåt sämre reservplaceringar` |
| `The overlap mode controls whether overlapping labels are permitted for features in the layer, and how they should be handled.` | `Överlappningsläget kontrollerar om överlappande etiketter tillåsts för objekt i lagret, och hur de ska hanteras.` | `Överlappningsläget styr om överlappande etiketter tillåts för objekt i lagret och hur de hanteras.` |
| `Generates or transforms the geometry to be used for labeling` | `Skapar eller transformerar geometrin som används för etiketter` | `Skapar eller omvandlar geometri som används för etikettering` |
| `The expression will be applied to each feature while rendering and the label will be placed based on the expression result.` | `Uttrycket kommer att användas för varje objekt under renderingen och etiketten kommer placeras baserat på uttryckets resultat.` | `Uttrycket tillämpas på varje objekt vid rendering och etiketten placeras utifrån uttryckets resultat.` |
| `Prevents other labels from being placed closer than specified margin distance to labels from this layer.` | `Förhindrar att andra etiketter placeras närmare än angivet marginal-avstånd till etiketter från detta lager.` | `Förhindrar att andra etiketter placeras närmare än det angivna marginalavståndet till etiketter från det här lagret.` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
