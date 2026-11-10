# QGIS: metadatafältet Administrative Area 041

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`

I metadatawidgetens fältetikett rättades den geografiskt för snäva
översättningen `Län`:

| Källa | Tidigare svenska | Svenska |
|---|---|---|
| `Administrative Area` | `Län` | `Administrativt område` |

`Län` är en särskild svensk administrativ indelning. QGIS-fältet är däremot
allmänt och kan avse flera administrativa nivåer. Den nya översättningen
bevarar därför datamodellens betydelse.

Kontroller: JSON-schema med `jq`, regenererad QGIS-TM med `msgfmt --check`,
`git diff --check` och Gitleaks utan fynd. Transifex bulk-PATCH svarade HTTP
200 med den uppdaterade översättningen. API-token som tidigare kunde läsa
tillbaka strängen ger nu HTTP 401; den separata återläsningen är därför inte
verifierad i denna batch.
