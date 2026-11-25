# Svenska GNOME-termer

Denna lista används vid den lokala radgranskningen i `GNOME-granskning`.
Den följer etablerat svenskt GNOME-språk: korta, tydliga imperativ i menyer
och naturliga svenska i hjälptexter. Källtext och sammanhang avgör alltid;
listan är stöd, inte en ursäkt för mekanisk ersättning.

## Gränssnitt och åtgärder

| Engelska | Rekommenderad svenska | Anmärkning |
|---|---|---|
| Open | Öppna | Menyåtgärd. |
| Open Folder | Öppna mapp | Använd inte *folder* i svensk UI-text. |
| Save | Spara | |
| Save As | Spara som | |
| Close | Stäng | |
| Cancel | Avbryt | |
| Apply | Verkställ | *Tillämpa* bara när något faktiskt tillämpas. |
| Delete | Ta bort | *Radera* endast där det är etablerat i kontexten. |
| Remove | Ta bort | |
| Rename | Byt namn | |
| Edit | Redigera | |
| Preferences | Inställningar | I appmeny och dialogrubrik. |
| Settings | Inställningar | Bevara produktnamnet **Inställningar** där det avses. |
| Properties | Egenskaper | |
| Details | Detaljer | |
| Search | Sök | |
| Select All | Markera alla | |
| Help | Hjälp | |
| About | Om | |
| Quit | Avsluta | |
| Back / Forward | Bakåt / Framåt | |
| Enable / Disable | Aktivera / Inaktivera | |
| Default | Standard | |

## Filer, mappar och data

| Engelska | Rekommenderad svenska | Anmärkning |
|---|---|---|
| file | fil | |
| folder / directory | mapp | Använd *katalog* i teknisk eller filsystemsorienterad text. |
| path | sökväg | |
| filename | filnamn | |
| location | plats | |
| trash | papperskorg | |
| backup | säkerhetskopia | Verb: *säkerhetskopiera*. |
| restore | återställ | |
| import / export | importera / exportera | |
| clipboard | urklipp | |

## System och teknik

| Engelska | Rekommenderad svenska | Anmärkning |
|---|---|---|
| application / app | program | *App* kan användas i produktnamn eller etablerad mobilkontext. |
| extension | tillägg | |
| plugin | insticksmodul | Använd *tillägg* när GNOME-modulen använder termen extension. |
| update | uppdatering | Verb: *uppdatera*. |
| notification | avisering | |
| permission | behörighet | |
| authentication | autentisering | |
| authorization (polkit) | behörighet | För användarvänd text om att få utföra en åtgärd. |
| action ID (polkit) | åtgärds-ID | I polkits kommandoradssyntax översätts metavariabeln ACTION till ÅTGÄRD. |
| subject (polkit) | subjekt | Polkit-objekt som identifierar användare eller process. |
| process specifier | processangivelse | Används om värdet för --process. |
| account | konto | |
| password | lösenord | |
| network | nätverk | |
| connection | anslutning | |
| proxy | proxy | Oböjligt i korta UI-etiketter. |
| codec | kodek | |
| decoder | avkodare | Avser komponent/funktion, inte nödvändigtvis appnamnet **Decoder**. |
| encoder | kodare | |
| hardware | maskinvara | |
| firmware | fast programvara | Använd *firmware* när det är projektets etablerade tekniska term. |
| sample (pixbuf) | värde | Kanalsampel för en bildpunkt; här avses värdet, inte själva samplingsprocessen. |
| preview | förhandsvisning / förhandsvisa | Substantiv respektive verb; välj efter sammanhang. |
| previewer | förhandsvisare | Komponenten som visar en filförhandsvisning. |
| fullscreen | helskärmsläge | I åtgärder: *Växla helskärmsläge*. |
| rowstride | radsteg | Antal byte mellan motsvarande lägen på efterföljande pixelrader. |
| chunk (bildformat) | block | En avgränsad del av en bildfil, exempelvis PNG-textblock. |
| pixbuf | pixbuf | GTK/GdkPixbuf-API-typ; behåll identifieraren och böj vid behov: *pixbufen*. |
| colorspace | färgrymd | Färgrymd som pixelvärdena tolkas i. |

## Färg och bildbehandling

