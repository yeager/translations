# QGIS: Transifex-import av fullgranskning 038

Datum: 10 november 2026  
Projekt: `qgis/QGIS`  
Resurs: `qgis-application`  
Språk: `sv`

## Underlag

- 273 lokalt granskade poster i `yeager/swedish-tm` motsvarade 268 unika
  Transifex-strängar. Fem upprepade samma Transifex-ID; deras svenska måltext
  normaliserades innan den slutliga kontrollen.
- Transifex dokumenterar högst 150 poster per bulk-PATCH. Fulla förkontroll-
  deltafiler ligger i `deltas/` och de upplåsta följddeltafilerna innehåller
  endast poster som tjänsten tillåter att ändra.
- Råexporten i `raw/` har inte ändrats.

## Resultat

| Del | Försökt | Resultat |
|---|---:|---|
| Förkontroll 001 | 150 | 41 låsta som redan granskade |
| Upplåst delta 001 | 108 unika | 108 accepterade, HTTP 200 |
| Förkontroll 002 | 119 | 26 låsta som redan granskade |
| Upplåst delta 002 | 93 | 93 accepterade, HTTP 200 |
| Normalisering av dubbletter | 4 | 4 accepterade, HTTP 200 |
| Totalt | 268 unika | 201 importerade och verifierade; 67 låsta |

`permission_denied` gällde uteslutande strängar som Transifex själv angav som
granskade. Ingen uppladdning påstås för dessa 67 strängar. De behöver låsas upp
eller ändras av en Transifex-granskare med rätt behörighet.

## Verifiering

- Varje lyckat svar innehöll samma uppsättning resursöversättnings-ID:n som
  respektive upplåsta deltafil.
- Den samlade svarsjämförelsen mot det normaliserade lokala underlaget visade
  inga avvikelser efter det avslutande fyrasträngarsdeltaet.
- Tre direkta GET-återläsningar bekräftade svensk måltext, `origin: API` och
  `reviewed: false` för en allmän QGIS-sträng, ett GRASS-fel och en
  geometri-/attributsträng.
- JSON-schemat kontrollerades med `jq`; `msgfmt --check` godkände den
  regenererade QGIS-TM-katalogen med 273 översatta meddelanden. `l10n-lint`
  rapporterade 0 fel och 10 kända varningar: två ISO-datumformat i kodtaggar,
  Qt-snabbtangenter, pluralformer och medvetna skiljeteckensskillnader mot
  engelskan. De är inga format- eller betydelsefel.
- `git diff --check`, `svlang`, Hunspell-kontroll av diskussionsunderlaget,
  TM-validering, 12 tester och Gitleaks kördes före arkivering.
