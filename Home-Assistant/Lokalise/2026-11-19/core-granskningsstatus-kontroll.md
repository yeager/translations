# Kontroll av Core-granskningens lokala status

Kontrollerad 2026-11-19 mot den lokala rapportlistan i `ha-core/README.md` och dess länkade filer. Detta är en kontroll av dokumentationen, inte en verifiering av Lokalises aktuella innehåll.

- Rapportlistan når position 38 718 i en äldre sorteringsögonblicksbild. Positionsnummer är inte stabila när nycklar tillkommer eller försvinner.
- Position 38 555–38 564 saknar ett rapporterat intervall i den lokala listan och måste undersökas mot nycklar och aktuell Lokalise-ordning. Det går inte att utifrån positionsluckan ensamt fastställa om enskilda nycklar har granskats i andra rapporter.
- Fjorton rapportlänkar för 31 381–33 060 förekom två gånger i den lokala översikten. Dubbletterna har tagits bort lokalt; samtliga länkade Markdown-filer fanns lokalt vid kontrollen.
- Översiktens inledning angav tidigare 37 084 trots att listan nådde längre. Den har korrigerats lokalt utan att hävda sammanhängande täckning.
- Den senast dokumenterade lokala rapporten är `granskning-38715-38718.md`; den anger äldre nästa nyckel-ID 650052831. Kontrollera aktuell ordning och tidigare dokumentation innan fortsatt granskning.

Öppna uppgifter: kontrollera luckan och överlapp mellan rapporter på faktisk fullständig nyckel, undersök ändrade och nytillkomna strängar mot aktuell källa, och säkerställ att samtliga lokala rapporter är kopierade till detta arkiv. Ingen översättning ändrades i Lokalise vid denna kontroll.

## Uppföljning av positionsluckan

Den [kompletterande Matter-rapporten](matter-uppfoljning-2026-11-19.md) innehåller tio redan dokumenterade nycklar som kan motsvara intervallet. Livekontroll i Lokalise den 19 november visade att `esa_state::state::fault` och `esa_state::name` direkt följer `esa_state::state::offline` i sökresultatens ordning. Referensmålet `common::state::fault` är ”Fault” / ”Fel”, i enlighet med rapporten. Antalet och de första nycklarna ger stöd för sambandet, men bevisar inte att alla tio positioner motsvarar rapporten: verifiera hela ordningen mot den äldre exporten eller jämför faktiska nycklar innan luckan stängs. Inga översättningar ändrades.

## Miele och Immich

[Granskningen av två Miele- och tio Immich-sensorer](granskning-miele-immich-2026-11-19.md) jämför aktuell Lokalise-text med den historiska TMX:en. Mieles procentvärdens innebörd och den ofiltrerade ordningen kring grupperna återstår att kontrollera. Inga Lokalise-ändringar gjordes.

[Immichs konfiguration och tre referensmål](granskning-immich-konfiguration-2026-11-19.md) har granskats. Sju gemensamma Home Assistant-referensmål och SSL-förslagets terminologi har därefter kontrollerats; rapporten dokumenterar resultaten. Förslaget är inte sparat i Lokalise.

[YoLink, homee och Eheim](granskning-yolink-homee-eheim-2026-11-19.md): tio strängar kontrollerade, två lokala YoLink-förslag tillagda i separat förslagsminne. homee-textens kontext och ofiltrerad ordning återstår att verifiera.

## Sparning påbörjad

Efter användarens instruktion att spara ändringarna har [tre översättningar sparats och återlästs](sparade-andringar-yolink-immich.md). Tidigare uppgifter om osparade förslag avser läget före denna batch. Övriga rapporterade förslag måste jämföras med aktuell Lokalise-text och sparas efter kontroll. Den felaktiga tillfälliga YoLink-versionen kan finnas kvar i Lokalises översättningsminne och behöver följas upp.

Ytterligare [två SwitchBot-översättningar](sparade-andringar-switchbot.md) är sparade och återlästa. Totalt fem sparade i dessa två batcher; övriga förslag återstår.

Ytterligare tre SwitchBot-feltexter sparades och återlästes, dokumenterade i [ändringsloggen](sparade-andringar-switchbot.md). Totalt åtta sparade poster i de senaste batcherna; övriga förslag återstår.

Fem [Miele-programnamn](sparade-andringar-miele.md) sparades och återlästes. Totalt 13 poster har sparats i de senaste batcherna. Den separata TMX-filen för osparade förslag är nu tom, men många förslag finns fortfarande i granskningsrapporterna och återstår att kontrollera och spara.

Två [gemensamma kalenderbeskrivningar](sparade-andringar-judisk-kalender.md) sparades och återlästes. Totalt 15 ändringar har sparats i de senaste batcherna; övriga förslag återstår.

En [Probe Plus-beskrivning](sparade-andringar-probe-plus.md) har sparats och återlästs. Totalt 16 ändringar i de senaste batcherna; övriga förslag återstår.

Fyra [Probe Plus-sensornamn](sparade-andringar-probe-plus.md) sparades och återlästes med `{slot}` bevarad. Totalt 20 ändringar i de senaste batcherna; övriga förslag återstår.

En [Bosch Alarm-beskrivning](sparade-andringar-bosch-alarm.md) sparades och återlästes. Totalt 21 ändringar i de senaste batcherna; övriga förslag återstår.

Ett [solnedgångsfel](sparade-andringar-judisk-kalender.md) sparades och återlästes. Totalt 22 ändringar i de senaste batcherna; övriga förslag återstår.

Ett [säkerhetskopieringsmeddelande](sparade-andringar-backup.md) sparades och återlästes med formatering och platshållare bevarade. Totalt 23 ändringar i de senaste batcherna; övriga förslag återstår.

Två [SmartThings-centrifugeringslägen](sparade-andringar-smartthings.md) sparades och återlästes. Totalt 25 ändringar i de senaste batcherna; övriga förslag återstår.

Tre [SmartThings-texter för smutsgrad](sparade-andringar-smartthings.md) sparades och återlästes. Totalt 28 ändringar i de senaste batcherna; övriga förslag återstår.

Två [Met Office-texter](sparade-andringar-metoffice.md) sparades och återlästes, med länkmålet bevarat. Totalt 30 ändringar i de senaste batcherna; övriga förslag återstår.

Tre [Squeezebox-feltexter](sparade-andringar-squeezebox.md) sparades och återlästes med platshållarna bevarade. Totalt 33 ändringar i de senaste batcherna; det fjärde Squeezebox-förslaget och övriga förslag återstår.

Den fjärde [Squeezebox-feltexten](sparade-andringar-squeezebox.md) sparades och återlästes med `{host}` bevarad. Totalt 34 ändringar i de senaste batcherna; övriga förslag återstår.

Två [Wallbox-texter](sparade-andringar-wallbox.md) sparades och återlästes. Totalt 36 ändringar i de senaste batcherna; övriga förslag återstår.

En [Matter-text om automatisk återlåsning](sparade-andringar-matter.md) sparades och återlästes. Totalt 37 ändringar i de senaste batcherna; övriga förslag återstår.

