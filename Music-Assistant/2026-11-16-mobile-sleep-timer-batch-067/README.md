# Music Assistant Mobile – insomningstimer, batch 67

Datum: 2026-11-16

Fem nya utlösare för mobilappens insomningstimer. De är val i samma kontroll,
så de har samma form: “När … är slut”. Det anger tydligt när uppspelningen
ska upphöra.

Terminologi: *audiobook* är *ljudbok*, *chapter* är *kapitel*, *episode* är
*avsnitt* och *track* är *spår*, i enlighet med Music Assistants tidigare
svenska texter. *Current item* återges som *det aktuella objektet*, eftersom
valet kan omfatta fler medietyper än ett musikspår.

Status: alla fem poster uppdaterades via Lokalise API och lästes tillbaka med
samma översättnings-ID:n. API:t bekräftar `is_untranslated: 0` och
`is_fuzzy: false` för varje post. En full ny genomräkning av Music Assistant
Mobiles 615 svenska poster gav 0 tomma och 0 oöversatta värden. Arkivposten
är pushad till vårt arkiv; detta är inte ett upstream-godkännande eller en
release.

Kontroller: JSON, källnycklar, l10n-lint, svlang, Hunspell, kontroll av tre
identiska tecken i följd, diffkontroll och Gitleaks. `msgfmt` är inte
tillämpligt på JSON-kataloger.

`svlang` markerade “När det aktuella objektet är slut” som ett V2-fel. Det är
en falsk positiv, eftersom *När* inleder en bisats där finita verbet korrekt
står senare.
