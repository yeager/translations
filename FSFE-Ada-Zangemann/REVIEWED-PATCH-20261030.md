# Ada & Zangemann: bedömning av extern korrekturdiff

Datum: 2026-10-30

En extern diff för `docbook/po/text/sv.po` granskades rad för rad. Den ska
inte tillämpas oförändrad: den innehåller både tydliga sakrättelser och flera
terminologiska eller semantiska försämringar.

## Godkänn

- `Titel-sida` till `Titelsida`.
- `skateboard-bräda` till `skateboard`, och `på gatan` till `på trottoaren`.
- `frågade dem` till `frågade de`.
- `haka` till `smalben` för engelska `shin`, samt ljudeffekten `BAM!`.
- `högtalare är mycket högre` till `högtalare spelar mycket högre`.

## Begär ändring

- Den globala ersättningen av `programvara` med `mjukvara` ska inte tas in som
  en maskinell ändring. I synnerhet är **fri programvara** den etablerade
  svenska FSFE-termen och den ska behållas i sak- och licenstexterna.
- `polotröja` ska inte bli `skjorttröja`: en `turtle-neck sweater` är en
  polotröja.
- Titeln ska ha svensk plural och normal skiljeteckensättning: **Mjukvara,
  skateboardar och hallonglass**, utan kommatecken före `och`.
- `lät maskinen göra ett litet fisljud` är oidiomatiskt. Skriv i stället
  **gav maskinen ifrån sig ett litet fisljud**.
- `glasskopp` återger inte `fish-shaped ice cream cone`. Behåll **glasstrut**.
- `en blyerts som skriver` är fel. Bildbeskrivningen ska säga **en
  blyertspenna som skriver**.

## Slutsats

Inför de konkreta betydelse- och grammatikrättelserna, men avvisa den breda
terminologiförskjutningen och de semantiskt felaktiga bildbeskrivningarna.
Denna bedömning är ett granskningsunderlag och ändrar inte den redan
verifierade Weblate-katalogen förrän samma förslag har bedömts mot den aktuella
källsträngen där.
