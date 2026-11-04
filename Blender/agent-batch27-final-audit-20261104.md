# Slutgranskning: Blender Manual batch 27

Granskad fil: `blender-manual-sv-review-batch-20261104-27.po`.
Underlag: råexportens `render/materials/components/displacement.rst:7,50`
och `render/materials/legacy_textures/types/index.rst:4`, Blender UI-exporten,
`TERMINOLOGY.md` och den oberoende renderingsgranskningen.

| Post | Bedömning | Kontrollspår |
| --- | --- | --- |
| Materialets förskjutningsuppsättning | Godkänd | RST-destinationerna för `Displacement` och `Vector Displacement` matchar råexporten. `Förskjutning`, `Vektorförskjutning` och `Materialutdata` är UI-belägna former. |
| Adaptiv underindelning | Godkänd | `:ref:`-rollen och dess mål är oförändrade. `Adaptiv underindelning` ersätter den äldre, mindre precisa formen enligt UI och termlistan. |
| Äldre texturtyper | Godkänd | Återger både *Legacy* och *Types* och är idiomatisk svensk rubrikform. |

## Verktygsresultat

- `msgfmt --check`: godkänd.
- `l10n-lint`: 0 fel och 0 varningar.
- `svlang skrivregler`: inga skrivregelfel i de svenska måltexterna.
- Hunspell-resterna är förväntade RST-roller, engelska källtexter,
  filvägar och Blender-/API-identifierare; inga svenska stavfel hittades.
- `gitleaks detect --no-git --source`: inga träffar.
- `git diff --check`: inga fel för batchen.

Slutsats: alla tre poster kan ingå i den samlade, lokalt validerade
manualbatchen. De är inte uppladdade separat.
