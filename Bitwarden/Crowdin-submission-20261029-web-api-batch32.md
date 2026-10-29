# Bitwarden Web — Crowdin API-häfte 32

Fem HTTP-autentiseringstexter återanvänder de redan kvalitetssäkrade svenska
formuleringarna från Bitwarden Browser och Desktop. Web-komponenten saknade
fortfarande aktuella svenska måltexter för samtliga fem nycklar.

- Projekt: Bitwarden - Web (`308189`), svenska (`sv-SE`).
- Underlag: `Bitwarden-Web-api-http-auth-batch32-20261029.json`.
- Översättnings-id: `1980803`–`1980811`.

Efter POST lästes samtliga fem måltexter tillbaka från Crowdins API med exakt
textjämförelse. `turnOnPasswordRepromptTitle` passerar Crowdins QA; de fyra
övriga är sparade som förslag med projektets QA-status `failed` och väntar på
mänsklig granskning. Platshållare förekommer inte i häftet.

Före uppladdning passerade JSON-validering, `svlang skrivregler` och
`hunspell-sv`.
