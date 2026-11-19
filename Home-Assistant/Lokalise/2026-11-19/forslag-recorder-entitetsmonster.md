# Recorder: entitetsmönster och databasnamn

> **Aktuell status:** Båda förslagen nedan sparades och återlästes i Lokalise 2026-11-19 efter användarens instruktion. Terminologin Recorder/inspelaren är fortfarande ojämn och bör ses över samlat. Tidigare formuleringar om osparade förslag avser läget före sparningen.

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

## Terminologiuppföljning

Vid kontroll i Lokalise 2026-11-19 används ”inspelaren” i flera felrubriker:

- `component::recorder::issues::database_engine_too_old::title`: ”Update {database_engine} to {min_version} or later to continue using the recorder” / ”Uppdatera {database_engine} till {min_version} eller senare för att kunna fortsätta använda inspelaren”.
- `component::recorder::issues::database_engine_not_supported_lts::title`: ”Update {database_engine} to a supported LTS version to continue using the recorder” / ”Uppdatera {database_engine} till en LTS-version som stöds för att kunna fortsätta använda inspelaren”.
- `component::recorder::issues::sqlite_too_old::title`: ”Update SQLite to {min_version} or later to continue using the recorder” / ”Uppdatera SQLite till {min_version} eller senare för att fortsätta använda inspelaren”.

Däremot använder åtgärden `component::recorder::services::purge_entities::name` ”Recorder” och `component::recorder::services::get_statistics::name` likaså. Dessa exempel visar en befintlig skillnad mellan grupperna, men räcker inte för att slå fast en generell term för hela projektet. Förslaget ”Rensa Recorders databas” förblir osäkert; befintlig text behålls tills en bredare terminologikontroll har gjorts. En sökning efter `component::recorder::title` gav ingen träff och visar därför inget integrationsnamn. Ingen Lokalise-ändring gjordes vid uppföljningen.
