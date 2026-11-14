# PCSX2: svensk terminologi

Den här listan gäller den svenska PCSX2-katalogen. Den är ett
granskningsunderlag, inte en ersättning för strängens konkreta UI-kontext.

| Källterm | Svenskt val | Anmärkning |
| --- | --- | --- |
| controller | handkontroll | `Kontroll` används bara när sammanhanget inte gäller en fysisk eller emulerad handkontroll. |
| controller mapping | handkontrollsmappning | `Typ av handkontroll` används hellre än den felaktiga formen `handkontrollertyp`. |
| render | rendering | Används i grafiska inställningar. Produktnamn och API-namn lämnas oförändrade. |
| time stretching | tidssträckning | Gäller SoundTouch och relaterade ljudinställningar. |
| slow motion | långsam uppspelning | Gäller etiketter och snabbtangenter för uppspelningshastighet. |
| fast forward | snabbspolning | Gäller etiketter och snabbtangenter för uppspelningshastighet. |
| Multitap | Multitap | Sony-relaterat tekniskt namn som behålls. |
| Vulkan, OpenGL, Metal | Vulkan, OpenGL, Metal | Grafik-API:er och synliga tekniknamn översätts inte. |
| codec | kodek | Används i svensk löptext och inställningar. |
| load | läs in, inläsning | Välj form efter UI-kontext. Undvik `ladda` när innebörden är att läsa in data eller en fil. |
| savestate | sparläge | Används för emulatorns sparlägesfunktion i beskrivande text. Åtgärden `Save State` skrivs `Spara tillstånd`. |
| PS2 BIOS | PS2-BIOS | Bindestrecket gör den svenska sammansättningen läsbar. |
| BIOS image | BIOS-avbild | Används i installationsguiden och BIOS-inställningarna. |
| game dump, disc dump | skivavbild | Välj `skivavbild` i löptext och hjälptexter; behåll filformatnamn oförändrade. |
| game list | spellista | Gäller PCSX2:s lista över identifierade spel. |
| controller port | handkontrollport | Gäller konsol- och Multitap-portar. |
| train controller | tågförarhandkontroll | Gäller Densha De Go!-kompatibla handkontroller med kraft- och bromsreglage. |
| power lever | kraftspak | Gäller kraftreglaget på tågförarhandkontroller. |
| demangle | demangla | Felsökarterm; behåll den etablerade tekniska formen och böj som `demanglade`. |
| trace logging | spårningsloggning | Gäller felsökarens globala loggningsinställning. |
| software rendering | programvarurendering | Gäller växlingen mellan maskinvaru- och programvarurendering. |
| input recording | inmatningsinspelning | Gäller inspelning och uppspelning av handkontrollsinmatning. |
| deadzone | dödzon | Gäller tröskeln för ratt- och vridningsaxlar i JogCon-inställningarna. |
| condition | villkor | Gäller felsökarens uttrycksparser, inte ett programtillstånd. |
| ternary operator | ternär operator | Gäller felsökarens uttrycksparser. |
| Force Feedback | Force Feedback | Synligt funktionsnamn för rattar och haptisk återkoppling; behålls på engelska i PCSX2:s gränssnitt. |
| present | visa | Gäller visning av redan renderade bildrutor. Undvik `presentera` i grafikinställningarna. |
| frame pacing | bildruteintervall | Gäller jämnheten i tiden mellan visade bildrutor. |
| frame rate | bildrutehastighet | Gäller visad eller emulerad frekvens, bland annat NTSC och PAL. |
| framebuffer | bildbuffert | Gäller grafikdata som både kan visas och användas som inmatningstextur. |
| input lag | inmatningsfördröjning | Gäller fördröjning mellan användarens inmatning och spelets respons. |
| notification | avisering | Gäller PCSX2:s systemmeddelanden och tillhörande ljud. |
| leaderboard | topplista | Gäller resultatlistor i RetroAchievements-relaterade inställningar. |
| overlay | överlägg | Gäller informationslager som visas ovanpå spelbilden. |
| Hardcore Mode | hardcoreläge | RetroAchievements synliga lägesnamn används som produktnamn. |
| Big Picture Mode | Big Picture-läge | Synligt Steam-namn bevaras. |
| header | filhuvud | Gäller filformat och GSDump. |
| draw call | ritanrop | Gäller GS- och renderingsstatistik. |
| texture replacement | texturersättning | Gäller ersättningar som läses in för speltexturer. |
| preload | förinläsning | Gäller särskilt texturer som läses in i cache före användning. |
| TLB hack | TLB-hack | TLB är en teknikförkortning; använd den svenska sammansättningen i spelåtgärder. |
| EE Cycle Skipping | EE-cykelöverhoppning | Gäller hastighetsinställningen för den emulerade Emotion Engine-processorn. |
| Force Even Sprite Position | Tvinga jämn sprite-position | Gäller kryssrutan som minskar mellanrum mellan bildpunkter vid uppskalning. |
| precaching | förinläsning | Gäller förinläsning av skivdata före användning. |
| expand | utvidgning | Gäller SoundTouchs interna ljudutvidgningssteg i latenstext. |
| Use Title File Names | Använd speltitel som filnamn | Etikett i dialogen för omslagsbilder; samma formulering används i dess hjälptext. |
| bilinear filtering | bilinjär filtrering | Gäller grafikinställningen; `Bilinjär` används i korta valetiketter. |
| trilinear filtering | trilinjär filtrering | Gäller grafikinställningen; `Trilinjär` används i korta valetiketter. |
| TV shader | TV-shader | Projektspecifik teknisk sammansättning för TV-liknande bildfilter. |
| interlacing | radsprångsvisning | Används för bildsammanflätning i videoinställningar. |
| interlace offset | radsprångsförskjutning | Gäller den separata grafikinställningen. |
| Game Fixes | spelfixar | Etablerat namn på PCSX2:s särskilda inställningspanel. Böj som plural, till exempel `Spelfixar är inte aktiverade`. |
| patch, game patch | patch, spelpatch | Behålls när det är en teknisk spelpatch eller patchfil. För vanliga programrättningar används i stället `korrigering` eller `programfix` efter kontext. |
| Blit Swap Chain | blit-växlingskedja | Tekniskt grafikval. `Blit` behålls som fackterm medan `Swap Chain` försvenskas. |
| Spin CPU/GPU During Readbacks | Låt CPU:n/GPU:n snurra under återläsningar | Gäller det explicita energikrävande arbetet som håller hårdvaran aktiv vid återläsning. |
