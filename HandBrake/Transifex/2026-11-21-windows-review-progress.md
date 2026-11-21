# HandBrake – Windows UI: pågående svensk radgranskning

Datum: 2026-11-21  
Plattform: Transifex API  
Resurser: `o:HandBrakeProject:p:WinUI:r:resourcesresx` och `o:HandBrakeProject:p:WinUI:r:resourcestooltipsresx`

## Aktuell inventering

- Huvudresursen har 1 013 aktuella Transifex-källsträngar och 1 018 RESX-poster. De fem extra, tomma RESX-posterna saknar motsvarande aktuell källsträng och behandlas som strukturella/referensberoende, inte som översättningsluckor.
- Tooltip-resursen har 91/91 parade käll- och målsträngar samt inga tomma mål.
- Källorna hämtades via Transifex REST API och jämfördes nyckel för nyckel med de aktuella svenska RESX-exporterna.

## Sparade och API-återlästa ändringar

| Fullständig Transifex-resurssträng | Engelska | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- | --- |
| `o:HandBrakeProject:p:WinUI:r:resourcesresx:s:13b49bb76879cab3dce011f3f3c509d6` | Chroma Smooth: | Chroma Smooth: | Kromautjämning: | Synligt generiskt filternamn, konsekvent med Linux- och macOS-gränssnitten. |
| `o:HandBrakeProject:p:WinUI:r:resourcesresx:s:4ff80499717a3c58bbd0359b971b9952` | Deblock | Deblock | Blockborttagning | Synligt generiskt filternamn, konsekvent med Linux- och macOS-gränssnitten. |

Båda ändringarna skickades genom Transifex API och lästes tillbaka från respektive resursöversättning.

## Status

Inventering och kontroll av tomma värden är klar för båda Windows-resurserna. Semantisk radgranskning fortsätter; rapporten är inte ett 100-procentigt godkännande av Windows UI, Tooltips eller HandBrake som helhet.