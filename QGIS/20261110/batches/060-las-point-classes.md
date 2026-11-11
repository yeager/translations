# QGIS: LAS-klasser för punktmoln 060

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`  
Källkod: `src/core/pointcloud/qgspointclouddataprovider.cpp`

Terminologikällor: [ASPRS LAS 1.4](https://www.asprs.org/wp-content/uploads/2010/12/LAS_1_4_r13.pdf)
och [Svenska kraftnät om fas- och topplinor](https://www.svk.se/48e643/siteassets/2.utveckling-av-kraftsystemet/transmissionsnatet/utbyggnadsprojekt/betasen-nasse/uppdaterad-koncessionsansokan/miljokonsekvensbeskrivning-version-2.0.pdf).

QGIS visar ASPRS LAS 1.4-klasser som etiketter i punktmoln. Fyra etiketter är
helt oöversatta, `Bridge Deck` har blivit den för breda termen `Bro`, och två
klassnamn har fel pluralform. Termerna för kraftledningar följer Svenska
kraftnäts användning av `topplina`, `fasledare` och `kraftledningsstolpe`.
ASPRS anger att klass 16 omfattar isolatorer och anslutningsdetaljer mellan
ledning och konstruktion, vilket här återges med den korta UI-termen
`Ledningsfäste (isolator)`.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Reserved` | `Reserverade` | `Reserverad` |
| `Wire - Guard (Shield)` | `Wire - Guard (Shield)` | `Topplina (skärm)` |
| `Wire - Conductor (Phase)` | `Wire - Conductor (Phase)` | `Fasledare` |
| `Transmission Tower` | `Transmission Tower` | `Kraftledningsstolpe` |
| `Wire-Structure Connector (Insulator)` | `Wire-Structure Connector (Insulator)` | `Ledningsfäste (isolator)` |
| `Bridge Deck` | `Bro` | `Brobana` |
| `High Noise` | `High Noise` | `Kraftigt brus` |
| `User Definable` | `Användardefinerade` | `Användardefinierad` |

`Reserved` förekommer i tre källkodslägen men är en och samma
översättningsenhet. Ingen extern ändring har gjorts; aktuella
Transifex-enhetsidentifierare behöver hämtas innan en deltafil kan skapas.
