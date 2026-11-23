# Home Assistant Core – nytillagda Lokalise-poster

Lokalises livefilter för oöversatta Core-poster visade 405 nya poster från
`translations-upload.json`, trots att en äldre lokal export saknade tomma
svenska värden. Därför är den äldre exporten inte ett statusunderlag.

Fyra explicita batcher har granskats och sparats via API den 23 november 2026:

- batch 1–2: 30 poster;
- batch 3: 30 poster;
- batch 4: 30 poster.

Varje PUT följdes av en API-läsning av samma översättnings-id. Efter den
ursprungliga noteringen har batch 5–17 också granskats: Victron GX,
Libre-hubbar, sensorer, KNX IP Secure, väder, A Better Routeplanner, WebDAV,
BLUETTI, Jellyfin, Seafile och radar. Totalt omfattar de dokumenterade
livebatcherna 312 poster.

De är införda i den kanoniska HA Core-TMX:en i
`github.com/yeager/swedish-tm`, grenen `ha-tmx-validator`, med manifest
och stabila Lokalise-id:n. TMX-valideringen efter batch 17 godkände 3 914
poster (3 683 med Lokalise-id).

Arbetet fortsätter med återstående liveposter; detta dokument gör inget
anspråk på att Core är helt färdiggranskat.