Tre [MQTT-beskrivningar](sparade-andringar-mqtt.md) sparades och återlästes. Totalt 40 ändringar i de senaste batcherna; övriga förslag återstår.

Tre [MQTT-tillstånd](sparade-andringar-mqtt.md) sparades och återlästes. Totalt 43 ändringar i de senaste batcherna; övriga förslag återstår.

Två [MQTT-tillstånd för öppning och stängning](sparade-andringar-mqtt.md) sparades och återlästes. Totalt 45 ändringar i de senaste batcherna; övriga förslag återstår.

Tre [MQTT-fältnamn](sparade-andringar-mqtt.md) sparades och återlästes. Totalt 48 ändringar i de senaste batcherna; övriga förslag återstår.

Ett [MQTT-fältnamn för stopp av lutning](sparade-andringar-mqtt.md) sparades och återlästes. Totalt 49 ändringar i de senaste batcherna; övriga förslag återstår.

En [MQTT-hjälptext för stopp av lutning](sparade-andringar-mqtt.md) sparades och återlästes. Totalt 50 ändringar i de senaste batcherna; övriga förslag återstår.

Tre [MQTT-fel om position](sparade-andringar-mqtt.md) sparades och återlästes med ordlistans term ”topic”. Totalt 53 ändringar i de senaste batcherna; övriga förslag återstår.

Tre [MQTT-feltexter](sparade-andringar-mqtt.md) anpassades till ordlistans ”topic”, sparades och återlästes. Totalt 56 ändringar i de senaste batcherna; övriga förslag återstår.

[Mallbeskrivningen för MQTT-position](sparade-andringar-mqtt.md) sparades och återlästes med ursprungliga variabelnamn och länkmål. Totalt 57 ändringar i de senaste batcherna; övriga förslag återstår.

Tre [MQTT-positionsfält](sparade-andringar-mqtt.md) sparades och återlästes. Totalt 60 ändringar i de senaste batcherna; övriga förslag återstår.

Två [beskrivningar av MQTT-positionsvärden](sparade-andringar-mqtt.md) sparades och återlästes. Totalt 62 ändringar i de senaste batcherna; övriga förslag återstår.

Två [fältnamn för MQTT-positionsvärden](sparade-andringar-mqtt.md) sparades och återlästes. Totalt 64 ändringar i de senaste batcherna; övriga förslag återstår.

En [MQTT-mallbeskrivning för positionsvärde](sparade-andringar-mqtt.md) sparades och återlästes med variabler och länkmål bevarade. Totalt 65 ändringar i de senaste batcherna; övriga förslag återstår.

En [beskrivning av MQTT-topic för position](sparade-andringar-mqtt.md) sparades och återlästes med länkmålet bevarat. Totalt 66 ändringar i de senaste batcherna; övriga förslag återstår.

Två [MQTT-hjälptexter för tillstånd](sparade-andringar-mqtt.md) sparades och återlästes. Totalt 68 ändringar i de senaste batcherna; övriga förslag återstår.

Tre [MQTT-tillståndsbeskrivningar](sparade-andringar-mqtt.md) sparades och återlästes. Totalt 71 ändringar i de senaste batcherna; övriga förslag återstår.

En [MQTT-hjälptext för positionskommandon](sparade-andringar-mqtt.md) sparades och återlästes med villkor och länkmål bevarade. Totalt 72 ändringar i de senaste batcherna; övriga förslag återstår.

Två [MQTT-lutningsfält](sparade-andringar-mqtt.md) sparades och återlästes. Totalt 74 ändringar i de senaste batcherna; övriga förslag återstår.

En [MQTT-hjälptext för stängd lutning](sparade-andringar-mqtt.md) sparades och återlästes. Totalt 75 ändringar i de senaste batcherna; övriga förslag återstår.

En [MQTT-hjälptext för öppen lutning](sparade-andringar-mqtt.md) sparades och återlästes. Totalt 76 ändringar i de senaste batcherna; övriga förslag återstår.

Två [MQTT-topicfält för lutning](sparade-andringar-mqtt.md) sparades och återlästes. Totalt 78 ändringar i de senaste batcherna; övriga förslag återstår.

En [MQTT-beskrivning för lutningsstatus](sparade-andringar-mqtt.md) sparades och återlästes med länkmålet bevarat. Totalt 79 ändringar i de senaste batcherna; övriga förslag återstår.

En [mallbeskrivning för MQTT-lutningsstatus](sparade-andringar-mqtt.md) sparades och återlästes med variabler och länkar bevarade. Totalt 80 ändringar i de senaste batcherna; övriga förslag återstår.

En [beskrivning av optimistiskt lutningsläge](sparade-andringar-mqtt.md) sparades och återlästes med länkmålet bevarat. Totalt 81 ändringar i de senaste batcherna; övriga förslag återstår.

En [hjälptext för MQTT-lutningskommandon](sparade-andringar-mqtt.md) sparades och återlästes med länkmålet bevarat. Totalt 82 ändringar i de senaste batcherna; övriga förslag återstår.

En [mallbeskrivning för lutningskommandon](sparade-andringar-mqtt.md) sparades och återlästes med variabler och länkar bevarade. Totalt 83 ändringar i de senaste batcherna; övriga förslag återstår.

Två [MQTT-texter för oscillation](sparade-andringar-mqtt.md) sparades och återlästes. Totalt 85 ändringar i de senaste batcherna; övriga förslag återstår.

Fyra [MQTT-beskrivningar för oscillation](sparade-andringar-mqtt.md) sparades och återlästes med länkar och platshållare bevarade. Totalt 89 ändringar i de senaste batcherna; övriga förslag återstår.

Fem [MQTT-texter för fläktriktning](sparade-andringar-mqtt.md) sparades och återlästes med länkar och kodvärden bevarade. Totalt 94 ändringar i de senaste batcherna; övriga förslag återstår.

Sju [MQTT-texter för förinställda fläktlägen](sparade-andringar-mqtt.md) sparades och återlästes. Flera klimatnycklar hänvisar till dessa mål. Totalt 101 ändringar i de senaste batcherna; övriga förslag återstår.

Fyra [MQTT-beskrivningar för förinställda fläktlägen](sparade-andringar-mqtt.md) sparades och återlästes med länkar och platshållare bevarade. Totalt 105 ändringar i de senaste batcherna; övriga förslag återstår.

Tre [MQTT-texter för stöd och återställning av förinställda lägen](sparade-andringar-mqtt.md) sparades och återlästes. Totalt 108 ändringar i de senaste batcherna; övriga förslag återstår.

Två [Matter-texter för pumpens driftlägen](sparade-andringar-matter.md) sparades och återlästes; referensmålet för normalläget kontrollerades. Totalt 110 ändringar i de senaste batcherna; övriga förslag återstår.

Fyra [referenser för historikstatistik](sparade-andringar-history-stats.md) återställdes och lästes tillbaka; sex gemensamma mål kontrollerades. En fråga om tekniska värden i typbeskrivningen återstår. Totalt 114 ändringar i de senaste batcherna; övriga förslag återstår.

