# QGIS: HANA-schema och CRS-fel 262

Datum: 11 november 2026
Resurs: `qgis-application`, språk `sv`
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`

Batchen granskar SAP HANA-datakällans feltexter. Produktnamnet `SAP HANA`
bevaras. `CRS` återges som `koordinatreferenssystem` i löpande svensk text;
identifikatorn skrivs som `ID`.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Unable to create a new unit of measure. Unit of measure with name '%1' and different type already exist.` | `Kan inte skapa en ny måttenhet. Måttenhet med namnet '%1' och annan typ finns redan.` | `Det gick inte att skapa en ny måttenhet. Det finns redan en måttenhet med namnet '%1', men av en annan typ.` |
| `Unable to retrieve the authority identifier for an CRS with id = %1.` | `Kunde inte hämta auktoritetsidentifierare för koordinatsystemet med id = %1` | `Det gick inte att hämta auktoritetsidentifieraren för ett koordinatreferenssystem med ID %1.` |
| `Schema name cannot be empty` | `Schemanamn kan inte vara tomt` | `Schemanamnet får inte vara tomt.` |
| `Geometry type '%1' is not supported` | `Geometrityp '%1' stöds ej` | `Geometritypen '%1' stöds inte.` |
| `Creation of fields failed` | `Skapandet av fält misslyckades` | `Det gick inte att skapa fälten.` |

Ingen extern ändring har gjorts. De rekommenderade texterna är lokala
kandidater tills de har jämförts mot aktuella Transifex-enheter vid en senare
uppladdning. Ändringarna är lokalt granskade och inte skickade externt.
