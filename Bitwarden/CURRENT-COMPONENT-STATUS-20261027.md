# Bitwarden: aktuell komponentstatus

Kontrollen utgår från Bitwardens klientkällkod vid commit
`0866e906e341da366eb265f95ece5ecc6542ca75`. Den senaste observerade
webbklienttaggen är `web-v2026.9.1`; den uppfyller kravet på en release yngre
än 48 månader.

| Komponent | Aktuell engelsk katalog | Saknade svenska måltexter i källträdet | Arkiverat 2026-10-27 | Upstreamstatus |
| --- | ---: | ---: | ---: | --- |
| Web | 4 952 | 263 | 263 | [PR #24212](https://github.com/bitwarden/clients/pull/24212) stängdes 2026-10-28 utan merge. Underhållaren hänvisar till Bitwardens Crowdin-flöde; deltat är inte infört uppströms. |
| Browser | 2 318 | 10 | 10 | [PR #24212](https://github.com/bitwarden/clients/pull/24212) stängdes 2026-10-28 utan merge. Underhållaren hänvisar till Bitwardens Crowdin-flöde; deltat är inte infört uppströms. |
| Desktop | 2 014 | 46 | 46 | [PR #24212](https://github.com/bitwarden/clients/pull/24212) stängdes 2026-10-28 utan merge. Underhållaren hänvisar till Bitwardens Crowdin-flöde; deltat är inte infört uppströms. |
| Mobile | 905 | 0 tomma; 42 engelska kandidater | 23 rättningar arkiverade och tillämpade i lokal branch | `bitwarden/mobile` är arkiverat och skrivskyddat på GitHub. Branch `yeager:codex/swedish-mobile-localization-20261028` innehåller validerade ändringar, men GitHub avvisade PR-skapande 2026-10-28. |
| Authenticator iOS | 52 relevanta äldre nycklar i aktuell katalog | 0 tomma; två tydliga grammatikfel | 60 äldre rättningar arkiverade | Den arkiverade källan är ersatt av aktiva `bitwarden/ios`. Av 60 gamla poster finns 52 kvar; åtta har utgått eller döpts om. Två verifierade grammatikrättningar skickades som [PR #3159](https://github.com/bitwarden/ios/pull/3159) 2026-10-28; väntar på CI och upstreamgranskning. |
| Authenticator Android | 152 i den äldre katalogen | 0 tomma; 49 engelska kandidater | 46 rättningar arkiverade | Mappat mot den aktiva efterföljaren `bitwarden/android` 2026-10-28: 43 nycklar finns redan med svenska måltexter, medan tre gamla nycklar har försvunnit eller döpts om. Ingen PR behövs för det gamla deltat. |

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

2026-10-28 stängdes PR #24212 utan merge. Bitwardens underhållare bekräftade
att Web-, Browser- och Desktop-översättningarna ska hanteras genom deras
Crowdin-flöde och synkas därifrån till GitHub. De 319 arkiverade posterna ska
alltså inte räknas som införda uppströms; innan en eventuell Crowdin-import
måste deras aktuella måltexter jämföras med deltorna för att undvika
dubbletter eller överskrivningar.

2026-10-28 tillämpades Mobile-deltats 23 poster på den då aktuella
`AppResources.sv.resx` i en lokal branch. Alla svenska måltexter och
platshållare matchar arkivdeltat; `xmllint`, `l10n-lint`, `git diff --check`
och staged Gitleaks passerade. Efter push till forken avvisade GitHub en PR
eftersom `bitwarden/mobile` är arkiverat. Ändringen är därför inte upstream-
inskickad och måste vid behov portas till en efterföljande, skrivbar mobilkod-
bas eller till projektets etablerade översättningsflöde.

Den 2026-10-28 bekräftades att även `bitwarden/authenticator-android` är
arkiverat och har ersatts av det aktiva `bitwarden/android`. Den gamla
46-postersfilen får därför inte appliceras på den arkiverade källan. En
källjämförelse visade också att `file_could_not_be_processed` i den äldre
källan innehåller synliga dubbla citattecken; arkivdeltat rättades för att
bevara dem. Deltat mappades samma dag mot efterföljarens
`ui/src/main/res/values-sv-rSE/strings.xml`: 43 nycklar återfinns där redan
med svenska måltexter och tre gamla nycklar (`enter_a_setup_key`,
`move_to_bitwarden` och `add_code_to_bitwarden`) saknas. För fem av de
återfunna nycklarna har engelskan ändrats sedan arkivet skapades, och den
aktuella svenska måltexten följer den nya källan. Ingen duplicerande PR är
därför lämplig för Android-deltat.

Den 2026-10-28 jämfördes Authenticator iOS-deltat med efterföljaren
`bitwarden/ios`. Av de 60 äldre posterna återfinns 52 i den aktuella
`Localizable.strings`-katalogen; åtta gamla nycklar saknas där. Flera av de
befintliga svenska texterna är fullt rimliga alternativa formuleringar och
skrevs därför inte över. Två aktuella bekräftelsetexter innehöll däremot
grammatikfelet ”din standardalternativ”. De korrigerades, syntaxkontrollerades
med `plutil`, kontrollerades med `git diff --check` och staged Gitleaks, och
skickades som PR #3159. Den fullständiga l10n-lintkörningen har ett äldre,
oavhängigt platshållarfel i `StepOfStep`; den nya tvåsträngarsdiffen innehåller
inte kontrollfelet.
