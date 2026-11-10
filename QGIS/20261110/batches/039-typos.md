# QGIS: stavningsrättningar 039

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`

Tre oblockerade Transifex-strängar granskades rad för rad efter
`l10n-lint`-träffar och rättades:

| Källa | Svenska |
|---|---|
| `Invalid date` | `Ogiltigt datum` |
| `Invalid datetime` | `Ogiltigt datum och tid` |
| `dem,total curvature,terrain` | `dem,total krökning,terräng` |

Kontroller: JSON-schema med `jq`, regenererad QGIS-TM med `msgfmt --check`,
`git diff --check` och Gitleaks utan fynd. Transifex bulk-PATCH svarade HTTP
200 med tre uppdaterade översättningar. Direkta GET-återläsningar bekräftade
alla tre måltexter och `origin: API`.
