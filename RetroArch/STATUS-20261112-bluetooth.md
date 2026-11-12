# RetroArch, svenska, komplettering 2026-11-12

Projekt: RetroArch i Crowdin, projekt-ID `380544`
Språk: `sv-SE`
Komponent: huvudresurs, `fileId` `11735`

## Omfattning

Tre oöversatta Bluetooth-strängar i huvudresursen granskades och kompletterades. Käll- och språkresursens sträng-ID:n jämfördes direkt via Crowdins API: 4 822 källsträngar, 4 819 svenska översättningar före arbetet och 4 822 efteråt.

Batch: `retroarch-sv-batch-20261112-bluetooth.json`

## Terminologi

- Bluetooth bevaras som produkt- och tekniknamn.
- `Show` i gränssnittet: `Visa`.
- `Scan for … devices`: `Sök efter …-enheter`.

## Kontroller

- JSON-syntax och unika sträng-ID:n: godkända.
- Platshållare och markup: inga förekommer i batchen.
- `svlang skrivregler`: inga träffar.
- `hunspell-sv`: inga träffar.
- Em dash-kontroll: inga förekomster.
- `gitleaks detect --no-git --source … --redact`: inga hemligheter hittades.
- `git diff --check`: godkänd.

## Upstreamstatus

Alla tre översättningar skickades som vanliga Crowdin-förslag och returnerade HTTP 201. Texterna lästes därefter tillbaka från API:t och matchade batchfilen exakt. Huvudresursen visar nu 4 822 av 4 822 översatta strängar (100 %). Godkännandegraden är 46 %; godkännande utfördes inte automatiskt.

Versionskälla: [RetroArch v1.22.2](https://github.com/libretro/RetroArch/releases/tag/v1.22.2), publicerad 2025-11-20 och därmed yngre än 48 månader.
