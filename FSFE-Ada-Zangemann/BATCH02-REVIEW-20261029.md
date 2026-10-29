# Ada & Zangemann, svenska — häfte 2

Häfte 2 innehåller 48 granskade poster: 47 tidigare oöversatta, sammanhängande
berättelsesträngar samt en rättelse av rubriken om skateboardar. Texten omfattar
Adas första möte med hårdvara, mjukvara och programmering. Den är en ren
deltakatalog och innehåller inga andra, tidigare svenska måltexter.

Kontroller:

- `msgfmt --check` passerar för hela arbetskatalogen och deltakatalogen.
- `l10n-lint` rapporterar inga fel. En kommateckensvarning avser den engelska
  källtextens Oxfordkomma, inte svensk måltext.
- `svlang skrivregler` passerar för de nya svenska måltexterna.
- `hunspell-sv` rapporterar endast egennamnet Zangemann.
- `gitleaks` finner inga hemligheter.
- `git diff --check` passerar. Häftet saknar DocBook/XML-markup och påverkar
  därför inte tagg- eller radbrytningsparitet.

Projektets egna riktlinjer är följda: Ada, Zangemann och Alan lämnas
oförändrade, teknikorden är konsekventa och berättartexten är läst med
högläsning för barn i åtanke.

Häftet importerades i Hosted Weblate den 29 oktober som "översättning som
behöver redigeras". Importen av de 47 berättelseposterna med "ändra endast
oöversatta strängar" uppdaterade 46 poster och hoppade över en post som redan
hade en svensk måltext. Den separata rubrikrättelsen importerades därefter med
"ändra översatta strängar" och uppdaterade 1 av 1 post. Därmed skrevs inga
andra befintliga svenska översättningar över.

Efter importen återstår 35 oöversatta poster i den lokalt granskade katalogen.
