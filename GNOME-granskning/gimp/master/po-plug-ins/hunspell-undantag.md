# Hunspell-undantag — GIMP plug-ins

`hunspell -d sv_SE` kördes på hela katalogen och på samtliga 149 nya eller
ändrade strängar. Rålistorna ligger bredvid denna notering. De många okända
orden i hela katalogen är till stor del GIMP-namn, format, protokoll,
identifierare, färgmodeller, filändelser och tekniska sammansättningar.

Rimliga undantag i de nya strängarna är `aalib`, `CALS`, `C23`, `trigrafer`,
`RGBE`, `OpenEXR`, `gegl:rgbe-load`, `gegl:rgbe-save`, `gegl:exr-save`, `JPEG XL`,
`MNG`, `MPO`, `FourCC`, `ICNS`, `LibRaw`, `FBDD`, `demosaikering`, `VNG`, `PPG`,
`AHD`, `DCB`, `DHT`, `IFD`, `ImageSourceData`, `RAW`, `PlayStation`, `Photoshop`
och `URI`. Källnamn, produktnamn och webbadresser behölls.

L10n-lint har två dokumenterade anmärkningstyper: svensk text ersätter källans
felaktiga engelska `e.g.:` med *exempelvis* utan kolon i två sidintervall; och
*filter* har samma form i svensk singular och plural, så de två översatta
pluralformerna är avsiktligt identiska. Katalogens `B&W`-accelerator har
lokaliserats till `S/&V` (V-tangenten); övriga `_`-acceleratorer i ändrade
strängar bevarar sin markerade bokstav.
