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

Alla femton var oöversatta i den aktuella Qt-katalogen. Formuleringarna följer
Audacitys etablerade termer `klipp`, `spår` och `spelområde` och är korta
kommandoetiketter enligt respektive källkommentar.

## Verifiering

- `xmllint --noout` godkände den ändrade TS-filen.
- Källplats, platsmarkörer och TS-struktur kontrollerades för varje post; inga
  platshållare förekommer i denna batch.
- Aktuell arbetskopia efter batchen: SHA-256
  `33bf0729c0b0e0347a03db4dd588c946717582cdbaab86caf7925b6badfd304b`.
- `lrelease` saknas i den här miljön, så QM-kompilering har inte påståtts vara
  genomförd.
