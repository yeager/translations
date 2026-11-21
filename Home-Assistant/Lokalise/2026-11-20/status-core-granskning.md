# Status – svensk granskning av Home Assistant Core

Senast uppdaterad: 2026-11-21.

## Omfattning och kontrollpunkt

- Granskning har genomförts rad för rad t.o.m. Lokalise-sida 730.
- Sida 731 är granskad och dess sex sparade ändringar har återlästs och förts in i TMX-minnet.
- Tidigare arbete fram till sida 614 finns i tidigare rapporter i denna katalog. Sidor 615–730 är fortsatt spårade genom Lokalise-ID:n och det kanoniska TMX-minnet; sidor 727–730 har kompletterande fullständig ändringsrapport.

## Kanoniskt Home Assistant-minne

- Fil: `yeager/swedish-tm/Home-Assistant/sv-home-assistant-core-lokalise-verified-20261120-canonical.tmx`.
- Senast verifierad nivå: **1 374** unika översättningsenheter (231 historiska nyckelbaserade och 1 143 med Lokalise-ID), inklusive löpande Lokalise-granskningar från 2026-11-21.
- XML-kontroll: unika `tuid`-värden och fullständig `source`-proveniens för varje post.
- Alla 1 374 enheter har full nyckel som `source`, engelskt och svenskt segment samt statusen `saved-and-read-back` eller, för redan korrekta och återverifierade Lokalise-värden, `verified-existing`.
- 1 143 senare poster använder `lokalise:<översättnings-id>` som `tuid`. De 231 historiska posterna använder i stället den fullständiga källnyckeln som `tuid`; deras Lokalise-ID behöver hämtas från API:t innan de kan migreras säkert.
- Produktnamnskontroll 2026-11-21: samtliga **31** TMX-enheter vars engelska segment innehåller `Home Assistant` innehåller exakt samma produktnamn i det svenska segmentet (0 avvikelser).

## Pågående uppföljning

