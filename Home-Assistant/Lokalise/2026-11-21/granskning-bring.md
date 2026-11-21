# Home Assistant Core – Bring

Datum: 2026-11-21

Källa: Home Assistant Core `2fdaa177`,
`homeassistant/components/bring/strings.json`, äldre delrapporter och direkt
återläsning från Lokalise API.

## Resultat

Alla 94 aktuella nycklar under `component::bring::*` radgranskades direkt i
Lokalise. 27 säkra korrigeringar sparades via API och lästes därefter tillbaka
ordagrant. De omfattar produktnamnets sammansättningar, svenska termer för
inköpslistans varor, status- och hjälptexter samt återställning av det tekniska
fältet `data['item']`; inga platshållare, länkar eller kodvärden ändrades.

De 20 verifierade språkparen har lagts in i den kanoniska Home Assistant-TMX:n,
som efter validering innehåller 1 904 poster.
