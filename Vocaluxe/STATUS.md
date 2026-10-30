# Vocaluxe: svensk översättning

2026-10-26: Huvudresursen på utvecklingsgrenen innehöll 403 engelska och 304 svenska strängar. Ett lokalt utkast lägger till de 99 saknade strängarna utan att ändra de tidigare 304. Källor: `Output/Languages/en.xml` och `sv.xml`, utvecklingsrevision 336d08040ee31312acb13d860b5cbbd7aef10d8d. Utkastet är inte skickat till Transifex. Projektets tidigare länk till Transifex gav 404; en aktuell översättningslänk behöver verifieras. Partylägen och webbappen har separata resurser som ännu inte har granskats.

Den officiella versionskandidaten 0.5.0.rc publicerades 2024-12-01 och faller inom 48 månader. Senaste stabila versionen 0.4.1 publicerades 2020-03-10; en nattversion från 2026-10-26 finns också. Källor: https://github.com/Vocaluxe/Vocaluxe/releases och https://www.vocaluxe.org/.

Kontroller av de 99 tilläggen: alla nycklar finns och platshållarna `%s`, `%d` och `{0}` med flera matchar källan. L10n-lint och svlang gav inga fynd; Hunspell markerade tekniska namn och sammansättningar. XML-filen har inte testats i programmet. Före inskick behövs jämförelse med aktuella strängar i Transifex och fortsatt språk- och kontextgranskning.

2026-10-26: [Partnerbyte](partylagen/partnerswap-sv-utkast.xml) har ett utkast för samtliga 39 strängar; i [Challenge](partylagen/challenge-sv-utkast.xml) har två saknade strängar lagts till i den befintliga svenska filen. Källan är utvecklingsgrenens filer från revision 336d08040ee31312acb13d860b5cbbd7aef10d8d. Nycklar och platshållare jämfördes mot engelskan. L10n-lint och svlang gav inga fynd; Hunspell markerade förkortningen ”Plac.” och symbolen Ø. Filerna är inte inskickade eller testade i programmet. Övriga partylägen och webbappen återstod vid detta steg, liksom jämförelse med eventuell aktuell Transifex-data.

2026-10-26: Utkast för [lagöverlevnad](partylagen/teamsurvival-sv-utkast.xml) (33 strängar) och [utslagningsturnering](partylagen/tournament-sv-utkast.xml) (28 strängar) har skapats, och [luffarschack](partylagen/tictactoe-sv-utkast.xml) har kompletterats med två strängar. Engelska nycklar och platshållare har jämförts. L10n-lint och svlang gav inga fynd; Hunspell markerade tangenten Esc. Utkasten är inte inskickade eller testade i programmet. Regelroulette och webbappen återstår, liksom verifiering mot eventuell aktuell Transifex-data.

2026-10-26: [Regelroulette](partylagen/ruleroulette-sv-utkast.xml) har ett svenskt utkast för alla 81 strängar. Källnycklar och platshållare matchar engelskan. L10n-lint och svlang gav inga fynd; Hunspell markerade namn, en förkortning och sammansättningar. Utkastet är inte inskickat eller testat i programmet. Alla sex partylägen har nu utkast eller kompletteringar; webbappen återstår. Samtliga filer behöver jämföras med eventuell aktuell Transifex-data och granskas i sammanhang före inskick.

2026-10-26: Webbappens [första utkast](webbapp/sv-utkast-del1.json) omfattar 68 av 225 strängar för administration, inloggning och gemensamma kontroller. Det är en partiell fil, inte en färdig språkfil. Platshållare jämfördes per nyckel; l10n-lint och svlang gav inga fynd. Hunspell markerade projektnamn, filnamn, platshållare och sammansättningen ”köspellistan”. De övriga 157 strängarna, sammanhangskontroll och inskick återstår.

2026-10-26: [Andra webbappsutkastet](webbapp/sv-utkast-del2.json) innehåller 84 ytterligare strängar för navigering, profiler, spellistor och köhantering. Tillsammans med första delen täcks 152 av 225 strängar; 73 återstår. Platshållare jämfördes per nyckel; l10n-lint och svlang gav inga fynd. Hunspell markerade projektnamn, platshållare och sammansättningen ”låtmeny”. Ingen inskickning eller programtest har gjorts.

