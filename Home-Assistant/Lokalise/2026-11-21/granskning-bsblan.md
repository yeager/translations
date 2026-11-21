# Home Assistant Core – BSB-LAN

Datum: 2026-11-21

Källa: Home Assistant Core `2fdaa177`,
`homeassistant/components/bsblan/strings.json`, tidigare delrapporter och direkt
återläsning från Lokalise API.

## Resultat

Alla 125 aktuella `component::bsblan::*`-nycklar har radgranskats och lästs
direkt från Lokalise. Sju säkra korrigeringar sparades via API och återlästes
ordagrant. De omfattar BSB-LAN-namnets bindestreck, sammansättningen
”Totalenergi”, enhetsbestämning i anslutningsfel och enhetliga formuleringar
för varmvatten- och uppvärmningsscheman. Platshållarna `{host}` och `{error}`
verifierades bevarade.

De verifierade språkparen finns i den kanoniska HA-TMX:n, som efter validering
innehåller 1 925 poster.
