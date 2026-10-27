# Open Shaders: Effects11-redigerarens omladdning, häfte 44

Detta häfte omfattar fem aktuella, tidigare tomma texter för att kompilera om
och läsa in Effects11-shaders på nytt. Källtexterna har jämförts med Open
Shaders `dev` vid revision `c1b1ef1` den 27 oktober 2026 och med den svenska
Weblate-exporten från 19 oktober 2026.

*Compile-time options* har förtydligats till *alternativ som styr
kompileringen*. Den etablerade svenska texten *Ladda om shaders* återanvänds.
Filändelsen `.fx` bevaras.

`open-shaders-effects11-editor-reload-sv-20261027.json` är ett delta på fem
nycklar. Det får importeras först efter upplåsning och en ny jämförelse med
Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, `l10n-lint` och Gitleaks passerar. Källnycklarna och filändelsen
`.fx` matchar den engelska katalogen. `svlang` ger 8,8 av 10 och rapporterar
endast den normala huvudsatsen ”Alternativ som styr kompileringen har ändrats”
som en falsk V2-varning. Hunspell markerar bara tekniktermer och filändelsen.
