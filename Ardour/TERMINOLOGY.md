# Ardour – svensk terminologi

Den här listan avser Ardours gränssnitt för ljud, MIDI, transport och export. Termerna har kontrollerats mot Ardours källsträngar, användarhandbok, den befintliga svenska katalogen och etablerad svensk ljudteknisk användning.

| Engelska | Rekommenderad svenska | Sammanhang och kommentar |
| --- | --- | --- |
| audio interface | ljudgränssnitt | Ljudenhet för inspelning och uppspelning. |
| audition | förhandslyssning / förhandslyssna | Substantiv i rubriker och statusfält, verb i uppmaningar. Avser tillfällig uppspelning för kontroll av material eller MIDI-program. |
| Auditioner | förhandslyssningsspår | Ardours interna spår för förhandslyssning. Kodidentifieraren behålls i tekniska symboler, men diagnoser beskriver funktionen på svenska. |
| Bender (MIDI) | tonhöjdsböjning | MIDI-lane för pitch-bend-data, inte det engelska agentordet `bender`. |
| bus | buss | Behåll DAW-termen, exempelvis `masterbuss` och `monitorbuss`. |
| clip library | klippbibliotek | Ardours katalog med återanvändbara klipp; `clip` är här ett medieklipp, inte ett programklipp. |
| cue | cue | Ardours namngivna cue-funktion; inte samma sak som en vanlig markör. |
| bounce to trigger slot / Clip Library | mixa ner till triggerplats / klippbiblioteket | Åtgärden renderar eller kopierar bearbetat material till en triggerplats eller användarens klippbibliotek. `Studsa` är missvisande i detta DAW-sammanhang. |
| bounce | mixa ner | Meny- och dialogåtgärd som renderar markerat material till en ny ljudkälla, med eller utan bearbetning. |
| launch style | startläge | Valet `Trigger`, `Retrigger`, `Gate`, `Toggle` eller `Repeat` styr hur ett klipp startas. Det är ett funktionsläge, inte en produktlansering eller en stil. |
| punch range | punchintervall | Det specifika intervall som styr punch-in/-ut-inspelning; det är inte ett musikaliskt slagintervall. |
| fade | toning | `fade in`/`fade out` uttrycks vid behov som intoning/uttoning. |
| fade-in length/shape/active | intoningslängd/intoningsform/aktivera intoning | Parametrar och åtgärder för en regions intoning. Använd inte den konkurrerande termen `inbländning` i samma UI. |
| stretch tempo / stretch end tempo | sträck tempo / sträck sluttempot | Ångraåtgärder när användaren drar en tempopunkt eller en temposlutpunkt; de är verbfraser och inte beskrivningen `sträckt tempo`. |
| crossfade | korstoning | Överlappande in- och uttoning mellan två regioner. |
| region fades | regiontoningar | Toningar knutna till en regions början eller slut. |
| fade length | toningslängd | Längden på en intoning eller uttoning i verktyget för att ta bort tystnad. |
| Fade before Fx | toning före effekter | Regionen tonas före bearbetning med dess effekter. |
| feedback (audio) | rundgång | Varning för återkopplad ljudsignal eller felaktig portanslutning. |
| foldback | medhörning | Svenska ljudtekniska termen för musikernas monitorlyssning; `foldback bus` blir **medhörningsbuss**. |
| follow action | följåtgärd | Åtgärd som clip launcher-funktionen utför när ett klipps följlängd har löpt ut. |
| follow length | följlängd | Den användardefinierade speltid som föregår en följåtgärd; projektspecifik UI-term. |
| gain | förstärkning | Ljudnivå före eller i fader-/regionbearbetning; `vinst` används inte i ljudgränssnittet. |
| latency | latens | Används för ljud- och I/O-latens. |
| samples latency | samplingars latens | Latens uttryckt som antal samplingsvärden; undvik särskrivningen `samplings latens`. |
| round-trip latency | rundreselatens | Sammanlagd latens för utgående och återgående I/O-signal. |
| legatize | Gör legato | MIDI-redigeringsåtgärd som anpassar notlängder så att noterna binds samman. |
| MIDI note | MIDI-not | `note` är **not** i musikkontext, aldrig teknisk anteckning. |
| MIDI All Notes Off | MIDI-kommandot All Notes Off | Standardiserat MIDI-kanalmeddelande 123. Namnet behålls för igenkänning, men UI-texten anger att det är ett MIDI-kommando. |
| Bars:Beats | Takter:slag | Musikaliskt tidsformat i linjal, klocka och exportval. |
| MIDI program change | MIDI-programändring | MIDI-händelse som väljer program/klang; inte en allmän programförändring. |
| MIDI patch / patch selection | MIDI-program / MIDI-programval | Väljare för MIDI-bank och -program; undvik oöversatta `patch` i svensk UI-text. |
| Medium (sinc) | Medel (sinc) | Mellanläget för sinc-baserad samplingsfrekvensomvandling vid export. `sinc` är algoritmens namn och behålls. |
| note off | Note Off | Standardiserat MIDI-meddelande; behåll termen med versalt O. |
| plugin | insticksmodul | Används i svensk löptext och menyer. Produktformat som VST3 och AudioUnit behålls. |
| plugin editor | insticksmodulsredigerare | Fönster för en enskild insticksmoduls reglage och egenskaper; skriv ihop enligt svensk sammansättningsprincip. |
| pin mode | stiftläge | Ruttens läge för stiftanslutningar; samma `stift` som i stiftkonfigurationen. |
| plugin DSP load | insticksmodulers DSP-belastning | Belastning från insticksmoduler på digital signalbehandling; `DSP` behålls som etablerad förkortning. |
| plugin GUI | insticksmodulens gränssnitt | Inställningsrubrik för insticksmodulens grafiska användargränssnitt. |
| plugin setup | konfiguration av insticksmodul | Dialog för den valda insticksmodulens anslutningar och parametrar. |
| plugin input/output configuration | insticksmodulens ingångs-/utgångskonfiguration | Konfiguration av insticksmodulens signalstift. |
| no-inplace | ej in-place | Teknisk debuggetikett: insticksmodulen kan inte bearbeta i samma buffert utan behöver en tillfällig kopia. |
| output presets | förinställningar för utgångar | Förinställda konfigurationer för insticksmodulens utgångar. |
| plugin scan | skanning av insticksmoduler | Sökning och uppdatering av den lokala listan över tillgängliga insticksmoduler. |
| Pinout | stiftkonfiguration | Knappen öppnar Ardours fönster för insticksmodulens in- och utgångsstift. Följer katalogens befintliga `Pin Configuration` → **Stiftkonfiguration**. |
| MIDI Input Pins | MIDI-ingångar | MIDI-anslutningar till en insticksmodul; samma korta UI-term som ljudingångar. |
| panner | panorerare | Reglage eller modul som placerar signalen i stereobilden eller surroundfältet. |
| panner controls | panorerarkontroller | Kontroller som hör till en panorerarmodul. |
| surround panner | surroundpanorerare | Panorerarmodul som placerar signaler i ett surroundfält. |
| Stereo Panner | stereopanorerare | Stereo-varianten av Ardours panorerarmodul. |
| pre-/post-fader | före/efter fader | Mät- och sändningspunkt i signalflödet. |
| preset | förinställning | Gäller insticksmoduler, export och sparade konfigurationer. |
| region | region | Ardours avgränsade medieobjekt på tidslinjen, inte geografiskt område. |
| opaque region | ogenomskinlig region | Inställningen gör att regioner på lager under den inte hörs; `ogenomskinlig` är den etablerade redigeringsmetaforen här, inte en optisk beskrivning av ljudet. |
| region tempo | regionstempo | Tempostyrning som hör till en enskild region. |
| region automation line | automatiseringslinje för regionen | Automatiseringskurva för en kontrollegenskap i en regioneffekt. |
| route group / Collect Group | grupp / Samla grupp | En grupp kopplar samman spår eller bussar. Åtgärden placerar medlemmarna intill varandra i redigeraren eller mixern. |
| range tool | intervallverktyg | Verktyget markerar ett tidsintervall för bland annat redigering och analys. |
| region boundary | regionsgräns | Gräns vid en enskild regions början eller slut; skrivs som en sammansättning. |
| selected regions | valda regioner | Aktuellt markerade regioner i Ardours UI; använd konsekvent `valda`, inte den blandade formen `utvalda`. |
| range mode | intervalläge | Redigeringsläge som använder en tidsintervallmarkering. |
| sample rate | samplingsfrekvens | Exempelvis sessionens samplingsfrekvens. |
| sample-rate mismatch | samplingsfrekvenserna stämmer inte överens | Konflikt mellan två källors samplingsfrekvenser, inte en enskild felaktig frekvens. |
| Plugin Editor | insticksmodulsredigerare | Dialog som redigerar en specifik insticksmoduls kontroller och egenskaper. |
| resampling | omprovtagning | Konvertering mellan samplingsfrekvenser vid import eller export. |
| sample position / sample time | samplingsposition | Position uttryckt i samplingsenheter; det är varken samplingsfrekvens eller en fysisk tidpunkt. |
| sample format | samplingsformat | Kodningsformatet för individuella samplingsvärden vid import eller export, inte ett exempel-format. |
| sample (library asset) | ljudprov | En återanvändbar ljudfil i klipp- eller samplingsbiblioteket; skiljs från det tekniska samplingsvärdet i `sample rate`. |
| snap length | fästlängd | Längd enligt aktuell fästnings- eller rutnätsinställning. |
| sound on sound | ljud på ljud | Inspelningsläge där nya regioner läggs i ett lager och befintligt material fortfarande hörs. |
| session | session | Etablerad DAW-term. |
| Strip Silence | Ta bort tystnad | Verktyget klipper bort avsnitt under en angiven tystnadströskel utan att förstöra ursprungsljudet. |
| state directory | tillståndskatalog | Katalog som hör till en sparad spårmall och innehåller dess tillståndsdata. Inte en statlig katalog. |
| serialized state / state file | tillstånd / tillståndsfil | Sparat eller XML-serialiserat Ardour-tillstånd, exempelvis en sessions eller regions inställningar; skiljs från allmän användarstatus. |
| auto-map | automatisk mappning | Automatisk tilldelning av importerade kanaler till lokala spår efter ID eller namn. |
| automation point / guard point | automatiseringspunkt / skyddspunkt | En redigerbar punkt på en automatiseringslinje; skyddspunkter bibehåller form och värden vid närliggande ändringar. |
| send routing | sändningsruttning | Hur en sändning kopplas mellan kanal, buss och utgång. |
| port-matrix destination | mål | Kolumn- eller radhuvud för signalens anslutningsmål. `Resmål` har en transportbetydelse och passar inte signalruttning. |
| send/output | sändning/utgång | I/O-paret för extern routing; `output` betyder ljudutgång, aldrig utskrift. |
| solo isolate | soloisolering | Förhindrar att ett spår tystas när andra spår solospelas. |
| Slide (edit mode) | Flytta | Fritt redigeringsläge där regioner kan flyttas och överlappa. |
| Ripple (edit mode) | Krusning | Etablerad term i svensk videoredigering; efterföljande regioner flyttas vid redigering. |
| snapshot | ögonblicksbild | Sparat sessionsläge; inte datorskärmdump. |
| recording take | inspelningstagning | En enskild inspelning i Ardours inspelningsflöde; skiljs från den resulterande regionen och dess ljudfiler. |
| time-stretch quality | Mjuk / Jämn / Tydlig / Blandad | Kvalitetsval för Rubber Band-algoritmens transientbehandling. Termerna beskriver behandlingen, inte ett visuellt tillstånd. |
| Stretch Mode | tidssträckningsläge | Redigerarläge för tidssträckning av ljud- och MIDI-regioner med bibehållen tonhöjd. |
| timecode | tidskod | Video- och transportsynkronisering. |
| mux | multiplexera | Videoexport som kopierar videoströmmen till den nya behållaren utan omkodning; `mux` är inte ett svenskt verb i UI-text. |
| MTC rate/drop | bildfrekvens-/drop-frame-värde | MTC-fältet kombinerar bildfrekvens och drop-frame-markering; översätt inte som fysisk hastighet eller minskning. |
| track | spår | Spår i tidslinjen, mixern och analysfönstret; aldrig verbet `spåra`. |
| record-enabled / rec-armed | inspelningsaktiverad | Ett spår som har aktiverats för inspelning; aldrig de bokstavliga felöversättningarna `återbeväpnad` eller `omarmerad`. |
| editor-selected | redigeringsvald | Spår eller buss som är valt i redigeraren, inte ett separat redigeringskommando. |
| transport master | transportmaster | Ardours synkroniseringskälla för transporten; ett sammansatt substantiv i svensk UI-text. |
| monitor dim / cut | monitordämpning / monitoravstängning | Funktioner för att tillfälligt sänka respektive stänga av kontrollrummets monitorutgång. |
| monitor channel action | stäng av/dämpa/solospela monitorkanal | Åtgärder för en enskild kanal i monitorsektionen; `cut` är signalavstängning, inte redigeringskommandot `klipp`. |
| monitor processor box | processorpanelen i monitorsektionen | Den visningsbara panel där monitorsektionens effektprocessorer hanteras; åtgärden visar eller döljer panelen. |
| return/input | retur/ingång | Returens inkommande signal i den externa I/O-insatsen; `input` är ljudingång, inte textinmatning. |
| peak meter | mätare | PeakMeter är Ardours signalnivåmätare; den korta UI-etiketten ska därför följa katalogens redan etablerade svenska `mätare`. |
| auto punch | automatisk punch | Ardours namngivna DAW-funktion för automatiskt punch-in/punch-out; termen `punch` behålls, inte den missvisande `stämpling`. |
| VCA master | VCA-master | Ardours VCA-styrning för flera kanalers nivå; `master` behålls som etablerad ljudteknisk term. |
| AFL / PFL solo | solo efter/före fader | Soloavlyssning efter respektive före kanalens fader. Förkortningarna AFL och PFL behålls. |
| pre-/post-fader processor or send | processor eller sändning före/efter fader | Signalflödets placering i förhållande till fadeln. `pre-fader` och `post-fader` översätts i beskrivande UI-texter, medan AFL/PFL behålls där de är standardförkortningar. |
| loudness analysis | ljudstyrkeanalys | Analys av ljudstyrka enligt export- och masterbussens kontext; inte en generell volymmätning. |
| limiter | begränsare | Processor som begränsar signalens toppnivå i masterbussens signalflöde. |
| loudness | ljudstyrka | Mätbar upplevd ljudnivå, bland annat uttryckt i LUFS. |
| clip tempo | klipptempo | Det tempo Ardour uppskattar för ett ljudklipp i en triggerplats; används som underlag för tidssträckning mot sessionens tempo. |
| roll (transport) | starta uppspelning | Transportåtgärden anropar `transport_roll`; den kastar inte material. |
| play range | spela upp intervallet | Menyåtgärden anropar `Editor::play_selection()` för det valda tidsintervallet. |
| playhead forward/backward | flytta spelhuvudet framåt/bakåt | Åtgärden flyttar genom att begära en ny transportposition; den spelar inte ljud bakåt. |
| jump target | mål för hopp | Målval för triggerfunktionen `FollowAction::JumpTrigger`; ordningen är naturligare än sammansättningen `hoppmål`. |
| toggle record | växla inspelning | Verktygstips för transportens inspelningsknapp; aktiverar eller inaktiverar inspelning, inte växling mellan textposter. |
| play range/selection | spela upp intervall/markering | Verktygstips för transportknappen som spelar valt intervall eller markerat material. |
| marker click only selects | klick på markör markerar endast | Radioläge som förhindrar att ett markörklick flyttar transportpositionen. |
| rolling transport | när transporten rullar | Åsyftar pågående transport, inte nödvändigtvis aktiv inspelning. |
| sustained / percussive note mode | uthålligt / perkussivt läge | MIDI-redigerarens visuella notlägen: uthållna toner ritas med längd, perkussiva toner som träffar. |
| Smart Mode | smartläge | Redigerarläge som lägger vissa intervallfunktioner till flyttläget; skrivs som svensk sammansättning. |
| Smart | smartläge | Den förkortade menyetiketten för samma redigerarläge som `Smart Mode`; den ska följa den fullständiga svenska formen. |
| I/O map | I/O-mappning | Insticksmodulens tilldelning av signalin- och utgångar. |
| tempo map | tempokarta | Visningen i MIDI-filinformationen beskriver en karta med flera tempoavsnitt. |
| tempo mapping: end-stretch / mid-twist | tempokartläggning: slutsträcka / sträckning i mitten | Ångra-beskrivningar när en tempoändring dras vid slutet eller mellan omgivande tempopunkter. `mid-twist` är en sträckning av den mittersta delen, inte en oöversatt produktterm. |
| VCA Assigns | VCA-tilldelningar | Mixerremsans visningsval för kopplingar till VCA-master; substantiv, inte verbet `tilldelar`. |
| VCA Assign | VCA-tilldelning | Rubrik och verktygstips för samma VCA-koppling; singularform för den enskilda kontrollen. |
| Disassociate | koppla från | Åtgärden lösgör en kanals anslutning i bunthanteraren; den oidiomatiska direktformen `icke-associera` används inte. |
| Monitor Buttons | monitorknappar | Mätarbryggans knappar för monitorfunktioner, inte en allmän övervakningskategori. |
| Main Outs | huvudutgångar | Signalvägens huvudsakliga utgångar i Ardours ruttmeny. |
| Broadcast Wave | Broadcast Wave | Namnet på ljudfilformatet (BWF); det är inte en beskrivning av sändningsvågor. |
| time-stretching | tidssträckning | Anpassning av ett klipps längd/tempo till sessionens tempokarta. |
| varispeed | varispeed | Ardours etablerade namn för variabel uppspelnings- eller inspelningshastighet. I sammansättningar skrivs det med bindestreck, exempelvis **MTC-varispeed**. |
| drag deadzone | dödzon för dragning | Inställning för den rörelse som krävs innan en dragåtgärd börjar påverka ett reglage. |
| I/O resampling | I/O-omprovtagning | Omprovtagning som Ardour använder för uppspelning eller inspelning med vari-speed. |
| peak | toppnivå | Signalens högsta nivå i krav på export och normalisering. |
| peak file | toppfil | Analysfil som innehåller vågforms- eller toppinformation; `Rebuild` innebär att bygga om den, inte återställa den. |
| edit range / edit point | redigeringsintervall / redigeringspunkt | Tidsintervall eller punkt som används av Ardours redigeringsåtgärder. |
| denormal handling | hantering av denormala tal | Inställning för mycket små flyttal i DSP-behandling. |
| limit/normalize peak | begränsa/normalisera toppnivå | Exportinställningar för högsta signalnivå; `peak` ska inte bli den ogrammatiska formen `gränsvärde topp`. |
| shaped noise | brusformning | Ditheringens brusformning; ljudteknisk term, inte bokstavliga `formad brus`. |
| pre-roll | förrullning | Transportens förlopp före uppspelning eller inspelning, inte förhandsvisning. |
| document root / docroot | dokumentrot | Videoserverns katalogrot för publicerade videoresurser; behåll inte den oöversatta interna termen `docroot` i användargränssnittet. |
| session framerate / timecode framerate | sessionsbildfrekvens / sessionens tidskods bildfrekvens | Bildfrekvens i video- och tidskodssynkronisering; använd genitivformen för att visa vilket tidskodssystem värdet hör till. |
| MIDI patch change | MIDI-programändring | Ändring av MIDI-programmet på ett instrument eller spår. |
| DPM fall-off | DPM-avklingning | Tidsförloppet när digitala toppmätare faller tillbaka, inte ett avbrott. |
| locate | gå till | Transportåtgärden flyttar spelhuvudet till markör eller tidpunkt; `lokalisera` är här en oidiomatisk direktöversättning. |
| Solo-in-place mute cut | ljuddämpning i solo-in-place | Nivådämpning som används när solo-in-place aktiveras; skiljs från ett fysiskt avbrott. |
| outboard gear | extern utrustning | Extern ljudutrustning som kräver export i realtid. |
| velocity | anslagsstyrka | MIDI-noters dynamiska styrvärde, inte fysisk hastighet. |
| MIDI patch / `.midnam` patch file | MIDI-program / MIDI-programfil | `MidiPatchManager` läser in namn- och programdefinitioner från `.midnam`-filer; `patch` ska inte bli anglicismen `patch` i denna användartext. |
| Patch Selector | MIDI-programväljare | Menyåtgärden väljer MIDI-program för ett MIDI-spår eller instrument. |
| meter colors / track color | mätarfärger / spårfärg | Val för MIDI-spårets färgsättning; `Track Color` är spårfärg, inte en generell bakgrundsfärg. |
| `AutomationList` diagnostic | fick XML-noden | Källkoden lämnar en XML-nod till listan; använd inte den bokstavliga och felaktiga formen `passerade XML-nod`. |
| allow mush | tillåt begränsning | Vid MIDI-redigering får värden begränsas till intervallet 0–127 i stället för att hela åtgärden avbryts. |
| Video Server | videoserver | Ardours externa tjänst för videovisning och videohantering. |
| fixed time region drag | dra region med låst tidsposition | Ångra-beskrivning för en regionsförflyttning som är låst i tidsled och därför bara kan byta spår eller lager. |
| I/O output | utgång | I/O-väljarens ljudutgång; `utdata` är inte den etablerade DAW-termen här. |
| input / output | ingång / utgång | Signalanslutningar och kanalens I/O i Ardour; använd inte processorden `inmatning` och `utmatning` för dessa kontroller. |
| systemic latency | systemlatens | Fast, intern latens i ljud- eller MIDI-systemet. |
| round-trip latency | rundreselatens | Uppskattad sammanlagd latens från utgång tillbaka till ingång; i mätningstexten är **uppmätt** mer precist än `upptäckt`. |
| sample count | samplingar | Antal diskreta samplingsvärden i en ljudbuffert eller latensangivelse. |
| transient | transient | Kort, snabb amplitudförändring i ljudmaterial; `Placera transient` skapar eller flyttar dess redigeringsposition. |
| Auto Input | Automatisk ingång | Transportstyrd övervakning där spårens ljudingångar lyssnas när transporten är stoppad; en funktion, inte allmän textinmatning. |
| onset | ansats | Starten på en ton eller ljudhändelse i Rhythm Ferrets onsetdetektering; `anfall` är en falsk vän. |
| inter-onset time | tid mellan ansatser | Minsta tidsintervall mellan detekterade ljudansatser. |
| cut position | klipp-position | Position där Rhythm Ferret delar en region; bindestreck används för att undvika tre p i följd. |
| peak hold time | hålltid för toppvärde | Tidslängd som nivåmätaren behåller sitt toppvärde. |
| Bars & Beats | takter och slag | Musikalisk tidsvisning; `bar` är takt och `beat` är slag i Ardours svenska UI. |
| auto-punch in/out | automatisk punch-in/punch-out | Transportens automatiska inspelningsstart och -stopp vid punchgränserna. |
| I/O tooltip input/output | INGÅNG/UTGÅNG | Versala rubriker i I/O-knappens verktygstips; avser ljudanslutningar, inte allmänna data. |
| input monitoring | ingångslyssning | Övervakning av spårets inkommande ljudsignal, styrd av transporten eller monitorvalet. |
| master level meter | masternivåmätare | Nivåmätare för masterbussen i redigerarens programrad. |
| pitch shift audio | Förskjut ljudets tonhöjd | Dialog som ändrar tonhöjd utan att vara en etikett för en abstrakt `tonhöjdsförskjutning`. |
| sync position | synkroniseringsposition | Transportmasterns avlästa synkroniseringsposition i dialogens kolumnrubrik. |
| meterbridge | mätarbrygga | Ardours fönster med samtidiga nivåmätare; översätt komponentnamnet i användarvända feltexter. |
| quick snapshot | snabb ögonblicksbild | Snabbt sparad ny versionsbild av sessionen; `översikt` ändrar betydelsen. |
| cycle edit mode | Växla redigeringsläge | Växlar mellan redigeringslägen; det är en åtgärd, inte namnet på ett särskilt cykelläge. |
| VU Meter standard | VU-mätarstandard | Standard för VU-mätning; skrivs som en sammansättning. |
| sample data | samplingsdata | Diskreta ljudvärden i en källfil eller buffert; skiljs från ett återanvändbart ljudprov i biblioteket. |
| file mapping | filkartläggning | Operativsystemets minnesmappning av en toppfil; `mappning` är processen, inte en geografisk karta. |
| I/O inputs / outputs | ingångar / utgångar | Portanslutningar i Ardours interna I/O-XML; använd inte de generiska formerna `inmatningar` och `utdata`. |
| input/output device | ingångs-/utgångsenhet | Ljudmotorns fysiska eller virtuella ljudenhet; samma signalvägstermer som i I/O-väljaren. |
| bundle | bunt | Ardours objekt som grupperar ljud- eller MIDI-portar och kanaler; inte ett filpaket. `Bundle Manager` blir **Bunthanterare**. |
| monitor channel cut | stäng av monitorkanal | `cut_channel()` stänger av signalen; det är inte klippning av ljudmaterial. |
| VCA state | VCA-tillstånd | Sparat/återställt tillstånd för ett VCA-objekt; inte allmän användarstatus. |
| plugin-stub | insticksmodulsstubb | Ersättningsprocessor när den ursprungliga insticksmodulen inte kan konfigureras vid sessionsinläsning. Ardours övriga svenska UI använder redan `stub`/`stubbar`; `stubb` följer den befintliga tekniska användningen och sammanhanget är en diagnostiklogg. |
| MTC quarter-frame message | MTC-quarter-frame-meddelande | Namngivet MIDI Time Code-protokollmeddelande. MTC skickar åtta sådana delmeddelanden för att överföra en hel tidskodsposition; behåll protokollnamnet i stället för den felaktiga vardagsbilden `kvartersram`. |
| downcast | nedkonvertera | Programmeringsterm för en explicit omvandling från basklass till underklass; `nedgradera` betyder i stället att sänka version eller kvalitet. |
| plugin scan | skannar insticksmoduler | Pågående förloppsstatus från insticksmodulhanteraren; verbformen är konsekvent med övriga statusrader och inte en menyåtgärd i infinitiv. |
| plugin order | insticksmodulsordning | Sparad ordning i vilken insticksmoduler visas eller behandlas; använd inte den ogenomskinliga sammansättningen `insticksmodulsorderfil`. |
| corrupt cache file | skadad cachefil | Filen har ogiltigt eller skadat innehåll; `korrupt` undviks i svensk användartext. |
| audio I/O bundle | bunt / ingångsbunt / utgångsbunt | Namngiven samling av Ardours ljudportar. I feltexter används `bunt`; med den variabla riktningen blir sammansättningen till exempel `ingångsbunt`. `paket` används inte eftersom det syftar på program- eller filpaket. |
| unclean shutdown | okontrollerad avstängning | Processen avslutades utan ordnad nedstängning och portregistret behöver återställas; varken `orättvis` eller `smutsig` avstängning uttrycker betydelsen. |
| control surface protocol | kontrollyteprotokoll | Protokoll för en extern fysisk eller virtuell kontrollyta; skrivs som svensk sammansättning, inte den brutna formen `kontrollyta-protokoll`. |
| Rubber Band stretcher | Rubber Band-tidssträckare | Rubber Bands processor för ljudets tidssträckning i Ardour. Produktnamnet behålls, medan funktionsnamnet översätts. |
| locate | gå till | Transportåtgärden flyttar spelhuvudet till en position; `positionera` är ett otydligt verb här. |
| send / return | sändning / retur | Signalvägens sändning och returlänk. `send` är i dessa namn ett substantiv, inte imperativet `skicka`; `return` är inte programflödets `returnera`. |
| foldback | medhörning | Separat återgivningssignal för medverkande eller musiker. |
| Solo-Isolate propagation | soloisoleringsspridning | Intern signalvägsuppdatering av Ardours soloisolering; bind inte ihop den med engelska `Solo-Isolate`. |
| Click I/O | klickets I/O | Klickmetronomens signalanslutningar; `Click` är ett substantiv här, inte uppmaningen `Klicka`. |
| Butler | Butler | Ardours interna bakgrundstråd för diskbaserad uppspelning och inspelning. Klassnamnet behålls och skrivs med versal. |
| read-ahead / write-behind | framåtläsning / efterskrivning | Butler fyller upp uppspelningsbuffertar från disk respektive skriver inspelningsdata till disk i efterhand. `diskström` används för den berörda diskströmmen i diagnostiken. |
| Snap to Speaker | Fäst vid högtalare | Växlar att ett surroundobjekt fästs vid en högtalarposition; `snäpp` är här inte etablerad svensk UI-terminologi. |
| MIDI note / note ID | not / not-ID | Tonhändelse och dess identifierare i Ardours MIDI-modell. `anteckning` är en falsk vän i musik- och MIDI-kontext. |
| MIDI note property | notegenskap | Egenskap hos en MIDI-not i den serialiserade ändringen; sammansättningen skiljer betydelsen från en allmän anteckningsegenskap. |
| complete MIDI/audio file | hela MIDI-/ljudfilen | Regionen skapas för filens hela innehåll, inte för en allmänt beskriven `komplett` fil. |
| input / output latency | ingångslatens / utgångslatens | Begärda värden för ljudgränssnittets signalväg. De är särskilda latensvärden, inte allmänt beskrivna förseningar. |
| period count | antal perioder | Ljudgränssnittets antal bearbetningsperioder i buffertkonfigurationen. |
| solo cut control | solodämpningskontroll | Gain-liknande kontroll för konfigurationsvärdet `solo-mute-gain`, uttryckt i dB. |
| monitor section | monitorsektion | Ardours namngivna monitorfunktion; använd samma term i feltexter som i gränssnittet. |
| Console1 Send | Console1 Send | Reserverat I/O-namn för Softubes Console 1-kontroll; produktnamn och portnamn översätts inte. |
| Console1 Recv | Console1 Recv | Reserverat I/O-namn för Softubes Console 1-kontroll; måste behålla exakt produktnamn och portändelse. |
| sample position | samplingsposition | Diskläsarens exakta position i en ljuddataström; `prov` skulle avse en fysisk provbit och saknar positionsbetydelsen. |
| diskstream / diskstream-id | diskström / diskströms-id | Äldre sessionsmetadata identifierar en diskbaserad spårström. Behåll den tekniska identifierarformen med svensk sammansättning i diagnostiken. |
| explicit solo | direkt solo | Spåret är solospelat av egen kontroll, i motsats till upp- eller nedströms spritt solo. |
| CPU DMA latency request | CPU-DMA-latensbegäran | Linux-gränssnittets begäran om minsta DMA-latens. Förkortningen behålls med bindestreck som svensk teknisk sammansättning. |
| Stop and Forget Capture | Stoppa och förkasta inspelningen | Transportåtgärd som stoppar rullning och kastar inspelat material; `Capture` är inte ett egennamn här. |
| Solo Selection | Spela upp endast markeringen | Transportåtgärd som spelar endast den aktuella redigeringsmarkeringen; det är inte ett substantiviskt urval av solon. |
| inline mixer-strip controls | direktvisade mixerremskontroller | Insticksmodulkontroller som visas direkt i mixerremsan, begränsade genom inställningen `max-inline-controls`. |
| Play loop | loopuppspelning | Transportläge som tvingar kontinuerlig uppspelning av loopintervallet. |
| global strip template | global mall för mixerremsa | Mall som är tillgänglig för alla sessioner, till skillnad från en sessionslokal mixerremsmall. |
| loop range / punch range | loopintervall / punchintervall | Namngivna Ardour-intervall för upprepad uppspelning respektive automatisk punch. Skrivs som svenska sammansättningar utan onödigt bindestreck. |
| Play/Start/Finish Loop or Punch Range | Spela upp/Starta/Avsluta loop- eller punchintervallet | Åtgärder på det bestämda, aktuella intervallet. `stansningsområde` och `slingintervall` används inte. |
| Add/assign pre-fader or post-fader | lägg till/tilldela före fader eller efter fader | Signalflödets position anges med svensk fras i alla blandar- och ruttdialoger; lämna inte `prefader` eller `postfader` oöversatt. |
| Return (signal route) | retur | Returväg i Ardours signalflöde och processorlista; aldrig navigeringsordet `Tillbaka` eller den bokstavliga `återlämning`. |
| Sync (settings category) | synkronisering | Namn på kategorin med A/V-, video- och extern synkroniseringsinställning; det är ett substantiv, inte uppmaningen `Synkronisera`. |
| timecode frames-per-second / fps | tidskodens bildfrekvens / tidskod: bildfrekvens | Bildfrekvensen som tidskodsformatet använder; `ramar per sekund` är en direktöversättning som inte följer svensk videoteknisk term. |
| Transport Master | transportmaster | Ardours valda transport-synkroniseringskälla; ett sammansatt namn, inte `transportmästare`. |

## Avsiktliga undantag

- Produktnamn, kommandon, filformat, kodord och MIDI-/videostandarder, till exempel `JACK`, `VST3`, `LUFS`, `SMPTE`, `ffmpeg`, `ffprobe`, `xjadeo`, `harvid` och `dBFS`, översätts inte.
- Låneord som `punch` och `cue` behålls när de namnger Ardours särskilda funktioner; använd annars idiomatisk svensk förklaring i löptext.
