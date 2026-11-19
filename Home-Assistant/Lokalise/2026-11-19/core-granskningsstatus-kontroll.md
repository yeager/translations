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
