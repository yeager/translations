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
200 med den uppdaterade översättningen. En separat återläsning i den inloggade
Transifex-redigeraren bekräftade måltexten, kontexten `QgsMetadataWidgetBase`,
stränghashen `892fb3efe5dfc1e15c3a7b403fc9eb73` och att ändringen tillskrevs
`yeager`.
