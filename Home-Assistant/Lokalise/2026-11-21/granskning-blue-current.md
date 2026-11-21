# Home Assistant Core – Blue Current

Datum: 2026-11-21  
Källa: Core `2fdaa177`, `homeassistant/components/blue_current/strings.json`, tidigare radrapporter samt Lokalise API med direkt återläsning.

Status: samtliga 64 aktuella Lokalise-poster som motsvarar komponentens bladsträngar och referensmål är radgranskade. Tretton korrigeringar är sparade och återlästa.

| Omfattning | Sparad text | Motivering |
|---|---|---|
| Ström, fas 1–3 | `Ström fas 1`, `Ström fas 2`, `Ström fas 3` | Gemener i `fas` enligt svenska mätarnamn. |
| Elnätsström, fas 1–3 | `Elnätsström fas 1`–`3` | Korrekt svensk sammansättning. |
| Elnätets medel/maxström | `Genomsnittlig elnätsström`, `Maximal elnätsström` | Korrekt ordföljd och sammansättning. |
| Total kostnad | `Totalkostnad` | Etablerad UI-sammansättning. |
| Laddkorts-ID | `Laddkorts-ID` samt fullständig fältbeskrivning | ID skrivs med bindestreck; meningen har förenklats utan betydelseförlust. |
| Enhets-ID | `Enhets-ID` och `ID för Blue Current-laddningspunkten.` | Korrekt bindestreck och produktnamnssammansättning. |

Övriga konfigurations-, aktivitets-, fordons-, laddningskorts-, växlings- och tjänstesträngar är korrekta. Referensen för omstart har kontrollerats mot `common::action::reboot`. TMX-ledgern innehåller de tretton API-återlästa posterna och är validerad efter uppdateringen.
