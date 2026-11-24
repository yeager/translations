# SmartyPlants: webhook-hemlighet vid omkonfigurering

| Fullständig nyckel | Befintlig svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| `component::smartyplants::config::step::reconfigure_secret::data_description::webhook_secret` | `Signeringshemligheten från SmartyPlants-appen. Lämna den tom för att endast använda avfrågning.` | `Signeringshemligheten som SmartyPlants-appen visar när du har lagt till webhook-URL:en. Den används för att verifiera att skickade uppdateringar verkligen kommer från SmartyPlants.` | Den nuvarande Core-källan och config flow visar hur hemligheten skapas och verifierar webhook-uppdateringar. Den kortare tidigare texten nämnde endast avfrågning och utelämnade syftet med signeringshemligheten. Lokalise-värdet sparades och lästes tillbaka 2026-11-24. |
