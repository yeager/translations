# Home Assistant Core: LIFX-teman, batch 15

Åtta aktuella svenska luckor har granskats i LIFX-temaväljaren. Länder använder etablerade svenska namn, och musikgenren med etablerat internationellt namn behålls som **Synthwave**. Det beskrivande temanamnet `Taps` återges med den naturliga svenska pluralformen **Kranar**.

Kontroller före inskick:

- JSON och platshållare är giltiga.
- `l10n-lint`, Hunspell-sv och `svlang` har körts; Synthwave är ett etablerat genrenamn.
- `git diff --check` och Gitleaks har körts.
- `msgfmt` är inte tillämpligt eftersom Lokalise API-batchen är JSON, inte en PO-fil.

Upstreamstatus: alla 8 översättningar har sparats med Lokalise API och har en separat, exakt API-läsning efteråt. Det bekräftar sparat innehåll, inte extern granskning, sammanslagning eller en utgåva.
