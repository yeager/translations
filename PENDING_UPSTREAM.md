# Väntande upstream-importer

Följande arbete är ännu inte fullt verifierat eller inskickat:

- **sK1:** Det svenska utkastet är inte inskickat. Bekräfta att senaste utgåvan uppfyller 48-månaderskravet innan arbetet fortsätter. Se [sK1-status](sK1/STATUS.md).
- **DuckStation:** Ett verifierat delta med 14 rättningar finns i `DuckStation/duckstation-qt_sv-lint-fixes-20261027.delta.ts`. Samtliga källnycklar finns i aktuell upstreamkatalog, men filen är inte inskickad. Se [granskningen](DuckStation/LINT-REVIEW-20261027.md).
- **GnuCash:** Ett granskat delta med 59 rättningar finns i `GnuCash/gnucash-program-sv-reviewed-delta-20261027.po`. Fem av 64 avvikelser är utelämnade; tre gäller den dokumenterade termkonflikten för `split`. Se [upstreamjämförelsen](GnuCash/UPSTREAM-DIFF-20261027.md) och [termgranskningen](GnuCash/SPLIT-TERM-REVIEW-20261027.md).
- **FreeCAD:** Fyra tidigare saknade strängar (194951, 176822, 177244 och 2593990) är dolda från översättning och kräver ingen uppladdning. De senare granskningsfilerna laddades upp, men Crowdin hoppade över merparten och API-kontrollen visar att förslag i huvudsak inte är valda eller godkända. Återstår gör de fyra CAM-rättningarna för termen `matris`, som är kontrollerade men ännu inte sparade i Crowdin. Se [status och filer](FreeCAD/review-20261026/STATUS.md).
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
