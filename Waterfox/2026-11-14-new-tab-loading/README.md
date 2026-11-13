# Waterfox – nya flikens inläsningstexter

Datum: 2026-11-14  
Komponent: `browser/extensions/newtab/webext-glue/locales/sv-SE/browser/newtab/newtab.ftl`  
Källversion: Waterfox `6.7.8`, publicerad 2026-11-07

## Granskning

Fyra kontextbundna status- och feltexter för nya fliken har rättats. De avser
inläsning av innehåll och bildadresser, inte uppladdning av filer.

- `Bilden misslyckades att ladda` → `Det gick inte att läsa in bilden`
- `Laddar…` → `Läser in…`
- tidsgränstexten anger nu tydligt att avsnittet nästan hann läsas in
- den allmänna feltexten använder `skulle läsas in`

## Kontroller

- Hunspell-sv: inga stavfel i ändringarna
- `svlang`: endast två felaktiga V2-varningar för korrekta bisatser
- `git diff --check`: godkänd
- Gitleaks: godkänd
- `l10n-lint`: kan inte användas som godkänd kontroll för denna Fluent-katalog;
  den feltolkar plattformsväljare och varumärkesreferenser som saknade texter

## Upstream

Commit `9d6cf923` är pushad till
[`yeager/waterfox:l10n/sv-newtab-loading-20261114`](https://github.com/yeager/waterfox/tree/l10n/sv-newtab-loading-20261114).
Skapandet av PR mot `BrowserWorks/waterfox` nekades av GitHub: kontot saknar
behörigheten `CreatePullRequest`. Ingen upstream-PR eller merge finns.
