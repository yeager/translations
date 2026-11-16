# PCSX2 – kontroll av QA-kategorier med högre felrisk

Datum: 2026-11-16  
Tjänst: Crowdin, projekt 561203 (PCSX2 Emulator)  
Språk: `sv-SE`

## Urval

Hela den åtkomliga svenska QA-kön filtrerades till andra kategorier än ren stavningskontroll. Därifrån granskades samtliga träffar för tal, platshållare eller avslutande skiljetecken som kan innebära en verklig funktionsrisk.

| Sträng-id | Källtext | Måltxt | Bedömning |
| --- | --- | --- | --- |
| 13062 | D3D11-fel med `0x{:08X}` och `10.0` | Samma platshållare och versionsnummer | Korrekt. QA tolkar inte versionsnumrets format. |
| 13366 | `Create Default "%1" Layout` | `Skapa standardlayouten "%1"` | Korrekt svensk ordföljd och bevarad platshållare. Semikolonvarningen är felaktig. |
| 13958 | CPU-trådar med `(P)` och `(E)` | Samma tekniska markörer | Korrekt; `12:e` ersätter inte ett betydelsebärande tal utan svensk ordningstalsskrivning. |
| 14618, 14620 | `Merge 2 Fields` | `sammanfoga två fält` | Korrekt utskrivet svenskt räkneord. |
| 15698 | Källan saknar punkt | Svenskan har punkt | Korrekt svensk meningsinterpunktion. |
| 16059, 16165 | Källan saknar slutpunkt och använder apostrofgenitiv | Svenskan har punkt och `spelets` | Korrekt svenska; apostrofentiteten ska inte kopieras. |
| 16667 | `%1x%2 (%3x)` | `%1×%2 (%3×)` | Alla platshållare är bevarade. Multiplikationstecknet är avsiktlig svensk typografi för dimensionsformat. |

## Resultat

Ingen ändring skickades in. Inga kontrollerade träffar visade en verklig platshållar-, siffer- eller skiljeteckenskada. QA-kön innehåller därför både korrekta och irrelevanta automatiska markeringar; den kan inte användas som underlag för massändringar.

## Kontroll

- Käll- och måltexter lästes via Crowdins API.
- Ingen katalogfil eller upstream-översättning ändrades i denna genomgång.
- Gitleaks hittade inga hemligheter i granskningsloggen.