| Engelska | Rekommenderad svenska | Anmärkning |
|---|---|---|
| color profile | färgprofil | ICC-profil. |
| colorspace / color space | färgrymd | ICC- och bilddata. |
| spot color | dekorfärg | Tryckfärg som anges separat, även vid färgmätning. |
| color gamut | färgomfång | |
| gamut volume | färgomfångsvolym | Volymen i en färgomfångsgraf. |
| whitepoint / white point | vitpunkt | ICC-profiler. |
| luminance | luminans | |
| tone reproduction curve | tonåtergivningskurva | |
| colorimeter | kolorimeter | |

## GIMP och GIMP Help

Använd dessa termer konsekvent i GIMP:s gränssnitt och användarhandbok.
GIMP har etablerade verktygs- och filtertermer; kontrollera sammanhanget och
översätt inte produktnamn eller namn på algoritmer mekaniskt.

| Engelska | Rekommenderad svenska | Anmärkning |
|---|---|---|
| selection | markering | Det markerade bildområdet; använd *markera* för åtgärden. |
| selection tool | markeringsverktyg | Verktyg som skapar eller ändrar en markering. |
| path | bana | GIMP:s Bézierbanor; använd *sökväg* endast för filsystemssökvägar. |
| layer | lager | |
| layer mask | lagermask | |
| channel | kanal | Bildkanal eller alfakanal enligt sammanhang. |
| brush | pensel | Verktyg eller penselform. |
| paintbrush tool | målarpensel | GIMP-verktyget; skilj från penselresursen. |
| gradient | toning | GIMP:s färgövergång; använd *toningsverktyg* för verktygsnamnet. |
| gradient map | toningskarta | Filter/funktion som mappar toningar till färger. |
| bucket (histogram) | intervall | Värdeintervall som samlar färg- eller bildpunktsvärden; översätt inte med *hink* eller *färgbucket*. |
| bucket size | intervallstorlek | Storleken på varje värdeintervall i histogram-/färgkubsanalys. |
| color value range | färgvärdesintervall | Beskrivande term för ett intervall av grupperade kanalvärden. |
| Blending Options | Blandningsalternativ | GIMP-lager-/filterinställning; översätt inte *blending* med *toning*. |
| chroma range | krominansomfång | GIMP-färgförbättring; skilj från nyans och ljushet. |
| HSV (GIMP UI) | NMI | GIMP:s etablerade svenska beteckning för nyans, mättnad och intensitet; behåll HSV i teknisk förklaring/kod där identifieraren avses. |
| blending options | blandningsalternativ | GIMP:s lager- och filterblandning; inte *toningsalternativ*. |
| hot spot (image map) | aktivt område | Klickbart område i en bildkarta. |
| semi-transparency | halvgenomskinlighet | När ett bildformat simulerar genomskinlighet utan alfakanal. |
| edge-detect filter | kantdetekteringsfilter | Filterkategori. |
| generic filter | allmänt filter | Använd inte *generiskt filter* i användartext. |
| dock (GIMP panel) | docka | En panel som kan dockas; plural *dockor*. Använd *dockning* för själva placeringen. |
| dockable dialog | dockningsbar dialogruta | Dialogruta som kan placeras i en docka. |
| context menu | snabbmeny | Meny med kommandon för den klickade delen av gränssnittet. |
| single-window mode | enfönsterläge | GIMP-läge där dockor och bild visas i ett programfönster. |
| tab bar | flikrad | Raden med flikar för öppna bilder. |
| Desaturate (GIMP command) | Avmätta | Etablerat namn på GIMP-kommandot; använd *mättnad* i löpande text. |
| luminance | luminans | Relativ fysisk luminans; beräknas med linjäriserade RGB-värden. |
| luma | luma | Behåll den tekniska termen för gammakodad luminans; skilj den från *luminans*. |
| lightness | ljushet | HSL/LAB-komponent; skilj från luminans. |
| Value (HSV, GIMP UI) | NMI-intensitet | GIMP:s svenska UI-term för nyans, mättnad och intensitet. |
| sepia toning | sepiatoning | Bildbehandlingseffekt med varm brun ton. |
| Filmstrip (GIMP filter) | Filmremsa | Filter som sammanfogar bilder till en illustration av en fotografisk filmremsa. |
| Depth Merge (GIMP filter) | Djupsammanfogning | Filter som använder djupmappningar för att avgöra vilka delar av bildlager som visas. |
| map (Depth Merge) | mappning | Bild som används som mask för att styra sammanfogningen. |
| gradient (GIMP tool) | toning | Färgövergång som skapas med toningsverktyget; undvik *gradient* i användartext. |
| default browser | standardwebbläsare | Programmet som öppnar webblänkar som standard. |
| procedure browser | procedurbläddrare | GIMP-verktyget för att söka i PDB (Procedurdatabasen). |
| GEGL Filter Browser | GEGL-filterbläddrare | GIMP-verktygets etablerade namn. |
| Plug-In Browser | Bläddrare för insticksmoduler | GIMP-verktygets etablerade namn; *plug-in* översätts med *insticksmodul*. |
| issue tracker | ärendehanteringssystem | Plats för felrapporter och önskemål om nya funktioner. |
| Slur (GIMP filter) | Smeta ut | Filter som smetar ut bildpunkter nedåt. |
| Dulling (GIMP noise option) | dämpning | Styr hur mycket slumpmässigt färgvärde påverkar befintlig färg. |
| speckle noise | fläckbrus | Multiplikativt, korrelerat brus. |
| CIE LCh | CIE LCh | Färgrymdsmodell med ljushet, krominans och nyans; behåll akronymens versaler. |
| opacity | opacitet | Använd *ogenomskinlighet* i förklarande löptext vid behov. |
| feather (selection) | mjuka upp kanter | Åtgärd på en markering; substantivet är *kantutjämning* endast när kontexten avser utjämning. |
| floating selection | flytande markering | GIMP:s särskilda lager-/markeringsläge. |
| foreground / background color | förgrundsfärg / bakgrundsfärg | |
| clone tool | kloningsverktyg | |
| healing tool | läkningsverktyg | Verktyget som korrigerar bildområden med omgivande bilddata. |
| dodge / burn | skugga / efterbelys | GIMP:s verktygsnamn; behåll etablerade UI-etiketter. |
| tone mapping | tonmappning | HDR-/färgbehandling; skilj från *toningskarta*. |
| filter | filter | GIMP-menyn och bildbehandlingsfilter. |
| plug-in | insticksmodul | GIMP:s tillägg som laddas separat. |
| drawable | rityta | GIMP-objekt som kan målas på, exempelvis lager eller kanal. |
| drop shadow | skugga | Script-Fu-inställningen för en skugga bakom/under ett objekt; undvik den onaturliga sammansättningen *skuggkastning*. |
| bevel | avfasning | Avfasad kant eller effekt; använd *avfasning* i menyer och *avfasad* som adjektiv. |
| highlight (effect settings) | högdagerområde | Ljusa bildområden i effektinställningar; skriv hellre *högdagerområdets färg* än täta sammansättningar. |
| stencil | mask | Gråskalemask som begränsar effekt eller karvning; i beskrivande sammanhang kan *schablon* passa. |
| multi-layer image | bild med flera lager | Föredras framför den svårlästa sammansättningen *flerlagersbild*. |
| marching ants | markeringskontur | Beskrivande term för den animerade streckade kanten runt markeringen. |

