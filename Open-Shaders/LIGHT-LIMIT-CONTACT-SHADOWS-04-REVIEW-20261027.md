# Begränsning av ljuskällor: kontaktskuggor, häfte 04

## Omfattning

Häftet omfattar 16 oarkiverade strängar för inställning och diagnos av
kontaktskuggor.

## Språkval

- `contact shadows` är **kontaktskuggor** och `raymarch` är
  **strålmarsch** i den tekniska hjälpen.
- `CLUSTERED`, `lightDist/radius` och LOD är kod- eller motortermer och
  behålls för att inte ändra logikens betydelse.
- `cull` uttrycks som **gallring** i diagnostexten.

## Kontrollresultat

JSON-syntax, `l10n-lint`, Gitleaks, formatmarkörer, bokstavliga
procenttecken och radbrytningar är godkända. Språkverktyget hittade
`skugggallring`, som rättades till **gallring av skuggor** enligt regeln om
tre lika konsonanter. Kommat före `och` i en lång teknisk mening ersattes med
semikolon. Övriga V2-varningar gäller grammatiskt korrekta facktexter.
Hunspell-träffarna är tekniska identifierare och granskade fackord.

Filen ska jämföras med en ny Weblate-export innan import kan ske.
