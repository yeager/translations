# QGIS: M3C2-parametrar och mätfel 256

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen fortsätter granskningen av PDAL-verktyget M3C2. `M3C2`, `PDAL` och
`VPC` behålls som tekniska namn. Parametern `Comparison Point Cloud` behöver
en svensk sammansättning för att skiljas från åtgärden att jämföra lager.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `The M3C2 algorithm calculates the distance between two point clouds by considering the local orientation of the surface. It estimates surface normals at a user-defined scale and measures the average distance between clouds within a cylindrical projection along those normals.` | `M3C2 algoritmen beräknar avståndet mellan två punktmoln genom att analysera den lokala orienteringen av ytan. Den uppskattar normaler för ytor på en användardefinierad skala och mäter medeldistansen mellan moln inom en cylindrisk projektion längs dessa normaler.` | `M3C2-algoritmen beräknar avståndet mellan två punktmoln genom att ta hänsyn till ytans lokala orientering. Den uppskattar ytnormaler i användardefinierad skala och mäter medelavståndet mellan molnen inom en cylindrisk projektion längs dessa normaler.` |
| `The approach is highly robust against sensor noise and surface roughness, making it the standard for detecting change in complex natural environments. It also provides a sign (indicating whether a surface has moved in or out) and a statistically significant level of detection to distinguish real change from measurement error.` | `Tillvägagångssättet är mycket robust mot sensorbrus och ytojämnheter vilket gör den till standarden för att upptäcka förändringar i komplexa naturliga miljöer. Den ger också ett tecken (som indikerar om en yta har flyttat sig in eller ut) och en statistisk signifikant nivå för upptäckt för att skilja mellan verkliga förändringar och mätfel.` | `Metoden är mycket robust mot sensorbrus och ojämnheter i ytan, vilket gör den till standardmetod för att upptäcka förändringar i komplexa naturmiljöer. Den anger också tecknet, som visar om en yta har rört sig inåt eller utåt, och en statistiskt säkerställd detektionsnivå för att skilja verkliga förändringar från mätfel.` |
| `Radius of the sphere around each core point that defines the neighbors from which normals are calculated.` | `Radie på sfären runt varje kärnpunkt som definierar grannarna från vilka normaler beräknas.` | `Radien för sfären runt varje kärnpunkt anger vilka grannar som används för att beräkna normaler.` |
| `The half-length of the cylinder of neighbors used for calculating change.` | `Halv längden på cylindern inom vilken punkter söks för att beräkna förändring.` | `Halvlängden på cylindern med grannar som används för att beräkna förändring.` |
| `Which direction to orient the cylinder/normal vector used for comparison between the two point clouds.` | `Vilken riktning att orientera cylindern/normalvektorn som används för att jämföra de två punktmolnen.` | `Anger i vilken riktning cylindern eller normalvektorn för jämförelsen mellan de två punktmolnen ska orienteras.` |
| `Comparison Point Cloud` | `Jämfört punktmoln` | `Jämförelsepunktmoln` |
| `This algorithm requires PDAL version 2.10 or higher.` | `Denna algoritm kräver PDAL version 2.10 eller högre.` | `Denna algoritm kräver PDAL-version 2.10 eller senare.` |

Ingen extern ändring har gjorts. De rekommenderade texterna är lokala
kandidater tills de har jämförts mot aktuella Transifex-enheter vid en senare
uppladdning. Ändringarna är lokalt granskade och inte skickade externt.
