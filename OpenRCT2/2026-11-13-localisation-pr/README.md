# OpenRCT2, svenska aktuella poster i rätt översättningsarkiv, 13 november 2026

OpenRCT2:s huvudarkiv stängde de ursprungliga PR:erna och hänvisade till det
separata officiella arkivet `OpenRCT2/Localisation`, vars innehåll synkas in i
huvudprojektet varje dag. Den här posten samlar därför de två tidigare lokala
batcherna i en enda korrekt upstream-PR.

Batchen omfattar 50 svenska poster:

- paneler, statusfält, stegstyrning och besökarstatus
- sju interna formatmallar med oförändrade layoutmarkörer
- 18 färgnamn

Kontroller:

- samtliga 50 id:n och alla layoutmarkörer jämförda med den aktuella engelska
  huvudresursen
- Hunspell-sv: de återstående träffarna är avsiktliga projektnamn, markörer och
  korrekt stavade sammansättningar
- svlang: varnar enbart för markörer och korta UI-etiketter i det id-baserade formatet
- l10n-lint: stöder inte formatet
- projektets integritetskontroll körd; den rapporterar befintlig katalogdrift i
  andra språk eftersom Localisation ligger efter den kontrollerade engelska resursen
- diffkontroll och Gitleaks för deltat: godkända

Upstream: [OpenRCT2/Localisation PR #3571](https://github.com/OpenRCT2/Localisation/pull/3571),
öppen den 13 november 2026. CI körs; PR:en är varken godkänd eller mergad.