## Föräldrakontroller och användarkonton

| Engelska | Rekommenderad svenska | Anmärkning |
|---|---|---|
| Parental Controls | Föräldrakontroller | GNOME-appens namn. |
| child user / child account | barnkonto | Föredras framför *barnanvändare*. |
| non-administrator account | konto utan administratörsbehörighet | Tydligt i hjälptext. |
| Control Center (legacy GNOME) | Kontrollcenter | Äldre appnamn; välj inte *Kontrollpanel* i GNOME-dokumentation. |
| Application Suitability | Lämplighet för program | Etikett i föräldrakontrollernas gränssnitt. |
| age rating / age suitability | åldersklassificering / åldersinställning | Välj efter om texten beskriver en klassificering eller användarens inställning. |
| under supervision | under tillsyn | Skriv inte *under översikt*. |

## Profilering (Sysprof)

| Engelska | Rekommenderad svenska | Anmärkning |
|---|---|---|
| profiling | profilering | |
| profiler | profilerare | |
| sampling profiler | stickprovsprofilerare | Sysprof samlar in stickprov av anropsstackar. |
| tracing profiler | spårningsprofilerare | Registrerar varje funktionsanrop. |
| stacktrace | stackspår | Följer GNOME-TM. |
| call graph | anropsgraf | |
| heap | heap | Behåll det tekniska minnesbegreppet och stacketiketten `[heap]`. |
| Context Switch | Context Switch | Bevara det exakta pseudo-ramnamnet som visas i resultat. |

## Kommandoradsmetavariabler

