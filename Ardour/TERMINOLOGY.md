# Ardour – svensk terminologi

Den här listan avser Ardours gränssnitt för ljud, MIDI, transport och export. Termerna har kontrollerats mot Ardours källsträngar, användarhandbok, den befintliga svenska katalogen och etablerad svensk ljudteknisk användning.

| Engelska | Rekommenderad svenska | Sammanhang och kommentar |
| --- | --- | --- |
| audio interface | ljudgränssnitt | Ljudenhet för inspelning och uppspelning. |
| bus | buss | Behåll DAW-termen, exempelvis `masterbuss` och `monitorbuss`. |
| cue | cue | Ardours namngivna cue-funktion; inte samma sak som en vanlig markör. |
| fade | toning | `fade in`/`fade out` uttrycks vid behov som intoning/uttoning. |
| latency | latens | Används för ljud- och I/O-latens. |
| MIDI note | MIDI-not | `note` är **not** i musikkontext, aldrig teknisk anteckning. |
| note off | Note Off | Standardiserat MIDI-meddelande; behåll termen med versalt O. |
| plugin | insticksmodul | Används i svensk löptext och menyer. Produktformat som VST3 och AudioUnit behålls. |
| preset | förinställning | Gäller insticksmoduler, export och sparade konfigurationer. |
| region | region | Ardours avgränsade medieobjekt på tidslinjen, inte geografiskt område. |
| sample rate | samplingsfrekvens | Exempelvis sessionens samplingsfrekvens. |
| session | session | Etablerad DAW-term. |
| snapshot | ögonblicksbild | Sparat sessionsläge; inte datorskärmdump. |
| timecode | tidskod | Video- och transportsynkronisering. |
| velocity | anslagsstyrka | MIDI-noters dynamiska styrvärde, inte fysisk hastighet. |

## Avsiktliga undantag

- Produktnamn, kommandon, filformat, kodord och MIDI-/videostandarder, till exempel `JACK`, `VST3`, `LUFS`, `SMPTE`, `ffmpeg`, `ffprobe`, `xjadeo`, `harvid` och `dBFS`, översätts inte.
- Låneord som `punch` och `cue` behålls när de namnger Ardours särskilda funktioner; använd annars idiomatisk svensk förklaring i löptext.
