# Väntande upstream-importer

Följande arbete är ännu inte fullt verifierat eller inskickat:

- **Bitwarden:** Web (263), Browser (10) och Desktop (46) jämfördes på nytt
  mot aktuell `main`, validerades och skickades som [PR #24212](https://github.com/bitwarden/clients/pull/24212)
  2026-10-28. PR:n är öppen; dess säkerhetskontroll är grön men GitHub visar
  `BLOCKED` i väntan på underhållargranskning.
  Mobile-deltat (23) är validerat och pushat till en forkbranch, men
  `bitwarden/mobile` är arkiverat och GitHub avvisar PR:er. Authenticator
  Androids gamla repo är också arkiverat och har ersatts av `bitwarden/android`;
  43 av dess 46 deltaposter finns redan på svenska i efterföljaren och de
  tre övriga nycklarna finns inte längre, så ingen duplicerande PR behövs.
  Authenticator iOS-deltat jämfördes med aktiva `bitwarden/ios`: 52 av 60
  äldre nycklar finns kvar, åtta har utgått eller döpts om, och två verifierade
  grammatikrättningar skickades som [PR #3159](https://github.com/bitwarden/ios/pull/3159)
  2026-10-28. PR:n är öppen; dess säkerhetskontroll är grön men GitHub visar
  `BLOCKED` i väntan på underhållargranskning. Se
  [komponentstatus](Bitwarden/CURRENT-COMPONENT-STATUS-20261027.md).
- **sK1:** Det svenska utkastet är inte inskickat. Bekräfta att senaste utgåvan uppfyller 48-månaderskravet innan arbetet fortsätter. Se [sK1-status](sK1/STATUS.md).
- **FreeCAD:** Fyra tidigare saknade strängar (194951, 176822, 177244 och 2593990) är dolda från översättning och kräver ingen uppladdning. De senare granskningsfilerna laddades upp, men Crowdin hoppade över merparten och API-kontrollen visar att förslag i huvudsak inte är valda eller godkända. De fyra CAM-rättningarna för termen `matris` i `FreeCAD/review-20261026/freecad-cam-matris-20261027.xliff` försöktes importeras i Crowdin 2026-10-27; alla fyra hoppades över eftersom samma förslag redan finns. För minst strängen ”Creates an array from selected toolpaths” är den aktiva, godkända översättningen fortfarande ”Skapar en array från valda verktygsbanor”, medan ”Skapar en matris från valda verktygsbanor” redan finns som ett ogranskat förslag. Ändringen kräver därför val eller godkännande av befintliga förslag per sträng, inte en ny filuppladdning. Se [status och filer](FreeCAD/review-20261026/STATUS.md).
- **FreeCAD-addons:** Den senare 12-strängarsfilen laddades upp; API-kontrollen visar att samtliga måltexter redan finns som förslag. Kontrollera vald översättning och granskningsstatus per sträng före ny ändring. Se [status och filer](FreeCAD/review-20261026/STATUS.md).
- **Vocaluxe:** Huvudfilen, webbappen och alla sex partylägen är uppladdade i Transifex och visas som 100 % översatta, men 0 % granskade. Sex granskade huvudfilsrättningar (`Low`, `Medium`, `High`, `Tags`, `No Tags` och sökhjälpen) samt samtliga tio dialogrättningar har sparats och återlästs i Transifex 2026-10-28. Upstreamexport och programkörning återstår. Se [status](Vocaluxe/STATUS.md).
- **ShadPS4:** Två lokala, validerade rättningar för `SettingsDialog` har jämförts med de aktuella, godkända texterna och skickats som manuella Crowdin-förslag 2026-10-28. De väntar på att projektet väljer eller godkänner dem; den redan godkända svenska texten är ännu inte ersatt. Se [inställningsrättelserna](ShadPS4/inställningar-kvalitetsfix-20261027.md).
- **Cacti:** Core och Routerconfigs kontrollerades i Cacti Translate 2026-10-27. Båda komponenterna är serverlåsta eftersom Weblate inte kan pusha respektive arkiv. De lokalt kontrollerade komponentdeltana ska inte laddas upp förrän låsningen är hävd och aktuella måltexter har jämförts på nytt.
- **Open Shaders:** 4 400 unika nycklar från den aktuella källkatalogen finns i 297 syntaktiskt giltiga, lokala JSON-arkivfiler. Komponenten är låst i Hosted Weblate. Scenhanteraren är komplett med 170 av 170, våteffekter med 201 av 201, Wind med 279 av 279 och begränsning av ljuskällor med 326 av 326 nycklar; alla fyra har helkontrollerats. Se [batchstatus](Open-Shaders/BATCH-STATUS-20261027.md). Ladda inte upp förrän låsningen är hävd och komponentens aktuella export har jämförts.
- **Rust Coreutils/join:** Sex förslag finns redan i Hosted Weblate, men komponenten är låst eftersom arkivet inte kan sammanfogas. Se [status](Rust-Coreutils/STATUS-2026-10-22.md). Ingen filimport ska göras innan låsningen har hävts.
- **MATE Control Center, hjälp och Terminal:** De tre granskade kandidaterna är kvar lokalt eftersom Fedora Weblate är låst. Se [väntande uppladdningar](MATE/PENDING_UPLOADS.md). Hämta en ny export och kör kontrollkedjan på nytt efter upplåsning.

Senast kontrollerades även:

- Hosted Weblate Application: 40 granskade ändringar importerade och verifierade.
- Hosted Weblate Website: 7 granskade ändringar importerade och verifierade.
- GNU Mailman Core: den sista radbrytningsrättningen sparades i Weblate
  2026-10-27 och kontrollvarningen för posten försvann.
- GnuCash Program: 59 granskade poster importerade i Weblate 2026-10-27; 58
  var redan identiska och en uppdaterades. De fem medvetet utelämnade
  avvikelserna, däribland tre `split`-poster, kvarstår oförändrade.
- GitLab EE i Crowdin: 53 tidigare Orbit-enheter samt 35 nya
  AI-governance-, Orbit-, säkerhets- och paketpolicysträngar är importerade
  och verifierade mot Crowdins API. Huvudfilen är 34 423 av 34 423 strängar
  översatt.

Arkivet innehåller deltafilerna och de aktuella Weblate-exporterna. Nya ändringar
skapas som egna deltafiler och måste verifieras efter import innan de räknas som
insända.
