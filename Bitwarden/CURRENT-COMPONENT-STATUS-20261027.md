# Bitwarden: aktuell komponentstatus

Kontrollen utgår från Bitwardens klientkällkod vid commit
`0866e906e341da366eb265f95ece5ecc6542ca75`. Den senaste observerade
webbklienttaggen är `web-v2026.9.1`; den uppfyller kravet på en release yngre
än 48 månader.

| Komponent | Aktuell engelsk katalog | Saknade svenska måltexter i källträdet | Arkiverat 2026-10-27 | Upstreamstatus |
| --- | ---: | ---: | ---: | --- |
| Web | 4 952 | 263 | 263 | Inte inskickat; arkivdeltan behöver kopplas till aktuella plattforms-id:n före import. |
| Browser | 2 318 | 10 | 10 | Inte inskickat; se `bitwarden-browser-current-missing-sv-20261027.json`. |
| Desktop | 2 014 | 46 | 46 | Inte inskickat; se `bitwarden-desktop-current-missing-sv-20261027.json`. |
| Mobile | 905 | 0 tomma; 42 engelska kandidater | Ingen ny ändring | Jämförd mot `bitwarden/mobile` vid `b543459f8d71324aa11914da1e6f6ad3d7abce54`; radvis innehållsgranskning återstår. |
| Authenticator iOS | 159 | 0 tomma; 66 engelska kandidater | Ingen ny ändring | Jämförd mot `bitwarden/authenticator-ios` vid `9fbbceb1bd030a6360ba50e4c143ea5440e7428f`; radvis innehållsgranskning återstår. |
| Authenticator Android | 152 | 0 tomma; 49 engelska kandidater | 26 rättningar arkiverade | Jämförd mot `bitwarden/authenticator-android` vid `1fa1322827a4fefc1cac4666402e6ef3b4aceded`; kandidaterna måste skiljas från produktnamn och andra avsiktligt oförändrade texter. |

Webbdeltana 01–22 innehåller samtliga 263 poster som saknas i den aktuella
svenska webbkatalogen, i den ordning de förekommer i den engelska katalogen.
Desktopfilen återanvänder 33
tidigare API-verifierade arkivtexter och kompletterar 13 nya eller ändrade
poster. Browserdeltat omfattar samtliga tio aktuellt saknade poster.

Alla nya JSON-deltan har kontrollerats för JSON-syntax, platshållare,
trippelidentiska konsonanter, `l10n-lint`, Hunspell, `svlang` och Gitleaks.
`svlang` analyserar även engelska källfält i deltaformatet; dess engelska
träffar räknas därför inte som svenska språkfel. Ingen källkatalog har
ändrats, och ingen post är därmed påstått uppladdad eller godkänd upstream.

Webbdeltana är lokala granskningsunderlag och ändrar inte Bitwardens
källkatalog. Den aktuella mobil- och autentiseringsjämförelsen fann inga tomma
tomma svenska måltexter, men en efterföljande likhetssökning mot engelskan
fann kandidater som kräver radvis bedömning. De senaste observerade releaserna
är Mobile `v2024.10.0` (2024-10-17), Authenticator iOS `v2025.2.0`
(2025-02-12) och Authenticator Android `v2025.1.0` (2025-02-11); samtliga
uppfyller färskhetskravet.

Nästa arbete är att koppla webbdeltana till aktuella plattforms-id:n inför
import och att göra en separat radvis innehållsgranskning av Mobile och
Authenticator, eftersom full täckning inte i sig bevisar språkkvalitet.
