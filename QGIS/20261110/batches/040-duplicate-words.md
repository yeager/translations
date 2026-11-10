# QGIS: dubbla ord 040

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`

Två oblockerade strängar granskades i sin faktiska Qt-källkontext och
rättades:

| Källa | Tidigare svenska | Svenska |
|---|---|---|
| `A numeric value representing the scale denominator` | `Ett numeriskt värde som som motsvarar en kartskala` | `Ett numeriskt värde som motsvarar en kartskala` |
| `Load from External File` | `Läs in från från extern fil` | `Läs in från extern fil` |

Kontroller: JSON-schema med `jq`, regenererad QGIS-TM med `msgfmt --check`,
`git diff --check` och Gitleaks utan fynd. Transifex bulk-PATCH svarade HTTP
200 med två uppdaterade översättningar. Direkta GET-återläsningar bekräftade
båda måltexter och `origin: API`.
