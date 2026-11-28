# Home Assistant: svenska termer

Senast uppdaterad: 2026-11-28

Listan innehåller beslut som är kontrollerade i Home Assistants konkreta
entitets- och UI-kontext. Den är inte en generell ordlista och ersätter inte
källtextens sammanhang.

| Engelska | Svenska | Kontext och kommentar |
| --- | --- | --- |
| cloud services | molntjänster | HP Printer, binär sensors etikett för tillgängliga tjänster. |
| cloud registered | registrerad i molnet | HP Printer, registreringsstatus. |
| paper jam | pappersstopp | HP Printer, skrivarfel och räknarstatus. |
| scanner jam | pappersstopp i dokumentmataren | HP Printer, pappersstopp i dokumentmataren enligt komponentens dokumentation. |
| printed pages | utskrivna sidor | HP Printer, ackumulerad räknare. |
| copied pages | kopierade sidor | HP Printer, ackumulerad räknare. |
| scanned pages | skannade sidor | HP Printer, ackumulerad räknare. |
| faxed pages | faxade sidor | HP Printer, ackumulerad räknare. |
| scanned pages from glass | skannade sidor från skannerglaset | HP Printer, flatbäddsskannerns räknare; förtydligar att glaset är skannerns. |
| copied black and white pages | kopierade svartvita sidor | HP Printer, räknare för svartvita kopior. |
| copied color pages | kopierade färgsidor | HP Printer, räknare för färgkopior. |
| close door or cover | stäng luckan eller locket | HP Printer, aktiv åtgärdsstatus. |
| shutting down | stängs av | HP Printer, pågående status. |
| manufacturing date | tillverkningsdatum | HP Printer, informationsfält. |
| paper mispicks | pappersmatningsfel | HP Printer, räknare för misslyckade pappersmatningar. |
| scanner mispicks | matningsfel i dokumentmataren | HP Printer, räknare för misslyckade matningar i dokumentmataren. |
| faxed pages from document feeder | faxade sidor från dokumentmataren | HP Printer, faxräknare. |
| faxed pages from glass | faxade sidor från skannerglaset | HP Printer, faxräknare via skannerglaset. |
| faxed pages from computer | faxade sidor från datorn | HP Printer, faxräknare för datorutskick. |
| consumable installation date | installationsdatum för [färg] patron | HP Printer, datum då en bläck- eller tonerpatron installerades. |
| consumable level | nivå för [färg] patron | HP Printer, procentuell kvarvarande mängd för patronen. |
| consumable manufacturing date | tillverkningsdatum för [färg] patron | HP Printer, informationsfält. |
| consumable pages printed | utskrivna sidor med [färg] patron | HP Printer, ackumulerad patronräknare. |
| consumable pages remaining | återstående sidor för [färg] patron | HP Printer, uppskattning för patronen. |
| consumable warranty expiration date | garantins utgångsdatum för [färg] patron | HP Printer, informationsfält. |
| genuine refills | äkta påfyllningar för [färg] patron | HP Printer, diagnostisk ackumulerande räknare. |
| counterfeit refills | förfalskade påfyllningar för [färg] patron | HP Printer, diagnostisk ackumulerande räknare. |
| indoor humidity | luftfuktighet inomhus | Helty Cloud och andra klimatentiteter; egenskapsnamn. |
| indoor temperature | inomhustemperatur | Helty Cloud och andra klimatentiteter; egenskapsnamn. |
| outdoor temperature | utomhustemperatur | Helty Cloud och andra klimatentiteter; egenskapsnamn. |
| thinking type | typ av resonemang | Anthropic, val för hur Claude använder ytterligare token. |
| effort | ansträngning | Anthropic, val för hur många token Claude använder vid svar. |

| Honeywell temporary hold | tillfällig temperaturhållning | Honeywell-termostat: håller en vald temperatur till ett angivet klockslag innan schemat återupptas. |
| RF timing | RF-puls eller RF-paus (med längd) | Broadlink: källkoden använder växlande pulser och pauser; termen avser längden på en enskild del, inte en generell ”RF-timing”. |
| Cooking end | sluttid för tillagningen | VeSync: tidsstämpelsensor för när airfryerns tillagning slutar. |
| Substream | sekundär videoström | Hikvision-kamera: alternativ videoström. |
| Total carbohydrates | totala kolhydrater | Google Health: etikett för näringsvärde. |
| Sync baskets | synkronisering av korgar | VeSync: binär statussensor som visar om airfryerns korgar synkroniseras. |
| Standby | viloläge | VeSync-status; följer Home Assistants gemensamma översättning och ersätter en tidigare avvikande term. |

| Scratch status | klådfrekvens | Tractive: visar hur ofta hunden kliar sig; produktens hälsokort jämför kliandet med normalnivån. |

| Fan request | begäran om fläktdrift | AeroSmart: diagnostisk signal från värmepumpen eller zonstyrningen som begär fläktdrift. |

| Hot water electric heater request | begäran om elvärme för varmvatten | AeroSmart: begäran om att elvärmaren värmer bruksvatten; inte en begäran om varmvatten från elvärmaren. |

| Hot water heat pump request | begäran om varmvattenuppvärmning med värmepump | AeroSmart: begäran om bruksvattenuppvärmning via värmepump. |

