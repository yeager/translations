# Väntande upstream-importer

Följande arbete är ännu inte fullt verifierat eller inskickat:

- **GNU Mailman Core:** Den enda kvarvarande radbrytningsrättningen i `GNU Mailman/mailman-core-sv-live-jamford-20261027.delta.po` jämfördes med den aktuella Core-katalogen och sparades i Weblate 2026-10-27. Weblates radbrytningskontroll för posten försvann efter sparning. Tre rättningar fanns redan uppströms och sju berör föråldrade källtexter.
- **sK1:** Det svenska utkastet är inte inskickat. Bekräfta att senaste utgåvan uppfyller 48-månaderskravet innan arbetet fortsätter. Se [sK1-status](sK1/STATUS.md).
- **DuckStation:** Två verifierade, små deltafiler finns: 14 rättningar i `DuckStation/duckstation-qt_sv-lint-fixes-20261027.delta.ts` och nio separata språkförbättringar i `DuckStation/duckstation-qt_sv-kvalitetsfixar-20261027.delta.ts`. Samtliga 23 kontext- och källtextnycklar finns i aktuell upstreamkatalog och skiljer fortfarande från dess svenska måltexter, men filerna är inte inskickade. Se [lintgranskningen](DuckStation/LINT-REVIEW-20261027.md) och [språkgranskningen](DuckStation/QUALITY-REVIEW-20261027.md).
- **GnuCash:** Ett granskat delta med 59 rättningar finns i `GnuCash/gnucash-program-sv-reviewed-delta-20261027.po`. Fem av 64 avvikelser är utelämnade; tre gäller den dokumenterade termkonflikten för `split`. Se [upstreamjämförelsen](GnuCash/UPSTREAM-DIFF-20261027.md) och [termgranskningen](GnuCash/SPLIT-TERM-REVIEW-20261027.md).
- **FreeCAD:** Fyra tidigare saknade strängar (194951, 176822, 177244 och 2593990) är dolda från översättning och kräver ingen uppladdning. De senare granskningsfilerna laddades upp, men Crowdin hoppade över merparten och API-kontrollen visar att förslag i huvudsak inte är valda eller godkända. De fyra CAM-rättningarna för termen `matris` i `FreeCAD/review-20261026/freecad-cam-matris-20261027.xliff` försöktes importeras i Crowdin 2026-10-27; alla fyra hoppades över eftersom samma förslag redan finns. För minst strängen ”Creates an array from selected toolpaths” är den aktiva, godkända översättningen fortfarande ”Skapar en array från valda verktygsbanor”, medan ”Skapar en matris från valda verktygsbanor” redan finns som ett ogranskat förslag. Ändringen kräver därför val eller godkännande av befintliga förslag per sträng, inte en ny filuppladdning. Se [status och filer](FreeCAD/review-20261026/STATUS.md).
- **FreeCAD-addons:** Den senare 12-strängarsfilen laddades upp; API-kontrollen visar att samtliga måltexter redan finns som förslag. Kontrollera vald översättning och granskningsstatus per sträng före ny ändring. Se [status och filer](FreeCAD/review-20261026/STATUS.md).
- **Vocaluxe:** Huvudfilen, webbappen och alla sex partylägen är uppladdade i Transifex och visas som 100 % översatta, men 0 % granskade. Upstreamexport och programkörning behöver fortfarande verifieras. Se [status](Vocaluxe/STATUS.md).

Senast kontrollerades även:

- Hosted Weblate Application: 40 granskade ändringar importerade och verifierade.
- Hosted Weblate Website: 7 granskade ändringar importerade och verifierade.
- GitLab EE i Crowdin: 53 tidigare Orbit-enheter samt 35 nya
  AI-governance-, Orbit-, säkerhets- och paketpolicysträngar är importerade
  och verifierade mot Crowdins API. Huvudfilen är 34 423 av 34 423 strängar
  översatt.

Arkivet innehåller deltafilerna och de aktuella Weblate-exporterna. Nya ändringar
skapas som egna deltafiler och måste verifieras efter import innan de räknas som
insända.
