# Väntande upstream-importer

Följande arbete är ännu inte fullt verifierat eller inskickat:

- **sK1:** Det svenska utkastet är inte inskickat. Bekräfta att senaste utgåvan uppfyller 48-månaderskravet innan arbetet fortsätter. Se [sK1-status](sK1/STATUS.md).
- **DuckStation:** De två verifierade deltafilerna med sammanlagt 23 rättningar har sammanförts med aktuell `master` och skickats som [PR #3817](https://github.com/stenzek/duckstation/pull/3817) 2026-10-27. XML, `git diff --check` och Gitleaks passerar; l10n-lint rapporterar 0 fel och åtta tidigare helkatalogsvarningar. Samtliga Windows-, Linux-, macOS-, ARM- och översättningslintjobb passerar nu. PR:n är fortfarande öppen, med `mergeStateStatus` `BLOCKED` och utan underhållargranskning. Se [lintgranskningen](DuckStation/LINT-REVIEW-20261027.md) och [språkgranskningen](DuckStation/QUALITY-REVIEW-20261027.md).
- **FreeCAD:** Fyra tidigare saknade strängar (194951, 176822, 177244 och 2593990) är dolda från översättning och kräver ingen uppladdning. De senare granskningsfilerna laddades upp, men Crowdin hoppade över merparten och API-kontrollen visar att förslag i huvudsak inte är valda eller godkända. De fyra CAM-rättningarna för termen `matris` i `FreeCAD/review-20261026/freecad-cam-matris-20261027.xliff` försöktes importeras i Crowdin 2026-10-27; alla fyra hoppades över eftersom samma förslag redan finns. För minst strängen ”Creates an array from selected toolpaths” är den aktiva, godkända översättningen fortfarande ”Skapar en array från valda verktygsbanor”, medan ”Skapar en matris från valda verktygsbanor” redan finns som ett ogranskat förslag. Ändringen kräver därför val eller godkännande av befintliga förslag per sträng, inte en ny filuppladdning. Se [status och filer](FreeCAD/review-20261026/STATUS.md).
- **FreeCAD-addons:** Den senare 12-strängarsfilen laddades upp; API-kontrollen visar att samtliga måltexter redan finns som förslag. Kontrollera vald översättning och granskningsstatus per sträng före ny ändring. Se [status och filer](FreeCAD/review-20261026/STATUS.md).
- **Vocaluxe:** Huvudfilen, webbappen och alla sex partylägen är uppladdade i Transifex och visas som 100 % översatta, men 0 % granskade. Sjutton ytterligare granskade huvudfilsrättningar finns i två små deltafiler och är ännu inte sparade i Transifex. Upstreamexport och programkörning behöver fortfarande verifieras. Se [status](Vocaluxe/STATUS.md).
- **ShadPS4:** Två lokala, validerade rättningar för `SettingsDialog` har jämförts med de aktuella, godkända texterna i Crowdin. De måste lämnas som manuella förslag i editorn; de kan inte importeras som en separat fil i projektets vanliga arbetsflöde. Se [inställningsrättelserna](ShadPS4/inställningar-kvalitetsfix-20261027.md).
- **Cacti:** Core och Routerconfigs kontrollerades i Cacti Translate 2026-10-27. Båda komponenterna är serverlåsta eftersom Weblate inte kan pusha respektive arkiv. De lokalt kontrollerade komponentdeltana ska inte laddas upp förrän låsningen är hävd och aktuella måltexter har jämförts på nytt.
- **Open Shaders:** 67 komponentvisa deltafiler med 854 unika nycklar är lokalt kontrollerade, men komponenten är låst i Hosted Weblate. Se [batchstatus](Open-Shaders/BATCH-STATUS-20261027.md). Ladda inte upp förrän låsningen är hävd och komponentens aktuella export har jämförts.
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
