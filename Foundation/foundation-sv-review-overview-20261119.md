# Foundation – svensk granskningsöversikt 2026-11-19

Denna översikt knyter ihop den API-baserade granskningsomgången för Foundation på Crowdin.

## Täckning

En full API-inventering av svenska poster med tom översättning gav följande täckning:

- `general.json` (11), `buildings.json` (1), `agents.json` (1), `rules.json` (1), `dlc_agriculture_achievements.json` (1) och `compendium.json` (1): granskade i respektive arkiverade batch.
- `steam_page.json` (41): komplett granskat i Steam-batcherna.
- `dlc_agriculture_general.json` (15): granskat i skördefestivalbatchen.
- `ks_church.json` (11 aktuellt tomma, samt rubriken): granskat i grundarkyrkobatchen.
- `ks_content.json` (52): komplett granskat i fyra drak-/stödjarbatcher.
- `general.release.json` (1): granskat i den separata utgåvesträngsrapporten.

Tidigare explicit godkända ändringar i `menu.json` skickades till Crowdin. Övriga förslag i denna omgång är medvetet endast utkast.

## Kvalitet

- Alla nya utkast har kontrollerats med `l10n-lint --language sv` och `hunspell -d sv_SE`.
- Platshållare, BBCode, HTML-entiteter, listmarkörer, radbrytningar och tal har verifierats per batch.
- Terminologi följer [TERMINOLOGY.md](TERMINOLOGY.md), bland annat *village* → *by* och *founder* → *grundare*.
- Projektets Crowdin-TM var åtkomligt och användes som referens under granskningen; ingen lokal, separat körbar `swedish-tm` fanns installerad.

Se de enskilda rapporterna i samma katalog för full redovisning med källsträng, tom nuvarande svensk text, förslag och eventuella kontrollanmärkningar.
