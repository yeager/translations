# Blender UI — konsekvent term för keyframe

Datum: 2026-11-09  
Katalog: `blender-ui-ui-sv (6).po`  
SHA-256: `7cbf644d990d1d648e91fa42b6ed214545661fc4e2db2dba461f49dbfd3a408f`

## Omfattning

93 poster i animeringsredigerarna granskades rad för rad. De omfattar
operatorer, etiketter och hjälptexter i Action Editor, Graph Editor, Dope
Sheet, sequencern och Grease Pencil. Källtexten använder både *keyframe* och
den kortare formen *key* för samma animeringspunkt.

## Beslut

I samtliga granskade poster betyder den svenska formen *nyckelruta* Blenders
tekniska keyframe. Den etablerade och entydiga UI-termen är
**nyckelbildruta**. Former som *nyckelbildrutor*,
*nyckelbildrutors handtag* och *tidsförskjutningsnyckelbildrutor* följer
svenska böjnings- och sammansättningsregler.

Ändringen avgränsas till animeringsdata. Den normaliserar inte orelaterade
förekomster av ordet *nyckel*, exempelvis tangentbordstangenter eller
åtkomstnycklar.

## Kontroll

Deltafilen har 93 poster, inga fuzzy-markeringar och inga återstående
förekomster av den äldre formen i sina måltexter. `msgfmt`, l10n-lint,
svlang, konsistenskontroll och Gitleaks passerade. Hunspell-sv:s träffar
består av tekniska sammansättningar, metadata och källidentifierare.

Detta dokumenterar lokal granskning och importberedskap. Det bekräftar inte
att filen har importerats i Blender Translate.