| Nyckel | Status | Nästa säkra kontroll |
| --- | --- | --- |
| Nya tomma HotSpring-poster och följdposter | HotSpring-källan är nu publicerad i Core (`67a75a0a`); alla nio dokumenterade HotSpring-sensorer och Evohome-felet `api_credentials_invalid` är sparade och återlästa. Tankerkoenigs två poster är redan korrekt översatta och återverifierade i Lokalise. | Samtliga tidigare dokumenterade poster är åtgärdade eller verifierade; komponenter kan återkontrolleras vid källändring. |
| `component::hotspring` | Alla 50 aktuella nycklar är granskade genom smalare Lokalise-sökningar och mot den nu publicerade Core-källan; de fyra dokumenterade korrigeringarna är sparade och återlästa i Lokalise. Produktlägen med *boost* är medvetet lämnade som produkttermsberoenden. | Återkontrollera vid källändring eller när produkttermen *boost* kan verifieras. |
| `component::timer_list` | Alla 61 aktuella strängar är granskade mot Core-källan; komponenttiteln, dess referens, sex kompletta triggerpar, samtliga tjänster, statusval och felmeddelandet för okänt timer-ID är sparade och återlästa. | Komponenten kan återkontrolleras vid källändring. |
| `component::evohome` | Alla **36** aktuella källsträngar har kontrollerats mot Core-källan; tre ändringar är sparade och återlästa i Lokalise, och en tom rad har ett äldre, odubblerat förslag. | Lokalise innehåller även historiska nycklar som inte motsvarar aktuell Core-källa; den tomma raden kan sparas efter separat kontroll. |
| `component::ezviz` | Alla **82** aktuella Core-strängar är granskade mot Core-källan; tre obligatoriska referenser och sex språkändringar är sparade och återlästa. | Komponenten kan återkontrolleras vid källändring; 12 Lokalise-rader som saknas i aktuell Core-källa är dokumenterade som historiska. |
| `component::fivem` | Alla 12 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::feedreader` | Alla 7 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag; tre äldre Lokalise-rader är markerade som historiska. | Komponenten kan återkontrolleras vid källändring. |
| `component::fing` | Alla 15 aktuella Core-strängar är granskade mot Core-källan; Fing-API-texten är sparad och återläst i Lokalise. | Komponenten kan återkontrolleras vid källändring. |
| `component::fibaro` | Alla 16 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag; en äldre Lokalise-rad är markerad som historisk. | Komponenten kan återkontrolleras vid källändring. |
| `component::filesize` | Alla 10 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag; en äldre Lokalise-rad är markerad som historisk. | Komponenten kan återkontrolleras vid källändring. |
| `component::gogogate2` | Alla 10 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::kmtronic` | Alla 10 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::laundrify` | Alla 10 aktuella Core-strängar är granskade mot Core-källan; två ändringar är sparade och återlästa i Lokalise, och en äldre Lokalise-rad är markerad som historisk. | Komponenten kan återkontrolleras vid källändring. |
| `component::luftdaten` | Alla 10 aktuella Core-strängar är granskade mot Core-källan; feltexten för ogiltig sensor är sparad och återläst i Lokalise. | Komponenten kan återkontrolleras vid källändring. |
| `component::paj_gps` | Alla 10 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::openexchangerates` | Alla 10 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag; en äldre Lokalise-rad är markerad som historisk. | Komponenten kan återkontrolleras vid källändring. |
| `component::emonitor` | Alla 9 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::brunt` | Alla 10 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag; en äldre Lokalise-rad är markerad som historisk. | Komponenten kan återkontrolleras vid källändring. |
| `component::energenie_power_sockets` | Alla 9 aktuella Core-strängar är granskade mot Core-källan; `Socket {socket_id}` → `Uttag {socket_id}` är sparad och återläst i Lokalise. | Komponenten kan återkontrolleras vid källändring. |
| `component::eufylife_ble` | Alla 9 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag; två äldre Lokalise-rader är markerade som historiska. | Komponenten kan återkontrolleras vid källändring. |
| `component::igloohome` | Alla 9 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::medcom_ble` | Alla 9 aktuella Core-strängar är granskade mot Core-källan; ett osäkert CPM-terminologiförslag är dokumenterat och en äldre Lokalise-rad är markerad som historisk. | Jämför CPM-termen med produktdokumentation före eventuell Lokalise-skrivning. |
| `component::ourgroceries` | Alla 9 aktuella Core-strängar är granskade mot Core-källan; två obligatoriska referenser är återställda, sparade och återlästa i Lokalise. | Komponenten kan återkontrolleras vid källändring. |
| `component::pglab` | Alla 9 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag; en äldre Lokalise-rad är markerad som historisk. | Komponenten kan återkontrolleras vid källändring. |
| `component::private_ble_device` | Alla 9 aktuella Core-strängar är granskade mot Core-källan; två språkändringar är sparade och återlästa i Lokalise. | Komponenten kan återkontrolleras vid källändring. |
| `component::prana` | Alla direkta aktuella strängar är granskade; ett osparat förslag för displayens ljusstyrka är dokumenterat. | Spara och återläs förslaget när det har bekräftats. |
| `component::profiler` | Alla 42 bladnycklar är granskade. Tre osparade språkförslag är dokumenterade. | Spara och återläs de tre förslagen när de har bekräftats. |
| `component::progettihwsw` | Alla 24 aktuella Lokalise-nycklar, inklusive 16 reläetiketter och referenser, är granskade utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::proximity` | Direkta strängar och referenser är inventerade; en osparad förbättring av borttagen-entitet-texten är dokumenterad. | Spara och återläs förslaget när det har bekräftats. |
| `component::pterodactyl` | Alla **26** aktuella bladnycklar är granskade mot Core och Lokalise; två ytterligare Lokalise-poster är historiska. Ett osparat format- och språkförslag för drifttid är dokumenterat. | Spara och återläs enbart det dokumenterade drifttidsförslaget efter uttrycklig bekräftelse; därefter kan komponenten återkontrolleras vid källändring. |
| `component::pure_energie` | Alla **11** aktuella bladnycklar är granskade mot Core och Lokalise utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::purpleair` | Alla **43** aktuella bladnycklar är granskade. Tre osparade förslag är dokumenterade; 13 ytterligare Lokalise-poster är historiska. | Spara och återläs de tre förslagen efter uttrycklig bekräftelse; därefter synkas verifierade värden till TMX. |
| `component::pushbullet` | Alla **19** aktuella bladnycklar är granskade. Två osparade referenskorrigeringar är dokumenterade; en extra Lokalise-rad är historisk. | Spara och återläs de två förslagen efter uttrycklig bekräftelse; därefter synkas verifierade värden till TMX. |
| `component::pvoutput` | Alla **23** aktuella bladnycklar är granskade. Två osparade referenskorrigeringar är dokumenterade; historiska Lokalise-poster är avgränsade. | Spara och återläs de två förslagen efter uttrycklig bekräftelse; därefter synkas verifierade värden till TMX. |
| `component::pyload` | Alla **55** aktuella Core-strängar är granskade mot aktuell Core-källa. Två osparade språk- och markupförslag är dokumenterade; 20 ytterligare Lokalise-poster är historiska. | Spara och återläs de två förslagen efter uttrycklig bekräftelse; därefter synkas verifierade värden till TMX. |
| `component::qbus` | Alla **15** aktuella Core-strängar är granskade mot aktuell Core-källa. Två osparade språkförslag är dokumenterade. | Spara och återläs de två förslagen efter uttrycklig bekräftelse; därefter synkas verifierade värden till TMX. |
| `component::qingping` | Alla **8** aktuella Core-strängar är granskade mot aktuell Core-källa utan ändringsförslag; en extra Lokalise-rad är historisk. | Komponenten kan återkontrolleras vid källändring. |
| `component::qvr_pro` | Alla **8** aktuella Core-strängar är granskade mot aktuell Core-källa utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::qnap_qsw` | Alla **19** aktuella Core-strängar är granskade mot aktuell Core-källa. Fyra osparade bindestreckskorrigeringar är dokumenterade; två extra Lokalise-poster är historiska. | Spara och återläs de fyra förslagen efter uttrycklig bekräftelse; därefter synkas verifierade värden till TMX. |
| `component::qnap` | Alla **43** aktuella Core-strängar är granskade mot aktuell Core-källa. Två osparade ordföljdsförbättringar är dokumenterade; en extra Lokalise-rad är historisk. | Spara och återläs de två förslagen efter uttrycklig bekräftelse; därefter synkas verifierade värden till TMX. |
| `component::qbittorrent` | Alla **48** aktuella Core-strängar är granskade mot aktuell Core-källa. Tre osparade tjänsteformuleringar är dokumenterade. | Spara och återläs de tre förslagen efter uttrycklig bekräftelse; därefter synkas verifierade värden till TMX. |
| `component::rhasspy` | Den enda aktuella Core-strängen är granskad mot aktuell Core-källa utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::route53` | Båda aktuella Core-strängarna är granskade mot aktuell Core-källa utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::raspberry_pi` | Alla **5** aktuella Core-strängar är granskade mot aktuell Core-källa utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::rest_command` | Alla **5** aktuella Core-strängar är granskade mot aktuell Core-källa utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::rapt_ble` | Alla **6** aktuella Core-strängar är granskade mot aktuell Core-källa utan ändringsförslag; en extra Lokalise-rad är historisk. | Komponenten kan återkontrolleras vid källändring. |
| `component::rflink` | Alla **6** aktuella Core-strängar är granskade mot Lokalise och aktuell Core-källa utan ändringsförslag. Två YAML-migreringsnycklar i Lokalise är historiska. | Komponenten kan återkontrolleras vid källändring. |
| `component::ruuvi_gateway` | Alla **6** aktuella Core-strängar är granskade mot Lokalise och aktuell Core-källa utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::radio_browser` | Alla **7** aktuella Core-strängar är granskade. En obligatorisk referens och en Home Assistant-formulering behöver korrigeras. | Spara och återläs de två dokumenterade förslagen; synka därefter verifierade värden till TMX. |
| `component::refoss` | Alla **7** aktuella Core-strängar är granskade. Korrigeringen av *energy returned* är sparad och återläst; tre extra Lokalise-nycklar är historiska. | Komponenten kan återkontrolleras vid källändring. |
| `component::recollect_waste` | Alla **8** aktuella Core-strängar är granskade mot Lokalise och aktuell Core-källa utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::rabbitair` | Alla **17** aktuella Core-strängar är granskade mot Lokalise och aktuell Core-källa utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::radiotherm` | Alla 9 aktuella Core-strängar är granskade mot Core-källan utan ändringsförslag. | Komponenten kan återkontrolleras vid källändring. |
| `component::simplepush` | Alla 9 aktuella Core-strängar är granskade mot Core-källan; felmeddelandet om sändning sparades i Lokalise och återlästes i redigeringsfältet. | Ta med värdet vid nästa verifierade TMX-synkning. |
| `component::tankerkoenig` | Del 1–2: konfiguration och synliga sensorattribut är lästa mot aktuell Core-källa. Alla tio fastställda ändringar är sparade och återlästa i Lokalise. | Kontrollera historiska Lokalise-rader mot API-proveniens när full export finns. |
| `component::irm_kmi` | Samtliga **75** aktuella Core-strängar är kontrollerade mot Lokalise och aktuell Core-källa. Tolv felaktiga eller föråldrade mål har sparats och återlästs; övriga är dokumenterat korrekta. | Komponenten kan återkontrolleras vid källändring. |
| 197 historiska TMX-enheter | Strukturellt giltiga men saknar Lokalise-ID i `tuid`. | Slå upp varje fullständig `source`-nyckel via Lokalise-API:t och ersätt `tuid` först efter en unik matchning. |