2026-10-26: [Komplett webbappsutkast](webbapp/sv-utkast-full.json) omfattar samtliga 225 källnycklar; den [tredje delen](webbapp/sv-utkast-del3.json) tillförde 73 strängar. Platshållare och antalet pluralvarianter har jämförts per nyckel. L10n-lint och svlang gav inga fynd; Hunspell markerade projektnamn, tangenter, platshållare och sammansättningar. Hela filen behöver fortfarande granskas i sammanhang, jämföras med aktuell Transifex-data och testas i webbappen; inget har skickats in.

2026-10-26: Webbappens `src/i18n/index.ts` upptäcker `src/locales/sv.json` automatiskt och väljer `sv` för en svensk webbläsare. En lokal kopia av utkastet placerades där i utvecklingsrevision 336d08040ee31312acb13d860b5cbbd7aef10d8d. `npm ci --ignore-scripts` och `npm run build` lyckades. Ett separat test med projektets vue-i18n tolkade samtliga 225 svenska meddelanden och provade pluralformer utan undantag. Detta verifierar byggning och meddelandeformat, inte faktisk visning, anslutning till spelets server eller språklig slutgranskning. Filen är fortfarande inte inskickad.

2026-10-26: Det aktuella projektet finns på https://app.transifex.com/darkice/vocaluxe/. Den svenska webbappens JSON-fil och turneringens XML-fil har laddats upp. Transifex visar efteråt 100 % översatt för båda resurserna (225 respektive 28 strängar), men 0 % granskade enligt Transifex egen granskningsstatus. Den lokala webbappens svenska inloggningssida visades även i webbläsare utan anslutning till spelservern. Huvudfilen och övriga fem partylägen återstår att jämföra med aktuella Transifex-översättningar och skicka in; de tidigare statusraderna beskriver läget vid respektive arbetssteg.

2026-10-26: PartnerSwap, TeamSurvival och RuleRoulette hade inga svenska översättningar i Transifex före importen. Deras respektive svenska XML-filer har laddats upp, och Transifex visar därefter 100 % översatt för vardera resursen (39, 33 respektive 81 strängar), men 0 % granskad. Huvudfilen, Challenge och TicTacToe återstår att jämföra med de befintliga översättningarna i Transifex och komplettera.

2026-10-26: Aktuella svenska filer laddades ner från Transifex och jämfördes nyckel för nyckel med utkasten. Challenge hade 30 befintliga och två saknade strängar; TicTacToe hade 32 befintliga och två saknade. Samtliga befintliga strängar var identiska med utkasten. Efter uppladdning visar Transifex 100 % översatt för båda. Huvudfilen hade 304 befintliga och 99 saknade strängar, också utan skillnader i de befintliga. Efter uppladdning visar Transifex även huvudfilen som 100 % översatt, 0 % granskad.

2026-10-27: Transifex projektöversikt visar nu svenska med 0 strängar att översätta och 875 strängar att granska. Det bekräftar att samtliga aktuella resurser har svenska översättningar. Resursvyn fastnade i laddning vid kontrollen, så de sju lokala kvalitetsrättningarna i `sv-huvudfil-kvalitetsfix-20261027.delta.xml` har inte jämförts mot aktuell måltext eller laddats upp på nytt.

2026-10-27: Huvudresursen `Game` kunde därefter öppnas i Transifex-redigeraren. Samtliga sju deltaenheter skiljer sig fortfarande från måltexten: `Low` = `Lågt`, `Medium` = `Mellan`, `High` = `Högt`, `Tags` = `Tagger`, `No tags` = `Inga tagger`, `Date added` = `Tillagd datum` och sökhjälpen använder både `t ex.` och `tagger`. Deltats `Låg`, `Medel`, `Hög`, `Etiketter`, `Inga etiketter`, `Datum tillagt` och `t.ex.` är därför fortfarande aktuella. Inga ändringar har sparats i Transifex efter denna jämförelse.

