# Open Shaders: Effects11-redigerarens vädervärden, häfte 43

Detta häfte omfattar tolv aktuella, tidigare tomma texter för Effects11:s
väderberoende värden, tidsperioder och regneffekter. Källtexterna har jämförts
med Open Shaders `dev` vid revision `c1b1ef1` den 27 oktober 2026 och med den
svenska Weblate-exporten från 19 oktober 2026.

*Time of day* översätts konsekvent till *tid på dygnet*. Den tidigare
granskade översättningen *Ljusbrytning i regn* återanvänds för *Rain
Refraction*. Produktnamn, filnamn, konfigurationsnycklar och platsmarkörerna
`{period}` och `{reason}` bevaras.

`open-shaders-effects11-editor-weather-sv-20261027.json` är ett delta på tolv
nycklar. Det får importeras först efter upplåsning och en ny jämförelse med
Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, `l10n-lint` och Gitleaks passerar. Källnycklarna samt
platsmarkörerna `{period}` och `{reason}` matchar den engelska katalogen.
`svlang` ger 7,6 av 10 och två falska V2-varningar för den imperativa texten
”Välj …” och den normala meningen ”Ljusbrytning i regn är avstängd”. Hunspell
markerar bara produktnamn, filnamn, konfigurationsnycklar och platsmarkören.