## Miljöstatus

En autentiserad Lokalise-yta är tillgänglig igen. Fastställda ändringar sparas
omedelbart och läses tillbaka; fortsatt arbete använder inte `/tmp`.

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

- En separat, ren grund klon av Home Assistant Core används från och med 2026-11-21, eftersom den tidigare lokala klonen har en avvikande ympad historik och inte kan snabbspolas säkert. Den rena klonen står på uppströms-commit `2fdaa177` (`dev`). Nya komponentgranskningar ska alltid göras mot denna klon; äldre resultat behåller sin dokumenterade historiska källrevision tills de återkontrolleras.
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
- [Prana](../2026-11-21/granskning-prana.md)
- [Profiler](../2026-11-21/granskning-profiler.md)
- [ProgettiHWSW](../2026-11-21/granskning-progettihwsw.md)
- [Proximity](../2026-11-21/granskning-proximity.md)
- [Pterodactyl](../2026-11-21/granskning-pterodactyl.md)
- [Pure Energie](../2026-11-21/granskning-pure-energie.md)
- [PurpleAir](../2026-11-21/granskning-purpleair.md)
- [Pushbullet](../2026-11-21/granskning-pushbullet.md)
- [PVOutput](../2026-11-21/granskning-pvoutput.md)
- [pyLoad](../2026-11-21/granskning-pyload.md)
- [Qbus](../2026-11-21/granskning-qbus.md)
- [Qingping](../2026-11-21/granskning-qingping.md)
- [QVR Pro](../2026-11-21/granskning-qvr-pro.md)
- [QNAP QSW](../2026-11-21/granskning-qnap-qsw.md)
- [QNAP](../2026-11-21/granskning-qnap.md)
- [qBittorrent](../2026-11-21/granskning-qbittorrent.md)
- [Rhasspy](../2026-11-21/granskning-rhasspy.md)
- [Route 53](../2026-11-21/granskning-route53.md)
- [Raspberry Pi](../2026-11-21/granskning-raspberry-pi.md)
- [REST command](../2026-11-21/granskning-rest-command.md)
- [RAPT BLE](../2026-11-21/granskning-rapt-ble.md)
- [RFLink](../2026-11-21/granskning-rflink.md)
- [Ruuvi Gateway](../2026-11-21/granskning-ruuvi-gateway.md)
- [Radio Browser](../2026-11-21/granskning-radio-browser.md)
- [Radio Frequency](../2026-11-21/granskning-radio-frequency.md)
- [REFOSS](../2026-11-21/granskning-refoss.md)
- [Recollect Waste](../2026-11-21/granskning-recollect-waste.md)
- [RabbitAir](../2026-11-21/granskning-rabbitair.md)
- [Rachio](../2026-11-21/granskning-rachio.md)
- [Radarr](../2026-11-21/granskning-radarr.md)
- [RadioTherm](granskning-radiotherm.md)
- [Rain Bird](../2026-11-21/granskning-rainbird.md)
- [Simplepush](granskning-simplepush.md)
- [Tankerkoenig, del 1](granskning-tankerkoenig-del-1.md)
- [Tankerkoenig, del 2](granskning-tankerkoenig-del-2.md)
- [Timer list: fortsatt granskning av tomma strängar](granskning-timer-list-fortsattning.md)
- [Timer list: återstående granskade tjänststrängar](granskning-timer-list-tjanster.md)