2026-10-27: Deltat validerades på nytt före eventuell publicering. XML är välformat och l10n-lint rapporterar inga fel. svlang rapporterar enbart en längdvarning eftersom det analyserar XML-märkningen som löptext samt sällsynta XML-attribut och fackord. Hunspell markerar de avsiktliga sökprefixen `fi` och `fo` samt det korrekta sammansatta ordet `mappnamn`, som inte ingår i ordlistan. Övriga måltermer följer översättningsminnet: `Låg`, `Medel`, `Hög` och `etikett`.

2026-10-27: Tio tydliga språkfel i felrapporteringsdialogen har isolerats i `sv-huvudfil-rapportdialog-20261027.delta.xml`. Rättningarna bevarar de två `\r\n`-brytningarna per sträng och ger en sammanhängande du-form. XML, nycklar, radbrytningar, l10n-lint och en avgränsad Gitleaks-kontroll passerar. Hunspell markerar endast projektnamnet Vocaluxe. svlang ger två falska V2-varningar för uppmaningarna ”Ladda upp …”, men inget faktiskt ordföljdsfel. Filen är ännu inte sparad i Transifex.

2026-10-28: Två av huvudfilens kvalitetsrättningar har sparats och lästs tillbaka från Transifex-resursen `Game`: `Low` = `Låg` och `Medium` = `Medel`. Transifex visar kontot `yeager` som sparare för båda. Resterande fem poster i kvalitetsdeltat och de tio i rapportdialogdeltat är inte inskickade i detta steg. Sökning efter den arkiverade posten `High` gav ingen träff i den aktuella resursen och kräver ny jämförelse med den synkade källan innan ändring.

2026-10-28: Tre ytterligare kvalitetsrättningar har jämförts mot den aktuella
`Game`-resursen, sparats och återlästs från Transifex med kontot `yeager`:
`Tags` = `Etiketter`, `No Tags` = `Inga etiketter` och sökhjälpen för
artist-/titelsökning. I sökhjälpen bevaras samtliga sökprefix, intervallet
`1980-1989` och specialtecknen; bara `t.ex.` och `etiketter` rättades.
Kvalitetsdeltat har nu endast den saknade `High`-posten kvar. De tio
rättningarna för felrapporteringsdialogen är fortfarande lokala och osparade.

2026-10-28: En första dialogrättning har sparats och återlästs från
Transifex med kontot `yeager`: `The link to your report:` = `Länken till din
rapport:`. Kolon och singularisdu bevaras. Nio dialogrättningar återstår.

2026-10-28: Fyra ytterligare dialogrättningar har sparats och återlästs från
Transifex med kontot `yeager`: `Error uploading the log.` = `Det gick inte
att ladda upp loggen.`, `Last error` = `Senaste felet` och `Not available` =
`Inte tillgängligt`. Dessutom har valet att inte ladda upp något sparats med
den granskat naturliga formuleringen `Ladda inte upp något (du kan fortfarande
kopiera felmeddelandet ovan)`. Fem dialogrättningar återstår.

2026-10-28: Alternativet för att ladda upp och skapa ett GitHub-ärende har
sparats och återlästs från Transifex med kontot `yeager`. QA-kontrollen
rapporterade först en saknad vänsterparentes; måltexten och arkivdeltat har
justerats så att de nu bevarar både parenteserna och GitHub-kontokravet:
`Ladda upp och skapa ett ärende (ärendet blir offentligt synligt och det krävs
ett GitHub-konto)`. Fyra dialogrättningar återstår.

2026-10-28: Alternativet för att ladda upp en offentlig rapportlänk har
sparats och återlästs från Transifex med kontot `yeager`:
`Ladda upp och få en länk till din rapport (synlig offentligt)`. Båda
parenteserna bevaras och Transifex visade ingen QA-varning. Tre
dialogrättningar återstod vid detta steg.

