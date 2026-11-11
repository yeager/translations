# QGIS: tilläggshanterarens instruktioner 085

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar säkerhetsvarning, instruktioner för ZIP-installation,
uppdateringskontroll och ett felmeddelande om ett tillägg som inte kan
lokaliseras. HTML-strukturen, den synliga knapptexten, platshållaren `{}` och
den enda radbrytningen bevaras.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Installing a plugin from an untrusted source can harm your computer. Only continue if you received the plugin from a source you trust. Continue?` | `Installera en tillägg från en opålitlig källa kan skada din dator. Fortsätt bara om du fick pluginen från en källa du litar på. Fortsätta?` | `Att installera ett tillägg från en opålitlig källa kan skada din dator. Fortsätt bara om du har fått tillägget från en källa som du litar på. Vill du fortsätta?` |
| HTML-hjälpen för `Install plugin` från ZIP | Felaktig HTML och engelsknära svensk ordföljd | `<html><head/><body><p>Om du har fått ett ZIP-paket med ett tillägg som ska installeras väljer du filen nedan och klickar på knappen <span style=" font-style:italic;">Installera tillägg</span>.</p><p>Observera att den här funktionen inte är lämplig för de flesta användare, eftersom det är bättre att installera tillägg från en centralkatalog.</p></body></html>` |
| HTML-varningen för automatisk uppdateringskontroll | `Om denna funktionen är aktiverad kommer QGIS att informera dig var tredje dag när det finns tillgängliga uppdateringar till tillägg. Annars kommer kontrollen ske när fönstret för pluginhantering öppnas.` | `<html><head/><body><p><span style=" font-weight:600;">När den här funktionen är aktiverad informerar QGIS dig var tredje dag om en tillgänglig tilläggsuppdatering.</span> Annars hämtas centralkatalogerna när fönstret Tilläggshanterare öppnas.</p></body></html>` |
| `The plugin seems to have been installed but it's not possible to know where. The directory "{}" has not been found. Probably the plugin package contained a wrong named directory.\nPlease search the list of installed plugins. You should find the plugin there, but it's not possible to determine which of them it is and it's also not possible to inform you about available updates. Please contact the plugin author and submit this issue.` | `Detta tillägg verkar vara installerat men det är inte möjligt att veta var. Katalogen "{}" hittades inte. Förmodligen innehöll pluginpaketet en katalog med felaktigt namn.\nVänligen sök i listan med installerade tillägg. Du borde hitta pluginen där, men det är inte möjligt att avgöra vilken av dem det är och det är också inte möjligt att informera dig om tillgängliga uppdateringar. Vänligen kontakta ägaren av detta tillägg och beskriv problemet.` | `Tillägget verkar ha installerats, men det går inte att avgöra var. Katalogen "{}" hittades inte. Tilläggspaketet innehöll förmodligen en felaktigt namngiven katalog.\nSök i listan över installerade tillägg. Du bör hitta tillägget där, men det går inte att avgöra vilket tillägg det är och det går inte heller att informera om tillgängliga uppdateringar. Kontakta tilläggets upphovsperson och rapportera problemet.` |

Ingen extern ändring har gjorts. Aktuella Transifex-enhetsidentifierare måste
hämtas och måltexterna jämföras före en separat deltafil kan skapas.
