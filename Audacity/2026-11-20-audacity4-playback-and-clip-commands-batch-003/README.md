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

Alla sju var oöversatta i den aktuella Qt-katalogen. Formuleringarna följer
Audacitys etablerade termer `klipp`, `spår` och `spelområde` och är korta
kommandoetiketter enligt respektive källkommentar.

## Verifiering

- `xmllint --noout` godkände den ändrade TS-filen.
- Källplats, platsmarkörer och TS-struktur kontrollerades för varje post; inga
  platshållare förekommer i denna batch.
- Aktuell arbetskopia efter batchen: SHA-256
  `ea4a3c81935acf0abb103a09c771cb193b2e49efd9e9395386467957a34b1d9c`.
- `lrelease` saknas i den här miljön, så QM-kompilering har inte påståtts vara
  genomförd.
