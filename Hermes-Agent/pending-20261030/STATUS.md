# Hermes Agent: pågående svenska kataloger

Datum: 2026-10-30.

Detta är en återställningskopia av tre oinscheckade svenska kataloger från
den lokala arbetskopian. De hör **inte** till den redan inskickade,
avsiktligt partiella desktopkatalogen i PR #101116 och ska inte beskrivas som
uppströmsarbete.

| Fil | SHA-256 | Status |
| --- | --- | --- |
| `static-sv.yaml` | `451194825ae203369ad22e43d99147a4698ef87a1b8fa9a5e7f5b8cd423b003a` | YAML kan tolkas; behöver nyckelparitet och kontextgranskning. |
| `tui-sv.ts` | `2082ef37d960485217084576bdf2058dc86cfc2748c460280dc8ea252de1d1a6` | Behöver strukturmigrering, typkontroll, tester och radgranskning mot den engelska katalogen. |
| `web-sv.ts` | `754bb731e87c8b69a9aa3a54f0b7a19eaf1704b60c4889f5dfebc3fd89b0b19d` | Behöver typkontroll, tester och radgranskning mot den engelska katalogen. |

Gitleaks hittade inga hemligheter i någon av filerna. Ingen av dessa filer har
pushats eller skickats uppströms i detta steg.

## Desktopkatalog, uppdaterad 2026-11-05

