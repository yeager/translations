# Home Assistant Core: VeSync tillagningsstatus, batch 6

Åtta aktuella svenska luckor har granskats i VeSync-integreringens statusmodell för fritöskorgar. Statusvärdena är inte menykommandon. Därför används tillståndsformer som **Tillagar**, **Förvärmer** och **Varmhållning**. Det otydliga interna värdet `appointing` används när apparaten schemaläggs och återges som **Schemaläggning**.

Kontroller före inskick:

- JSON och platshållare är giltiga.
- `l10n-lint`, Hunspell-sv och `svlang` har körts.
- `git diff --check` och Gitleaks har körts.
- `msgfmt` är inte tillämpligt eftersom Lokalise API-batchen är JSON, inte en PO-fil.

Upstreamstatus: alla 8 översättningar har sparats med Lokalise API och har en separat, exakt API-läsning efteråt. Det bekräftar sparat innehåll, inte extern granskning, sammanslagning eller en utgåva.
