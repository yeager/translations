# Status – svensk granskning av Home Assistant Core

Senast uppdaterad: 2026-11-20.

## Omfattning och kontrollpunkt

- Granskning har genomförts rad för rad t.o.m. Lokalise-sida 730.
- Sida 731 är granskad och dess sex sparade ändringar har återlästs och förts in i TMX-minnet.
- Tidigare arbete fram till sida 614 finns i tidigare rapporter i denna katalog. Sidor 615–730 är fortsatt spårade genom Lokalise-ID:n och det kanoniska TMX-minnet; sidor 727–730 har kompletterande fullständig ändringsrapport.

## Kanoniskt Home Assistant-minne

- Fil: `yeager/swedish-tm/Home-Assistant/sv-home-assistant-core-lokalise-verified-20261120-canonical.tmx`.
- Senast verifierad nivå: **769** unika översättningsenheter, t.o.m. sida 731.
- XML-kontroll: unika `tuid`-värden och fullständig `source`-proveniens för varje post.
- Alla 769 enheter har full nyckel som `source`, engelskt och svenskt segment samt statusen `saved-and-read-back`.
- 572 senare poster använder `lokalise:<översättnings-id>` som `tuid`. De 197 historiska posterna använder i stället den fullständiga källnyckeln som `tuid`; deras Lokalise-ID behöver hämtas från API:t innan de kan migreras säkert.

## Pågående uppföljning