[Uppföljningen av typvärden](sparade-andringar-history-stats.md) visade att väljaren har översatta etiketter ”Tid”, ”Kvot” och ”Antal”; beskrivningen behölls. Inga ytterligare Lokalise-ändringar gjordes vid kontrollen.

Två [referenser för skyddens hastighet](sparade-andringar-cover.md) återställdes och lästes tillbaka. Markisens referensmål kontrollerades; övriga mål och ytterligare referensavvikelser återstår. Totalt 116 ändringar i de senaste batcherna.

[Fördröjningen för en Matter-närvarosensor](sparade-andringar-matter.md) sparades och återlästes. Ett av två [hastighetsreferensmål](sparade-andringar-cover.md) kontrollerades direkt; det andra återstår. Totalt 117 ändringar i de senaste batcherna.

En [Amazon Devices-text om engångskoder](sparade-andringar-amazon-devices.md) sparades och återlästes. Totalt 118 ändringar i de senaste batcherna; ytterligare förslag återstår.

Sex [MQTT-texter för fläkthastighet](sparade-andringar-mqtt.md) sparades och återlästes med länkar och platshållare bevarade. Totalt 124 ändringar i de senaste batcherna; övriga förslag återstår.

Två [MQTT-texter om procenttillstånd och värdemall](sparade-andringar-mqtt.md) sparades och återlästes. Totalt 126 ändringar i de senaste batcherna; övriga förslag återstår.

En [Android TV-anvisning för appikoner](sparade-andringar-androidtv.md) sparades och återlästes med sökvägar bevarade. Menyvalets exakta benämning återstår att följa upp. Totalt 127 ändringar i de senaste batcherna.

Två [MQTT-beskrivningar av inkommande tillstånd](sparade-andringar-mqtt.md) sparades och återlästes. Totalt 129 ändringar i de senaste batcherna; övriga förslag återstår.

En [MQTT-beskrivning av prenumeration på tillstånd](sparade-andringar-mqtt.md) sparades och återlästes med platshållare och länk bevarade. Totalt 130 ändringar i de senaste batcherna; övriga förslag återstår.

[Amazon-flödets gemensamma referensmål](sparade-andringar-amazon-devices.md) kontrollerades. En möjlig felaktig källreferens för kodfältets etikett och integrationens status på utvecklingsgrenen behöver följas upp. Ingen Lokalise-ändring gjordes vid kontrollen.

Ett [separat verifierat Core-TMX-tillägg](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx) publicerades med fyra tidigare sparade MQTT-översättningar. Format, nycklar, språkpar, platshållare och länkmål kontrollerades; övriga sparade ändringar återstår att föra in. Den äldre exporten är oförändrad. Ingen ny Lokalise-ändring gjordes vid denna uppdatering.

[Det verifierade Core-TMX-tillägget](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx) utökades från fyra till 67 unika språkpar från fem ändringsloggar. XML, språkpar, nycklar, platshållare och länkmål kontrollerades, och de tidigare fyra posterna jämfördes. Ändringar utan tillräckligt strukturerade källpar och övriga loggar återstår. Ingen ny Lokalise-ändring gjordes i denna uppföljning.

[Det verifierade Core-TMX-tillägget](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx) utökades från 67 till 94 språkpar genom tio ytterligare ändringsloggar, inklusive den flerradiga säkerhetskopieringstexten. Tidigare par, XML, unika nycklar, språkpar, platshållare och länkmål kontrollerades. Resterande dokumenterade ändringar återstår att föra in. Ingen ny Lokalise-ändring gjordes vid uppföljningen.

[MQTT-loggen](sparade-andringar-mqtt.md) kompletterades med engelska källtexter från tre tidigare granskningsrapporter för 20 redan sparade texter. De lades till i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), som nu innehåller 114 språkpar; XML och tidigare par kontrollerades. Ingen ny Lokalise-ändring gjordes i denna uppföljning.

[Core-TMX-tillägget](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx) innehåller nu 115 språkpar; MQTT-loggens tabellförda sparade nycklar finns med, liksom dess separat dokumenterade prenumerationstext. Sex återställda nyckelreferenser i skydds- och historikloggarna behandlas separat och förs inte in som textsegment. Ytterligare avstämning av övriga ändringsloggar återstår. Ingen ny Lokalise-ändring gjordes.

Avstämning av de 17 ändringsloggarna i denna katalog gav 130 unika dokumenterade nycklar: 124 textpar i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx) och sex återställda referenser som dokumenteras separat. Nio MQTT-beskrivningar lades till efter jämförelse av kodvariabler, platshållare och länkmål. XML och tidigare par validerades. Detta avser endast dessa loggar, inte hela Core eller andra datum. Ingen ny Lokalise-ändring gjordes vid avstämningen.

## Kontroll av minnestilläggets innehåll och releaseunderlag

Samtliga 124 engelska och svenska segment i [Core-TMX-tillägget](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx) jämfördes med de 17 sparloggarna i denna katalog. 123 par matchade tabell- eller textposter och det flerradiga säkerhetskopieringsparet matchade separat de två kodblocken, inklusive radbrytningar. Avstämningen kontrollerar dokumenterad överensstämmelse, inte om Lokalise har ändrats sedan återläsningen.

Senaste [swedish-tm-releasen v1.1.8](https://github.com/yeager/swedish-tm/releases/tag/v1.1.8) ligger 664 commits bakom huvudgrenen enligt GitHubs jämförelse vid kontrollen. Skillnaden omfattar även omfattande Blender-, QGIS- och annat arbete. En release av hela huvudgrenen kräver därför kontroll av mer än HA-tillägget; någon ny release gjordes inte i denna kontroll.

Fyra [Miele-programnamn för kakor](sparade-andringar-miele.md) sparades och återlästes. Totalt 134 ändringar i de senaste batcherna; de fyra nya textparen återstår att lägga in i Core-TMX.

De fyra nya Miele-programnamnen har lagts till i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), som nu innehåller 128 språkpar. XML och de tidigare 124 paren kontrollerades.

Två [Miele-programnamn för matpaj](sparade-andringar-miele.md) sparades och återlästes samt lades till i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML och tidigare par kontrollerades. Totalt 136 ändringar i de senaste batcherna, inklusive sex referenser; TMX innehåller 130 språkpar.

Två [Miele-programnamn för fruktpaj](sparade-andringar-miele.md) sparades och återlästes samt lades till i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML och tidigare par kontrollerades. Totalt 138 ändringar i de senaste batcherna, inklusive sex referenser; TMX innehåller 132 språkpar.

Två [Miele-programnamn för Linzer Augen](sparade-andringar-miele.md) sparades och återlästes samt lades till i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML och tidigare par kontrollerades. Totalt 140 ändringar i de senaste batcherna, inklusive sex referenser; TMX innehåller 134 språkpar.

Två [Miele-programnamn för frallor](sparade-andringar-miele.md) sparades och återlästes samt lades till i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML och tidigare par kontrollerades. Totalt 142 ändringar i de senaste batcherna, inklusive sex referenser; TMX innehåller 136 språkpar.

Två [Miele-programnamn för fläsk och gratäng](sparade-andringar-miele.md) sparades och återlästes samt lades till i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML och tidigare par kontrollerades. Totalt 144 ändringar i de senaste batcherna, inklusive sex referenser; TMX innehåller 138 språkpar.

