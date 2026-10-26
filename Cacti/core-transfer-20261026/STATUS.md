# Jämförelse mellan core 1.2 och core

2026-10-26. En tidigare och en senare export av core 1.2 jämfördes med en export av core efter radgranskningen. Av 1 754 ändrade poster från core 1.2 hade 94 en annan översättning i core. Jämförelsen finns i comparison.tsv. Matchning avser kontext, källtext och pluralform; äldre exporter kan innehålla poster som inte längre används i Weblate.

Ett försök att överföra elva utvalda poster med rejected-upload.po gav 0 uppdaterade och 11 saknade i Weblate. Dessa elva saknas även i den lokala källmallen från cacti-core-current-source, commit febd2af. PO-filen är ett underlag för felsökning och ska inte skickas upp igen utan kontroll. 36 av de 94 posterna finns i den lokala källmallen; deras olika formuleringar behöver bedömas mot den aktuella versionen i Weblate. Ingen av de elva försökte importera har verifierats uppdaterad.

## Kontroll mot Weblates export

Jämförelse med Weblates CSV-export för core från 2026-10-26 (5 198 aktiva strängar) identifierade 1 754 ändrade poster mellan de två core 1.2-exporterna. Av dessa matchade 1 498 en aktiv post i core med samma källtext och kontext; 1 462 hade redan samma svenska text och 36 hade en annan text. Återstående 256 saknade aktiv matchning i core-exporten. CSV-exporten kan ha förändrats sedan hämtningen.

De 36 olika formuleringarna har jämförts manuellt. Den nyss radgranskade core-texten behålls: skillnaderna är alternativa formuleringar eller skulle återinföra exempelvis sämre terminologi, felaktig interpunktion, engelsk text eller mindre fullständig information. Ingen av de 36 har därför skrivits över. Detta avslutar jämförelsen mot de nämnda exporterade versionerna, men innebär inte att hela core 1.2-filen har skickats upp till core.
