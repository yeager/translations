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

Upstream-status: **inte inskickad**. Ingen åtkomlig Hosted Weblate-API-nyckel
fanns i de kontrollerade nyckelringsposterna. Den enda funna generella
Weblate-token som kunde testas avvisades dessutom av Hosted Weblate med HTTP
401 den 13 november 2026. Projektets etablerade kanal är
https://hosted.weblate.org/projects/prismlauncher/launcher/.
