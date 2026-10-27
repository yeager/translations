# Open Shaders: Effects11-redigerarens grunder, häfte 39

Detta häfte omfattar tolv aktuella, tidigare tomma gränssnittstexter i
Effects11-redigeraren. Källtexterna har jämförts med Open Shaders `dev` vid
revision `c1b1ef1` den 27 oktober 2026 och med den svenska
Weblate-exporten från 19 oktober 2026.

Platsmarkörerna `{brand}` och `{file}` samt sektionsnamnet `[PARTICLE]`
bevaras. *Hotkey* översätts till *kortkommando* och *Discard changes* till
*Förkasta ändringar*, vilket stämmer med den svenska gränssnittsterminologin.

`open-shaders-effects11-editor-basics-sv-20261027.json` är ett delta på tolv
nycklar. Det får importeras först efter upplåsning och en ny jämförelse med
Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, `l10n-lint` och Gitleaks passerar. Källnycklarna, de två
platsmarkörerna och radbrytningen i partikelbeskrivningen matchar den
engelska katalogen. `svlang` rapporterar endast den imperativa
gränssnittstexten ”Högerklicka …” som möjlig V2-avvikelse; det är ett
falsklarm. Hunspell markerar produktnamnet `Effects11`, sektionsnamnet
`[PARTICLE]` och platsmarkören `{key}`, men inga svenska ord.
