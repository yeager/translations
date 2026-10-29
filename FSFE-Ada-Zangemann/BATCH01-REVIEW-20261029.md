# Ada & Zangemann, svenska — häfte 1

Den 29 oktober 2026 hämtades den aktuella svenska PO-katalogen från Hosted
Weblate. Komponenten omfattar 299 strängar, varav 112 var oöversatta.

Häfte 1 innehåller 31 sammanhängande berättelsesträngar från bokens inledning
och Zangemanns första uppfinningar. Den är avsiktligt en ren deltakatolog:
tidigare svenska måltexter ingår inte och kan därför inte skrivas över vid
uppladdning.

Kontroller:

- `msgfmt --check` passerar.
- `l10n-lint` rapporterar inga fel. Fyra kommateckensvarningar avser engelska
  källtexter med Oxfordkomma, inte svenska måltexter.
- `svlang skrivregler` passerar på den nya berättelsetexten.
- `gitleaks` finner inga hemligheter.
- XML/DocBook-markup saknas i häftets nya poster, så ingen tagg- eller
  radbrytningsparitet påverkas.

Projektets egna riktlinjer är lästa: Ada, Zangemann och Alan behåller sina
namn, och texten skrivs för att fungera vid högläsning för barn.

Häftet importerades i Hosted Weblate den 29 oktober: 31 av 31 strängar
uppdaterades, inga hoppades över och inga saknades. Uppladdningsläget var
"översättning som behöver redigeras" och konflikthanteringen begränsades till
tidigare oöversatta strängar. Weblate visar därefter 81 oöversatta strängar.

Återstående arbete: 81 oöversatta strängar, huvudsakligen fortsatt
berättartext samt kolofon och tacktext.