Översätt beskrivande metavariabler i användningsrader och hjälptexter. Behåll
flaggor som `--action-id`, faktiska miljövariabler som `$PATH`, formatmarkörer,
API-/protokollnamn och kodidentifierare oförändrade. Välj term efter vad
argumentet betyder i just det programmet.

| Engelsk metavariabel | Rekommenderad svenska | Anmärkning |
|---|---|---|
| ACTION | ÅTGÄRD | Polkit-åtgärd. |
| ARGUMENTS | ARGUMENT | Svensk plural är också *argument*. |
| BUS_NAME | BUSSNAMN | D-Bus-ägarnamn. |
| CERT | CERTIFIKAT | Certifikatfil/-värde enligt sammanhang. |
| COMMAND | KOMMANDO | |
| DIR | KATALOG | I teknisk kommandoradssyntax; vanlig UI-text kan använda *mapp*. |
| FILE | FIL | |
| FILES | FILER | |
| FILENAME | FILNAMN | |
| INPUT_FILE / INPUT_FILE1 / INPUT_FILE2 | INDATAFIL / INDATAFIL1 / INDATAFIL2 | Bevara indexsiffrorna. |
| MSI_FILE | MSI-FIL | Argumentnamn för en MSI-fil. |
| METAINFO | METADATA | Beskrivande fwupd-argument; inte filnamnet `metainfo.xml`. |
| KEY | NYCKEL | |
| OPTION | FLAGGA | Själva metavariabeln; literal flagga lämnas oförändrad. |
| PATH | SÖKVÄG | Behåll `$PATH`; välj *bana* när det avser en geometrisk bana. |
| PRIVKEY | PRIVATNYCKEL | |
| START_TIME | STARTTID | |
| TIMEOUT | TIDSGRÄNS | |
| VALUE | VÄRDE | |

## Korsord (GNOME Crosswords)

| Engelska | Rekommenderad svenska | Anmärkning |
|---|---|---|
| acrostic | akrostikon | Korsordsvariant som bygger på ett citat. |
| barred crossword | korsord med stoppar | Bevara denna tydliga omskrivning i hjälptexter. |
| clue | ledtråd | |
| cryptic clue / crossword | kryptisk ledtråd / kryptiskt korsord | |
| enumeration | längdangivelse | Visar svarslängd, till exempel `(3,4)`. |
| setter | konstruktör | Personen som skapar korsordet. |
| editor (publication credit) | redaktör | Personen som redigerar korsordet inför publicering; inte en programvaruredigerare. |
| settability | konstruktionssvårighet | Mått på hur svårt korsordet är att konstruera. |
| pangram | pangram | Etablerad term för ett korsord som använder hela alfabetet. |

## Form och skydd

- Bevara `printf`-platshållare, Rust-/Python-variabler, XML/HTML-markup,
  URL:er, kommandon, filnamn och radbrytningar exakt.
- Behåll acceleratormarkören `_` men välj om möjligt inte Å, Ä eller Ö som
  acceleratortangent. Kontrollera också kollisioner i samma meny.
- Översätt inte egennamn, utvecklarnamn, GNOME, GTK, GLib, D-Bus, Wayland,
  PipeWire, Flatpak, AppStream, systemd eller etablerade protokollnamn.
- Använd svenska citattecken ”…” i löpande svensk text. Låt citattecken i
  kommandon och kod vara oförändrade.
- Skriv sammansättningar naturligt: *inställningsdialog*, *filhanterare*,
  *säkerhetskopia*. Undvik engelska nominaliseringar när en enkel svensk
  verbform fungerar bättre.

## Valideringsordning

1. Kontrollera betydelse och kontext mot aktuell källsträng.
2. Jämför platshållare, markup, pluraler, acceleratorer och radbrytningar.
3. Kör filformatkontroll, `l10n-lint` och `hunspell-sv`.
4. Dokumentera ett avsiktligt identiskt egennamn eller tekniskt undantag i
   modulens `README.md`.


## Poddar (GNOME Podcasts)

| Engelska | Rekommenderad svenska | Anmärkning |
|---|---|---|
| podcast | podd / poddsändning | Använd *podd* i korta gränssnittstexter och *poddsändning* där den fulla termen passar bättre. |
| podcast show / show (noun) | podd | GNOME Podcasts använder *show* om en prenumererad podd och dess avsnitt. Översätt inte med *show* eller *show(er)*. |
| feed | flöde | I korta UI-etiketter: *flödes-URL* när det behövs. |
| episode | avsnitt | |
| queue | kö | |
| played / listened | spelad / lyssnad | Anpassa böjningen till det som avsnittet avser. |

