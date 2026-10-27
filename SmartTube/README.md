# SmartTube: svensk UI-granskning 2026-10-27

SmartTube `32.68s`, publicerad 2026-10-20, uppfyller 48-månadersregeln.
Komponentens svenska Android-katalog innehåller 752 av 752 källsträngar och
inga tomma måltexter.

`strings-sv-ui-korrektur-20261027.xml` innehåller fem säkra rättelser från
den radvisa språkgranskningen: två felskrivningar, felstavade *kommentarer*,
en felaktig böjningsform och en mer begriplig översättning av *Carousel* i
förhandsvisningsinställningen.

`strings-sv-livesandningar-20261027.xml` normaliserar tretton strängar om
live-streaming till **livesändning** och ersätter den engelskpåverkade
etiketten *Feedback* med **Återkoppling**. Detta omfattar även hjälptexter om
återspolning, buffring och enheter med låg prestanda.

`strings-sv-spellista-20261027.xml` rättar en betydelseavvikelse: engelska
*Shuffle any playlist* avser en valfri spellista, inte samtliga spellistor.

`strings-sv-spel-20261027.xml` översätter kategorietiketten *Gaming* till
**Spel**. Övriga identiska måltexter i samma kontroll är produktnamn,
formatnamn eller etablerade facktermer.

`strings-sv-felmeddelanden-20261027.xml` rättar sju rader om spelarfel och
prestanda. Häftet återställer en felaktig Android-radbrytning, förtydligar
nätverksfel och använder svensk teknisk terminologi för V-Sync.

De fem deltafilerna jämfördes med aktuell `master` och omfattade fortfarande
27 avvikande måltexter. De skickades som
[PR #6371](https://github.com/yuliskov/SmartTube/pull/6371) den 27 oktober
2026. Se [insändningsunderlaget](upstream-pr-6371-20261027.md) för commit,
kontroller och kvarvarande begränsning i den lokala Gradle-miljön.
