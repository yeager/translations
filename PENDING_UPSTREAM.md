# Väntande upstream-importer

Följande arbete är ännu inte fullt verifierat eller inskickat:

- **NX2Apple:** Komplett svensk lokalisering med 616 av 616 poster är skickad
  som [PR #168](https://github.com/LNPANDY/NX2Apple/pull/168) 2026-10-28.
  Swift- och Qt-katalogerna är arkiverade tillsammans med kontrollunderlaget.
  PR:n saknar för närvarande konfigurerade CI-jobb och väntar på
  underhållargranskning. Se [status](NX2Apple/STATUS.md).

- **Bitwarden:** Web (263), Browser (10) och Desktop (46) jämfördes på nytt
  mot aktuell `main`, validerades och skickades som [PR #24212](https://github.com/bitwarden/clients/pull/24212)
  2026-10-28. PR:n stängdes samma dag utan merge; underhållaren hänvisade
  till Bitwardens Crowdin-flöde, som synkar översättningar till GitHub.
  Web-deltat importerades sedan i Crowdin 2026-10-28: 262 svenska
  översättningar lades till, en post hoppades över och inga godkändes
  automatiskt. Browser- och Desktop-deltana är arkiverade men behöver
  fortfarande jämföras med aktuella Crowdin-måltexter före import.
  Mobile-deltat (23) är validerat och pushat till en forkbranch, men
  `bitwarden/mobile` är arkiverat och GitHub avvisar PR:er. Authenticator
  Androids gamla repo är också arkiverat och har ersatts av `bitwarden/android`;
  43 av dess 46 deltaposter finns redan på svenska i efterföljaren och de
  tre övriga nycklarna finns inte längre, så ingen duplicerande PR behövs.
  Authenticator iOS-deltat jämfördes med aktiva `bitwarden/ios`: 52 av 60
  äldre nycklar finns kvar, åtta har utgått eller döpts om, och två verifierade
  grammatikrättningar skickades som [PR #3159](https://github.com/bitwarden/ios/pull/3159)
  2026-10-28. PR:n stängdes samma dag utan merge eftersom Bitwarden hanterar
  översättningar i Crowdin. En svensk granskarroll är begärd; jämför de lokala
  deltorna med aktuella Crowdin-måltexter först när rollen har bekräftats. Se
  [komponentstatus](Bitwarden/CURRENT-COMPONENT-STATUS-20261027.md).
- **sK1:** Den kompletta svenska katalogen är skickad som [PR #348](https://github.com/sk1-project/sk1-wx/pull/348) 2026-10-28. Den väntar på uppströmsgranskning och CI. Se [sK1-status](sK1/STATUS.md).
- **FreeCAD:** Fyra tidigare saknade strängar (194951, 176822, 177244 och 2593990) är dolda från översättning och kräver ingen uppladdning. De senare granskningsfilerna laddades upp, men Crowdin hoppade över merparten och API-kontrollen visar att förslag i huvudsak inte är valda eller godkända. De fyra CAM-rättningarna för termen `matris` i `FreeCAD/review-20261026/freecad-cam-matris-20261027.xliff` försöktes importeras i Crowdin 2026-10-27; alla fyra hoppades över eftersom samma förslag redan finns. För minst strängen ”Creates an array from selected toolpaths” är den aktiva, godkända översättningen fortfarande ”Skapar en array från valda verktygsbanor”, medan ”Skapar en matris från valda verktygsbanor” redan finns som ett ogranskat förslag. Ändringen kräver därför val eller godkännande av befintliga förslag per sträng, inte en ny filuppladdning. Se [status och filer](FreeCAD/review-20261026/STATUS.md).
- **FreeCAD-addons:** Den senare 12-strängarsfilen laddades upp; API-kontrollen visar att samtliga måltexter redan finns som förslag. Kontrollera vald översättning och granskningsstatus per sträng före ny ändring. Se [status och filer](FreeCAD/review-20261026/STATUS.md).
- **Vocaluxe:** Huvudfilen, webbappen och alla sex partylägen är uppladdade i Transifex och visas som 100 % översatta, men 0 % granskade. Sex granskade huvudfilsrättningar (`Low`, `Medium`, `High`, `Tags`, `No Tags` och sökhjälpen) samt samtliga tio dialogrättningar har sparats och återlästs i Transifex 2026-10-28. Upstreamexport och programkörning återstår. Se [status](Vocaluxe/STATUS.md).
- **ShadPS4:** Två lokala, validerade rättningar för `SettingsDialog` har jämförts med de aktuella, godkända texterna och skickats som manuella Crowdin-förslag 2026-10-28. De väntar på att projektet väljer eller godkänner dem; den redan godkända svenska texten är ännu inte ersatt. Se [inställningsrättelserna](ShadPS4/inställningar-kvalitetsfix-20261027.md).
- **Cacti:** Core och Routerconfigs kontrollerades i Cacti Translate 2026-10-27. Core kontrollerades på nytt 2026-10-29 och är fortfarande automatiskt låst eftersom Weblate inte kan pusha arkivet; se [livekontrollen](Cacti/cacti-core-live-lock-20261029.md). Core har nu trettio arkiverade, validerade språk-, URL- och HTML-rättningar. En trettioförsta Core-post går inte att göra `msgfmt`-giltig på svenska förrän projektet tar bort den felaktiga `php-format`-markeringen i källsträngen; se [formatspärren](Cacti/cacti-core-php-format-source-defect-20261029.md). Ladda inte upp komponentdeltan förrän låsningen är hävd och aktuella måltexter har jämförts på nytt.
- **Open Shaders:** Samtliga 5 136 aktuella nycklar från den lokala engelska
  källkatalogen finns i 337 syntaktiskt giltiga JSON-arkivfiler. Komponenten
  är fortfarande låst i Hosted Weblate eftersom arkivet inte kan
  sammanfogas. Livekontrollen 2026-10-29 visar 1 238 av 5 140 översatta
  strängar och 17 översatta med fallerande kontroller; se
  [livestatus](Open-Shaders/LIVE-LOCK-STATUS-20261029.md). Även
  efterbehandling är nu komplett med 672 nycklar i 27 häften. Se
  [batchstatus](Open-Shaders/BATCH-STATUS-20261027.md). Ladda inte upp förrän
  låsningen är hävd och komponentens aktuella export har jämförts.
- **SkyrimMT:** Svensk lokalisering med resursmekanism, 1 064 katalogposter och lokaliserade dynamiska statusrader har skickats som [PR #12](https://github.com/HorrorPills/skyrimmt/pull/12) den 2026-10-29. Full paketbyggning, `plutil`, nyckeltäckning, platsvariabelkontroll, `svlang`, Hunspell och avgränsad Gitleaks är verifierade. PR:n är öppen och mergebar, utan konfigurerade CI-jobb, och väntar på underhållargranskning. Se [status](SkyrimMT/STATUS-20261028.md).
- **Skyrim Community Shaders:** Komplett svensk katalog med 4 238 av 4 238
  nycklar skickades som [PR #3051](https://github.com/community-shaders/skyrim-community-shaders/pull/3051)
  2026-10-28. PR:en är squashad till en commit och dess aktuella
  rubrikkontroll passerar. GitHubs versionskontroll blockerar dock PR:en på
  grund av fyra versionsposter/INI-filer i baskoden, inte i den enda ändrade
  svenska JSON-filen. PR:n kräver dessutom underhållargranskning. Se
  [status](Skyrim-Community-Shaders/STATUS.md).
- **Rust Coreutils/join:** Sex förslag finns redan i Hosted Weblate, men komponenten är låst eftersom arkivet inte kan sammanfogas. Se [status](Rust-Coreutils/STATUS-2026-10-22.md). Ingen filimport ska göras innan låsningen har hävts.
- **MATE Control Center, hjälp och Terminal:** De tre granskade kandidaterna är kvar lokalt eftersom Fedora Weblate är låst. Se [väntande uppladdningar](MATE/PENDING_UPLOADS.md). Hämta en ny export och kör kontrollkedjan på nytt efter upplåsning.

Senast kontrollerades även:

- Hosted Weblate Application: 40 granskade ändringar importerade och verifierade.
- Hosted Weblate Website: 7 granskade ändringar importerade och verifierade.
- GNU Mailman Core: den sista radbrytningsrättningen sparades i Weblate
  2026-10-27 och kontrollvarningen för posten försvann.
- GnuCash Program: Den aktuella `stable`-katalogen har alla 59 granskade
  nycklar kvar, men ingen av de förbättrade svenska måltexterna. Den
  radbevarande uppdateringen skickades som
  [PR #2341](https://github.com/Gnucash/gnucash/pull/2341) 2026-10-29, men
  stängdes utan merge av underhållaren med hänvisning till projektets
  Weblate-flöde. En färsk Weblate-export jämfördes samma dag: alla 59
  granskade måltexter finns redan där och kräver ingen import. De fem
  medvetet utelämnade avvikelserna, däribland tre `split`-poster, kvarstår
  oförändrade. Se [Weblate-kontrollen](GnuCash/WEBLATE-STATUS-20261029.md).
- GitLab EE i Crowdin: 53 tidigare Orbit-enheter samt 35 nya
  AI-governance-, Orbit-, säkerhets- och paketpolicysträngar är importerade
  och verifierade mot Crowdins API. Huvudfilen är 34 423 av 34 423 strängar
  översatt.

Arkivet innehåller deltafilerna och de aktuella Weblate-exporterna. Nya ändringar
skapas som egna deltafiler och måste verifieras efter import innan de räknas som
insända.
