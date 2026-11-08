# Blender UI – USD-tillgångar och skelett

## Omfattning

70 tidigare ospårade strängar med källhänvisning under
`source/blender/io/usd/` har lästs i sin importer-/exportörskontext mot
exportalternativ och diagnostik för USD. Granskningen omfattar bland annat
tillgångssökvägar, samlingar, prims, instanser, material, UV-attribut,
skelett, leder, morfmål, kurvor och VDB-filer.

## Korrigeringar

- `package-relative file name` → `paketrelativt filnamn`.
- `Xform ancestor` → `Xform-förfader`; `root primitive` → `rotprimitiv`.
- `Curve width size` → `Kurvbreddens storlek`.

De övriga 67 kontrollerade strängarna är korrekta i sin tekniska kontext och
lämnas oförändrade. Termerna `USD`, `prim`, `Xform`, `SkelRoot`, `VDB` och
`big-endian` är avsiktliga format- eller API-namn. `armatur`, `skelett`,
`led`, `formnyckel`, `morfmål`, `samling`, `uttag` och `resurs` används
konsekvent med den etablerade Blender-terminologin.

## Kontroller

- `msgfmt --check`: godkänd; endast normala varningar om frivilliga
  rubrikfält i den minimala deltafilen.
- `l10n-lint`: 0 fel och 0 varningar; två irrelevanta informationsnotiser om
  valutaformat.
- `svlang consistency`, `svlang skrivregler`, `svlang svengelska`:
  godkända.
- `hunspell-sv`: godkänd för svensk löptext.
- Gitleaks och `git diff --check`: godkända.
