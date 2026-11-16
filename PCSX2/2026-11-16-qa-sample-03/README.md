# PCSX2 – tredje riktade genomgången av QA-diagnostik

Datum: 2026-11-16  
Tjänst: Crowdin, projekt 561203 (PCSX2 Emulator)  
Språk: `sv-SE`

## Tre verifierade integritetsavvikelser

| Sträng-id | Källa och kontext | Korrekt befintlig översättning | Senare felaktigt förslag |
| --- | --- | --- | --- |
| 5379 | `%1 (%2)`; versionsnummer och tidsstämpel | `%1 (%2)` (översättning 252904) | `Ansluten till %1:%2: skickar begäran` (268860) |
| 6067 | `PC`; kort etikett för *Program Counter* i avlusaren | `PC` (255694) | `st` (268926) |
| 7213 | `B 1`; USB-handkontrollens knapptangentskod | `B 1` (255728) | `Identifierad till konto: <b>%1</b>` (268958 och 293328) |

De felaktiga förslagen kan inte vara korrekta för respektive källsträng: de saknar nödvändiga platshållare, innehåller text från orelaterade funktioner eller förvanskar en kort teknisk etikett.

## Uppladdningskontroll

Crowdins API nekade nya inskick med de korrekta måltexterna som dubbletter. API:t svarade: `Duplicate translation. Please vote or approve the original.` De korrekta strängarna finns alltså redan som historiska översättningar.

Ingen röst, ändring eller radering gjordes på de äldre förslagen. Projektets svenska arbetsflöde har inga automatiskt godkända översättningar enligt aktuell språkprogress, och ett byte av aktiv historisk översättning kräver en uttrycklig, projektgodkänd metod. Det är därför inte säkert att tvinga fram ändringen via API.

## Övriga QA-träffar i urvalet

Entitetsträffar för engelskans apostrof och träffar på kolon i svenska sammansättningar bedömdes mot exakt källtext. De är falska positiva när svenskan använder korrekt genitiv eller `CPU:n`/`GPU:n`. `Bredbilds-` och `kompatibilitetspatchar` är korrekta svenska sammansättningar.

## Kontroll

- Källkontext samt alla tillgängliga svenska förslag för de tre strängarna lästes via Crowdins API.
- Ett nytt normalt API-inskick testades för sträng 5379 och avvisades som en dubblett. Ingen data ändrades av försöket.
- Ingen katalogfil eller upstream-översättning ändrades i den här genomgången.
- Gitleaks hittade inga hemligheter i granskningsloggen.
