# Blender Manual: sammanställd batchkontroll

## Uppdatering 5 november 2026

Den här kontrollen har senare utökats från de ursprungliga 32 batcherna till
batcherna 01–69. Den samlade deltan
`upload-candidates/2026-11-04/blender-manual-sv-reviewed-all.po` innehåller
868 granskade översatta meddelanden och passerar `msgfmt --check`.

Filen importerades den 5 november 2026 till den generiska
Manual-komponenten i Blender Translate, i läget *Lägg till som översättning*.
Importhistoriken visar 868 bearbetade meddelanden: 856 uppdaterade, 11
hoppade över och 1 som inte hittades. En andra, likadan import uppdaterade 0
meddelanden och hoppade över 867; det bekräftar den första importen och
kvarvarande saknad nyckel. Nästa steg är att hämta en ny export och isolera
den saknade nyckeln. Avsnitten nedan beskriver den historiska kontrollen av
den tidigare delmängden på 350 meddelanden.

## Historisk kontroll 4 november 2026

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

## Historisk uppladdningsstatus

Vid den ursprungliga kontrollen hade ingen sammanslagen fil laddats upp. Den
statusen ersattes den 5 november av den verifierade importen som beskrivs
ovan. Råexporter ska fortsatt vara oförändrade.
