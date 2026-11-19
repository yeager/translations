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
