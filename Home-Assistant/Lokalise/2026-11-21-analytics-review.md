# Home Assistant – Analytics: svensk radgranskning

Datum: 2026-11-21  
Projekt: Home Assistant Core i Lokalise  
Komponent: `analytics`

## Underlag och kontroll

Samtliga fem strängar jämfördes med aktuell `homeassistant/components/analytics/strings.json` och Lokalise API. Den längre Markdown-texten kontrollerades med `svlang` och `hunspell-sv`; träffarna avser produktnamn och URL-delar. Båda länkmålen jämfördes programmatiskt mot engelskan före sparandet.

## Radvis resultat

| Fullständig nyckel | Engelska | Befintlig svenska | Resultat |
| --- | --- | --- | --- |
| `component::analytics::exceptions::supervisor_not_ready::message` | Supervisor was not ready during setup, will retry | Supervisor var inte redo under installationen, kommer att försöka igen | Behåll. |
| `component::analytics::preview_features::snapshots::description` | Information om Open Home Foundation Device Database | Längre svensk beskrivning | Sparad med full täckning av “free, open source community-powered resource”, idiomatisk term **smarta hemenheter**, samt bevarade Markdown-länkar. |
| `component::analytics::preview_features::snapshots::disable_confirmation` | Your data will no longer be shared … | Dina data kommer inte längre att delas … | Behåll. |
| `component::analytics::preview_features::snapshots::enable_confirmation` | This feature is still in development … | Denna funktion är fortfarande under utveckling … | Behåll. |
| `component::analytics::preview_features::snapshots::name` | Device database | Enhetsdatabas | Behåll. |

## Verifiering

Den ändrade beskrivningen skickades till Lokalise och lästes tillbaka via API. De två engelska länkmålen finns oförändrade i den sparade svenska texten.