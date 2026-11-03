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
