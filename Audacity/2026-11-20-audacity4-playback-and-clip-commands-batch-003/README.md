# Audacity 4 – uppspelning och klippkommandon, batch 3

Radgranskning av Qt TS-katalogen `audacity4-sv-review-batch-002-20261120.ts`.

| Källsträng | Svensk översättning | Källfil och rad |
| --- | --- | --- |
| `Seek` | `Sök` | `playbackcommandsregister.cpp:102` |
| `Change play region` | `Ändra spelområde` | `playbackcommandsregister.cpp:115` |
| `Cut clip` | `Klipp ut klipp` | `trackeditcommandsregister.cpp:76` |
| `Copy clip` | `Kopiera klipp` | `trackeditcommandsregister.cpp:89` |
| `Delete clip` | `Ta bort klipp` | `trackeditcommandsregister.cpp:102` |
| `Split cut clip` | `Dela och klipp ut klipp` | `trackeditcommandsregister.cpp:115` |
| `Split delete clip` | `Dela och ta bort klipp` | `trackeditcommandsregister.cpp:128` |
| `Split tracks at` | `Dela spår vid` | `trackeditcommandsregister.cpp:190` |
| `Mix and render` | `Mixa och rendera` | `trackeditcommandsregister.cpp:331` |
| `Group` | `Gruppera` | `trackeditcommandsregister.cpp:361` |
| `Ungroup` | `Avgruppera` | `trackeditcommandsregister.cpp:370` |
| `Set selection` | `Ställ in markering` | `trackeditcommandsregister.cpp:451` |
| `Select track` | `Markera spår` | `trackeditcommandsregister.cpp:464` |
| `At zero crossings` | `Vid nollgenomgångar` | `trackeditcommandsregister.cpp:476` |
| `Split track` | `Dela spår` | `trackeditcommandsregister.cpp:804` |

Alla etthundratjugo var oöversatta i den aktuella Qt-katalogen. Formuleringarna följer
Audacitys etablerade termer `klipp`, `spår` och `spelområde` och är korta
kommandoetiketter enligt respektive källkommentar.

## Fortsatt radgranskning

Ytterligare 22 oöversatta kommando- och hjälptexter granskades i samma
katalog. De omfattar linjalens och tidslinjens snabbmenyer, effektkommandon,
inställningsgenvägar, molnprojekt, FFmpeg-export, rullning och uppspelning.
De nya översättningarna är: `Öppna linjalens snabbmeny`, `Använd %1`,
`Konfigurera %1`, `Om Qt`, `Be om hjälp`, `Öppna inställningarna för
kortkommandon`, `Öppna redigeringsinställningarna`, `Öppna
spektrograminställningarna`, `Visa/dölj makrohanteraren`, `Öppna rundturen på
audio.com och logga in först vid behov`, `Öppna den inloggade användarens
profilsida på audio.com`, `Hantera en audacity://-URL`, `Öppna molnprojekt`,
`Importera mediefiler till ett nytt projekt`, `Öppna de anpassade
exportalternativen för FFmpeg`, `Öppna anpassad kanalmappning för export`,
`Rulla tidslinjen åt vänster en skärmbredd`, `Rulla tidslinjen åt höger en
skärmbredd`, `Öppna tidslinjens snabbmeny`, `Spela upp de angivna spåren`,
`Flytta spelhuvudet till angiven tid` och `Ändra spelområdet`.

`%1` har kontrollerats och bibehållits. `swedish-foss-terminology` och
`swedish-tm` ger stöd för `Konfigurera %1`; övriga val har kontrollerats mot
Audacitys källkontext. Hunspell markerar enbart egennamn och etablerade
produktnamn i det här tillskottet. `svlang` hittar inga nya mekaniska
skrivregelfel; dess katalogomfattande signaler gäller äldre, ej ändrade poster.

## Fortsatt radgranskning: spårredigering

Ytterligare 27 oöversatta hjälptexter har kompletterats för tidsinställd
inspelning, klippoperationer, samplingsfrekvens, gruppering, tidsmarkering,
nollgenomgång, spårfärg, sammanslagning, duplicering, delning och
effektförinställningar. Samtliga är direkta UI-åtgärder och har granskats mot
sin respektive `trackeditcommandsregister.cpp`-kontext. Skillnaden mellan
*klipp* och *spår* bevaras, och `given` återges konsekvent som `angivna` när
kommandot arbetar på parametriserade objekt.

Tre avslutande kommandohjälptexter i avsnittet har också översatts:
`Använd %1 med de angivna parametrarna`, `Välj parametrarna för %1 utan att
använda den` och `Exportera projektljudet som en MP3-fil till mappen för
makroutdata`. Platshållaren `%1` är oförändrad.

## Diagnostik och automatisk duckning

Tolv ytterligare oöversatta poster har granskats: en diagnostiktext med `%1`
och Auto duck-effektens två namnposter, reglage och förklarande feltext.
Effekten översätts konsekvent som `Automatisk duckning`, medan dess etablerade
tekniska funktion förklaras med `Kontrollspår`, `Nivåsänkning` och `Hålltid`.
Platshållaren `%1` är bibehållen exakt.

## Makrohanteraren

27 oöversatta strängar för att redigera, köra, flytta, exportera och ta bort
makron har kompletterats. Alla `%1`-platshållare och typografiska citattecken
har bevarats, och makrorelaterade meny- och tabellrubriker använder konsekvent
`makro`, `makron` och `makrokommando`.

Ytterligare 14 makrosträngar för körning på filer, status, filer och
steghantering har kompletterats. Tre platshållare och radbrytningen i
felmeddelandet om saknade steg är bevarade exakt.

## Verifiering

- `xmllint --noout` godkände den ändrade TS-filen.
- Källplats, platsmarkörer och TS-struktur kontrollerades för varje post; inga
  platshållare förekommer i denna batch.
- Aktuell arbetskopia efter batchen: SHA-256
  `a1a47e4835c8b728c14174c07201d8f6f53bc4f585a5dadbbd1d021c1000a466`.
- `lrelease` saknas i den här miljön, så QM-kompilering har inte påståtts vara
  genomförd.
