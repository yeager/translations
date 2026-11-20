# OpenStreetMap på Transifex – svensk granskningsstatus

Datum: 2026-11-20  
Omfattning: hela Transifex-organisationen `openstreetmap`.

## Inventering

Organisationen har 19 offentliga projekt. Prioritering utgår från svenska
översättningar som kan granskas och kompletteras utan att duplicera tidigare
arbete.

| Projekt | Ord | Senast uppdaterat | Status |
| --- | ---: | --- | --- |
| BRouter-Web | 1 130 | 3 månader sedan | Ej påbörjat |
| ConditionalRestrictionParser | 15 | 1 år sedan | Ej påbörjat |
| CWG Resources | 6 830 | 3 år sedan | Ej påbörjat |
| iD Editor | 60 130 | 25 minuter sedan | Tidigare arbete återläst; se nedan |
| Irish Townlands | 2 920 | 3 år sedan | Ej påbörjat |
| JosmFilterParser | 82 | 1 år sedan | Ej påbörjat |
| Level0 | 338 | 2 månader sedan | Ej påbörjat |
| OpeningHoursFragment | 1 810 | 16 dagar sedan | Ej påbörjat |
| OpeningHoursParser | 137 | 1 år sedan | Ej påbörjat |
| OSM Awards | 3 310 | 10 månader sedan | Ej påbörjat |
| OSM Cards | 740 | 2 år sedan | Ej påbörjat |
| osm.ch | 2 280 | 2 år sedan | Ej påbörjat |
| OSM Streak | 1 960 | 2 år sedan | Ej påbörjat |
| OSMyBiz | 1 030 | 7 månader sedan | Ej påbörjat |
| Presets | 15 660 | 1 dag sedan | Ej påbörjat |
| SOSM | 264 | 5 år sedan | Ej påbörjat |
| switch2osm | 0 | 3 år sedan | Inga källsträngar |
| uMap | 3 180 | 2 dagar sedan | Ej påbörjat |
| Vespucci OSM Editor | 14 050 | 1 timme sedan | Ej påbörjat |

Uppgifterna ovan är hämtade från organisationens offentliga sida i Transifex.
Ordantal är avrundade som sidan visar dem och får inte användas som mått på
svenska oöversatta strängar.

## Redan dokumenterat arbete: iD Editor

Arkivet `../../iD-Editor/Transifex/2026-11-12/` visar att 87 då oöversatta
strängar i resurserna `core`, `imagery`, `community` och `presets` skickades
via Transifex API och lästes tillbaka. Det arbetet ska inte göras om. En ny
API-läsning behövs innan nya ändringar övervägs, eftersom projektet uppdateras
aktivt.

## Nästa steg

1. Autentisera med den säkert lagrade Transifex-tokenen och hämta per-projekt-
   och per-resursstatistik för `sv`.
2. Skapa en prioriterad kö över oöversatta strängar. Små, stabila projekt
   granskas först; aktivt uppdaterade projekt läses om omedelbart före skrivning.
3. Radgranska mot källa, `sv-lang`, `hunspell-sv`, terminologibanken och
   `swedish-tm`.
4. Spara varje accepterad ändring direkt via Transifex API, läs tillbaka den
   och arkivera delta samt kvitto här.

## Åtkomstläge

Den publika Transifex-sidan är åtkomlig, men den aktuella webbläsarsessionen
är inte inloggad och ingen API-token exponeras i den här körmiljön. Inga
strängar har därför ändrats i detta arbetspass. Fortsättning kräver att den
befintliga säkra tokenkällan görs tillgänglig för processen, eller att användaren
loggar in i Transifex i webbläsaren.
