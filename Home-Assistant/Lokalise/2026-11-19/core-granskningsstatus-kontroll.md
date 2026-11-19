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
