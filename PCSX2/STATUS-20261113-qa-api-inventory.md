# PCSX2: svensk QA-inventering via Crowdin API, 13 november 2026

## Underlag

Crowdins API för projekt `PCSX2 Emulator` (`561203`), svenska och den aktiva filen `15` returnerade 1 628 öppna QA-poster vid hämtningen. Det är inte samma räknesätt som den tidigare UI-siffran 1 547 och ska inte tolkas som en radvis språkgranskning.

| Kontrolltyp | Antal |
| --- | ---: |
| `spellcheck` | 1 489 |
| `entities_check` | 65 |
| `spaces_after_punctuation_check` | 54 |
| `parentheses_check` | 5 |
| `numbers_check` | 5 |
| `punctuation_check` | 4 |
| `multiple_uppercase_check` | 4 |
| `capitalize_check` | 1 |
| `c_variables_check` | 1 |

De första posterna visar att stavningskontrollerna bland annat träffar `PCSX2`, `RetroAchievements`, `PlayStation`, `GitHub-förråd`, `MIPS-processortolkar` och `omkompilatorer`. Dessa är produktnamn, tekniska termer eller svenska sammansättningar och inte bevis på felaktig måltext.

## Beslut

Inga QA-poster har avfärdats eller massgodkänts. Formateringskontroller ska jämföras med exakt käll- och måltext före varje rättning. Stavningsposter behandlas endast när den konkreta svenska formuleringen är fel, inte därför att Crowdins ordlista saknar termen.

## Första radgranskade rättningen

Post `3113` är informationstexten i `AboutDialog` och innehöll den faktiska språkbristen "PCSX2 är an gratis emulator". Källans HTML-struktur och platshållarliknande entiteter kontrollerades mot måltexten. En ny, ogranskad Crowdin-kandidat med översättnings-id `449927` skickades via API den 13 november 2026. Den återlästes direkt efteråt och har samma HTML-struktur som källan.

Den tidigare felaktiga kandidaten `449925`, som saknade HTML-strukturen, raderades omedelbart innan den hann lämnas över för granskning. Ingen befintlig översättning eller godkännandestatus ändrades. Kandidaten `449927` är inskickad men ännu inte upstreamgranskad eller vald som aktiv översättning.

Post `10498` i FullscreenUI använder den källspecifika förklaringen "auto fire". Den tidigare svenska kandidaten behöll det engelska uttrycket. Efter kontroll mot källans inställningskontext skickades därför kandidat `449929` med *automateld*. Den återlästes direkt; Hunspell-sv hade inga träffar och svlang bedömde formuleringen som naturlig svenska. Även denna kandidat är ogranskad och inte vald som aktiv översättning.