| Nyckel | Status | Nästa säkra kontroll |
| --- | --- | --- |
| Nya tomma HotSpring-poster och följdposter | 14 förslag dokumenterade utan Lokalise-skrivning. | Kontrollera att HotSpring-källan publicerats i Core före ett eventuellt sparbeslut. |
| `component::hotspring` | Alla 50 aktuella nycklar är granskade genom smalare Lokalise-sökningar; fyra ändringsförslag och produkttermsberoenden är dokumenterade. | Återkontrollera mot publicerad Core-källa innan ett eventuellt sparbeslut. |
| `component::timer_list` | Alla 61 aktuella, tomma strängar är granskade mot Core-källan och dokumenterade som förslag. | Komponenten kan återkontrolleras vid källändring; fortsätt i Lokalise med nästa oavgranskade komponent. |
| `component::evohome` | Alla **36** aktuella källsträngar har kontrollerats mot Core-källan; tre konkreta ändringsförslag är dokumenterade och en tom rad har ett äldre, odubblerat förslag. | Komponenten kan återkontrolleras vid källändring; Lokalise innehåller även historiska nycklar som inte motsvarar aktuell Core-källa. |
| `component::ezviz` | Alla **82** aktuella Core-strängar är granskade mot Core-källan; nio förslag är dokumenterade, varav tre återställer obligatoriska referenser. | Komponenten kan återkontrolleras vid källändring; 12 Lokalise-rader som saknas i aktuell Core-källa är dokumenterade som historiska. |
| `component::fivem` | Alla 12 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::feedreader` | Alla 7 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag; tre äldre Lokalise-rader är markerade som historiska. | Komponenten kan återkontrolleras vid källändring. |
| `component::fing` | Alla 15 aktuella Core-strängar är granskade mot Core-källan; ett produktnamns- och böjningsförslag är dokumenterat. | Komponenten kan återkontrolleras vid källändring. |
| `component::fibaro` | Alla 16 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag; en äldre Lokalise-rad är markerad som historisk. | Komponenten kan återkontrolleras vid källändring. |
| `component::filesize` | Alla 10 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag; en äldre Lokalise-rad är markerad som historisk. | Komponenten kan återkontrolleras vid källändring. |
| `component::gogogate2` | Alla 10 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::kmtronic` | Alla 10 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::laundrify` | Alla 10 aktuella Core-strängar är granskade mot Core-källan; två ändringsförslag är dokumenterade och en äldre Lokalise-rad är markerad som historisk. | Komponenten kan återkontrolleras vid källändring; förslagen ska läsas tillbaka före eventuell TMX-synkning. |
| `component::luftdaten` | Alla 10 aktuella Core-strängar är granskade mot Core-källan; ett språkligt ändringsförslag är dokumenterat. | Komponenten kan återkontrolleras vid källändring; förslaget ska läsas tillbaka före eventuell TMX-synkning. |
| `component::paj_gps` | Alla 10 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::openexchangerates` | Alla 10 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag; en äldre Lokalise-rad är markerad som historisk. | Komponenten kan återkontrolleras vid källändring. |
| `component::emonitor` | Alla 9 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::brunt` | Alla 10 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag; en äldre Lokalise-rad är markerad som historisk. | Komponenten kan återkontrolleras vid källändring. |
| `component::energenie_power_sockets` | Alla 9 aktuella Core-strängar är granskade mot Core-källan; ett ändringsförslag är dokumenterat. | Komponenten kan återkontrolleras vid källändring; förslaget ska läsas tillbaka före eventuell TMX-synkning. |
| `component::eufylife_ble` | Alla 9 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag; två äldre Lokalise-rader är markerade som historiska. | Komponenten kan återkontrolleras vid källändring. |
| `component::igloohome` | Alla 9 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::medcom_ble` | Alla 9 aktuella Core-strängar är granskade mot Core-källan; ett osäkert CPM-terminologiförslag är dokumenterat och en äldre Lokalise-rad är markerad som historisk. | Jämför CPM-termen med produktdokumentation före eventuell Lokalise-skrivning. |
| `component::ourgroceries` | Alla 9 aktuella Core-strängar är granskade mot Core-källan; två förslag återställer obligatoriska referenser. | Förslagen ska läsas tillbaka före eventuell TMX-synkning. |
| `component::pglab` | Alla 9 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag; en äldre Lokalise-rad är markerad som historisk. | Komponenten kan återkontrolleras vid källändring. |
| `component::private_ble_device` | Alla 9 aktuella Core-strängar är granskade mot Core-källan; två språkförslag är dokumenterade. | Komponenten kan återkontrolleras vid källändring; förslagen ska läsas tillbaka före eventuell TMX-synkning. |
| `component::radiotherm` | Alla 9 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::simplepush` | Alla 9 aktuella Core-strängar är granskade mot Core-källan; felmeddelandet om sändning sparades i Lokalise och återlästes i redigeringsfältet. | Ta med värdet vid nästa verifierade TMX-synkning. |
| `component::tankerkoenig` | Del 1: minst 38 av 72 aktuella Lokalise-nycklar granskade. Alla tio fastställda ändringar i del 1 är sparade och återlästa i Lokalise. | Granska återstående nycklar; vid nya fynd sparas och återläses ändringen direkt. |
| 197 historiska TMX-enheter | Strukturellt giltiga men saknar Lokalise-ID i `tuid`. | Slå upp varje fullständig `source`-nyckel via Lokalise-API:t och ersätt `tuid` först efter en unik matchning. |

## Miljöstatus

Den tidigare autentiserade Lokalise-sessionen och dess API-hjälpare återställdes av miljön, men en läsbehörig Lokalise-yta har återetablerats. Ingen Lokalise-skrivning görs. Fortsatt arbete använder inte `/tmp`; cache, rapporter och valideringsunderlag ska ligga i arbetsytan eller i respektive GitHub-repository.

### Tillfälligt åtkomsthinder efter RadioTherm-granskningen

- Den 20 november blev den lokala webbläsaråtkomsten för chatten otillgänglig
  innan Simplepush kunde läsas i Lokalise.
- Den läsande exporthjälparen i `swedish-tm` kontrollerades också. Den kräver
  `LOKALISE_TOKEN`, som inte är konfigurerad i den aktuella miljön.
- Simplepush har därför **inte** markerats som granskad och inga nya
  Lokalise- eller TMX-värden har skapats på basis av ett gammalt ögonblicksbildsunderlag.
- Den verifierade Core-TMX:en validerades lokalt under hindret: 769 giltiga
  enheter (572 med Lokalise-ID och 197 historiska nyckelbaserade enheter).

## Källkontroll efter sessionens återställning

- Home Assistant Core kontrollerades mot uppströms-commit `3d340fb5fdf03e7db48b45aec10f9b8da3b31c12` (2026-11-20).
- `homeassistant/components/logbook/strings.json` och `homeassistant/components/script/strings.json` innehåller fortfarande de engelska källtexter som sida 731 granskades mot, inklusive `Log activity`, `Reload scripts` och `Toggle script`.
- Detta bekräftar att de dokumenterade sida-731-förslagen inte bygger på föråldrad engelsk källtext. Det ersätter inte Lokalise-återläsningen av de svenska målvärdena och ger därför inte underlag för TMX-synkning.

## Verktygsaudit

- `svlang`, `hunspell-sv`, `swedish-foss-terminology` och `swedish-tm` har kontrollerats från rena arbetskopior i arbetsytan.
- Python-källorna kompilerar och `swedish-foss-terminology` kan starta sin export-CLI. Fulla pytest-sviter är inte körda eftersom den återställda miljön saknar `pytest`.
- Hunspell markerar `klimatprofilsindex`, trots att beståndsdelarna accepteras. Termen kommer från den aktuella Home Assistant-kontexten men saknar här en oberoende generell ordbokskälla. Enligt `hunspell-sv`-policyn läggs den därför inte in som en global enskild katalogterm; träffen är en granskningssignal, inte ett automatiskt verktygsfel.
- `swedish-tm` innehåller från commit `fac51ee` den beroendefria valideraren `scripts/validate_home_assistant_core_tmx.py`. Den validerar XML, språksegment, källproveniens och review-status samt rapporterar skillnaden mellan Lokalise-ID och historiska nyckelbaserade `tuid`-värden. Dess strikta migrationsläge är avsiktligt rött tills ID-rekonstruktionen kan verifieras via API:t.

## Referenser

- [Sparade ändringar på sidor 727–730](sparade-andringar-sidor-727-730.md)
- [Sida 731: granskning och kvarstående verifiering](granskning-sida-731-logbook-script.md)
- [Nya tomma HotSpring-strängar och följdposter](granskning-nya-tomma-strangar-hotspring.md)
- [HotSpring: befintliga svenska strängar](granskning-hotspring-befintliga-strangar.md)
- [Evohome: varmvattenöverstyrning](granskning-evohome-varmvatten.md)
- [Evohome: undantag](granskning-evohome-undantag.md)
- [Ezviz: brytare](granskning-ezviz-brytare.md)
- [Ezviz: konfiguration](granskning-ezviz-konfiguration.md)
- [Ezviz: sensorer](granskning-ezviz-sensorer.md)
- [Ezviz: val och reglage](granskning-ezviz-val-och-reglage.md)
- [Ezviz: återstående aktiva strängar](granskning-ezviz-aterstaende.md)
- [FiveM](granskning-fivem.md)
- [Feedreader](granskning-feedreader.md)
- [Fing](granskning-fing.md)
- [Fibaro](granskning-fibaro.md)
- [Filesize](granskning-filesize.md)
- [Gogogate2](granskning-gogogate2.md)
- [KMtronic](granskning-kmtronic.md)
- [Laundrify](granskning-laundrify.md)
- [Luftdaten](granskning-luftdaten.md)
- [PAJ GPS](granskning-paj-gps.md)
- [Open Exchange Rates](granskning-openexchangerates.md)
- [eMonitor](granskning-emonitor.md)
- [Brunt](granskning-brunt.md)
- [Energenie Power Sockets](granskning-energenie-power-sockets.md)
- [EufyLife BLE](granskning-eufylife-ble.md)
- [igloohome](granskning-igloohome.md)
- [Medcom BLE](granskning-medcom-ble.md)
- [OurGroceries](granskning-ourgroceries.md)
- [PG LAB Electronics](granskning-pglab.md)
- [Private BLE Device](granskning-private-ble-device.md)
- [RadioTherm](granskning-radiotherm.md)
- [Simplepush](granskning-simplepush.md)
- [Tankerkoenig, del 1](granskning-tankerkoenig-del-1.md)
- [Timer list: fortsatt granskning av tomma strängar](granskning-timer-list-fortsattning.md)
- [Timer list: återstående granskade tjänststrängar](granskning-timer-list-tjanster.md)