Två [Miele-programnamn för gås](sparade-andringar-miele.md) sparades och återlästes samt lades till i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML och tidigare par kontrollerades. Totalt 146 ändringar i de senaste batcherna, inklusive sex referenser; TMX innehåller 140 språkpar.

Två [Miele-programnamn för pizza](sparade-andringar-miele.md) sparades och återlästes samt lades till i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). Mieles recept stöder kvargtolkningen, men kopplingen till respektive nyckel är en bedömning och har märkts i minnet. XML och tidigare par kontrollerades. Totalt 148 ändringar i de senaste batcherna, inklusive sex referenser; TMX innehåller 142 språkpar.

Ett [Miele-programnamn för fruktkaka](sparade-andringar-miele.md) sparades och återlästes efter kontroll mot Mieles recept och lades till i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML och tidigare par kontrollerades. Totalt 149 ändringar i de senaste batcherna, inklusive sex referenser; TMX innehåller 143 språkpar.

Ett [Miele-programnamn](sparade-andringar-miele.md) ändrades till ”Pytt i panna” enligt användarens anvisning, sparades och återlästes i Lokalise och lades till i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML och tidigare par kontrollerades. Totalt 150 ändringar i de senaste batcherna, inklusive sex referenser; TMX innehåller 144 språkpar.

En [KACO Modbus-hjälptext](sparade-andringar-kaco-modbus.md) förtydligades och en referens återställdes; båda sparades och återlästes i Lokalise. Textparet fördes in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster kontrollerades. Totalt 152 ändringar i de senaste batcherna, inklusive sju referenser; TMX innehåller 145 språkpar.

En [MCP Server-text om administratörskonton](sparade-andringar-mcp-server.md) kompletterades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster kontrollerades. Totalt 153 ändringar i de senaste batcherna, inklusive sju referenser; TMX innehåller 146 språkpar.

En [Sofar-benämning för Modbus-enhets-ID](sparade-andringar-sofar.md) sparades och återlästes i Lokalise. Textparet lades till i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster kontrollerades. Totalt 154 ändringar i de senaste batcherna, inklusive sju referenser; TMX innehåller 147 språkpar.

Ett [Sunsynk-sensornamn](sparade-andringar-sunsynk.md) anpassades till rapportens skrivning ”i dag”, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster kontrollerades. Totalt 155 ändringar i de senaste batcherna, inklusive sju referenser; TMX innehåller 148 språkpar. Övriga Sunsynk-förslag återstår.

En [Peblar-text om uppdateringsordning](sparade-andringar-peblar.md) sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster kontrollerades. Totalt 156 ändringar i de senaste batcherna, inklusive sju referenser; TMX innehåller 149 språkpar.

