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
livebatcherna 383 poster.

De är införda i den kanoniska HA Core-TMX:en i
`github.com/yeager/swedish-tm`, grenen `ha-tmx-validator`, med manifest
och stabila Lokalise-id:n. TMX-valideringen efter batch 17 godkände 3 914
poster (3 744 med Lokalise-id).

## Full livekontroll efter batch 22

En sekventiell API-kontroll av samtliga 152 Core-sidor med
`include_translations=1` hittade inga svenska tomma poster med engelsk
källtext. Åtta svenska tomma poster återstår, men samtliga har helt tom
engelsk källtext och kan därför inte översättas i Lokalise:

- `component::sensor::issues::units_changed::description`
- `component::sensor::issues::unsupported_state_class::description`
- `component::sensor::issues::state_class_removed::description`
- `component::roborock::services::set_vacuum_goto_position::fields::x_coord::description`
- `component::roborock::services::set_vacuum_goto_position::fields::y_coord::description`
- `component::sensor::issues::mean_type_changed::description`
- `component::vacuum::issues::segments_changed::description`
- `component::vacuum::issues::segments_mapping_not_configured::description`

De är källprojektets tomma metadata, inte saknade svenska översättningar.

En efterföljande fullkontroll upptäckte 24 senare uppladdade Workday-poster
med källtext på den sista API-sidan. De granskades, sparades och lästes tillbaka
via API. Sista sidan verifierades därefter med noll oöversatta svenska poster
med källtext.

## Semantiska rättningar efter kökontrollen

En separat jämförelse av återkommande korta källsträngar identifierade och
verifierade 34 svenska inkonsekvenser. De berörde knapptriggers
(långtryck, tryck, släpp samt dubbel- till femklick), `AI tools`,
`Add conversation agent`, `Account name`, autentiseringsutgång och en
avvikande slutpunkt i `Account is already configured`, samt
`Actions on turn off`, larmklocka, upplevd temperatur och
applikationsuppgifter. Varje ändring sparades via
Lokalise API, lästes tillbaka och fördes in i den kanoniska TMX:en.

Arbetet fortsätter med återstående liveposter; detta dokument gör inget
anspråk på att Core är helt färdiggranskat.

## Struktur för granskningsunderlag

Den 23 november samlades allt Home Assistant-material i `swedish-tm` under
en enda katalog: `Home-Assistant/`. Den aktiva Lokalise-ledgern och den
kanoniska TMX:en ligger i rotkatalogen. Äldre importer och snapshots ligger i
`source-archive/home-assistant/`, medan de tidigare generella
granskningskopiorna ligger i `review-archive/`. Inga granskningsposter
raderades. Efter flytten validerades den kanoniska TMX:en med 4 036 poster,
varav 3 805 har stabilt Lokalise-id.

## Senare Core-uppladdning: SmartThings och Evohome

Ytterligare 20 strängar tillkom på Core-projektets sista API-sida. De omfattar
SmartThings API-planer, personliga åtkomsttoken och återanslutning samt sex
Evohome-felmeddelanden. Samtliga granskades i kontext, sparades och lästes
tillbaka via Lokalise API. De är införda i den kanoniska TMX:en, som därefter
validerade 4 056 poster (3 825 med stabilt Lokalise-id). En direkt kontroll av
den aktuella sista sidan gav därefter noll oöversatta svenska strängar med
källtext.

## Tomma Lokalise-nycklar

En livegranskning av samtliga 152 Core-sidor, inklusive arkiverade poster,
bekräftade åtta — inte 34 — nycklar där både engelsk och svensk text är tom.
Alla åtta är aktiva. De har felrapporterats som
[home-assistant/core#193961](https://github.com/home-assistant/core/issues/193961).
Det är ett separat fel från #193667, som gäller nycklar som helt saknas i
Lokalise. Revisionsdata och det återanvändbara API-verktyget sparas i
`yeager/swedish-tm`, grenen `ha-tmx-validator`.

## Terminologikontroll: auktorisering

HomeWizards titel för det tidsgränsöverskridna auktoriseringssteget hade den
avvikande svenska texten `Godkänn`, medan samma flöde och övriga
auktoriseringssteg använder `Auktorisera`. Den uppdaterades via Lokalise API,
lästes tillbaka och lades in i den kanoniska TMX:en. TMX-valideringen efter
rättelsen godkände 4 057 poster.

## Music Assistant: albumnamn

I två parallella Music Assistant-fältnamn var `Album name` översatt både som
`Albumets namn` och `Albumnamn`. Båda är korta fältetiketter; den avvikande
första varianten normaliserades till `Albumnamn`, sparades och lästes tillbaka
via Lokalise API. Den kanoniska TMX:en validerade sedan 4 058 poster.

## Template: åtgärder vid ljudavstängning

Template-integrationen hade två annars identiska fält för `Actions on mute`:
ett i konfigurationsflödet och ett i alternativflödet. Texten i
alternativflödet normaliserades från `Åtgärder vid avstängning av ljudet` till
`Åtgärder vid ljudavstängning`, sparades och lästes tillbaka via Lokalise API.
TMX-valideringen godkände därefter 4 059 poster.
