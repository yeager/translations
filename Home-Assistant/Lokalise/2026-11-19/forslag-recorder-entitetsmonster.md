# Recorder: entitetsmönster och databasnamn

Kontrollerat mot engelska och svenska i Lokalise 2026-11-19. Detta är **lokala förslag**, inte sparade ändringar i Lokalise. Kontrollera aktuella värden igen före eventuell användning.

## `component::recorder::services::purge_entities::fields::entity_globs::name`

**Engelska:** Entity globs to remove

**Befintlig svenska:** Entity-globs att ta bort

**Förslag:** Globmönster för entiteter som ska tas bort

Motivering: ”entity” översätts konsekvent med ”entitet”; den intilliggande beskrivningen förklarar att mönstren väljer entiteter vars data ska tas bort. Begreppet globmönster behålls.

## `component::recorder::services::purge::name`

**Engelska:** Purge Recorder database

**Befintlig svenska:** Rensa inspelarens databas

**Förslag:** Rensa Recorders databas

Osäkert terminologival: den närliggande åtgärden heter ”Rensa entiteter från Recorder” och beskrivningarna använder Recorder som namn. Samtidigt finns [tidigare Recorder-rubriker som använder ”inspelaren”](sparade-andringar-recorder.md). Avgör först om integrationsnamnet eller den översatta benämningen ska användas genomgående; ändra inte denna enskilda sträng utan den kontrollen.

## Kontroll

Svlang rapporterade inga skrivregelfel i förslagen. Hunspell markerade egennamnsformen ”Recorders”, som avser integrationsnamnet Recorder. Sökning i terminologiförrådet gav ingen verifierad globterm; terminologivalet är därför en kontextuell bedömning. Inga platshållare, pluralformer eller nyckelreferenser förekommer i dessa två texter.
