# PCSX2: femte riktade genomgången av QA-diagnostik

Datum: 2026-11-16  
Tjänst: Crowdin, projekt 561203 (PCSX2 Emulator)  
Språk: `sv-SE`

## Urval och bedömning

Denna genomgång täcker ett senare urval av stavnings- och
skiljeteckensträffar i Crowdins svenska QA-kö.

| Sträng-id | Källa | Bedömning |
| --- | --- | --- |
| 3659 | `R3` | Synlig handkontrollsbeteckning, korrekt oförändrad. |
| 3661 | `Pressure Modifier` | `Tryckmodifierare` är en korrekt svensk sammansättning. |
| 3673 | `SDL Input Source` | `SDL-inmatningskälla` är korrekt teknisk term. |
| 3717 | `Enable Mouse Mapping` | `Aktivera musmappning` är idiomatiskt i programkontexten. |
| 3749 | `Controller Port %1 Macros` | `Kontrollerport %1-makron` bevarar platshållaren och är korrekt. |
| 3973 | `Subnet Mask:` | `Subnätmask:` är etablerad svensk nätverksterm. |
| 4003 | `HDD File:` | `Hårddiskfil:` är korrekt svensk sammansättning. |
| 4265 | `Maximum Frame Latency:` | `Maximal bildrutelatens:` är korrekt teknisk etikett. |
| 4381 | `Use Software Renderer For FMVs` | `Använd programvarurenderare för FMV:er` är korrekt. |

Sträng 4193 hade däremot en verklig svensk ofullständighet: satsen saknade
verb. `Rich presence` är ett synligt tekniskt funktionsnamn och behålls, men
själva meddelandet rättades till `Funktionen Rich presence är inaktiverad
eller stöds inte.`

## Inskick och återläsning

Den slutliga formuleringen sparades via Crowdin API och lästes därefter
tillbaka som Crowdin-översättning 450331. En tidigare formulering samma minut,
450329, ersattes genast av den tydligare slutliga formuleringen och ska inte
användas som underlag. Ingen historik, röst eller aktiv översättning ändrades
utom genom normala nya Crowdin-förslag.

Detta är sparade Crowdin-förslag, inte belägg för granskning, godkännande
eller release uppströms.

## Kontroller

- XML-tolkning och l10n-lint godkände deltafilen utan fel.
- svlang markerade bara `Rich presence` som sällsynt och gav en V2-varning
  därför att det tvådelade funktionsnamnet feltolkas. Satsen har korrekt
  ordföljd med `Funktionen Rich presence` som subjekt och `är` som finit verb.
- Ett lågprioriterat, avgränsat Hunspell-prov godkände de svenska orden.
  `Rich presence` bedöms som synligt funktionsnamn, inte som ett stavfel.
- Diffkontroll och Gitleaks passerade.
- `msgfmt` gäller PO-filer och är inte tillämpligt på XLIFF; XML-tolkningen
  kontrollerar i stället filformatet.
