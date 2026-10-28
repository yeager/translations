# Bitwarden Web: Crowdin-importunderlag

Crowdin visade 2026-10-28 att svenska för Bitwarden Web är 95 % översatt och
18 % godkänd. Projektets språksida erbjuder XLIFF-import.

`Bitwarden-Web-sv-crowdin-upload-20261028.xliff` innehåller exakt 263 unika,
tidigare kontrollerade Web-poster från de 22 små JSON-deltana. Den äldre
sammanslagna XLIFF-filen med 1 248 poster används inte, eftersom den inte är
ett rent delta och kan innehålla redan aktuella måltexter.

Filen är XML-validerad, har 0 l10n-lint-fel och 0 Gitleaks-fynd. En
interpunktionsvarning avser en befintlig, avsiktlig formulering som lägger till
punkt i `No items in $FOLDER_NAME$`.

## Insändning

Den ursprungliga filen hade interna sträng-id:n och kunde därför inte matchas
av Crowdin. Den 2026-10-28 byggdes den därför om mot Crowdins aktuella
XLIFF-export, med samma 263 kontrollerade käll- och måltexter men med
Crowdins fil-id och numeriska trans-unit-id:n. Den inskickade filen är
`Bitwarden-Web-sv-crowdin-upload-20261028-current.xliff`.

Crowdin importerade 262 svenska översättningar, godkände inga automatiskt och
hoppade över en post. Språkstatusen ändrades från 95 % till 99 % översatt
(18 % godkänd). Den överhoppade posten saknar närmare feluppgift i Crowdins
detaljrapport och kräver ingen ytterligare uppladdning i denna omgång.