| Outdoor brine temperature sensor fault | fel på köldbärarens utetemperaturgivare | AeroSmart: brine avser vätskan i värmepumpens köldbärarkrets, inte uteluften. |

| NAD IR Remote | IR-styrning för NAD-enhet | Home Assistant-integrationen styr NAD-utrustning med en vald infraröd sändare; det är inte en fysisk fjärrkontroll. |

| Tile device | Tile-enhet | Tile BLE: Tile är produktnamnet på en spårningsbricka; håll produktnamnet oförändrat i svenska sammansättningar. |

| backup location | säkerhetskopieringskatalog | SFTP Storage: fjärrkatalogen där säkerhetskopior lagras. |

| Switcher sensor | Switcher-sensor | Switcher är produktnamn; bindestreck tydliggör sammansättningen före den svenska böjningen. |

| electric current | strömstyrka | HotSpring-spa: värdena anges i ampere; skilj den elektriska storheten från allmän ström. |

| apparent power | skenbar effekt | HotSpring-spa: mätvärdet anges i voltampere (VA), inte watt. |

| alder pollen | alpollen | IRM KMI: pollen från al (trädet); svensk artbenämning. |

| ash pollen | askpollen | IRM KMI: pollen från ask (trädet); svensk artbenämning. |

| mugwort pollen | gråbopollen | IRM KMI: mugwort benämns gråbo på svenska. |

| sleeping device | vilande enhet | Shelly: en batteridriven enhet som vaknar periodiskt och därför inte kan ta emot kommandon hela tiden. |
| AC input strength | AC-ingångens styrka | Victron GX: val med lägena Strong och Weak för växelströmsingången. |
| High current | hög strömstyrka | Victron GX: batteriets strömlarm; strömstyrka avser den elektriska storheten. |
| Disable PV | inaktivera solcellsproduktionen | Victron GX: PV återges som solcellsproduktion enligt svensk produktterminologi. |
| Disable PV inverters | inaktivera solcellsväxelriktare | Victron GX: PV-inverters är växelriktare för solceller. |
| Disable all PV | inaktivera all solcellsproduktion | Victron GX: skiljer avstängning av all solcellsproduktion från en enskild PV-växelriktare. |
| Maximum continuous current | maximal kontinuerlig strömstyrka | Enphase Envoy-generator: mätvärdet anges i ampere. |
| Nameplate rating | märkeffekt | Enphase Envoy-generator: källkoden anger en effektklass i kilowatt. |
| Start battery level | batterinivå för generatorstart | Enphase Envoy-generator: laddningsnivå i procent som utlöser start. |
| Stop battery level | batterinivå för generatorstopp | Enphase Envoy-generator: laddningsnivå i procent som utlöser stopp. |

| Routing | routning | KNXnet/IP: svensk nätverksterm för vidarebefordran mellan KNX-nät. |
| Secure routing | säker routning | KNX IP Secure: krypterad routing; behåll skillnaden mot säker tunnling. |
| Backbone key | stamnätsnyckel | KNX IP Secure: nyckel för KNX-stamnätet; visas i ETS-projektets säkerhetsrapport. |
| Keyring file | nyckelringsfil | KNX: exporterad `.knxkeys`-fil med nycklar. |
| Plugged in | inkopplad | A Better Routeplanner: bilen är fysiskt ansluten till laddaren men behöver inte ladda. |
| Relay switched | reläet har växlat läge | UniFi Protect: händelseetikett när ett relä växlar tillstånd. |
| SMHI API | SMHI:s API | Genitivformen används i felmeddelanden om anrop till myndighetens API. |
| polled (register) | register som systemet läser av på begäran | Nibe MODBUS: skiljer register som pumpen skickar spontant från register som systemet hämtar genom aktiv avläsning. |

| polling | regelbunden hämtning | SmartyPlants: beskriver att Home Assistant hämtar mätvärden när webhook-signering inte används. |
| signing secret | signeringshemlighet | SmartyPlants-webhook: hemlighet som används för att verifiera inkommande uppdateringar. |
| firmware version | version av fast programvara | BLUETTI: versionsuppgift för batteriets inbyggda programvara. |
| total charged energy | total energi som har laddats | BLUETTI Modbus: ackumulerad energisensor i Wh. |
| total discharged energy | total energi som har laddats ur | BLUETTI Modbus: ackumulerad energisensor i Wh, parallell med total laddad energi. |
| destination folder | målmapp | WebDAV: mappen dit filer överförs; den skapas automatiskt om den saknas. |

## Status

De två molnstatusetiketterna, `scanner_jams`, fem räknaretiketter, tre
skrivarstatusvärden, tre matnings- och informationsfält samt tre faxräknare är
sparade i Lokalise och återlästa där. Övriga texter i batch 41–45 var redan
korrekta vid den oberoende verifieringen.

Batch 48 omfattar 30 sparade och återlästa patronfält för svart, cyan,
magenta, trefärg och gul patron. Påfyllningsräknare är medvetet utelämnade
i väntan på en tydligare betydelsekontroll. Den kontrollen är nu genomförd:
batch 50 omfattar tio sparade och återlästa diagnostiska
påfyllningsräknare.
