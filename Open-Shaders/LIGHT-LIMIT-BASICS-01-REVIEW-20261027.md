# Begränsning av ljuskällor: grunder, häfte 01

## Omfattning

Häftet omfattar 16 tidigare oarkiverade nycklar för skuggatlas, ljuskällors
detaljnivå och prestandamätare i `feature.light_limit_fix`.

## Språkval

- `shadow atlas` och `shadow map` är **skuggatlas** och **skuggkarta**.
- `tile` är **ruta** och `reallocation` är **omfördelning**, eftersom den
  delade atlasens utrymme flyttas mellan ljuskällor.
- Texten efter `##` är en teknisk identifierare och lämnas oförändrad.
- Samtliga formatmarkörer, inledande blanksteg och radbrytningar bevaras.

## Kontrollresultat

JSON-syntax, `l10n-lint`, Gitleaks, formatmarkörer, bokstavliga
procenttecken och radbrytningar är godkända. Hunspell hittade ett verkligt
skrivfel, `ega`, som rättades till `egna` med bibehållen radbrytning.
Återstående Hunspell-träffar är formatfragment, tekniska identifierare och
fackord. `svlang` ger 4,0 av 10 eftersom en tekniskt tät flerradsdialog
innehåller många ord utanför frekvenslistan; de fem V2-varningarna är
grammatiskt korrekta satser.

Filen ska jämföras med en ny Weblate-export innan import kan ske.
