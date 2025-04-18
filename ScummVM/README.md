# [ScummVM LÄSMIG](https://www.scummvm.org/) - [![CI](https://github.com/scummvm/scummvm/actions/workflows/ci.yml/badge.svg)](https://github.com/scummvm/scummvm/actions/workflows/ci.yml) [![Översättningsstatus](https://translations.scummvm.org/widgets/scummvm/-/scummvm/svg-badge.svg)](https://translations.scummvm.org/engage/scummvm/?utm_source=widget) [![PRs välkomna](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md#pull-requests) [![Codacy Badge](https://app.codacy.com/project/badge/Grade/e06e5b18f8464fef859b5a7f78d10357)](https://www.codacy.com/gh/scummvm/scummvm/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=scummvm/scummvm&amp;utm_campaign=Badge_Grade)



## Om ScummVM



Med ScummVM kan du spela klassiska grafiska peka-och-klicka-äventyrsspel, textäventyrsspel och rollspel, så länge du redan har speldatafilerna. ScummVM ersätter de körbara filer som levereras med spelen, vilket innebär att du nu kan spela dina favoritspel på alla dina favoritenheter.



Så hur fick ScummVM sitt namn? Många av de berömda LucasArts-äventyrsspelen, som Maniac Mansion och Monkey Island-serien, skapades med hjälp av ett verktyg som heter SCUMM (Script Creation Utility for Maniac Mansion). ”VM” i ScummVM står för Virtual Machine (virtuell maskin).



ScummVM var ursprungligen utformat för att köra LucasArts SCUMM-spel, men med tiden har stöd lagts till för många andra spel: se hela listan [på vår wiki](https://wiki.scummvm.org/index.php?title=Category:Supported_Games). Anmärkningsvärda titlar inkluderar Broken Sword, Myst och Blade Runner, även om det finns otaliga andra dolda pärlor att utforska.



För mer information, kompatibilitetslistor, detaljer om donationer, senaste versionen, lägesrapporter och mycket mer, besök ScummVM:s [webbsida](https://www.scummvm.org/).



## Snabbstart



För de otåliga bland er, här är hur man får igång ScummVM i fem enkla steg.



1. Hämta ner ScummVM från [vår webbplats](https://www.scummvm.org/downloads/) och installera det.



2. Skapa en katalog på din hårddisk och kopiera speldatafilerna från originalmediet till den här katalogen. Upprepa detta för varje spel du vill spela.



3. Starta ScummVM, välj ”Lägg till spel”, välj den katalog som innehåller spelets datafiler (försök inte att välja själva datafilerna!) och tryck på Välj.



4. Dialogrutan Spelalternativ öppnas för att möjliggöra konfiguration av olika inställningar för spelet. Dessa kan konfigureras om när som helst, men för närvarande bör allt vara OK med standardinställningarna.



5. Välj det spel du vill spela i listan och tryck på Starta. Om du vill spela ett spel nästa gång hoppar du till steg 5, såvida du inte vill lägga till fler spel.



>

> > Tips:

>

> Om du vill lägga till flera spel på en gång håller du ned shift-tangenten och klickar sedan på ”Lägg till spel” - etiketten ändras till ”Lägg till flera” och om du trycker på den ombeds du igen att välja en katalog, men den här gången söker ScummVM igenom alla underkataloger rekursivt efter spel som stöds.







## Rapportera en bugg



För att rapportera en bugg, gå till ScummVM [Issue Tracker] (https://bugs.scummvm.org/) och logga in med ditt GitHub-konto.



Kontrollera att felet är reproducerbart och fortfarande förekommer i den senaste git/[Daily build](https://buildbot.scummvm.org/#/dailybuilds)-versionen. Kontrollera även [kompatibilitetslistan](https://www.scummvm.org/compatibility/) för det spelet för att säkerställa att problemet inte redan är känt. Rapportera inte buggar för spel som inte är listade som spelbara på wikisidan [Spel som stöds](https://wiki.scummvm.org/index.php?title=Category:Supported_Games) eller på kompatibilitetslistan. Vi vet redan att dessa spel har buggar!



Inkludera följande information i buggrapporten:



- ScummVM-version (testa den senaste git/[Daily build](https://buildbot.scummvm.org/#/dailybuilds))

- Detaljer om buggen, inklusive instruktioner för hur du återskapar buggen. Om möjligt, inkludera loggfiler, skärmdumpar och annan relevant information.

- Spelets språk

- Spelversion (t.ex. talkie eller floppy)

- Plattform och kompilator (t.ex. Win32, Linux eller FreeBSD)

- Ett bifogat sparat spel, om möjligt.

- Om felet har uppstått nyligen, bifoga den senaste versionen utan felet och den första versionen med felet. På så sätt kan vi åtgärda det snabbare genom att titta på de ändringar som gjorts.



Slutligen, rapportera varje problem separat; skicka inte in flera problem på samma ärende. Det är svårt att spåra statusen för varje enskild bugg när de inte finns på sina egna ärenden.



## Dokumentation



### Användardokumentation



För allt du behöver veta om hur du använder ScummVM, se vår [användardokumentation] (https://docs.scummvm.org/).



### ScummVM:s wiki



[The wiki](https://wiki.scummvm.org/) är platsen för information om alla spel som stöds av ScummVM. Om du är utvecklare finns det också en del mycket praktisk information i avsnittet Developer (Utvecklare).



### Ändringslogg



Vår omfattande ändringslogg finns tillgänglig [här](NEWS.md).



## SAST-verktyg



[PVS-Studio](https://pvs-studio.com/en/pvs-studio/?utm_source=github&utm_medium=organic&utm_campaign=open_source) - statisk analysator för C-, C++-, C#- och Java-kod.



## Tack till



Ett stort tack till hela teamet för att ha gjort ScummVM-projektet möjligt. Se alla medverkande [här](AUTHORS)!



-----



> Lycka till och hoppas på trevliga äventyr\!

> ScummVM-teamet.

> <https://www.scummvm.org/>
