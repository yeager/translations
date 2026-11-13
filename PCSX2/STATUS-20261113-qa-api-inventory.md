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

Post `8827` är den parallella informationstexten i FullscreenUI. Den exporterade måltexten hade bland annat engelsk apostrof i `PS2&amp;apos;s`, oböjd term `Recompilers` och en oidiomatisk ordföljd. En ny, ogranskad Crowdin-kandidat med översättnings-id `449931` skickades via API den 13 november 2026 och återlästes direkt efteråt.

Under kontrollen upptäcktes att post `3113` i AboutDialog redan hade en bättre exporterad måltext än den nyss skapade kandidaten. Kandidaten `449927` drogs därför tillbaka och dess frånvaro bekräftades med API-svaret 404. En ännu tidigare kandidat, `449925`, som saknade HTML-strukturen, hade redan raderats. Ingen befintlig översättning eller godkännandestatus ändrades. Kandidaten `449931` är inskickad men ännu inte upstreamgranskad eller vald som aktiv översättning.

Post `10498` i FullscreenUI använder den källspecifika förklaringen "auto fire". Den tidigare svenska kandidaten behöll det engelska uttrycket. Efter kontroll mot källans inställningskontext skickades därför kandidat `449929` med *automateld*. Den återlästes direkt; Hunspell-sv hade inga träffar och svlang bedömde formuleringen som naturlig svenska. Även denna kandidat är ogranskad och inte vald som aktiv översättning.

## Fortsatt exportgranskning

Tre ytterligare FullscreenUI- och ljudinställningsposter skickades som ogranskade kandidater och återlästes via API:

| Sträng | Kandidat | Beslut |
| --- | ---: | --- |
| `11360` | `449933` | Rättar felaktig *utdatavolym* till *snabbspolningsvolym*. |
| `11304` | `449935` | *5.1 Surround* normaliseras till *5.1-surroundljud*. |
| `11306` | `449937` | *7.1 Surround* normaliseras till *7.1-surroundljud*. |

Hunspell-sv och svlang hade inga språkvarningar för dessa tre kandidater. Post `3449` för procentformatet hade redan kandidaten `%1 %`; Crowdins API avvisade en identisk inskickning med `Duplicate translation`. Ingen röst eller befintlig kandidat ändrades.
