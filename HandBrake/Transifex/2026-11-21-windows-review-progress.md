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


### Fortsatt kontroll – plats­hållarhjälp

Den långa tooltipen för målfilens platshållare rättades språkligt och API-återlästes. Samtliga platshållare, kodnamn och radbrytningar bevarades; **codec** och **encoder** i klammerparenteser lämnades avsiktligt orörda.


### Fortsatt kontroll – statusdialoger

Fyra Windows-poster sparades och API-återlästes: åtgärden för misslyckade jobb, kapitelinformation för källmediet, Safe Mode-varningen och köns jobbstatus. Platshållarna `{0}`–`{3}` är bevarade.


Korrigering: åtgärdsetiketten för `Retry Failed` preciserades vidare till **Försök igen med misslyckade jobb** och API-återlästes.


### Fortsatt kontroll – förhandsvisning

Windows-posten `Preview {0}` sparades och API-återlästes som **Förhandsvisning {0}**. Den tidigare imperativformen ersattes med en korrekt rubrik; platshållaren `{0}` är bevarad.


### Fortsatt kontroll – ljudterminologi

Windows-posten **Mixdown** sparades och API-återlästes som **Nedmixning**. Därmed används samma etablerade term i Linux, macOS och Windows.


### Fortsatt kontroll – DVD- och Blu-ray-inläsning

En materiellt felaktig Windows-hjälptext sparades och API-återlästes. Posten för minsta DVD/Blu-ray-titellängd innehöll felaktigt systemfältsinställningen; den återger nu **Minsta titellängd för dvd och Blu-ray i sekunder. Kortare titlar hoppas över:**.


### Fortsatt kontroll – kö, kodning och acceleratorer

Följande ändringar sparades direkt i Transifex och lästes tillbaka via API: `_Exit` → `_Avsluta`, `Retry All Jobs` → `Försök igen med alla jobb`, `Reset Selected Jobs` → `Återställ valda jobb`, `Multi-Pass Encoding` → `Kodning med flera pass`, `Avg Bitrate (kbps):` → `Genomsnittlig bithastighet (kbps):` och `Encoder Tune:` → `Finjustering för kodare:`. Förklarande DVD/Blu-ray-texter rättades också, inklusive plural i instruktionen om val av videor och formuleringen `i stället` för `instead`. Acceleratormarkör och platshållare bevarades.


### Fortsatt kontroll – återställning och status

Sju poster i inställnings- och statusavsnittet sparades och API-återlästes. `portable.ini.template` anges nu exakt i återställningsinstruktionen, `Queue Recovery Possible` återges som **Köåterställning möjlig**, och texten om omedelbar åtgärd fick korrekt svensk versalisering. Två statusrader återfick källans tre punkttecken (`...`) i stället för ett annat ellipstecken. Uppdateringslänken fick idiomatisk formulering (**söka efter nya versioner**) och `Currently Paused` förkortades till den korrekta statusetiketten **Pausad**. Platshållaren `{0}` och måttenheten `GB` är bevarade.


### Fortsatt kontroll – processisolering och bildinställningar

Fem poster sparades och API-återlästes. QuickSync-maskinvaran fick svensk sammansättning, den lokala HTTP-servern beskrivs som att den **lyssnar på** loopback-adressen och portintervallet är nu entydligt. Det efterföljande blanksteget i `Enter a name: ` återställdes, och `Fine Tune Picture Settings` fick den fullständiga svenska handlingstexten **Finjustera bildinställningar**.


### Fortsatt kontroll – förhandsvisning, status och kö

Elva poster sparades och API-återlästes. `Source Preview:` är nu **Källförhandsvisning:**. Fem felstatusar använder den konsekventa uppmaningen **Se loggen för detaljer.** `Max Height` och `Max Width` fick fullständiga måttetiketter, kökommandona använder **längst upp/ned**, och formuleringen för Windows-aktivitetsfältet är nu korrekt sammansatt. Inga platshållare ändrades.
