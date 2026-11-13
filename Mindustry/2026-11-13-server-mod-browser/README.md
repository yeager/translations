# Mindustry, server- och modbläddrargränssnitt, 13 november 2026

Den här batchen omfattar 13 svenska UI-texter i
`core/assets/bundles/bundle_sv.properties`: säkerhetsdialoger för länkar och
urklipp, fel vid skärmdump, inläsning av ett externt översättningspaket,
skript, modbläddrarens utgåvor samt Steam Workshop.

Terminologiska beslut:

- `release` är **utgåva** i modbläddraren
- `bundle` är **paket**; en extern översättning **läses in**
- `script` är **skript**
- `Workshop` behålls som Steam Workshops synliga produktnamn

Kontroller:

- nycklar, platshållare och färgmarkörer jämförda med `bundle.properties`
- l10n-lint: godkänd
- Hunspell-sv: enbart befintliga tekniska markeringsord återstår
- svlang: hela den äldre resursen ger många befintliga V2- och anglicismträffar;
  batchens formuleringar har granskats manuellt
- diffkontroll och Gitleaks för deltat: godkända
- Gradle kunde inte köras i miljön eftersom Java-runtime saknas

Upstream: [Mindustry PR #12833](https://github.com/Anuken/Mindustry/pull/12833),
öppen den 13 november 2026. Den är inskickad men ännu inte granskad eller
mergad.
