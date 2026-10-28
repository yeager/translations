# Bitwarden: aktuell komponentstatus

Kontrollen utgår från Bitwardens klientkällkod vid commit
`0866e906e341da366eb265f95ece5ecc6542ca75`. Den senaste observerade
webbklienttaggen är `web-v2026.9.1`; den uppfyller kravet på en release yngre
än 48 månader.

| Komponent | Aktuell engelsk katalog | Saknade svenska måltexter i källträdet | Arkiverat 2026-10-27 | Upstreamstatus |
| --- | ---: | ---: | ---: | --- |
| Web | 4 952 | 263 | 263 | Skickat som [PR #24212](https://github.com/bitwarden/clients/pull/24212) 2026-10-28; väntar på upstreamgranskning och CI. |
| Browser | 2 318 | 10 | 10 | Skickat som [PR #24212](https://github.com/bitwarden/clients/pull/24212) 2026-10-28; väntar på upstreamgranskning och CI. |
| Desktop | 2 014 | 46 | 46 | Skickat som [PR #24212](https://github.com/bitwarden/clients/pull/24212) 2026-10-28; väntar på upstreamgranskning och CI. |
| Mobile | 905 | 0 tomma; 42 engelska kandidater | 23 rättningar arkiverade | Jämförd mot `bitwarden/mobile` vid `b543459f8d71324aa11914da1e6f6ad3d7abce54`; 19 avsiktligt oförändrade produkt- och tekniknamn återstår. |
| Authenticator iOS | 159 | 0 tomma; 66 engelska kandidater | 60 rättningar arkiverade | Jämförd mot `bitwarden/authenticator-ios` vid `9fbbceb1bd030a6360ba50e4c143ea5440e7428f`; sex avsiktligt oförändrade produkt- och tekniknamn återstår. |
| Authenticator Android | 152 | 0 tomma; 49 engelska kandidater | 46 rättningar arkiverade | Jämförd mot `bitwarden/authenticator-android` vid `1fa1322827a4fefc1cac4666402e6ef3b4aceded`; tre avsiktligt engelska kandidater återstår: två produktnamn och den kontextberoende `Add Item Rotation`. |

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
svenska måltexter, men en efterföljande likhetssökning mot engelskan fann
kandidater som har bedömts rad för rad. De senaste observerade releaserna
är Mobile `v2024.10.0` (2024-10-17), Authenticator iOS `v2025.2.0`
(2025-02-12) och Authenticator Android `v2025.1.0` (2025-02-11); samtliga
uppfyller färskhetskravet.

Den lokala granskningen omfattar 448 unika arkiverade poster utan dubbletter:
263 för Web, 10 för Browser, 46 för Desktop, 23 för Mobile, 46 för
Authenticator Android och 60 för Authenticator iOS. Den 2026-10-28 jämfördes
Web-, Browser- och Desktop-deltana på nytt mot `bitwarden/clients` huvudgren
och skickades i PR #24212. Källnycklarna och de engelska texterna matchade,
och samtliga 319 svenska måltexter applicerades exakt. JSON, Prettier,
`git diff --check` och en avgränsad staged Gitleaks-kontroll passerade.
Bitwardens `test:locales` kunde inte köras i den sparsamma checkouten eftersom
den kräver hela `apps/cli/src`-trädet och en basgrensfixtur; den är alltså inte
ett godkänt testresultat. Mobile och båda Authenticator-katalogerna återstår
att koppla till aktuella plattforms-id:n inför en separat PR. Den samlade
Gitleaks-körningen träffar två generiska mönster i den äldre Quartz-batchens
JSON-fält `key`; träffarna innehåller inga hemligheter.