Den avsiktligt partiella desktopkatalogen i [PR #101116](https://github.com/NousResearch/hermes-agent/pull/101116) är nu rebasad på aktuell uppströms-`main` och pushad som commit `fe7ec2c174`. Rebasen synliggjorde 20 nya nycklar, som nu har fått kontextgranskade svenska texter för MCP-serverstart, kontextkomprimering och samlad/automatisk uppdatering av pluginer.

`languages.test.ts` och `overlay-completeness.test.ts` passerar med 6/6 tester, liksom desktoplinten i pre-commit, `git diff --check` och en avgränsad Gitleaks-kontroll. Den breda TypeScript-typkontrollen stannar i den aktuella uppströmsfilen `use-session-actions.test.tsx`, eftersom `tests/fixtures/session-resume-active-turn.json` saknas; den diagnosen berör inte den svenska katalogen. GitHub visar den nya grenen men rapporterar ännu `BLOCKED` utan check-runs eller ny maintainergranskning.

## Webbkatalog, uppdaterad 2026-11-03

En uppdaterad och radgranskad webbkatalog har nu skapats från aktuell
huvudgren, registrerats som språkval i webbgränssnittet och skickats som
[PR #148618](https://github.com/NousResearch/hermes-agent/pull/148618).
Den exakta inskickade filen är `../web.sv-20261103.ts` med SHA-256
`c6220caaefd6e529d4521bfb9c178634bef3447f0fe4d3fcd5f2d8d32bc6f8ac`.

Kontrollerna `npm run typecheck --prefix web` och `npm run test --prefix web`
passerade (71 testfiler, 477 tester), liksom Prettier, skrivregler och
Gitleaks. `defineLocale` ger engelska reservtexter för framtida nycklar som
ännu inte har fått en svensk text; PR:n beskriver därför inte katalogen som
slutgiltigt komplett.

## Filer-sidan, uppdaterad 2026-11-03

Den nya webbsidan för filer hade användarvisade engelska strängar direkt i
komponentkoden. De är nu flyttade till den typade engelska katalogen och har
svenska motsvarigheter för knappar, status, fel, bekräftelser, tabellrubriker
och tillgänglighetsetiketter. Ändringen är pushad till samma
[PR #148618](https://github.com/NousResearch/hermes-agent/pull/148618) i
commit `7df54df99d`.

Den exakta svenska katalogen efter denna uppdatering är
`../web.sv-20261103-files-page.ts` med SHA-256
`9ba4d3744686b2cbb786fdd9e765a70fdfe1e0311f7e04c05d4db1ac755c8277`.
Webbens typkontroll och hela testsviten (71 testfiler, 477 tester) passerade,
liksom ESLint, skrivregler och Gitleaks. l10n-lint kan ännu inte tolka
TypeScript-kataloger och rapporterar därför ett syntaxfel på första raden; det
är ett verktygsformatsbegränsning, inte en katalogvarning.

## Sessions-sidan, uppdaterad 2026-11-03

Sessionssidans kvarvarande användarvisade engelska text är nu flyttad till en
typad engelsk katalog med svenska motsvarigheter: tillgänglighetsetiketter,
namnbyte och export, källfilter, status och fel, rensning samt import och
översikt. Generiska källnamn för API-server, verktyg och Vulcan-delegering
följer samma katalog; produkt- och protokollnamn är avsiktligt oförändrade.
Ändringen är pushad till [PR #148618](https://github.com/NousResearch/hermes-agent/pull/148618)
i commit `27bb85b11d`.

Den exakta svenska katalogen efter denna uppdatering är
`../web.sv-20261103-sessions-page.ts` med SHA-256
`a35334c4f3e155576cf05c8af80d86afc89fa8c392d20d502e4beb6e9edff0df`.
Webbens typkontroll och hela testsviten (71 testfiler, 477 tester) passerade,
liksom ESLint, skrivregler och Gitleaks.

## Parkopplingssidan, uppdaterad 2026-11-03

Parkopplingssidans statiska webbtexter är flyttade till den typade
webbkatalogen och har svenska översättningar för begäranden, godkännande,
återkallning, fel, bekräftelser, tidsangivelse och tillgänglighetsetiketter.
Användaridentiteter och plattformsnamn lämnas oförändrade. Ändringen är
pushad till [PR #148618](https://github.com/NousResearch/hermes-agent/pull/148618)
i commit `2265370c22`.

Den exakta svenska katalogen efter denna uppdatering är
`../web.sv-20261103-pairing-page.ts` med SHA-256
`09f671f26f53e46712aef0d84df983285b9305ac63b3640b37a577819318d6cc`.
Webbens typkontroll och hela testsviten (71 testfiler, 477 tester) passerade,
liksom ESLint, skrivregler och Gitleaks.

## Modellöversikten, uppdaterad 2026-11-03

Den första sammanhållna delen av Models-sidan är nu katalogiserad: token-
och kapacitetsetiketter, modellkortens status, menyn för att tilldela modeller
och varningen för särskilt dyra modeller. Produktnamn, modellidentifierare och
backendgenererade fel lämnas oförändrade. Ändringen är pushad till
[PR #148618](https://github.com/NousResearch/hermes-agent/pull/148618) i
commit `15d31ffd54`.

Den exakta svenska katalogen efter denna uppdatering är
`../web.sv-20261103-models-overview.ts` med SHA-256
`bf10dd2f96f08328bc9d577113cea70b6d5d20d1f3d6aac50da48e3961b26ea1`.
Webbens typkontroll och hela testsviten (71 testfiler, 477 tester) passerade,
liksom skrivregler och Gitleaks. ESLint rapporterar fortfarande en befintlig
varning för den oförändrade `load()`-anropet i Models-sidans effekt, men inga
fel.

## Modellinställningar, uppdaterad 2026-11-03

Models-sidans inställningspaneler och dialoger har kompletterats med svenska
texter för hjälpuppgifter, automatiskt modellval, återställning, Mixture of
Agents-förinställningar, referensmodeller och modellval. Modellnamn,
leverantörsnamn och serverdata förblir oförändrade. Ändringen är pushad till
[PR #148618](https://github.com/NousResearch/hermes-agent/pull/148618) i
commit `96362c47e7`.

Den exakta svenska katalogen efter denna uppdatering är
`../web.sv-20261103-models-settings.ts` med SHA-256
`9d22fcf249c7ad6ecea7114da40b975d0d43043a659696cf8e05994ae41dd206`.
Webbens typkontroll och hela testsviten (71 testfiler, 477 tester) passerade,
liksom skrivregler och Gitleaks. ESLint har fortfarande en befintlig varning
för den oförändrade `load()`-anropet i Models-sidans effekt, men inga fel.

## Modellstatistik, uppdaterad 2026-11-03

Den synliga förklaringen när token- och kostnadsstatistik är avstängd är nu
också flyttad till den typade webbkatalogen och översatt. Den behåller
konfigurationsnyckeln `dashboard.show_token_analytics` oförändrad, eftersom
den är en teknisk nyckel som användaren kan behöva skriva exakt. Ändringen är
pushad till [PR #148618](https://github.com/NousResearch/hermes-agent/pull/148618)
i commit `d481810f7b`.

Den exakta svenska katalogen efter denna uppdatering är
`../web.sv-20261103-models-analytics.ts` med SHA-256
`c688ecb41943663cea5a82bf6792e826dc4ff2f51e1c167bf972c4f0d328854b`.
Webbens typkontroll och hela testsviten (71 testfiler, 477 tester) passerade,
liksom skrivregler och Gitleaks. ESLint har fortfarande en befintlig varning
för den oförändrade `load()`-anropet i Models-sidans effekt, men inga fel.

## Models-sidan, färdig statisk UI-del 2026-11-03

En avslutande radgranskning hittade engelska reservetiketter för tomma
leverantörs- och modellfält i Mixture of Agents-dialogen. De är nu
katalogiserade och översatta, så den statiska Models-sidan är täckt av den
utökade webbkatalogen. Dynamiska modell-, leverantörs- och backendvärden
översätts inte i klienten. Ändringen är pushad till
[PR #148618](https://github.com/NousResearch/hermes-agent/pull/148618) i
commit `c86b61cb5b`.

Den exakta svenska katalogen efter denna uppdatering är
`../web.sv-20261103-models-complete.ts` med SHA-256
`a8ad90929d92f25deb2f0f58636bb2dcc8eb7abeb1d1d668620b92a373c5de20`.
Typkontroll, skrivregler och Gitleaks passerade. ESLint har fortfarande en
befintlig varning för det oförändrade `load()`-anropet i Models-sidans effekt,
men inga fel.

## MCP-server: skapa och installera, uppdaterad 2026-11-03

Den första MCP-delen är katalogiserad och översatt: inläsnings- och
felmeddelanden, skapande av server, OAuth-information, miljövariabler,
installationsdialog och statusmeddelanden. Servernamn, URL:er, hemligheter och
MCP-servrarnas dynamiska data lämnas oförändrade. Ändringen är pushad till
[PR #148618](https://github.com/NousResearch/hermes-agent/pull/148618) i
commit `fb84687ec0`.

Den exakta svenska katalogen efter denna uppdatering är
`../web.sv-20261103-mcp-creation.ts` med SHA-256
`503c300ba5e1b17ee870f818dc78f91cc97ddcddd33825e6f921587fdbd9ca6a`.
Typkontroll, ESLint, hela testsviten (71 testfiler, 477 tester), skrivregler
och Gitleaks passerade.

## MCP-serverhantering, uppdaterad 2026-11-03

MCP-sidan är nu radgranskad i sin helhet för statisk webbtext: serverlistan,
OAuth, aktivering, anslutningsprov, borttagning och katalogen använder den
typade engelska katalogen med svenska motsvarigheter. Servernamn, URL:er,
protokollnamn, katalogbeskrivningar, diagnostik och andra data från servern
lämnas avsiktligt oförändrade. Ändringen är pushad till
[PR #148618](https://github.com/NousResearch/hermes-agent/pull/148618) i
commit `c4905a21e1`.

Den exakta svenska katalogen efter denna uppdatering är
`../web.sv-20261103-mcp-management.ts` med SHA-256
`8952fc43932ad4e6c06fff0c9ceb60c2b3a9a471a091bedc542668257c719051`.
Typkontroll, ESLint, hela testsviten (71 testfiler, 477 tester), skrivregler,
l10n-lint och Gitleaks passerade. l10n-lint kördes på en strukturerad
export av de nya MCP-texterna eftersom verktyget ännu inte tolkar
TypeScript-kataloger direkt.

## Skills: lokala reglage och inlärning, uppdaterad 2026-11-03

Skills-sidans lokala reglage och dialog för att skapa en färdighet från
underlag är nu katalogiserade och översatta: navigering till katalogen,
skapande, redigering, konfigurering, sparbekräftelse och samtliga etiketter
och hjälptexter i inlärningsdialogen. Externa katalogresultat, dynamiska
färdighetsbeskrivningar och säkerhetsskannerns serverdata är avsiktligt
lämnade till nästa delgranskning. Ändringen är pushad till
[PR #148618](https://github.com/NousResearch/hermes-agent/pull/148618) i
commit `c3f4d1f432`.

Den exakta svenska katalogen efter denna uppdatering är
`../web.sv-20261103-skills-controls.ts` med SHA-256
`f944ed97d24f362a45bff0ece35dc077fd761d537aaf8b9f672aac312ad1d5ac`.
Typkontroll, hela testsviten (71 testfiler, 477 tester), skrivregler och
Gitleaks passerade. ESLint har fortfarande en befintlig varning i
Skills-sidans oförändrade förhandsgranskningskod om synkron state-uppdatering
i en effekt, men inga fel.

## Webhooks, uppdaterad 2026-11-03

Webhooks-sidans hela statiska gränssnitt är nu katalogiserat och översatt:
skapande och borttagning av prenumerationer, formulär, status, fel,
omstartsinformation, kopieringsknappar och tillgänglighetsetiketter.
Webhooknamn, händelseidentifierare, URL:er, hemligheter och fel från servern
lämnas oförändrade. Ändringen är pushad till
[PR #148618](https://github.com/NousResearch/hermes-agent/pull/148618) i
commit `f28ba6c580`.

Den exakta svenska katalogen efter denna uppdatering är
`../web.sv-20261103-webhooks.ts` med SHA-256
`1071ac894aa4e7ec08c04fff838d42c7d6f37fc9ce5b8b70d6f4ad2c84a2731f`.
Typkontroll, ESLint, hela testsviten (71 testfiler, 477 tester), skrivregler,
l10n-lint på en strukturerad export och Gitleaks passerade.

## Delade kanalbotar, uppdaterad 2026-11-03

Panelen för att länka ett konto till en delad kanalbot är nu katalogiserad
och översatt: länkning, QR-kod, vänteläge, fel, kontoborttagning och länkar
till Nous Portal. Kontonamn, kommandon, plattformar och serversvar förblir
oförändrade. Ändringen är pushad till
[PR #148618](https://github.com/NousResearch/hermes-agent/pull/148618) i
commit `716598d620`.

Den exakta svenska katalogen efter uppdateringen är
`../web.sv-20261103-relay-linking.ts` med SHA-256
`61fbb209c1176ec7901d37ddadd5dace2aa801019490d6385e714c098cc69f88`.
Typkontroll, hela testsviten (71 testfiler, 477 tester), skrivregler och
Gitleaks passerade. ESLint har en befintlig varning i den oförändrade
inläsningseffekten om synkron state-uppdatering, men inga fel.

## Profilbyggare, uppdaterad 2026-11-03

Profilbyggarens kompletta statiska arbetsflöde är katalogiserat och översatt:
identitet, modellval, skills, skillkatalog, MCP-servrar, granskningssteg,
validering, status och navigering. Modellnamn, skillnamn, servernamn,
kommandon, URL:er och dynamiska serversvar lämnas oförändrade. Ändringen är
pushad till [PR #148618](https://github.com/NousResearch/hermes-agent/pull/148618)
i commit `37dcde8411`.

Den exakta svenska katalogen är `../web.sv-20261103-profile-builder.ts` med
SHA-256 `4c7c1165ea3f92de5b53b73a22b8efe57df55332c398755ee75cc8e275219972`.
Typkontroll, ESLint, hela testsviten (71 testfiler, 477 tester), skrivregler
och Gitleaks passerade.

## Skills: katalog och säkerhetsgranskning, uppdaterad 2026-11-03

Den externa färdighetskatalogens statiska gränssnitt är nu katalogiserat och
översatt: sökning, uppdatering, körlogg, anslutna kataloger, träffar,
förhandsvisning, installation och säkerhetsgranskning. Katalogernas
färdighetsbeskrivningar, taggar, källnamn, diagnostik och skanningsfynd är
server- eller källstyrda data och lämnas därför oförändrade. Ändringen är
pushad till [PR #148618](https://github.com/NousResearch/hermes-agent/pull/148618)
i commit `f351820362`.

Den exakta svenska katalogen efter denna uppdatering är
`../web.sv-20261103-skills-hub.ts` med SHA-256
`fd5974a71d0a9277f06a7480a0783f3a0b2086461f5f2523aeb815e1230032b0`.
Typkontroll, hela testsviten (71 testfiler, 477 tester), skrivregler och
Gitleaks passerade. ESLint har fortfarande en befintlig varning i
Skills-sidans oförändrade förhandsgranskningskod om synkron state-uppdatering
i en effekt, men inga fel.

## Typkontroll 2026-10-30

Den första TUI-typkontrollen hittade en gammal import av `Translations`; den
är rättad till `./types.js`. Därefter visar kontrollen tre verkliga
strukturavvikelser i katalogen: faktureringsblocket `autoReload` har blivit ett
underobjekt, abonnemangstexterna har flyttats till underblock och
hjälpkommandona ligger nu under `help.commands`. Katalogen ska därför inte
skickas in förrän den har synkats mot den aktuella engelska katalogstrukturen.

Webbkatalogen är däremot kompatibel med den aktuella koden: `npm run
typecheck --prefix web` passerar och `npm run test --prefix web` passerar med
69 testfiler och 473 tester. Vites och jsdoms kända miljövarningar om
`localStorage`, `window.open()` och canvas förekommer i testutskriften men
testsviten godkändes. Detta bevisar typ- och testkompatibilitet, inte att
webbens svenska text är radgranskad eller uppströmsinskickad.

## Statisk YAML-paritet 2026-10-30

En rekursiv jämförelse mot aktuell `locales/en.yaml` ger 3 510 engelska
bladnycklar och 371 svenska. 3 140 engelska nycklar saknas; den enda extra
svenska nyckeln är `gateway.status.free_tier`. Den statiska katalogen är
alltså en äldre partiell katalog, inte ett säkert underlag för inkrementell
insändning. Den behöver skapas om från den aktuella nyckelstrukturen och
granskas i hanterbara batcher.
