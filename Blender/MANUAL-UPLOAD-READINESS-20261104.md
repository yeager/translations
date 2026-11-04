# Blender Manual: sammanställd batchkontroll

Datum: 4 november 2026
Målkomponent: **Blender Manual** (den vanliga Manual-komponenten, inte
versionsspecifika Manual 5.3)

## Underlag

De 32 separata, redan granskade deltafilerna
`blender-manual-sv-review-batch-20261104-01.po` till `-32.po` har slagits
samman endast för kontroll med `msgcat --use-first --no-location`.

Resultat:

- 350 unika översatta meddelanden.
- `msgfmt --check --statistics` passerar: **350 translated messages**.
- Var och en av de 350 `(msgctxt, msgid)`-nycklarna finns i råexporten
  `exports/2026-11-04/blender-manual-manual-sv.po`.
- Kontrollprogrammet jämförde nycklar radvis och gav **0 saknade nycklar**.

## Källformatets begränsning

Den nedladdade råexporten innehåller redan dubblettdefinitioner. Därför kan
GNU Gettexts `msgcmp` inte användas direkt mot den som helfil: felet gäller
källfilens upprepade definitioner, inte de 350 kandidaterna. Råexporten har
inte ändrats. Nyckelkontrollen ovan används i stället, tillsammans med
`msgfmt` på den sammanställda deltan.

## Uppladdningsstatus

Ingen sammanslagen fil har laddats upp i denna kontroll. 350 strängar är
validerade och arkiverade som de befintliga 32 mindre deltabatcherna, men
ligger under den önskade storleken 500–1000 strängar för Blender-uppladdning.
Fler självständigt granskade poster behövs innan en sammanslagen
uppladdningskandidat skapas. Råexporter ska fortsätta vara oförändrade.
