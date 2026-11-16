# Home Assistant Core: LIFX Moods, Library och Archives, batch 126

Batchen omfattar alla 68 då tomma svenska strängar vars källtext börjar med
`Moods`, `Library` eller `Archives`. LIFX-kategorierna har översatts som
`Stämningar`, `Bibliotek` och `Arkiv`. De två Seafile-fälten `Library` har
samma svenska term: `Bibliotek`.

Fyra tidigare arkivvarianter har normaliserats efter kontextgranskning:
`Filmkvällsromantik`, `Tallglöd`, `Pumpaglöd` och `Lågmäld`.

## Kontroller före inskick

- JSON-struktur och kategoriprefix: godkända
- `l10n-lint`: godkänd
- `svlang`: granskat; etiketterna är inte löpande prosa och egennamn/tematitlar
  är förväntade ordlisteträffar
- `hunspell-sv`: endast egennamn och sammansatta tematitlar
- `git diff --check`: godkänd
- Gitleaks: godkänd
- `msgfmt`: ej tillämpligt; Lokalise API-batchen använder JSON

## Upstreamresultat

Alla 68 poster sparades via Lokalise API med `is_unverified: false` och
återlästes direkt med respektive översättnings-ID. En ny fullständig kontroll
av kvarvarande tomma svenska poster hittar noll källtexter som börjar med
`Moods`, `Library` eller `Archives`.
