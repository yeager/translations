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
| `o:HandBrakeProject:p:WinUI:r:resourcestooltipsresx:s:cb007bff02436aaf93c2cdce48153ba9` | Setup behaviours … | Saknade slutpunkt | Slutpunkt tillagd | Källans interpunktion bevaras. |
| `o:HandBrakeProject:p:WinUI:r:resourcestooltipsresx:s:270afec0368625363ed8eaa1ba7275f3` | Setup behaviours … | Saknade slutpunkt | Slutpunkt tillagd | Källans interpunktion bevaras. |
| `o:HandBrakeProject:p:WinUI:r:resourcestooltipsresx:s:d3edbbdccbc15d7a5863e33ce64d8762` | one of two modes | ett eller två lägen | ett av två lägen | Återställer källans val mellan två lägen. |
| `o:HandBrakeProject:p:WinUI:r:resourcestooltipsresx:s:f5f3eac3e21be93ef2ae689bf2d73124` | Blu-ray and DVD sources | Blu-ray och dvd-källor | Blu-ray och DVD-källor | Produktförkortningen bevaras. |
| `o:HandBrakeProject:p:WinUI:r:resourcestooltipsresx:s:b90dd6bbc98684112c649588ff7cbf79` | Deblock reduces … | Deblock minskar … | Blockborttagning minskar … | Generiskt filternamn följer HandBrake-terminologin. |
| `o:HandBrakeProject:p:WinUI:r:resourcestooltipsresx:s:cd56e6385abbdccfc38fe728492aa2fd` | Denoise reduces … | Denoise … | Brusreducering … | Generiskt filternamn och dess böjningar översattes konsekvent. |
| `o:HandBrakeProject:p:WinUI:r:resourcestooltipsresx:s:6de18f3bdab540bf638c914fc80820f7` | Denoise filter preset. | Förinställning för filtret denoise. | Förinställning för brusreducering. | Generiskt filternamn översattes. |
| `o:HandBrakeProject:p:WinUI:r:resourcestooltipsresx:s:13b49bb76879cab3dce011f3f3c509d6` | Chroma Smooth Filter | Chroma Smooth-filter | Kromautjämningsfilter | Konsekvent med Linux- och macOS-gränssnitten. |

Samtliga ändringar skickades genom Transifex API och lästes tillbaka från respektive resursöversättning.

## Status

Inventering och kontroll av tomma värden är klar för båda Windows-resurserna. Semantisk radgranskning fortsätter; rapporten är inte ett 100-procentigt godkännande av Windows UI, Tooltips eller HandBrake som helhet.

## Fortsatt radgranskning – 2026-11-21

Färsk API-hämtning av 1 013 huvudsträngar och 91 tooltipsträngar användes vid kontrollen. En konsekvensrättning sparades och återlästes:

| Engelska | Tidigare svenska | Sparad svenska | Motivering |
| --- | --- | --- | --- |
| Passthru Common Metadata | Genomström vanliga metadata | För över vanliga metadata | Samma begripliga svenska åtgärdsform som i Linux- och macOS-resurserna. |

l10n-lint med språk=sv gav 0 fel för den samlade aktuella katalogen; inga nya Hunspell-sv-anmärkningar uppstod.


### Fortsatt semantisk kontroll

Sparade och API-återlästa: **Muxing: This may take a while…** → **Muxning: Detta kan ta en stund…** samt båda **When Done**-etiketterna → **Vid slutförande**. Denna passning inkluderar 0 l10n-lint-fel; kvarvarande varningar är dokumenterade falska positiva eller ett källfel.


### Fortsatt kontroll – filterterminologi

**Comb Detect** uppdaterades från **Kamdetektering** till **Comb-identifiering** och återlästes via Transifex API. Därmed används samma synliga HandBrake-term i Linux, macOS och Windows.
