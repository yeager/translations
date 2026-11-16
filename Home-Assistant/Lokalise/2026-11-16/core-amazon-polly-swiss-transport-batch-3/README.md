# Home Assistant Core: Amazon Polly och Swiss Public Transport, batch 3

Åtta aktuella svenska luckor granskades med källtext, komponentnyckel och etablerad svensk fackterminologi. `transportations` avser färdsätten i reseplaneringen och översätts därför konsekvent med **transportmedel**. I den här kontexten är `Leave empty` en fältinstruktion och blir **Lämna tomt**.

Kontroller före inskick:

- JSON och platshållare är giltiga.
- `l10n-lint`, Hunspell-sv och `svlang` har körts; produktnamnen Amazon Polly och Home Assistant är dokumenterade egna namn.
- `git diff --check` och Gitleaks har körts.
- `msgfmt` är inte tillämpligt eftersom Lokalise API-batchen är JSON, inte en PO-fil.

Upstreamstatus: alla 8 översättningar har sparats med Lokalise API och har en separat, exakt API-läsning efteråt. Det bekräftar sparat innehåll, inte extern granskning, sammanslagning eller en utgåva.
