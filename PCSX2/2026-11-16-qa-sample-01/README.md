# PCSX2 – riktad genomgång av QA-diagnostik

Datum: 2026-11-16  
Tjänst: Crowdin, projekt 561203 (PCSX2 Emulator)  
Språk: `sv-SE`

## Underlag och avgränsning

Projektets aktuella språkstatus är 5 338 av 5 338 fraser översatta, utan automatiskt godkända fraser. Crowdins QA-sammanställning redovisar fortfarande diagnostik. Den här genomgången gäller de första tio posterna i API-svaret, inte hela QA-kön.

## Granskade poster

| Sträng-id | QA-träff | Bedömning |
| --- | --- | --- |
| 3109 | `PCSX2` | Produktnamn; korrekt oförändrat. |
| 3111 | `SCM-version` | Teknisk beteckning; korrekt i sammanhanget. |
| 3113 | Stavning, skiljetecken och HTML-entitet | Svenskan använder den korrekta genitivformen `PS2:ans`; den behöver inte återskapa källans apostrofentitet. Den nyare svenska formuleringen saknar den äldre felskrivningen `an` före `fri`. Ingen säker ändring följer av QA-träffen. |
| 3115 | `Sony Interactive Entertainment` | Egennamn; ska inte översättas. |
| 3123 | `GitHub-förråd` | Korrekt svensk fackterm. |
| 3127 | `RetroAchievements` | Produktnamn; ska inte översättas. |
| 3129 | `RetroAchievements` | Produktnamn; ska inte översättas. |
| 3131 | `retroachievements.org`, `PCSX2`, `åtkomsttoken` | Domän- och produktnamn är korrekta. `åtkomsttoken` är en naturlig svensk teknisk term i den här instruktionen. |

## Resultat

Sträng 3191 hade en verklig avvikelse: de två citattecknen kring det synliga funktionsnamnet `Challenge` hade fallit bort. Den svenska texten rättades till `"Challenge"-läget för prestationer, med spårning av topplistor. Inaktiverar sparade tillstånd, fusk och funktioner för långsam körning.` och sparades via Crowdins API som översättning 450299. En separat API-läsning bekräftade den exakta sparade texten.

Övriga granskade träffar är falska positiva eller avser avsiktliga produktnamn, tekniska namn och korrekt svensk grammatik. Ingen QA-varning avfärdades via API, eftersom det inte behövs för språkgranskningen och det inte ändrar någon översättning.

Crowdins vanliga översättningssvar visar flera historiska förslag för vissa strängar, men inte vilket förslag som visas som aktivt i klienten. Därför gör dokumentet ingen vidare slutsats om historiska förslag än den som kan utläsas ur deras exakta texter.

## Kontroll

- Live-status hämtad från Crowdins språkprogress för `sv-SE`.
- Käll- och måltexter för de noterade strängarna jämförda via Crowdins sträng- och översättningsändpunkter.
- Deltafilen `pcsx2-sv-challenge-mode-qa-fix-20261116.xliff` bevarar exakt käll- och måltext för rättningen.
- Crowdin API-svar: översättning 450299 skapad 2026-11-16 17:04:20 UTC; efterföljande läsning bekräftade samma måltext.
- XML-tolkning och l10n-lint godkände deltafilen utan fel.
- svlang och Hunspell markerar `Challenge`, men det är det synliga funktionsnamnet i källtexten och ska därför behållas. Inga andra språk- eller skrivregelsvarningar återstår.
- `msgfmt` gäller PO-filer och kan inte kontrollera XLIFF; XML-tolkning används därför för filformatet.
- Gitleaks hittade inga hemligheter.
