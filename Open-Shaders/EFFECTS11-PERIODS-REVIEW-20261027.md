# Open Shaders: Effects11-perioder, häfte 52

Detta häfte omfattar tolv aktuella, tidigare tomma parametertexter,
tidsperioder och en förinställningsstatus för Effects11. Källtexterna har
jämförts med Open Shaders `dev` vid revision `c1b1ef1` den 27 oktober 2026
och med den svenska Weblate-exporten från 19 oktober 2026.

*Weather-separated* uttrycks som *separat per väder*. Tidsperioderna får
fullständiga svenska benämningar, där *Interior Day* och *Interior Night*
blir *Dagtid inomhus* och *Nattetid inomhus*. `shader` behålls som en
etablerad teknisk term.

`open-shaders-effects11-periods-sv-20261027.json` är ett delta på tolv
nycklar. Det får importeras först efter upplåsning och en ny jämförelse med
Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, `l10n-lint` och Gitleaks passerar. Samtliga källnycklar och
radbrytningen matchar den engelska katalogen. `svlang` ger 8,8 av 10 och
rapporterar den normala huvudsatsen efter etiketten ”Separat per väder” som en
falsk V2-varning. Hunspell markerar endast sammansättningar med tekniktermen
`shader`.
