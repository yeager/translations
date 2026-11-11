# QGIS: tilläggshanterarens hjälptexter 090

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar de kontextbundna hjälptexterna för flikarna i
tilläggshanteraren. Samtliga HTML-taggar, textformatering, färgmarkering,
ellips och synliga knappnamn bevaras.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| HTML-hjälpen `All Plugins` | Engelsknära text med inkonsekvent `plugin`, saknade instruktioner och felaktig flikreferens | `<h3>Alla tillägg</h3><p>Till vänster visas alla tillägg som är tillgängliga för QGIS, både installerade och sådana som kan hämtas. Vissa tillägg ingår i QGIS-installationen, medan de flesta tillhandahålls via tilläggscentralkatalogerna.</p><p>Du kan tillfälligt aktivera eller inaktivera ett tillägg. Du aktiverar eller inaktiverar det genom att kryssa i kryssrutan eller dubbelklicka på namnet…</p><p>Tillägg som visas i <span style='color:red'>rött</span> läses inte in på grund av ett fel. De finns också på fliken 'Ogiltiga'. Klicka på tilläggets namn för mer information eller för att installera om eller avinstallera tillägget.</p>` |
| HTML-hjälpen `Installed Plugins` | Delvis korrekt, men inkonsekvent ordföljd och anglicismen `plugin` | `<h3>Installerade tillägg</h3><p>Här visas endast tillägg <b>som är installerade i QGIS</b>.</p><p>Klicka på namnet för mer information.</p><p>Klicka i kryssrutan eller dubbelklicka på namnet för att <i>aktivera</i> eller <i>inaktivera</i> tillägget.</p><p>Du kan ändra sorteringen via snabbmenyn (högerklicka).</p>` |
| HTML-hjälpen `Not installed plugins` | Inkonsekvent term och tung instruktionstext | `<h3>Icke installerade tillägg</h3><p>Här visas alla tillägg som finns i centralkatalogerna men <b>inte har installerats ännu</b>.</p><p>Klicka på namnet för mer information.</p><p>Du kan ändra sorteringen via snabbmenyn (högerklicka).</p><p>Du kan hämta och installera ett tillägg genom att klicka på namnet och sedan på knappen 'Installera tillägg'.</p>` |
| HTML-hjälpen `New plugins` | `Nya plugin` | `<h3>Nya tillägg</h3><p>Här visas helt <b>nya</b> tillägg som kan installeras.</p>` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
