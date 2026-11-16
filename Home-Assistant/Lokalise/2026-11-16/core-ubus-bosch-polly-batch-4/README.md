# Home Assistant Core: UBUS, Bosch SHC och Amazon Polly, batch 4

Åtta aktuella svenska luckor har granskats mot komponentnyckel och befintlig Home Assistant-terminologi. SSL behålls som etablerad teknisk förkortning. Amazon Polly använder talmotorer, därför förtydligas `engine` som **talmotor** i felmeddelandet.

Kontroller före inskick:

- JSON och platshållare är giltiga.
- `l10n-lint`, Hunspell-sv och `svlang` har körts; SSL och platshållarna är tekniska undantag.
- `git diff --check` och Gitleaks har körts.
- `msgfmt` är inte tillämpligt eftersom Lokalise API-batchen är JSON, inte en PO-fil.

Upstreamstatus: alla 8 översättningar har sparats med Lokalise API och har en separat, exakt API-läsning efteråt. Det bekräftar sparat innehåll, inte extern granskning, sammanslagning eller en utgåva.
