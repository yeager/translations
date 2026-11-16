# Prism Launcher, svensk UI-granskning, 13 november 2026

Projektet använder Hosted Weblate och speglar översättningarna i
`PrismLauncher/Translations`. Den hämtade `sv.ts` hade tre markerade ofärdiga
men i sak tydliga poster. Deltan gör dem färdiga.

Kontroller:

- Qt `lrelease`: 2 534 färdiga, 0 ofärdiga översättningar.
- Hunspell-SV och svlang för de ändrade svenska texterna: godkända.
- l10n-lint kunde läsa katalogen men rapporterar befintliga katalogomfattande
  fel och varningar, huvudsakligen för `vanished`-poster. De är inte nya i
  den här deltan.
- Diffkontroll och Gitleaks: godkända.

Vid den förnyade kontrollen 16 november genererade Qt `lrelease` tre färdiga
och noll ofärdiga översättningar, och l10n-lint passerade för deltafilen.
Hunspell-sv och svlang markerar enbart facktermen `sökvägstraversering` som
ovanlig. Den motsvarar den engelska säkerhetstermen ”path traversal” och är
avsiktlig i den här kontexten.

Projektets etablerade kanal är
https://hosted.weblate.org/projects/prismlauncher/launcher/.

## Senast verifierade åtkomststatus

Kontrollerad 16 november 2026: Hosted Weblate-API:t var åtkomligt och den
arkiverade deltafilen skickades till komponenten `launcher` med
importmetoden `translate` och konfliktläget `ignore`. API:t svarade med
`total: 3`, `skipped: 3`, `accepted: 0` och `not_found: 0`.

Det betyder att samtliga tre poster redan var översatta upstream. Efteråt
hämtades den aktuella svenska TS-filen via API och alla tre kontexter lästes
tillbaka. Två måltexter motsvarar deltan exakt. Den tredje har redan den
naturligare formuleringen ”I Windows kan det krävas administratörsbehörighet
för att skapa symboliska länkar.” och lämnades därför medvetet orörd.

Inskicket är alltså verifierat, men skapade ingen ny upstreamändring eftersom
det inte fanns något att uppdatera.
