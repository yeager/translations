# QGIS: punktmolnsfrågor och rendering 095

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar frågebyggaren och renderarens hjälpfunktioner för punktmoln.
Platshållarna `%1`, radbrytningen i tolkfelet och de två tomma raderna i
zoomhjälpen bevaras. `Eye Dome Lighting` återställs exakt som tekniskt namn
enligt batch 079.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Set provider filter on %1` | `Sätt datakällsfilter på %1` | `Ange dataleverantörsfilter för %1` |
| `An error occurred while parsing the expression:\n%1` | `Ett fel uppstod vid tolkningen av uttrycket: %1` | `Ett fel uppstod när uttrycket tolkades:\n%1` |
| `"%1" not recognized as an available attribute.` | `"%1" är inte igenkänt som ett tillgängligt attribut.` | `"%1" känns inte igen som ett tillgängligt attribut.` |
| `The expression was successfully parsed.` | `Uttrycket lyckades tolkas.` | `Uttrycket tolkades utan fel.` |
| `Customize label text` | `Anpassa etikettext` | `Anpassa etiketttext` |
| `This renderer doesn't implement a graphical interface.` | `Denna renderare har inget grafisk gränssnitt.` | `Den här renderaren har inget grafiskt gränssnitt.` |
| `Show tile labels` | `Visa etikett för tile` | `Visa rutiketter` |
| Hjälpen för `Overview switching scale` | Felaktigt `dess utsträckningar` och otydlig zoomtext | `Anger zoomnivån då de enskilda punktmolnsfilerna renderas i stället för översikten eller deras utbredningar.\n\nNormal innebär ungefär att punktmolnets utbredning inte längre ryms inom kartans utbredning.\n\nVälj Tidigare för att växla vid mindre skala, när du har zoomat ut, eller Senare för att växla vid större skala, när du har zoomat in.` |
| `Eye-Dome Lighting` | `Eye- Dome Lighting` | `Eye Dome Lighting` |
| `Adjusts how strong the added shading will be. Greater values mean stronger effect.` | `Justerar hur stark den tillagda skuggningen kommer bli. Större värden ger större effekt.` | `Justerar styrkan hos den tillagda skuggningen. Ett högre värde ger en starkare effekt.` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
