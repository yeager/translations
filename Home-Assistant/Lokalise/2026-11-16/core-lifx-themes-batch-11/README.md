# Home Assistant Core: LIFX-teman, batch 11

Åtta aktuella svenska luckor har granskats i LIFX-temaväljaren. Namn på konstnärer, musikgenren Vaporwave och planeten Venus behålls. Övriga kategori- och platsnamn har svenska benämningar, exempelvis **Konstserie**, **Rymden** och **Vatikanstaten**.

Kontroller före inskick:

- JSON och platshållare är giltiga.
- `l10n-lint`, Hunspell-sv och `svlang` har körts; LIFX och Vaporwave är dokumenterade egna eller etablerade namn.
- `git diff --check` och Gitleaks har körts.
- `msgfmt` är inte tillämpligt eftersom Lokalise API-batchen är JSON, inte en PO-fil.

Upstreamstatus: alla 8 översättningar har sparats med Lokalise API och har en separat, exakt API-läsning efteråt. Det bekräftar sparat innehåll, inte extern granskning, sammanslagning eller en utgåva.
