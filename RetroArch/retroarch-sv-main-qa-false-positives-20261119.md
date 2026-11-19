# RetroArch – verifierade QA-falsklarm i huvudkatalogen, 2026-11-19

Följande QA-träffar i `msg_hash_us.json` har kontrollerats mot aktuell engelsk källa och svensk måltext. De kräver ingen svensk textändring.

| Sträng-ID | QA-kategori | Bedömning |
| --- | --- | --- |
| 4604589 | Radbrytning | Källa och mål har samma semantiska radbrytning. QA räknar den serialiserade `\\n`-formen fel. |
| 6224735 | Radbrytning | Källa och mål har båda tre textstycken med samma tomrader. |
| 6220281 | Radbrytning | Källa och mål har en radbrytning mellan styckena. |
| 6188167 | Taggar | `<Parent Directory>` → `<Överordnad katalog>` är en visningsetikett med bevarade vinkelparenteser, inte HTML. |
| 1932676 | Taggar | `<Ask me>` → `<fråga mig>` är en översatt visningsetikett, inte markup. |
| 1932800 | Taggar | `<multiple>` → `<flera>` är en översatt visningsetikett, inte markup. |
| 6183699 | Interpunktion | QA misstolkar den svenska förkortningsgenitiven `CPU:n` som kolon utan följande blanksteg. |
| 5091976 | Interpunktion | QA misstolkar den svenska förkortningsgenitiven `ISO:s` som kolon utan följande blanksteg. |
| 5117750, 5117748 | Tal | QA misstolkar frekvensangivelser med svenskt mellanrum före `Hz`; talvärdena är bevarade. |

De faktiska formateringsbrister som hittades i samma QA-genomgång är dokumenterade och rättade som separata utkast: Quit RetroArch (5118546), svarta bildrutor (5124352), extra shaderbildrutor (5124358), Spelläge (6220277), New3DS-klockhastighet (3398118) och BFI-varningen (5757604).

Ingen QA-status eller översättning har ändrats i Crowdin.
