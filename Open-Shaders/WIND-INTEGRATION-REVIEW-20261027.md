# Open Shaders: Wind – integrationsgranskning 2026-10-27

De 17 små Wind-häftena har sammanfogats till
`open-shaders-wind-sv-20261027.json`. Jämförelsen mot den aktuella engelska
källkatalogen visar 279 av 279 nycklar, utan saknade eller extra poster.

JSON-syntax, `l10n-lint` och Gitleaks är godkända. Samtliga formatmarkörer,
`##`-metadata, bokstavliga procenttecken och radbrytningar stämmer med
källan. Kontroll av tre lika konsonanter i följd är också godkänd efter att
URL:er har undantagits.

`svlang` ger tekniska frekvenssignaler och V2-varningar för imperativ,
fackspråk och fullständiga svenska huvudsatser. Signalerna har kontrollerats
manuellt; inga faktiska V2-fel återstår. Hunspell-listan består av tekniska
sammansättningar, speltermer, filnamn och bevarade identifierare.

Weblate-komponenten är fortfarande låst. Den färdiga komponentfilen ska
jämföras med en ny export före import när låset har hävts.
