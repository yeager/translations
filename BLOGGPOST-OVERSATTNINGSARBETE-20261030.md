# Sex månader av svensk översättning: från enstaka strängar till ett eget arbetsflöde

Översättning av fri programvara ser ofta enkel ut på håll. En text på engelska
får en svensk motsvarighet, någon trycker på spara och arbetet är klart. I
praktiken är det närmare produktutveckling än korrekturläsning. Varje sträng
har en plats i ett gränssnitt, en teknisk funktion och ett sammanhang som måste
fungera även när programmet växer, koden ändras och översättningen går genom
olika plattformar.

Under de senaste sex månaderna har vi arbetat med svenska översättningar i en
mycket bred flora av fria projekt: skrivbordsmiljöer, utvecklarverktyg,
emulatorer, spel, nätverkstjänster, ekonomi- och administrationsprogram,
mediaspelare och mobilappar. Vårt arkiv innehåller nu underlag från fler än 400
projektområden. Det är inte en lista över lika många färdiga publiceringar. Det
är en redovisning av granskat material, kataloger, förslag, statusrapporter och
uppföljningar som gör arbetet möjligt att återvända till.

Det viktiga är just uppföljningen. En lokal, kontrollerad katalog är inte samma
sak som en inskickad Weblate-ändring. Ett förslag i Crowdin eller Transifex är
inte automatiskt godkänt. En öppen pull request är inte mergad kod. Därför
skiljer vi i arkivet på färdigt underlag, inskickat arbete, arbete som väntar på
granskning och ändringar som faktiskt har tagits emot uppströms.

## Från stor katalog till fungerande svensk text

En del resultat går att beskriva med siffror. Skyrim Community Shaders fick en
heltäckande svensk katalog med 4 238 av 4 238 nycklar. Den avgränsade
ändringen skickades som pull request och slogs ihop den 29 oktober. NX2Apple
fick 616 av 616 svenska poster i sina Swift- och Qt-kataloger; även den
ändringen är mergad. Eden Emulator hade sex kvarvarande Qt-strängar om
fuskkoder. De översattes och kontrollerades via Transifex API, vilket gav 1 943
av 1 943 översatta strängar i den berörda resursen.

Andra projekt är nästan lika viktiga just därför att de inte är klara ännu.
Ghostty har en svensk PO-katalog med 253 poster och en registrerad svensk lokal.
Syntax, källsynkronisering och språkgranskning är kontrollerade, men pull
requesten väntar fortfarande på mänsklig granskning och merge. Cacti visar en
annan typ av hinder: den svenska Core-komponenten är låst i översättningssystemet
eftersom systemet inte kan pusha sitt arkiv. Där finns validerade rättningar och
en gemensam terminologi, men de ska inte påstås vara publicerade förrän låset är
hävt och aktuell källtext har jämförts på nytt.

Det här är mindre dramatiskt än att säga att allt är klart, men det är den
väsentliga skillnaden mellan ett seriöst översättningsarbete och en rad text som
bara ser färdig ut i en exportfil.

## Språkgranskning är mer än stavningskontroll

Svenska gränssnittstexter behöver vara begripliga utan att tappa teknisk
precision. Därför läses källtext och måltext tillsammans. Är *split* en
kontodelning, en delpost eller en uppdelning i just den här ekonomivyn? Är en
*poller* en datainsamlare när den samlar in mätvärden? När en graf skapas genom
att slå ihop data är *grafaggregation* tydligare än ett ord som låter som en
färdig grafkomponent.

Vi bygger därför terminologi där den behövs och granskar varje ändring med flera
olika verktyg. `l10n-lint` fångar format- och lokaliseringsfel, `svlang`
kontrollerar svenska skrivregler och Hunspell hjälper till att hitta ord som
behöver mänsklig bedömning. Dessutom jämförs platshållare, pluralformer,
HTML/Markdown, snabbkommandon och filformat med källan. En korrekt svensk
mening får inte råka förstöra `%s`, `{0}`, XML-taggar eller en Qt-accelerator.

Verktygen ersätter inte omdöme. De gör däremot den manuella granskningen skarpare.
En varning om ett oförändrat ord kan vara ett verkligt fel, ett produktnamn eller
en avsiktligt engelsk teknisk term. En misstänkt sammansättning behöver kontrolleras
i sin användningsmiljö. Språkvård handlar därför lika mycket om att avfärda
felaktiga varningar med dokumenterad motivering som om att rätta text.

## Ett arbete som spänner över flera vägar uppströms

De tekniska vägarna är olika från projekt till projekt. I vissa fall går
ändringarna via en vanlig GitHub-pull request. I andra fall används Weblate,
Crowdin eller Transifex. Ibland finns ett fristående språkpaket. Ibland måste
själva projektet först få stöd för flera språk, med en stabil engelsk
återfallstext och kataloger som andra språk kan läggas till i utan att bygga om
gränssnittet.

Det innebär också att det breda översättningsarbetet inte bara består av att
fylla i tomma rutor. Det handlar om att förstå hur en katalog genereras, om en
fil ska delas före import, om en plattform tar emot identiska käll- och
måltexter och om en ny release fortfarande är relevant att arbeta mot. För
varje projekt kontrolleras även om den senaste releasen är tillräckligt aktuell
för att översättningsinsatsen ska ha god chans att nå användarna.

GitHubs sökning visar dessutom att kontot har öppnat 454 pull requests sedan
början av maj. Siffran omfattar fler typer av arbete än översättning, men den
ger en bild av hur ofta språkförbättringar behöver samspela med kod, tester,
automatiska kontroller och underhållares beslut.

## Arkivet är en del av kvaliteten

Det kanske mest bestående resultatet är inte en enskild svensk knapptext utan
spårbarheten. I arkivet finns den katalog som granskades, de små deltas som är
säkra att importera, testresultat, källhänvisningar, terminologibeslut och en
ärlig status för nästa steg. Det gör att ett projekt kan tas upp igen när en
plattform låser upp, en ny version släpps eller en underhållare frågar varför
en viss svensk formulering valdes.

Det är också ett sätt att göra ett stort arbete hanterbart. Stora filer delas
upp i mindre häften före uppladdning. Återkommande begrepp får samma svenska
form i relaterade komponenter. Kontrollresultat sparas tillsammans med
förändringen i stället för att försvinna i ett chattfönster. När en förbättring
är mergad markeras det; när den väntar på granskning står det också.

Svensk lokalisering är i slutändan inte ett sidospår till programvaran. Den är
det som gör att en person kan förstå ett felmeddelande, välja rätt inställning,
läsa en säkerhetsvarning och använda ett program på sitt eget språk utan att
behöva växla mentalt till engelska. Det har varit målet under dessa månader:
inte bara fler översatta strängar, utan fler svenska gränssnitt som faktiskt
känns skrivna för den som använder dem.

---

*Faktaunderlag: projektarkivet den 30 oktober 2026, dess Git-historik och
verifierad upstreamstatus i respektive projekt. Se även
[projektregistret](PROJECTS-TOUCHED-20261030.md) och
[statusjournalen](STATUS.md).*
