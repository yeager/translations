# RetroArch – XMB, testnycklar och firmware, svensk granskningsbatch 2026-11-19

14 oöversatta svenska strängar i RetroArchs huvudfil `msg_hash_us.json` har granskats från aktuella Crowdin API-svar. Förslagen är inte sparade eller skickade till Crowdin.

| Sträng-ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 6234743 | Test Signing Key Notifications | — | Meddelanden om testsigneringsnyckel |
| 6234745 | Show the reminder that this build trusts a test signing key. | — | Visa påminnelsen om att den här versionen litar på en testsigneringsnyckel. |
| 6234747 | Plastic Effect | — | Plasteffekt |
| 6234749 | Apply translucent plastic shading and highlights to XMB icons and text. | — | Använd genomskinlig plastskuggning och högdagrar på XMB-ikoner och text. |
| 6234751 | Ribbon Glow | — | Bandglöd |
| 6234753 | Add a soft glow to the Ribbon menu shader. This has a performance hit. | — | Lägg till ett mjukt sken i shadern för bandmenyn. Detta påverkar prestandan. |
| 6234755 | Ribbon Particles | — | Bandpartiklar |
| 6234757 | Draw drifting specks of light over the Ribbon menu shader. | — | Visa svävande ljusprickar över shadern för bandmenyn. |
| 6234781 | Missing Firmware Notifications | — | Meddelanden om saknad firmware |
| 6234783 | Show a dialog when launching a core with missing required firmware. Offer to download firmware when its core info file provides a URL. | — | Visa en dialogruta när en kärna startas utan nödvändig firmware. Erbjud hämtning av firmware när kärnans informationsfil innehåller en URL. |
| 6234785 | Required firmware is missing: | — | Nödvändig firmware saknas: |
| 6234791 | Required firmware could not be installed. | — | Nödvändig firmware kunde inte installeras. |
| 6234793 | This firmware is available for download. | — | Den här firmware kan hämtas. |
| 6234795 | This firmware must be supplied manually. | — | Den här firmware måste tillhandahållas manuellt. |

## Terminologi och kontroller

- `XMB` och `Ribbon` är specifika RetroArch-gränssnittstermer. *Bandmenyn* används som beskrivande svensk form, medan XMB lämnas som produktnamn.
- *Firmware* är etablerad teknisk term i RetroArch och används utan svensk böjning.
- Inga platshållare, markup-taggar eller URL:er förekommer i batchen.
- RetroArchs projekt-TM söktes via API:ets concordance-funktion; den gav inga tillräckligt relevanta matchningar för de nya strängarna.
- `l10n-lint --language sv` passerade utan anmärkningar.
- `hunspell -d sv_SE` markerade `testsigneringsnyckel`, `XMB-ikoner` och `shadern`. De är korrekta sammansättningar eller tekniska/projektspecifika termer.
- Crowdins förhandsvalidering markerade `testsigneringsnyckel`, `XMB-ikoner` och `informationsfil` som möjliga stavfel. Ingen annan QA-kategori flaggade batchen.

## Omfattning

Detta är en avgränsad batch från de 81 oöversatta strängarna i huvudfilen vid API-hämtningen. Den ersätter inte en fullständig svensk granskning av RetroArch.
