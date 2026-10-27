# Scene Manager: platser och målinställningar 08 — granskningsprotokoll

## Omfattning

16 källsträngar: funktioner, platsval, celler, regioner och prioritering.

## Terminologi

- `interior` och `exterior` är **interiör** respektive **utomhus**.
- `location` är **plats**, `location type` är **platstyp** och `target` är **mål**.
- `worldspace` är **världsutrymme** och `cell` är **cell** i spelmotorns betydelse.
- `override` är **åsidosättning** och `precedence` är **prioritet**.
- De etablerade förkortningarna skrivs **COC-kod** och **SPID-nyckel**.

## Bevarade format

`{0}` och `{1}` är oförändrade. Inga källradbrytningar eller printf-markörer förekommer.

## Kontrollkedja

JSON, `l10n-lint`, `svlang`, Hunspell, Gitleaks samt markör- och radbrytningsjämförelse körs mot batchfilen.
