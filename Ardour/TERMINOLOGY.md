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
| punch range | punchintervall | Det specifika intervall som styr punch-in/-ut-inspelning; det är inte ett musikaliskt slagintervall. |
| fade | toning | `fade in`/`fade out` uttrycks vid behov som intoning/uttoning. |
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
| Bars:Beats | Takter:slag | Musikaliskt tidsformat i linjal, klocka och exportval. |
| MIDI program change | MIDI-programändring | MIDI-händelse som väljer program/klang; inte en allmän programförändring. |
| MIDI patch / patch selection | MIDI-program / MIDI-programval | Väljare för MIDI-bank och -program; undvik oöversatta `patch` i svensk UI-text. |
| Medium (sinc) | Medel (sinc) | Mellanläget för sinc-baserad samplingsfrekvensomvandling vid export. `sinc` är algoritmens namn och behålls. |
| note off | Note Off | Standardiserat MIDI-meddelande; behåll termen med versalt O. |
| plugin | insticksmodul | Används i svensk löptext och menyer. Produktformat som VST3 och AudioUnit behålls. |
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
| region tempo | regionstempo | Tempostyrning som hör till en enskild region. |
| region automation line | automatiseringslinje för regionen | Automatiseringskurva för en kontrollegenskap i en regioneffekt. |
| route group / Collect Group | grupp / Samla grupp | En grupp kopplar samman spår eller bussar. Åtgärden placerar medlemmarna intill varandra i redigeraren eller mixern. |
| range tool | intervallverktyg | Verktyget markerar ett tidsintervall för bland annat redigering och analys. |
| range mode | intervalläge | Redigeringsläge som använder en tidsintervallmarkering. |
| sample rate | samplingsfrekvens | Exempelvis sessionens samplingsfrekvens. |
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
| send/output | sändning/utgång | I/O-paret för extern routing; `output` betyder ljudutgång, aldrig utskrift. |
| solo isolate | soloisolering | Förhindrar att ett spår tystas när andra spår solospelas. |
| Slide (edit mode) | Flytta | Fritt redigeringsläge där regioner kan flyttas och överlappa. |
| Ripple (edit mode) | Krusning | Etablerad term i svensk videoredigering; efterföljande regioner flyttas vid redigering. |
| snapshot | ögonblicksbild | Sparat sessionsläge; inte datorskärmdump. |
| time-stretch quality | Mjuk / Jämn / Tydlig / Blandad | Kvalitetsval för Rubber Band-algoritmens transientbehandling. Termerna beskriver behandlingen, inte ett visuellt tillstånd. |
| timecode | tidskod | Video- och transportsynkronisering. |
| MTC rate/drop | bildfrekvens-/drop-frame-värde | MTC-fältet kombinerar bildfrekvens och drop-frame-markering; översätt inte som fysisk hastighet eller minskning. |
| track | spår | Spår i tidslinjen, mixern och analysfönstret; aldrig verbet `spåra`. |
| transport master | transportmaster | Ardours synkroniseringskälla för transporten; ett sammansatt substantiv i svensk UI-text. |
| monitor dim / cut | monitordämpning / monitoravstängning | Funktioner för att tillfälligt sänka respektive stänga av kontrollrummets monitorutgång. |
| peak meter | mätare | PeakMeter är Ardours signalnivåmätare; den korta UI-etiketten ska därför följa katalogens redan etablerade svenska `mätare`. |
| auto punch | automatisk punch | Ardours namngivna DAW-funktion för automatiskt punch-in/punch-out; termen `punch` behålls, inte den missvisande `stämpling`. |
| VCA master | VCA-master | Ardours VCA-styrning för flera kanalers nivå; `master` behålls som etablerad ljudteknisk term. |
| AFL / PFL solo | solo efter/före fader | Soloavlyssning efter respektive före kanalens fader. Förkortningarna AFL och PFL behålls. |
| loudness analysis | ljudstyrkeanalys | Analys av ljudstyrka enligt export- och masterbussens kontext; inte en generell volymmätning. |
| limiter | begränsare | Processor som begränsar signalens toppnivå i masterbussens signalflöde. |
| loudness | ljudstyrka | Mätbar upplevd ljudnivå, bland annat uttryckt i LUFS. |
| clip tempo | klipptempo | Det tempo Ardour uppskattar för ett ljudklipp i en triggerplats; används som underlag för tidssträckning mot sessionens tempo. |
| time-stretching | tidssträckning | Anpassning av ett klipps längd/tempo till sessionens tempokarta. |
| I/O resampling | I/O-omprovtagning | Omprovtagning som Ardour använder för uppspelning eller inspelning med vari-speed. |
| peak | toppnivå | Signalens högsta nivå i krav på export och normalisering. |
| peak file | toppfil | Analysfil som innehåller vågforms- eller toppinformation; `Rebuild` innebär att bygga om den, inte återställa den. |
| edit range / edit point | redigeringsintervall / redigeringspunkt | Tidsintervall eller punkt som används av Ardours redigeringsåtgärder. |
| denormal handling | hantering av denormala tal | Inställning för mycket små flyttal i DSP-behandling. |
| limit/normalize peak | begränsa/normalisera toppnivå | Exportinställningar för högsta signalnivå; `peak` ska inte bli den ogrammatiska formen `gränsvärde topp`. |
| shaped noise | brusformning | Ditheringens brusformning; ljudteknisk term, inte bokstavliga `formad brus`. |
| pre-roll | förrullning | Transportens förlopp före uppspelning eller inspelning, inte förhandsvisning. |
| document root / docroot | dokumentrot | Videoserverns katalogrot för publicerade videoresurser; behåll inte den oöversatta interna termen `docroot` i användargränssnittet. |
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

## Avsiktliga undantag

- Produktnamn, kommandon, filformat, kodord och MIDI-/videostandarder, till exempel `JACK`, `VST3`, `LUFS`, `SMPTE`, `ffmpeg`, `ffprobe`, `xjadeo`, `harvid` och `dBFS`, översätts inte.
- Låneord som `punch` och `cue` behålls när de namnger Ardours särskilda funktioner; använd annars idiomatisk svensk förklaring i löptext.
