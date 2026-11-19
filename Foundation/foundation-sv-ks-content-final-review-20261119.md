# Foundation – Drakens skatt IV och stödjarinnehåll, svensk granskningsbatch 2026-11-19

De återstående 17 oöversatta strängarna i `ks_content.json` har granskats via Crowdin API. Förslagen är utkast och har inte sparats i Crowdin.

| ID | Engelska | Nuvarande svenska | Förslag |
| --- | --- | --- | --- |
| 26532 | The Dragon's Treasure | — | Drakens skatt |
| 26534 | Your decision to let the villagers keep … | — | Ditt beslut att låta byborna behålla drakens rikedom gjorde dem mycket glada, även om deras glädje avtar med tiden. |
| 26536 | Earn Coins over the coming year. | — | Tjäna mynt under det kommande året. |
| 26538 | Dragon's Treasure Shared | — | Drakens skatt delas |
| 26540 | You have decided to share … | — | Du har beslutat att dela drakens rikedom med ditt folk. |
| 26542 | There is enough for everyone, let's share! | — | Det räcker åt alla, låt oss dela med oss! |
| 26544 | You will earn Coins … | — | Du kommer att tjäna mynt, och dina bybor blir lyckligare under det kommande året. |
| 26546 | Light Through Stone | — | Ljus genom sten |
| 26548 | Build a Modest Church with 5 … worth 200 … | — | Bygg en anspråkslös kyrka med 5 ”Den ymniga hängivenheten, målat glas”, värda 200 prästerskapspoäng |
| 26550 | Torre de Alcántara | — | Torre de Alcántara |
| 26552 | A village of mountaineers and woodcutters … | — | En by med bergsfolk och skogshuggare, med gamla stensatta gator. |
| 26554 | Fulkenburgh | — | Fulkenburgh |
| 26556 | A bustling little town … | — | En livlig liten stad som är stolt över sina långa, eviga hallar. |
| 26558 | Etzehoe | — | Etzehoe |
| 26560 | A peaceful traders’ haven … | — | En fridfull fristad för handelsmän, som blomstrar genom handel både på land och längs floden. |
| 26562 | Backer Content | — | Stödjarinnehåll |
| 26564 | Enable backer-created content … | — | Aktivera innehåll skapat av stödjare, till exempel nya händelser, bybornas namn, handelsrutter och porträtt av abbedissor och seneschalker. |

## Kontroller

- `l10n-lint --language sv` gav inga fel eller varningar. En informationsnotering gäller `Torre de Alcántara`, som avsiktligt lämnas oförändrat som egennamn.
- `hunspell -d sv_SE` passerade utan anmärkningar.
- Citattecken samt talen 5 och 200 i 26548 har bevarats.