## Hjälpmedel och AT-SPI

| Engelska | Rekommenderad svenska | Anmärkning |
|---|---|---|
| accessible object | tillgängligt objekt | Skriv inte bara *den tillgängliga*; avser AT-SPI-objektet. |
| accessible role | tillgänglighetsroll | |
| header / heading | rubrik | Använd inte *huvud* i den här betydelsen. |
| chart | diagram | |
| viewport | visningsområde | |
| combo box | kombinationsruta | |
| list item | listelement | |
| popup menu | snabbmeny | |
| page tab list | lista över sidflikar | |
| document spreadsheet | kalkylarksdokument | Använd parallellt *presentationsdokument*, *textdokument*, *webbdokument* och *e-postdokument*. |
| rating (AT-SPI role) | betyg | |

## GNOME Klotski (hjälpdokumentation)

| Engelska | Rekommenderad svenska | Anmärkning |
|---|---|---|
| move (in the puzzle) | drag | Ett drag i spelet, inte ett steg. |
| move a block | flytta ett block | I instruktioner: *dra blocket* när musgesten beskrivs. |
| header bar | rubrikrad | GNOME-gränssnittets header bar. |
| titlebar | titellist | Fönstrets namnlist i dokumentation och bildtext. |
| patterned block | mönstrat block | Spelets särskilda block. |
| markers | markeringar | De gröna markeringarna som visar målytan. |
| puzzle | pussel | En spelbrädesvariant. |

## Sushi (gränssnitt)

| Engelska | Rekommenderad svenska | Anmärkning |
|---|---|---|
| previewer | förhandsvisare | Komponent/program som visar en filförhandsvisning. |
| preview | förhandsvisning | Substantiv; verbet är *förhandsvisa*. |
| GNOME Files | Filer | GNOME-programmets svenska namn; skriv *Filer (Nautilus)* när äldre namn behövs för identifiering. |
| independent component | fristående komponent | Naturlig svensk formulering i programbeskrivningen. |

## Highscore (emulator)

| Engelska | Rekommenderad svenska | Anmärkning |
|---|---|---|
| gamepad | handkontroll | Används för externa spelkontroller. |
| control (gamepad input) | kontroll / knapp | *Kontroll* är den övergripande inmatningen; *knapp* när en fysisk knapp avses. |
| firmware | fast programvara | |
| boot ROM | start-ROM | Behåll ROM och systemnamn. |
| snapshot | ögonblicksbild | Highscore använder termen för en sparad emulatorsnapshot. |
| save state | sparat tillstånd | Skilj från spelens vanliga sparade data. |
| save data | sparade speldata | |
| deinterlacing | avflätning | Video. |
| interlacing | sammanflätning | Fält i sammanflätad video. |
| game library | spelbibliotek | |
| Screen Gap | mellanrum mellan skärmar | Nintendo DS-layoutens mellanrum mellan de två skärmarna. |
| Left/Right Trigger | vänster/höger avtryckare | Gamepadens analoga avtryckare. |
| CRT mask: dot / slot / aperture grille | punktmask / spaltmask / bländargaller | Skärmfilter. |
| Composite signal | komposit | Videosignal; *sammansatt* är för ospecifikt här. |
| scanner | skanner | Enheten som digitaliserar bilder; använd *skanner*, inte *bildläsare*. |
| destripe | ta bort bandning | GIMP-filter som tar bort lodräta band/ränder i bilder. |
| scale division (tone mapping) | antal skalor | Reglage för antal iterationer/skalor i Retinex-filter. |
| Toy Kit (Spyrogimp) | ritsats | Spirografens läge med kugghjul och hålpositioner från en rit-/spirografsats. |
| Bumps (Spyrogimp) | utbuktningar | Formläge med halvcirkelformade utbuktningar. |
| Epitrochoid | epitrokoid | Svensk fackterm för kurvtypen. |
| spirograph | spirograf | Mönster/figur ritad med kugghjulsbaserad spirograf. |
| gear tooth (Spyrogimp) | kugg | En tand på ett kugghjul. |
| sample average (histogram) | medelvärde för sampel | Medelvärdet av pixelvärden som används vid histogram-/färgberäkning. |
| Curve Pattern (Spyrogimp) | kurvform | Mönstrets kurvbaserade inställningssektion. |
