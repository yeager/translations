# Scene Manager: redigering 06 — granskningsprotokoll

## Omfattning

16 källsträngar: borttagning, osparade sceninställningar, åsidosättningar och förhandsgranskning.

## Terminologi

- `scene` är **scen** och `Scene Manager` är **scenhanteraren**.
- `overwrite` är **åsidosättning**; funktionsinställningar och användarinställningar hålls isär.
- `preview` är **förhandsgranskning**.
- `weather/time` skrivs ut som **väder och tid** för ett naturligt gränssnittsspråk.

## Bevarade format

`{feature}` och `{target}` är oförändrade. Inga källradbrytningar eller printf-markörer förekommer.

## Kontrollkedja

JSON, `l10n-lint`, `svlang`, Hunspell, Gitleaks samt markör- och radbrytningsjämförelse körs mot batchfilen.
