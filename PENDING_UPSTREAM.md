# Väntande upstream-importer

Följande arbete är ännu inte fullt verifierat eller inskickat:

- **Bitwarden:** Web (263), Browser (10) och Desktop (46) jämfördes på nytt
  mot aktuell `main`, validerades och skickades som [PR #24212](https://github.com/bitwarden/clients/pull/24212)
  2026-10-28. PR:n stängdes samma dag utan merge; underhållaren hänvisade
  till Bitwardens Crowdin-flöde, som synkar översättningar till GitHub.
  Web-deltat importerades sedan i Crowdin 2026-10-28: 262 svenska
  översättningar lades till, en post hoppades över och inga godkändes
  automatiskt. Den 29 oktober jämfördes ytterligare 37 äldre Web-förslag rad
  för rad med Crowdins aktuella måltexter. Sjutton kvarvarande rättningar och
  60 då oöversatta grupp-, åtkomst- och PAM-strängar är nu uppdelade i fem
  kvalitetssäkrade, separata XLIFF-deltan:
  [livegranskning](Bitwarden/Bitwarden-Web-live-reviewed-delta-20261029.xliff),
  [grupper och åtkomst](Bitwarden/Bitwarden-Web-groups-access-delta-20261029.xliff),
  [PAM](Bitwarden/Bitwarden-Web-pam-access-delta-20261029.xliff) och
  [PAM-dialog](Bitwarden/Bitwarden-Web-pam-request-dialog-delta-20261029.xliff)
  samt [PAM-återkoppling](Bitwarden/Bitwarden-Web-pam-request-feedback-delta-20261029.xliff).

  De två nya PAM-häftena med 156 förslag för åtkomstanslutningar och
  målsystem granskades mot huvudgrenen den 30 oktober. 137 matchande
  översättningar skickades därefter direkt i Crowdins redigerare; övriga
  kandidater hade redan en översättning. Web-filens filter för oöversatta
  strängar visade därefter 0 strängar. Se
  [status och kontroller](Bitwarden/Crowdin-pending-20261030-web-pam-batch38.md)
  och [inskicksloggen](Bitwarden/Crowdin-submission-20261030-web-pam-editor.md).
  Samtliga fem importerades i Crowdin den 29 oktober. API:t importerade 75 måltexter;
  två dubblettkontroller hoppades över eftersom samma måltext redan fanns, och en ny
  Crowdin-export bekräftar alla 77 arkiverade måltexter. Se
  [inskicksloggen](Bitwarden/Crowdin-submission-20261029-web-live-deltas.md).
  Browser- och Desktop-deltana jämfördes senare med Crowdins aktuella
  måltexter och importerades i små batcher den 29 oktober. API-återläsning
  bekräftar 2 343 av 2 343 svenska Browser-strängar och 2 178 av 2 178
  svenska Desktop-strängar; de är vanliga förslag som väntar på Crowdin-
  granskning, inte automatiskt godkända texter. Se
  [Browser- och Desktop-loggen](Bitwarden/Crowdin-submission-20261029-browser-desktop-api-batch37.md).
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
- **sK1:** Den kompletta svenska katalogen är skickad som [PR #348](https://github.com/sk1-project/sk1-wx/pull/348) 2026-10-28. Den har status `CLEAN`, inga konfigurerade CI-jobb och väntar på uppströmsgranskning. Se [sK1-status](sK1/STATUS.md).
- **FreeCAD:** Fyra tidigare saknade strängar (194951, 176822, 177244 och 2593990) är dolda från översättning och kräver ingen uppladdning. De senare granskningsfilerna laddades upp, men Crowdin hoppade över merparten och API-kontrollen visar att förslag i huvudsak inte är valda eller godkända. De fyra CAM-rättningarna för termen `matris` i `FreeCAD/review-20261026/freecad-cam-matris-20261027.xliff` försöktes importeras i Crowdin 2026-10-27; alla fyra hoppades över eftersom samma förslag redan finns. I Crowdin-redigeraren 2026-10-29 bekräftades för ”Creates an array from selected toolpaths” att den aktiva, godkända översättningen fortfarande är ”Skapar en array från valda verktygsbanor”, medan ”Skapar en matris från valda verktygsbanor” redan finns som ett ogranskat förslag med 0 poäng. Ändringen kräver därför val eller godkännande av befintliga förslag per sträng, inte en ny filuppladdning. Se [status och filer](FreeCAD/review-20261026/STATUS.md).
- **FreeCAD-addons:** Den senare 12-strängarsfilen laddades upp; API-kontrollen visar att samtliga måltexter redan finns som förslag. Kontrollera vald översättning och granskningsstatus per sträng före ny ändring. Se [status och filer](FreeCAD/review-20261026/STATUS.md).
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
- **Rust Coreutils/join:** Sex förslag finns redan i Hosted Weblate, men komponenten är låst eftersom arkivet inte kan sammanfogas. Se [status](Rust-Coreutils/STATUS-2026-10-22.md). Ingen filimport ska göras innan låsningen har hävts.
- **MATE Control Center, hjälp och Terminal:** De tre granskade kandidaterna är kvar lokalt eftersom Fedora Weblate är låst. De omvaliderades 2026-10-29 med `msgfmt` och l10n-lint; se [omkontrollen](MATE/REVALIDATION-20261029.md) och [väntande uppladdningar](MATE/PENDING_UPLOADS.md). Hämta en ny export och kör kontrollkedjan på nytt efter upplåsning.
- **Nextcloud:** Server `v33.0.10` från 2026-10-15 är aktuell. Core har en
  tvåformsplural för kontroll av signaturer som passerar skrivregel-,
  l10n-lint-, Hunspell-, platshållar- och Gitleaks-kontroller; den är
  arkiverad i [Transifex-statusen](Nextcloud/STATUS-20261030-transifex.md).
  Den aktuella Transifex-vyn verifierar att båda formerna redan finns och att
  Core har 0 oöversatta ord; ingen ny import krävs för den posten.
  Calendar är sparad med 0 oöversatta strängar. Contacts 31-strängarsbatch är
  skickad via Transifex API och verifierad till 0 oöversatta strängar; se
  [sändningsbeviset](Nextcloud/contacts-submission-20261030.md).
  Android Notes har fått nio granskade synkroniseringsfel via API och är
  verifierad till 0 oöversatta strängar.
  Android Talk har fått 25 granskade UI-rader via API och är verifierad till
  0 oöversatta strängar.
  Assistant har fått 17 granskade UI-rader via API och är verifierad till
  0 oöversatta strängar.
  Analytics har 15 skickade och verifierade UI-rader; endast en omfattande
  Markdown-beskrivning är kvar och väntar enligt dokumentationsundantaget.
  Calendar är också klar: dess enda pluralpost sparades i Transifex och
  filtret visar 0 oöversatta strängar. Agora är också komplett för den
  aktuella källan: dess tionde och sista UI-batch har API-verifierats och
  filtret för oöversatta svenska poster returnerar 0. De enda kvarvarande
  Nextcloud-posterna är uttryckligen uppskjuten dokumentation i Server Info,
  Deck och Maps. Se [statusen](Nextcloud/STATUS-20261030-transifex.md).

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
