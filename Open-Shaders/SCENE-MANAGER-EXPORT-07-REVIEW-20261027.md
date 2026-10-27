# Scene Manager: export och globala inställningar 07 — granskningsprotokoll

## Omfattning

16 källsträngar: export, globala borttagningar, åsidosättningsfiler och interiörscener.

## Terminologi

- `mod` är **modd**, i sammansättningar exempelvis **moddnamn**.
- `overwrite` är **åsidosättning** och `backing file` är **underliggande fil**.
- `Scene Manager` är **scenhanteraren** och `User Settings` är **användarinställningar**.
- `Interior` är **interiör**; `cell` förblir **cell** i spelmotorns betydelse.

## Bevarade format

`{0}` och `{1}` är oförändrade i båda förekomsterna. Inga källradbrytningar eller printf-markörer förekommer.

## Kontrollkedja

JSON, `l10n-lint`, `svlang`, Hunspell, Gitleaks samt markör- och radbrytningsjämförelse körs mot batchfilen.

`svlang` ger V2-varningar för korrekt imperativ och för UI-fragment, exempelvis
`Ange namnet på modden ...` och `Exporterar ...`. Hunspell saknar de produkt-
specifika sammansättningarna `moddnamn` och `åsidosättningsfiler`; båda är
korrekt bildade svenska ord.
