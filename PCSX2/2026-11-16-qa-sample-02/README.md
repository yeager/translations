# PCSX2 – andra riktade genomgången av QA-diagnostik

Datum: 2026-11-16  
Tjänst: Crowdin, projekt 561203 (PCSX2 Emulator)  
Språk: `sv-SE`

## Underlag

Genomgången täcker nästa sammanhängande urval ur Crowdins svenska QA-kö. Alla träffar i urvalet är stavnings-, versal- eller entitetskontroller. Käll- och måltext hämtades för de träffar som kräver faktisk språklig bedömning.

## Bedömning

| Sträng-id | Träff | Bedömning |
| --- | --- | --- |
| 3307–3323 | `VU0`, `VU1`, `mVU`, `MIPS-I`, `Flag-hack`, `Clamping-läge`, `omkompilerare` | Emulator- och processorbegrepp. Bindestreck och svenska sammansättningar är avsiktliga och korrekta. |
| 3327–3329 | `spelfixar`, `kompatibilitetspatcher` | Naturliga svenska sammansättningar i användargränssnittet. |
| 3433 | `ljudutdata` | Källan beskriver värdens ljudutgång. Översättningen `värdens ljudutdata` är korrekt och tekniskt tydlig. |
| 3497 | `PCSX2` | Produktnamn; ska behållas. |
| 3519 | Saknad `&apos;` | Källan har engelsk genitiv i `console's`. Svenskans `konsolens` är korrekt utan apostrofentitet. |
| 3631–3637, 3657 | `L1`, `L2`, `L3`, `R1`, `R2` | Synliga handkontrollsbeteckningar; ska behållas. |
| 3639 | Versaler | Källtexten är `Start`, men målet `START` återger den etablerade knapptangenten på handkontroller. Avsiktlig versalisering. |
| 3641 | `Select` | Synligt knapptangsnamn; ska behållas på engelska. |

## Resultat

Ingen ändring skickades in från detta urval. Samtliga träffar är falska positiva eller korrekt bevarade produkt-, processor- och handkontrollsbeteckningar. Inga QA-varningar avfärdades via API.

## Kontroll

- QA-kön och relevanta exakta käll- och måltexter hämtades via Crowdins API.
- Ingen katalogfil eller översättning ändrades i denna genomgång.
- Gitleaks hittade inga hemligheter i granskningsloggen.