En [Gemini-beskrivning och två referenser](sparade-andringar-google-generative-ai.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster kontrollerades. Totalt 159 ändringar i de senaste batcherna, inklusive nio referenser; TMX innehåller 150 språkpar. Andra referensavvikelser i Gemini-gruppen återstår att granska.

En [Music Assistant-beskrivning](sparade-andringar-music-assistant.md) kompletterades, sparades och återlästes i Lokalise. Textparet lades till i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster kontrollerades. Totalt 160 ändringar i de senaste batcherna, inklusive nio referenser; TMX innehåller 151 språkpar.

En [Green Planet Energy-text om prisintervall](sparade-andringar-green-planet-energy.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster kontrollerades. Totalt 161 ändringar i de senaste batcherna, inklusive nio referenser; TMX innehåller 152 språkpar.

En [Fish Audio-text om talhastighet](sparade-andringar-fish-audio.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster kontrollerades. Totalt 162 ändringar i de senaste batcherna, inklusive nio referenser; TMX innehåller 153 språkpar.

Ett [Teslemetry-sensornamn](sparade-andringar-teslemetry.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster kontrollerades. Totalt 163 ändringar i de senaste batcherna, inklusive nio referenser; TMX innehåller 154 språkpar.

Två tidigare tomma [Music Assistant-felmeddelanden](sparade-andringar-music-assistant.md) översattes, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster kontrollerades. Totalt 165 ändringar i de senaste batcherna, inklusive nio referenser; TMX innehåller 156 språkpar. Ytterligare ett tomt felmeddelande behöver terminologikontroll.

Tre [Music Assistant-texter](sparade-andringar-music-assistant.md) för favoritfilter och offset sparades och återlästes i Lokalise; den tidigare offsetfrågan är utredd mot aktuella fältnamn. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster kontrollerades. Totalt 168 ändringar i de senaste batcherna, inklusive nio referenser; TMX innehåller 159 språkpar.

Sex tidigare tomma [Music Assistant-köfält](sparade-andringar-music-assistant.md) fylldes, sparades och återlästes i Lokalise: tre beskrivningar och tre referenser. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster kontrollerades. Totalt 174 ändringar i de senaste batcherna, inklusive tolv referenser; TMX innehåller 162 språkpar.

Två tidigare tomma [Jellyfin-meddelanden](sparade-andringar-jellyfin.md) översattes, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster kontrollerades. Totalt 176 ändringar i de senaste batcherna, inklusive tolv referenser; TMX innehåller 164 språkpar.

Två tidigare tomma [Lyric-texter om nödvärme](sparade-andringar-lyric.md) översattes, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster kontrollerades. Totalt 178 ändringar i de senaste batcherna, inklusive tolv referenser; TMX innehåller 166 språkpar.

Två tidigare tomma [Switcher KIS-sensornamn](sparade-andringar-switcher-kis.md) översattes, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster kontrollerades. Totalt 180 ändringar i de senaste batcherna, inklusive tolv referenser; TMX innehåller 168 språkpar. Tillhörande nya reparationsmeddelanden återstår att översätta.

Fyra tidigare tomma [Switcher KIS-reparationsrubriker](sparade-andringar-switcher-kis.md) fylldes, sparades och återlästes i Lokalise: två texter och två referenser. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster kontrollerades. Totalt 184 ändringar i de senaste batcherna, inklusive fjorton referenser; TMX innehåller 170 språkpar. Fyra längre beskrivningar återstår.

En tidigare tom [Switcher KIS-reparationsinstruktion](sparade-andringar-switcher-kis.md) översattes, sparades och återlästes i Lokalise med variabler och stycken bevarade. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, variabler, stycken och tidigare poster kontrollerades. Totalt 185 ändringar i de senaste batcherna, inklusive fjorton referenser; TMX innehåller 171 språkpar. Tre längre beskrivningar återstår.

En tidigare tom [Switcher-instruktion för automationer och skript](sparade-andringar-switcher-kis.md) översattes, sparades och återlästes i Lokalise med variabler och stycken bevarade. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, variabler, stycken och tidigare poster kontrollerades. Totalt 186 ändringar i de senaste batcherna, inklusive fjorton referenser; TMX innehåller 172 språkpar. Två beskrivningar återstår i Switcher-gruppen.

Två tidigare tomma [Switcher-instruktioner om automatisk avstängning](sparade-andringar-switcher-kis.md) översattes, sparades och återlästes i Lokalise med variabler och stycken bevarade. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, variabler, stycken och tidigare poster kontrollerades. Totalt 188 ändringar i de senaste batcherna, inklusive fjorton referenser; TMX innehåller 174 språkpar. De åtta nycklarna i denna reparationsgrupp har nu svenska fält.

Tre tidigare tomma [my-PV-fält](sparade-andringar-my-pv.md) fylldes, sparades och återlästes i Lokalise: två rubriker och en referens. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, variabler och tidigare poster kontrollerades. Totalt 191 ändringar i de senaste batcherna, inklusive femton referenser; TMX innehåller 176 språkpar. Tre ytterligare my-PV-referenser återstår att kontrollera.

En tidigare tom [my-PV-referens för värdbeskrivning](sparade-andringar-my-pv.md) fylldes, sparades och återlästes i Lokalise efter kontroll av målet. Totalt 192 ändringar i de senaste batcherna, inklusive sexton referenser; Core-TMX innehåller fortsatt 176 språkpar. Två gemensamma referensmål återstår att kontrollera.

Två tidigare tomma [my-PV-referenser till gemensamma fältnamn](sparade-andringar-my-pv.md) fylldes, sparades och återlästes i Lokalise efter direkt kontroll av båda målen. Totalt 194 ändringar i de senaste batcherna, inklusive arton referenser; Core-TMX innehåller fortsatt 176 språkpar. De sex nycklarna i my-PV:s omkonfigurationsgrupp har svenska fält.

Två [Sofar-resultattexter](sparade-andringar-sofar.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster kontrollerades. Totalt 196 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 178 språkpar.

Två [Sofar-sensortexter](sparade-andringar-sofar.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster kontrollerades. Totalt 198 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 180 språkpar.

Två [Sofar-benämningar för reaktiv effekt](sparade-andringar-sofar.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster kontrollerades. Totalt 200 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 182 språkpar. Övriga effektförslag återstår.

Tre [Sofar-benämningar för reaktiv uteffekt per fas](sparade-andringar-sofar.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, fasbeteckningar och tidigare poster kontrollerades. Totalt 203 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 185 språkpar. Övriga effektförslag återstår.

Tre [Sofar-benämningar för effektfaktor per utgång](sparade-andringar-sofar.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, fasbeteckningar och tidigare poster kontrollerades. Totalt 206 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 188 språkpar. Övriga effektförslag återstår.

Tre [Sofar-benämningar för spänning vid ödrift](sparade-andringar-sofar.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, fasbeteckningar och tidigare poster kontrollerades. Totalt 209 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 191 språkpar. Övriga förslag återstår.

Tre [Sofar-benämningar för skenbar effekt vid ödrift](sparade-andringar-sofar.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, fasbeteckningar och tidigare poster kontrollerades. Totalt 212 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 194 språkpar. Övriga förslag återstår.

Tre [Sofar-benämningar för reaktiv effekt vid ödrift](sparade-andringar-sofar.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, fasbeteckningar och tidigare poster kontrollerades. Totalt 215 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 197 språkpar. Övriga förslag återstår.

Tre [Sofar-benämningar för aktiv effekt vid ödrift](sparade-andringar-sofar.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, fasbeteckningar och tidigare poster kontrollerades. Totalt 218 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 200 språkpar. De separata L1N- och L2N-fälten och övriga förslag återstår.

Två [Sofar-benämningar för aktiv effekt på L1N och L2N vid ödrift](sparade-andringar-sofar.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, fasbeteckningar och tidigare poster kontrollerades. Totalt 220 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 202 språkpar. Övriga förslag återstår.

En [Sofar-benämning för reaktiv effekt på utgången vid ödrift](sparade-andringar-sofar.md) sparades och återlästes i Lokalise, och lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML och tidigare poster verifierades. Ett tillfälligt felsparat värde rättades direkt; kontroll av Lokalises översättningsminne återstår. Totalt 221 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 203 språkpar. Övriga förslag återstår.

[Uppföljning av Sofars tillfälliga feltext](sparade-andringar-sofar.md): sökning i Lokalises anslutna översättningsminnen visade den korrigerade exakta källträffen; sökning efter det sammanfogade textfragmentet gav noll träffar. Ingen fullständig minnesexport gjordes. Övriga Sofar-förslag återstår.

Två [Sofar-benämningar för skenbar och aktiv effekt på utgången vid ödrift](sparade-andringar-sofar.md) sparades och återlästes i Lokalise och lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML och tidigare poster verifierades. Totalt 223 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 205 språkpar. Övriga förslag återstår.

En [Sofar-benämning för ström på utgången vid ödrift](sparade-andringar-sofar.md) sparades och återlästes i Lokalise och lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML och tidigare poster verifierades. Totalt 224 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 206 språkpar. Övriga förslag återstår.

Fem [Sofar-benämningar för utström vid ödrift](sparade-andringar-sofar.md) sparades och återlästes i Lokalise med L1, L2, L3, L1N och L2N bevarade och lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML, fasbeteckningar och tidigare poster verifierades. Totalt 229 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 211 språkpar. Övriga förslag återstår.

Fem [Sofar-benämningar för utström](sparade-andringar-sofar.md) sparades och återlästes i Lokalise med L1, L2, L3, L1N och L2N bevarade och lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML, fasbeteckningar och tidigare poster verifierades. Totalt 234 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 216 språkpar. Övriga förslag återstår.

Två [Sofar-benämningar för utspänning vid ödrift](sparade-andringar-sofar.md) sparades och återlästes i Lokalise med L1N och L2N bevarade och lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML, fasbeteckningar och tidigare poster verifierades. Totalt 236 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 218 språkpar. Övriga förslag återstår.

Två [Sofar-benämningar för spänning och frekvens vid ödrift](sparade-andringar-sofar.md) sparades och återlästes i Lokalise och lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML och tidigare poster verifierades. Totalt 238 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 220 språkpar. Övriga förslag återstår.

En [SimpliSafe-händelse för parkoppling av sensor](sparade-andringar-simplisafe.md) sparades och återlästes i Lokalise och lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML och tidigare poster verifierades. Sofars ”Importerad energi idag” kontrollerades och behölls: idag är en korrekt stavning. Totalt 239 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 221 språkpar. Övriga förslag återstår.

Två [Fronius-benämningar för AC-effekt](sparade-andringar-fronius.md) sparades och återlästes i Lokalise och lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML och tidigare poster verifierades. Separata Modbus-MPPT-texter med platshållaravvikelser behöver följas upp. Neopools serienummertext kontrollerades och behölls: pronomenet syftar på enheten. Totalt 241 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 223 språkpar. Övriga förslag återstår.

[Fronius Modbus-likspänning](sparade-andringar-fronius.md) rättades mot aktuell källa, sparades och återlästes i Lokalise och lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML och tidigare poster verifierades. Två andra fält återstår efter ett oväntat Lokalise-fel vid redigering. Totalt 242 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 224 språkpar.

De två återstående [Fronius Modbus-fälten för likström och effekt](sparade-andringar-fronius.md) rättades mot aktuell källa, sparades och återlästes i Lokalise och lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML och tidigare poster verifierades. Totalt 244 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 226 språkpar. Övriga förslag återstår.

Tre [HomematicIP Cloud-sensornamn](sparade-andringar-homematicip-cloud.md) rättades, sparades och återlästes i Lokalise och lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML och tidigare poster verifierades. Totalt 247 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 229 språkpar. Övriga förslag återstår.

Tre [ZhongHong-feltexter](sparade-andringar-zhong-hong.md) rättades, sparades och återlästes i Lokalise med platshållarna bevarade och lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML, platshållare och tidigare poster verifierades. Totalt 250 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 232 språkpar. Övriga förslag återstår.

Ett [ZhongHong-konfigurationsfel](sparade-andringar-zhong-hong.md) rättades, sparades och återlästes i Lokalise; avbrottsnyckelns referens till texten kontrollerades. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster verifierades. Totalt 251 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 233 språkpar. Övriga förslag återstår.

Två [Pushover-beskrivningar för avbrytande av nödmeddelanden](sparade-andringar-pushover.md) rättades, sparades och återlästes i Lokalise och lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML och tidigare poster verifierades. Totalt 253 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 235 språkpar. Övriga förslag återstår.

En [Cloud-bekräftelse om taltranskribering](sparade-andringar-cloud.md) rättades, sparades och återlästes i Lokalise och lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML och tidigare poster verifierades. Totalt 254 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 236 språkpar. Övriga förslag återstår.

Tre [Nexia RoomIQ-benämningar](sparade-andringar-nexia.md) rättades, sparades och återlästes i Lokalise och lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML och tidigare poster verifierades. Totalt 257 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 239 språkpar. Övriga förslag återstår.

En [UniFi Protect-beskrivning för API-nyckel](sparade-andringar-unifiprotect.md) rättades mot den aktuella källan, sparades och återlästes i Lokalise och lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML, platshållare och tidigare poster verifierades. Totalt 258 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 240 språkpar. Närliggande UniFi-förslag återstår.

En [UniFi Protect-beskrivning för upptäckt med API-nyckel](sparade-andringar-unifiprotect.md) rättades mot den aktuella källan, sparades och återlästes i Lokalise och lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML, tre platshållare och tidigare poster verifierades. Totalt 259 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 241 språkpar. Närliggande UniFi-förslag återstår.

En [UniFi Protect-beskrivning för omkonfigurering till API-nyckel](sparade-andringar-unifiprotect.md) rättades mot den aktuella källan, sparades och återlästes i Lokalise och lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). XML, platshållare och tidigare poster verifierades. Totalt 260 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 242 språkpar. Närliggande UniFi-förslag återstår.

Två [UniFi Protect-texter om lokala användare](sparade-andringar-unifiprotect.md) rättades, sparades och återlästes i Lokalise; tre referenser till användarnamnstexten kontrollerades. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster verifierades. Totalt 262 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 244 språkpar. Övriga förslag återstår.

En [UniFi Protect-beskrivning av API-nyckelfältet](sparade-andringar-unifiprotect.md) rättades, sparades och återlästes i Lokalise; tre referenser till texten kontrollerades. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster verifierades. Totalt 263 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 245 språkpar. Övriga förslag återstår.

Ett [Roborock-torkprogram](sparade-andringar-roborock.md) rättades, sparades och återlästes i Lokalise; mer specifikt ordval förutsätter kontroll av produktkontext. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster verifierades. Totalt 264 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 246 språkpar. Övriga förslag återstår.

Ett [Wattwächter-fel om inbyggd programvara](sparade-andringar-wattwaechter.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster verifierades. Totalt 265 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 247 språkpar. Övriga förslag återstår.

Två [AirGradient-benämningar för partikelantal](sparade-andringar-airgradient.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster verifierades. Totalt 267 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 249 språkpar. Övriga förslag återstår.

En [AirGradient-benämning för summer](sparade-andringar-airgradient.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster verifierades. Totalt 268 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 250 språkpar. Övriga förslag återstår.

Två [Silla Prism-benämningar för sessioner](sparade-andringar-silla-prism.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster verifierades. Totalt 270 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 252 språkpar. Övriga förslag återstår.

Ett [Remember The Milk-meddelande om inläsning av konto](sparade-andringar-remember-the-milk.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster verifierades. Totalt 271 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 253 språkpar. Övriga förslag återstår.

En [NeoPool-benämning för poolöverdrag](sparade-andringar-neopool.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster verifierades. Totalt 272 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 254 språkpar. Övriga förslag återstår.

Två [Silla Prism-feltexter för MQTT-topic](sparade-andringar-silla-prism.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster verifierades. Totalt 274 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 256 språkpar. Övriga förslag återstår.

Ett [Silla Prism-fältnamn för bastopic](sparade-andringar-silla-prism.md) rättades, sparades och återlästes i Lokalise; de relaterade beskrivningarna kontrollerades och behölls. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster verifierades. Totalt 275 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 257 språkpar. Övriga förslag återstår.

En [beskrivning av gyllene timmens början](sparade-andringar-sun.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster verifierades. Totalt 276 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 258 språkpar. Närliggande solbeskrivningar och periodväljaren återstår.

Tre [beskrivningar för gyllene och blå timmen](sparade-andringar-sun.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster verifierades. Totalt 279 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 261 språkpar. Periodväljaren och övriga förslag återstår.

[Periodväljarens alternativ Båda](sparade-andringar-sun.md) rättades, sparades och återlästes i Lokalise efter kontroll mot alternativen Morgon och Kväll. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster verifierades. Totalt 280 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 262 språkpar. Övriga förslag återstår.

Två [solvillkor för gyllene och blå timmen](sparade-andringar-sun.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster verifierades. Totalt 282 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 264 språkpar. Övriga förslag återstår.

[Solens gemensamma periodbeskrivning](sparade-andringar-sun.md) rättades, sparades och återlästes i Lokalise; sex referenser kontrollerades. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML och tidigare poster verifierades. Totalt 283 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 265 språkpar. Övriga förslag återstår.

Tre [Guntamatic-temperaturer för extra varmvatten](sparade-andringar-guntamatic.md) rättades, sparades och återlästes i Lokalise med kretsbeteckningar bevarade. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML, platshållare och tidigare poster verifierades. Totalt 286 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 268 språkpar. Övriga förslag återstår.

Tre [Guntamatic-temperaturer för varmvattenkretsar](sparade-andringar-guntamatic.md) rättades, sparades och återlästes i Lokalise; krets 0 kontrollerades och behölls. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx), vars XML, platshållare och tidigare poster verifierades. Totalt 289 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 271 språkpar. Övriga förslag återstår.

Två [temperaturer för Guntamatics buffertsteg](sparade-andringar-guntamatic.md) rättades, sparades och återlästes i Lokalise med `{tank}` bevarad. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 291 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 273 språkpar. Övriga förslag återstår.

Nio [Guntamatic-bufferttemperaturer](sparade-andringar-guntamatic.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 300 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 282 språkpar. Övriga förslag återstår.

Tre [Guntamatic-rumstemperaturer](sparade-andringar-guntamatic.md) rättades, sparades och återlästes i Lokalise med rumsnumren bevarade. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 303 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 285 språkpar. Övriga förslag återstår.

Tre [NexBlue-texter om energi och laddningsstatus](sparade-andringar-nexblue.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 306 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 288 språkpar från 46 ändringsloggar. Övriga förslag återstår.

Tre [Specialized Turbo-termer för cykelns sensorer](sparade-andringar-specialized-turbo.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 309 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 291 språkpar från 47 ändringsloggar. Övriga förslag återstår.

Tre [Specialized Turbo-texter om installation och parkoppling](sparade-andringar-specialized-turbo.md) rättades, sparades och återlästes i Lokalise. Platshållarna bevarades. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 312 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 294 språkpar. Övriga förslag återstår.

Två [Guntamatic-värmeprograms temperatursänkningslägen](sparade-andringar-guntamatic.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 314 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 296 språkpar. Övriga förslag återstår.

Fyra [Forecast.Solar-beskrivningar](sparade-andringar-forecast-solar.md) rättades, sparades och återlästes i Lokalise, inklusive de olika start- och slutgränserna. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 318 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 300 språkpar från 48 ändringsloggar. Övriga förslag återstår.

Två [Midea-namn för vattenförbrukning](sparade-andringar-midea.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 320 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 302 språkpar från 49 ändringsloggar. Övriga förslag återstår.

[Mideas färskvaruläge](sparade-andringar-midea.md) rättades, sparades och återlästes i Lokalise. Det oklara frysläget kräver fortsatt funktionskontroll. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 321 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 303 språkpar. Övriga förslag återstår.

[Mideas risprogram](sparade-andringar-midea.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 322 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 304 språkpar. Övriga förslag återstår.

[Fronius batteriladdning från elnätet](sparade-andringar-fronius.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 323 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 305 språkpar. Övriga förslag återstår.

[Två Midea-filtertexter](sparade-andringar-midea.md) rättades, sparades och återlästes i Lokalise med `{filter_number}` bevarad. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 325 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 307 språkpar. Övriga förslag återstår.

[Mideas centrifugeringstid](sparade-andringar-midea.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 326 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 308 språkpar. Övriga förslag återstår.

[Mideas varmhållningstid](sparade-andringar-midea.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 327 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 309 språkpar. Övriga förslag återstår.

[Två Midea-program för ris och risgröt](sparade-andringar-midea.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 329 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 311 språkpar. Övriga förslag återstår.

[Mideas puréprogram](sparade-andringar-midea.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 330 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 312 språkpar. Övriga förslag återstår.

[Mideas spannmålsprogram](sparade-andringar-midea.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 331 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 313 språkpar. Övriga förslag återstår.

[Mideas lergryteprogram](sparade-andringar-midea.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 332 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 314 språkpar. Övriga förslag återstår.

[Mideas aromatiska risgrötsprogram](sparade-andringar-midea.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 333 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 315 språkpar. Övriga förslag återstår.

[Fyra Reolink-texter om drift och inspelning](sparade-andringar-reolink.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 337 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 319 språkpar från 50 ändringsloggar. Övriga förslag återstår.

[Victron GX strömgräns för AC-ingång](sparade-andringar-victron-gx.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 338 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 320 språkpar från 51 ändringsloggar. Övriga förslag återstår.

Vid ny kontroll av Sofar i Lokalise hade de äldre förslagen för `system_state::state::grid_connected`, `sync_rtc_result::state::operation_in_progress`, `sync_rtc_result::state::operation_failed_controller_refused_to_respond` samt `reactive_power_output_total::name`, `reactive_power_output_l1::name` och `reactive_power_offgrid_total::name` redan motsvarande svenska texter. De behölls utan ändring den 19 november 2026. Den äldre rapporten för position 12241–12360 är en historisk ögonblicksbild och ska inte användas som underlag för att upprepa dessa ändringar utan ny kontroll.

[Fronius gräns för batteriets urladdningseffekt](sparade-andringar-fronius.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 339 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 321 språkpar. Övriga förslag återstår.

[Fronius Modbus-meddelande om saknad modell](sparade-andringar-fronius.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 340 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 322 språkpar. Övriga förslag återstår.

[Fronius Modbus-port](sparade-andringar-fronius.md) rättades, sparades och återlästes i Lokalise; en relaterad referens kontrollerades och behölls. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML och tidigare poster verifierades. Totalt 341 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 323 språkpar. Övriga förslag återstår.

Sex [TP-Link Omada-felmeddelanden](sparade-andringar-tplink-omada.md) rättades, sparades och återlästes i Lokalise med `{mac}` bevarad. Den tillfälliga sammanfogningen av gamla och nya texter korrigerades före återläsningen. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 347 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 329 språkpar från 52 ändringsloggar. Övriga förslag återstår.

Två ytterligare [TP-Link Omada-meddelanden om saknade styrenheter](sparade-andringar-tplink-omada.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 349 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 331 språkpar. Övriga förslag återstår.

Fyra [UniFi Protect-texter för föråldrade sensorinställningar](sparade-andringar-unifiprotect.md) rättades, sparades och återlästes i Lokalise. Platshållarna och kodmarkeringarna bevarades. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 353 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 335 språkpar. Övriga förslag återstår.

Tre [radartexter för Environment Canada](sparade-andringar-environment-canada.md) rättades, sparades och återlästes i Lokalise; bildfrekvensens beskrivning kontrollerades. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 356 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 338 språkpar från 53 ändringsloggar. Övriga förslag återstår.

Tre [Sofar-texter för modellidentifiering och anslutning](sparade-andringar-sofar.md) rättades, sparades och återlästes i Lokalise. Föråldrade platshållare togs bort enligt aktuell källtext. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 359 ändringar i de senaste batcherna, inklusive arton referenser; TMX innehåller 341 språkpar. Flera Sofar-referenser i konfigurationsstegen skiljer sig från källan och kräver uppföljning. Övriga förslag återstår.

Fyra [Sofar-referenser för värd och port](sparade-andringar-sofar.md) återställdes och återlästes i Lokalise efter kontroll av de gemensamma målen. Totalt 363 ändringar i de senaste batcherna, inklusive 22 referenser; TMX innehåller fortsatt 341 textpar. Övriga Sofar-referenser och andra förslag återstår.

Sex [Sofar-referenser för Modbus-enhets-ID och dess beskrivning](sparade-andringar-sofar.md) återställdes och återlästes i Lokalise efter kontroll av måltexterna. Totalt 369 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller fortsatt 341 textpar. Övriga förslag återstår.

[Sofars modellfel vid konfiguration](sparade-andringar-sofar.md) kompletterades med registermasker enligt källan, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 370 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 342 språkpar. Övriga förslag återstår.

[Modern Forms brisintensitet](sparade-andringar-modern-forms.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 371 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 343 språkpar från 54 ändringsloggar. Övriga förslag återstår.

[Lyngdorfs feltext för fjärrkontrollknapp](sparade-andringar-lyngdorf.md) rättades, sparades och återlästes i Lokalise med `{keys}` bevarad. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 372 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 344 språkpar från 55 ändringsloggar. Övriga förslag återstår.

Fyra [SmartThings-diskprogram](sparade-andringar-smartthings.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 376 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 348 språkpar. Övriga förslag återstår.

[SmartThings fältnamn för diskprogram](sparade-andringar-smartthings.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 377 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 349 språkpar. Övriga förslag återstår.

[Watergates automatiska avstängning](sparade-andringar-watergate.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 378 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 350 språkpar från 56 ändringsloggar. Övriga förslag återstår.

[Mealies beskrivning av rättyp](sparade-andringar-mealie.md) rättades, sparades och återlästes i Lokalise; fältnamnets referens var lika på båda språken. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 379 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 351 språkpar från 57 ändringsloggar. Övriga förslag återstår.

[Två Portainer-händelser](sparade-andringar-portainer.md) rättades, sparades och återlästes i Lokalise. Förslaget för `kill` kräver kontroll av signalens innebörd och lämnades oförändrat. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 381 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 353 språkpar från 58 ändringsloggar. Övriga förslag återstår.

[Två Home Connect-kameranamn](sparade-andringar-home-connect.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 383 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 355 språkpar från 59 ändringsloggar. Övriga förslag återstår.

[Två Midea-zonkurvor](sparade-andringar-midea.md) rättades, sparades och återlästes i Lokalise med zonnumren bevarade. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 385 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 357 språkpar. Övriga förslag återstår.

[Två Midea-lägen för rengöring och utomhusenhet](sparade-andringar-midea.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 387 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 359 språkpar. Övriga förslag återstår.

[Två förinställda Midea-fläktlägen](sparade-andringar-midea.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 389 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 361 språkpar. Övriga förslag återstår.

[Netios YAML-rubrik](sparade-andringar-netio.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 390 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 362 språkpar från 60 ändringsloggar. Mideas `binary_sensor::full_dust::name` är fortsatt ”Fullt damm”: [Home Assistants sensorkod](https://github.com/home-assistant/core/blob/dev/homeassistant/components/midea/binary_sensor.py) anger problemindikator men inte vad som är fullt. Kontrollera enhetens protokoll eller produktkontext innan ”Dammbehållare full” sparas. Övriga förslag återstår.

[Monzos avvisade överföring](sparade-andringar-monzo.md) rättades, sparades och återlästes i Lokalise utan att anta överföringsriktning. Platshållarna bevarades. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 391 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 363 språkpar från 61 ändringsloggar. Övriga förslag återstår.

[Två mellanlägen för Mideas horisontella luftflöde](sparade-andringar-midea.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 393 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 365 språkpar. Övriga förslag återstår.

[Serieportsbeskrivningar för Samsung Ex-Link och Tonewinner](sparade-andringar-serieportar.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 395 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 367 språkpar från 62 ändringsloggar. Övriga förslag återstår.

[Feltexter för Samsung Ex-Link och Tonewinner](sparade-andringar-serieportar.md) rättades, sparades och återlästes i Lokalise med `{error}` bevarad. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 397 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 369 språkpar. Övriga förslag återstår.

[Mideas sömnläge i lägesväljaren](sparade-andringar-midea.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 398 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 370 språkpar. Övriga förslag återstår.

[Tre behörighetstexter för Home Connect](sparade-andringar-home-connect.md) rättades, sparades och återlästes i Lokalise; bildåtkomstens beskrivning kontrollerades och behölls. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 401 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 373 språkpar. Övriga förslag återstår.

[Två Roborock-instruktioner för mopptorkning](sparade-andringar-roborock.md) rättades efter kontroll av brytarens etikett, sparades och återlästes i Lokalise med platshållare och kodmarkeringar bevarade. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 403 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 375 språkpar. Övriga förslag återstår.

[Två Gardena Bluetooth-texter för överhoppad bevattning](sparade-andringar-gardena-bluetooth.md) rättades, sparades och återlästes i Lokalise. Fuktsensorns typ återstår att kontrollera. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 405 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 377 språkpar från 63 ändringsloggar. Övriga förslag återstår.

[Två Hot Spring-texter](sparade-andringar-hotspring.md) rättades, sparades och återlästes i Lokalise. Textparen lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 407 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 379 språkpar från 64 ändringsloggar. Övriga förslag återstår.

Gardena-uppföljning: [GARDENA beskriver en fuktsensor som mäter markfuktighet och styr bevattningsscheman](https://www.gardena.com/int/c/discover/products/pumps). [Home Assistants kod](https://github.com/home-assistant/core/blob/dev/homeassistant/components/gardena_bluetooth/sensor.py) kopplar den aktuella hoppa-över-orsaken till AquaContour och har en separat fuktsensor av typen moisture. Detta ger stöd för markfuktighet men fastställer inte direkt att just AquaContours `humidity_sensor`-orsak använder samma sensor. Den befintliga översättningen lämnades tills kopplingen kan verifieras.

[Android TV:s feltext för saknad knappkod](sparade-andringar-androidtv.md) rättades, sparades och återlästes i Lokalise med `{command}` bevarad. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 408 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 380 språkpar. Övriga förslag återstår.

[Z-Wave JS-meddelandet om befintlig konfiguration](sparade-andringar-zwave-js.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 409 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 381 språkpar från 65 ändringsloggar. Övriga förslag återstår.

[Recorder-rubriken om databasversion](sparade-andringar-recorder.md) anpassades till närliggande terminologi, sparades och återlästes i Lokalise med båda platshållarna bevarade. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 410 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 382 språkpar från 66 ändringsloggar. Övriga förslag återstår.

[Portainers avbildningsversion](sparade-andringar-portainer.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 411 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 383 språkpar. Övriga förslag återstår.

[Lunatones skanningsstatus](sparade-andringar-lunatone.md) rättades, sparades och återlästes i Lokalise. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 412 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 384 språkpar från 67 ändringsloggar. Övriga förslag återstår.

[Hassios instruktion för blockerade monteringar](sparade-andringar-hassio-montering.md) rättades, sparades och återlästes i Lokalise. Knappetiketten behöver verifieras i reparationsflödet. Textparet lades in i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx); XML, platshållare och tidigare poster verifierades. Totalt 413 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 385 språkpar från 68 ändringsloggar. Övriga förslag återstår.

[UniFi Protects dörrklockstext](sparade-andringar-unifiprotect.md) rättades och återlästes i Lokalise. Sensorn hänvisar till samma text. Textparet lades till i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). Totalt 414 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 386 språkpar från 68 ändringsloggar. Övriga förslag återstår.

[Två UniFi Protect-knappnamn för signaler](sparade-andringar-unifiprotect.md) rättades och återlästes i Lokalise. Textparen lades till i [Core-TMX](https://github.com/yeager/swedish-tm/blob/main/home-assistant/sv-home-assistant-core-lokalise-verified-20261119.tmx). Totalt 416 ändringar i de senaste batcherna, inklusive 28 referenser; TMX innehåller 388 språkpar från 68 ändringsloggar. Övriga förslag återstår.
