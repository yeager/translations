# QGIS: geometrikontroll för glapp 047

Datum: 10 november 2026  
Resurs: `qgis-application`, språk `sv`  
Källsnapshot: `raw/qgis-application-sv-transifex-live-20261110.ts`  
Källkod: `src/analysis/processing/qgsalgorithmcheckgeometrygap.cpp` och
`src/analysis/vector/geometry_checker/qgsgeometrygapcheck.cpp`

Geometrikontrollens två närliggande komponenter använder redan termen
`glapp` i algoritmnamn, parametrar och lager. I den äldre åtgärdsdialogen har
samma topologiska begrepp däremot blandats med `hål` och `mellanrum`. Det
försvårar både sökning och förståelse. Följande lokala rättningsbatch
normaliserar termen och rättar de satser där fel ämne, riktning eller grammatik
har ändrat åtgärdens innebörd.

| Källa | Befintlig svenska | Rekommenderad svenska |
|---|---|---|
| `Gap check: %1` | `Hålkontroll: %1` | `Glappkontroll: %1` |
| `Allowed gaps layer could not be resolved` | `Lagret med tillåtna mellanrum kunde inte lösas` | `Lagret med tillåtna glapp kunde inte hittas` |
| `Add gap area to neighboring polygon with longest shared edge` | `Lägg till mellanrum till angränsande polygon baserat på den längsta delade kanten.` | `Lägg till glappets yta i den angränsande polygon som har längst gemensam kant.` |
| `Add gap to allowed exceptions` | `Lägg till mellanrum till tillåtna undantag` | `Lägg till glappet bland tillåtna undantag` |
| `Add to longest shared edge` | `Lägg till längsta delade kanten.` | `Lägg till i den längsta gemensamma kanten.` |
| `Add the gap area to the neighbouring polygon with the longest shared edge.` | `Lägg till mellanrummet till den angränsande polygonen med den längsta delade kanten.` | `Lägg till glappets yta i den angränsande polygonen med längst gemensam kant.` |
| `Create a new feature from the gap area.` | `Skapa nytt objekt från ytan i mellanrummet.` | `Skapa ett nytt objekt från glappets yta.` |
| `Add to largest neighbouring area` | `Lägg till största angränsande yta` | `Lägg till i den största angränsande ytan` |
| `Add Gap to Allowed Exceptions` | `Lägg till mellanrum till tillåtna undantag` | `Lägg till glappet bland tillåtna undantag` |
| `Create a new feature from the gap geometry on the allowed exceptions layer.` | `Skapa nytt objekt från ytan i mellanrumsgeometrin på lagret för tillåtna undantag.` | `Skapa ett nytt objekt från glappets geometri i lagret med tillåtna undantag.` |
| `Gap` | `Hål` | `Glapp` |
| `Detects gaps between polygons smaller than a given area.` | `Detekterar glapp mellan polygoner mindre än en angiven area.` | `Identifierar glapp mellan polygoner som är mindre än en angiven area.` |
| `This algorithm checks the gaps between polygons. …` | `Glapp som är större än tröskelvärdet för glapp är fel. …` | `Glapp med en area som är mindre än glapptröskeln är fel. …` |
| `Fills gaps detected with the “Small gaps” algorithm …` | `Fyller glapp detekterade med algoritmen …` | `Fyller glapp som identifierats med algoritmen …` |
| `This algorithm fills the gaps based on a gap and neighbors layer …` | `Det finns 3 olika metoder för att fixa felen vilka ger olika resultat.` | `Det finns tre olika åtgärdsmetoder som ger olika resultat.` |
| `Report layer from fixing gaps` | `Rapportlager från lagar glapp` | `Rapportlager från åtgärd av glapp` |

De längre strängarnas fullständiga rekommenderade måltexter är:

```text
Denna algoritm kontrollerar glapp mellan polygoner.
Glapp med en area som är mindre än glapptröskeln är fel.

Om ett lager med tillåtna glapp anges ignoreras glapp som finns i polygoner i det lagret.
En valfri buffert kan tillämpas på de tillåtna glappen.

Utdatalagret Grannar krävs av algoritmen Laga geometrier (glapp). Det är en 1:N-relationstabell som kopplar ett glapp till de unika id:na för dess grannobjekt.
```

```text
Denna algoritm fyller glapp utifrån lagren Glapp och Grannar från algoritmen ”Små glapp” i avsnittet ”Kontrollera geometri”.

Tre olika åtgärdsmetoder finns tillgängliga och de ger olika resultat.
```

Vid en framtida uppladdning måste de överföras som hela strängar, med
oförändrade radbrytningar och citattecken. Ingen extern ändring har gjorts;
respektive Transifex-enhets identifierare behöver hämtas från den aktuella
resursen innan en eventuell deltafil skapas.