2026-10-28: De tre återstående dialogrättningarna har sparats och återlästs
från Transifex med kontot `yeager`: båda flerradiga felrapporterna och
ärendemallen. De bokstavliga radbrytningstecknen `\\r\\n` respektive `\\n`
bevaras exakt, och mallen behåller platshållarna `{0}` och `{1}`. Därmed är
samtliga tio arkiverade dialogrättningar inskickade och verifierade i
huvudresursen. Endast den arkiverade `High`-posten återstår; den saknas i den
aktuella synkade källan och ska inte läggas till utan ny källjämförelse.

2026-10-28: Den lokala uppdateringen av Vocaluxes utvecklingsgren visar att
`TR_CONFIG_TEXTURE_HIGH` fortfarande finns i `Output/Languages/en.xml`.
Strängen hittades därefter i Transifex-resursen `Game`, rättades från `Högt`
till `Hög` och återlästes med kontot `yeager`. Alla sex kvalitetsposter och
samtliga tio dialogrättningar i de arkiverade deltorna är därmed inskickade
och verifierade. Upstreamexport och programkörning återstår.

2026-10-28: Transifex-projektets aktuella översikt visar åter 0 svenska
strängar att översätta och 875 att granska. Den lokala utvecklingsgrenen låg
en commit efter `origin/develop`; den nya commiten gäller enbart ljudloopar,
ljudfiler och eftertexter och ändrar inga lokaliseringsfiler. Arbetskopian
uppdaterades därför inte, eftersom den har en befintlig oinscheckad svensk
webbfil. Ingen lokal programkörning kan göras i den här miljön: `dotnet`,
`mono` och `wine` saknas.

2026-10-29: Den lokala svenska webbfilen `WebApp/src/locales/sv.json` har
kontrollerats på nytt mot engelska `en.json`: båda har 225 nycklar, utan
saknade, extra eller tomma svenska värden. JSON kan tolkas av Node.js utan
fel. Vid just detta kontrollsteg kördes inget nytt webbygge, eftersom
`WebApp/node_modules` saknas; beroenden installerades inte enbart för denna
kontroll. Detta är en katalogkontroll, inte en ersättning för programkörning
eller Transifex-granskning.

2026-10-29: Webbappens låsfil användes för ett reproducerbart bygge med
`npm ci --ignore-scripts` och `npm run build`. `vue-tsc --noEmit` och Vites
produktionsbygge passerade, med den oinscheckade svenska katalogen
`WebApp/src/locales/sv.json` i trädet. Byggningen verifierar att katalogen
kan typkontrolleras och paketeras i webbappen, men ersätter inte en
runtimekontroll mot spelets server eller Transifex-granskning.

2026-10-29: En ny kontroll av `origin/develop` visar att Vocaluxe nu har
synkat de svenska katalogerna till källträdet. Commit `22ad04e` innehåller
huvudkatalogens svenska kompletteringar och kvalitetsrättningar, medan
`ff291ad` innehåller webbappens svenska katalog. Den aktuella grenen har 403
av 403 XML-nycklar och 225 av 225 JSON-nycklar på svenska, med exakt samma
nyckelmängder och platshållare som engelskan. XML-syntaxen samt
`git diff --check` för de svenska filerna passerar. Den lokala, oinscheckade
webbfilen lämnades orörd. Programkörning i den här miljön återstår, eftersom
`dotnet`, `mono` och `wine` saknas.

2026-10-30: Transifex REST API bekräftar den aktuella offentliga platsen
`darkice/vocaluxe`. Alla åtta svenska resurser är kompletta och inga nya
översättningar behöver laddas upp: Game 403/403, webbappen 225/225, de fem
XML-resurserna 32/32, 34/34, 81/81, 33/33 och 39/39 samt Challenge 28/28.
Samtliga har 0 oöversatta strängar. Resursnamnen innehåller flera identiska
XML-etiketter, så kontrollen baseras på deras stabila Transifex-resurs-ID:n
och inte bara på visningsnamnen. Projektet är inte arkiverat; dess senaste
uppströmsaktivitet är aktuell enligt Transifex och GitHub.
