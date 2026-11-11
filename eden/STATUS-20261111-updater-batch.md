# Eden Qt: uppdaterarens svenska dialoger

Datum: 11 november 2026

## Underlag och omfattning

Den aktuella källan är `eden-emu/eden` vid revision
`cf654052c416f9e7c80cef0a7d321476b1c52f99` från 10 november 2026.
Eden är därmed aktivt underhållet. Den svenska Qt-katalogen innehöll 2 128
meddelanden och 17 oavslutade måltexter, samtliga i `UpdateDialog`.

Batchen i `eden-qt-sv-reviewed-20261111.ts` översätter dem rad för rad. Den
omfattar kontrollsummefel, mellanlagringskatalog, extrahering, uppdaterarens
körbara fil, avbruten hämtning och URL-fel. Qt-platsmarkörerna `%1` till `%4`
och radbrytningarna är bevarade.

Terminologin följer den omgivande Eden-katalogen: **uppdatering**,
**extrahera**, **mellanlagringskatalog**, **cachekatalog** och **hämta**.
Engelska produktnamn och format lämnas oförändrade när de är synliga i
gränssnittet.

## Lokala kontroller

- `lrelease` passerar: 2 134 färdiga och 0 oavslutade meddelanden i den
  lokala granskningskopian.
- `l10n-lint` har inga fynd i den ändrade `UpdateDialog`-batchen. En separat
  körning på hela katalogen rapporterar ett befintligt varningsfynd för
  språknamnet `Polska (polska)` och informationsfynd utanför batchen.
- Hunspell-SV med projektets svenska ordlista ger inga träffar för batchens
  svenska prosa.
- `svlang` på hela Qt-filen ger omfattande befintliga träffar för HTML,
  tekniska namn och hela katalogens äldre texter. Batchens formuleringar har
  kontrollerats manuellt i sin dialogkontext.
- `git diff --check` passerar.
- Gitleaks på den ändrade katalogfilen passerar utan fynd.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande
  formatkontroll.

## Arkivering och upstream

Batchen är arkiverad och skickades i Transifex-redigeraren för resursen
`edenemu / eden-emulator / Qt Translations`. Nio dialogposter sparades
individuellt med användaren `yeager`; sparandet kontrollerades genom att
filtret för oöversatta poster sjönk från 17 till 8.

De åtta återstående poster som Transifex visar som oöversatta är inte delar
av `UpdateDialog`-batchen. De har redan synliga svenska måltexter, bland annat
`Om Eden`, `Kommunicerar med servern…` och `Avbryt`, med tidigare
översättningshistorik. De behandlas därför som status- eller
mappningsavvikelser i tjänsten, inte som saknade svenska texter, och har inte
skrivits över.

Batchen är alltså **inskriven i Transifex**, men inte verifierad som
uppströmsgranskad, sammanslagen i Eden-källan eller släppt. Projektets
veckovisa Transifex-synk behöver fortfarande skapa och föra igenom sin
uppströmsändring.
