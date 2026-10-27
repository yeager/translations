# Våteffekter: grunder 01 — granskningsprotokoll

## Omfattning

16 källsträngar: förinställning, regnanalys, droppar, karaktärseffekter och felsökningsvyer.

## Terminologi

- `Wetness Effects` är **våteffekter**; `water shading` är **vattenskuggning**.
- `ripples` är **krusningar**, `rivulets` är **rännilar** och `coverage` är **täckning**.
- `Dynamic Cubemaps` återges som **dynamiska kubkartor**.
- `highlight` är **högdager**, inte det engelska låneordet.

## Bevarade format

`%s` i förinställningen är oförändrad. Inga källradbrytningar förekommer.

## Kontrollkedja

JSON, `l10n-lint`, `svlang`, Hunspell, Gitleaks samt markör- och radbrytningsjämförelse körs mot batchfilen.
