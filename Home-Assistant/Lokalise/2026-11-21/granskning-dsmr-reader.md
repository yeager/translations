# Home Assistant Core – DSMR Reader

Datum: 2026-11-21

Alla 87 aktuella strängar kontrollerades mot Core och lästes direkt från Lokalise. Mätarnamnen för dag, månad och år använde genomgående svenskt felaktig ordställning. 47 etiketter rättades för konsekvent termanvändning, böjning och läsbarhet.

Exempel: `Aktuell månad hög tariff kostnad` → `Aktuell månads kostnad för hög tariff`, `Hög tariff returnerad pris` → `Pris för återförd el med hög tariff` och `Total kostnad` → `Totalkostnad`.

Varje ändring PUT-sparades via Lokalise API och direktåterlästes. TMX-posten uppdateras från den sparade granskningsmanifestet.
