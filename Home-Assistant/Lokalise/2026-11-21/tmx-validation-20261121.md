# TMX-validering — 2026-11-21

Validering kördes mot samtliga 62 tillgängliga kanoniska Lokalise-exporter, sidorna 669–730. Varje senare export är en ny ögonblicksbild med successivt fler poster; valideringen bekräftar därför formatet i varje sparad version, inte att hela projektets alla nycklar har granskats.

| Kontroll | Resultat |
|---|---|
| XML och fullständiga TMX-poster | Godkänd |
| Dubblettnycklar | Inga |
| Runtime-platshållare | Inga avvikelser |
| Nyckelreferenser | Undantas från placeholder-jämförelsen |
| Hunspell-sv, senaste exporten | 272 unika träffar, manuellt bedömda som främst tekniska termer, produktnamn och identifierare |
| svlang, senaste exporten | Inga verifierade språkfel; dess enda anglicismträff avser en Habitica-URL |
| Aktuell Core-källtext | 486 direkt jämförbara rader; inga semantiska källskillnader efter normalisering av radbrytningar |

Vid källjämförelsen saknade 272 rader direkt motsvarighet i komponenternas `strings.json`. De är främst historiska Lokalise-ID:n och tjänstedefinitioner med andra källformat. De är därför inte belägg för en källändring och behöver jämföras i respektive ursprunglig källa före en eventuell översättningsändring.

Den tidigare signalen för `lokalise:2808665395` var falsk positiv. Engelskan är en Lokalise-referens till `component::telegram_bot::services::send_location::fields::target::description`, medan den befintliga svenska texten korrekt är kontextanpassad för fullständig nyckel `component::telegram_bot::services::send_poll::fields::target::description`. Ingen översättning ändrades.

För `lokalise:2810655843` markerade svlang ”Task” som anglicism. Förekomsten ingår i URL-fragmentet `#api-Task-CreateUserTasks` och ska bevaras.

Verktyget `validate-canonical-tmx.py` skiljer nu nyckelreferenser av formen `[%key:…%]` och `[%link:…%]` från runtime-platshållare innan paritetskontrollen körs.
