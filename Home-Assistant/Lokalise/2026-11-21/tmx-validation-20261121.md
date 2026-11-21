# TMX-validering — 2026-11-21

Validering kördes mot samtliga 62 tillgängliga kanoniska Lokalise-exporter, sidorna 669–730. Varje senare export är en ny ögonblicksbild med successivt fler poster; valideringen bekräftar därför formatet i varje sparad version, inte att hela projektets alla nycklar har granskats.

| Kontroll | Resultat |
|---|---|
| XML och fullständiga TMX-poster | Godkänd |
| Dubblettnycklar | Inga |
| Runtime-platshållare | Inga avvikelser |
| Nyckelreferenser | Undantas från placeholder-jämförelsen |

Den tidigare signalen för `lokalise:2808665395` var falsk positiv. Engelskan är en Lokalise-referens till `component::telegram_bot::services::send_location::fields::target::description`, medan den befintliga svenska texten korrekt är kontextanpassad för fullständig nyckel `component::telegram_bot::services::send_poll::fields::target::description`. Ingen översättning ändrades.

Verktyget `validate-canonical-tmx.py` skiljer nu nyckelreferenser av formen `[%key:…%]` och `[%link:…%]` från runtime-platshållare innan paritetskontrollen körs.
