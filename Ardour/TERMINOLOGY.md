# Ardour – svensk terminologi

Den här listan avser Ardours gränssnitt för ljud, MIDI, transport och export. Termerna har kontrollerats mot Ardours källsträngar, användarhandbok, den befintliga svenska katalogen och etablerad svensk ljudteknisk användning.

| Engelska | Rekommenderad svenska | Sammanhang och kommentar |
| --- | --- | --- |
| audio interface | ljudgränssnitt | Ljudenhet för inspelning och uppspelning. |
| audition | förhandslyssning / förhandslyssna | Substantiv i rubriker och statusfält, verb i uppmaningar. Avser tillfällig uppspelning för kontroll av material eller MIDI-program. |
| Bender (MIDI) | tonhöjdsböjning | MIDI-lane för pitch-bend-data, inte det engelska agentordet `bender`. |
| bus | buss | Behåll DAW-termen, exempelvis `masterbuss` och `monitorbuss`. |
| clip library | klippbibliotek | Ardours katalog med återanvändbara klipp; `clip` är här ett medieklipp, inte ett programklipp. |
| cue | cue | Ardours namngivna cue-funktion; inte samma sak som en vanlig markör. |
| fade | toning | `fade in`/`fade out` uttrycks vid behov som intoning/uttoning. |
| fade length | toningslängd | Längden på en intoning eller uttoning i verktyget för att ta bort tystnad. |
| feedback (audio) | rundgång | Varning för återkopplad ljudsignal eller felaktig portanslutning. |
| foldback | medhörning | Svenska ljudtekniska termen för musikernas monitorlyssning; `foldback bus` blir **medhörningsbuss**. |
| follow action | följåtgärd | Åtgärd som clip launcher-funktionen utför när ett klipps följlängd har löpt ut. |
| follow length | följlängd | Den användardefinierade speltid som föregår en följåtgärd; projektspecifik UI-term. |
| gain | förstärkning | Ljudnivå före eller i fader-/regionbearbetning; `vinst` används inte i ljudgränssnittet. |
| latency | latens | Används för ljud- och I/O-latens. |
| legatize | Gör legato | MIDI-redigeringsåtgärd som anpassar notlängder så att noterna binds samman. |
| MIDI note | MIDI-not | `note` är **not** i musikkontext, aldrig teknisk anteckning. |
| MIDI program change | MIDI-programändring | MIDI-händelse som väljer program/klang; inte en allmän programförändring. |
| MIDI patch / patch selection | MIDI-program / MIDI-programval | Väljare för MIDI-bank och -program; undvik oöversatta `patch` i svensk UI-text. |
| Medium (sinc) | Medel (sinc) | Mellanläget för sinc-baserad samplingsfrekvensomvandling vid export. `sinc` är algoritmens namn och behålls. |
| note off | Note Off | Standardiserat MIDI-meddelande; behåll termen med versalt O. |
| plugin | insticksmodul | Används i svensk löptext och menyer. Produktformat som VST3 och AudioUnit behålls. |
| Pinout | stiftkonfiguration | Knappen öppnar Ardours fönster för insticksmodulens in- och utgångsstift. Följer katalogens befintliga `Pin Configuration` → **Stiftkonfiguration**. |
| panner | panorerare | Reglage eller modul som placerar signalen i stereobilden eller surroundfältet. |
| pre-/post-fader | före/efter fader | Mät- och sändningspunkt i signalflödet. |
| preset | förinställning | Gäller insticksmoduler, export och sparade konfigurationer. |
| region | region | Ardours avgränsade medieobjekt på tidslinjen, inte geografiskt område. |
| route group / Collect Group | grupp / Samla grupp | En grupp kopplar samman spår eller bussar. Åtgärden placerar medlemmarna intill varandra i redigeraren eller mixern. |
| range tool | intervallverktyg | Verktyget markerar ett tidsintervall för bland annat redigering och analys. |
| sample rate | samplingsfrekvens | Exempelvis sessionens samplingsfrekvens. |
| sample (library asset) | ljudprov | En återanvändbar ljudfil i klipp- eller samplingsbiblioteket; skiljs från det tekniska samplingsvärdet i `sample rate`. |
| sound on sound | ljud på ljud | Inspelningsläge där nya regioner läggs i ett lager och befintligt material fortfarande hörs. |
| session | session | Etablerad DAW-term. |
| Strip Silence | Ta bort tystnad | Verktyget klipper bort avsnitt under en angiven tystnadströskel utan att förstöra ursprungsljudet. |
| solo isolate | soloisolering | Förhindrar att ett spår tystas när andra spår solospelas. |
| Slide (edit mode) | Flytta | Fritt redigeringsläge där regioner kan flyttas och överlappa. |
| Ripple (edit mode) | Krusning | Etablerad term i svensk videoredigering; efterföljande regioner flyttas vid redigering. |
| snapshot | ögonblicksbild | Sparat sessionsläge; inte datorskärmdump. |
| time-stretch quality | Mjuk / Jämn / Tydlig / Blandad | Kvalitetsval för Rubber Band-algoritmens transientbehandling. Termerna beskriver behandlingen, inte ett visuellt tillstånd. |
| timecode | tidskod | Video- och transportsynkronisering. |
| track | spår | Spår i tidslinjen, mixern och analysfönstret; aldrig verbet `spåra`. |
| transport master | transportmaster | Ardours synkroniseringskälla för transporten; ett sammansatt substantiv i svensk UI-text. |
| VCA master | VCA-master | Ardours VCA-styrning för flera kanalers nivå; `master` behålls som etablerad ljudteknisk term. |
| AFL / PFL solo | solo efter/före fader | Soloavlyssning efter respektive före kanalens fader. Förkortningarna AFL och PFL behålls. |
| loudness analysis | ljudstyrkeanalys | Analys av ljudstyrka enligt export- och masterbussens kontext; inte en generell volymmätning. |
| velocity | anslagsstyrka | MIDI-noters dynamiska styrvärde, inte fysisk hastighet. |
| Video Server | videoserver | Ardours externa tjänst för videovisning och videohantering. |

## Avsiktliga undantag

- Produktnamn, kommandon, filformat, kodord och MIDI-/videostandarder, till exempel `JACK`, `VST3`, `LUFS`, `SMPTE`, `ffmpeg`, `ffprobe`, `xjadeo`, `harvid` och `dBFS`, översätts inte.
- Låneord som `punch` och `cue` behålls när de namnger Ardours särskilda funktioner; använd annars idiomatisk svensk förklaring i löptext.
