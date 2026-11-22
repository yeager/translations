# Roborock och Teleinfo: lågtrafik

Elva aktuella Lokalise-rader rättades den 22 november 2026. Kvarlämnat
`off-peak`/`off peak` standardiserades till Home Assistants svenska tariffterm
`lågtrafik`.

| Komponent | Rättade rader | Sparad terminologi |
| --- | ---: | --- |
| Roborock | 3 | Laddning under lågtrafik; start- och sluttid för laddning under lågtrafik |
| Teleinfo | 8 | Lågtrafik; lågtrafikindex; lågtrafik under blå, röd och vit dag |

Samtliga elva ändringar sparades via Lokalise API och lästes tillbaka
ordagrant. De finns i validerad HA-TMX (`valid: 3348 entries`,
`swedish-tm`-commit `0490adb`).
