# Home Assistant Core: LIFX, Z-Wave JS och VeSync, batch 8

Åtta aktuella svenska luckor har granskats mot komponentnyckel och funktionskontext. LIFX-funktionen `Mood` är en användarvald ljussättning och återges konsekvent som **Stämning**. Firmware återges med den svenska termen **inbyggd programvara**. VeSync fortsätter använda tillagning och korg för fritösens kontroller.

Kontroller före inskick:

- JSON och platshållare är giltiga.
- `l10n-lint`, Hunspell-sv och `svlang` har körts; LIFX, Z-Wave och platshållaren är dokumenterade tekniska eller egna namn.
- `git diff --check` och Gitleaks har körts.
- `msgfmt` är inte tillämpligt eftersom Lokalise API-batchen är JSON, inte en PO-fil.

Upstreamstatus: alla 8 översättningar har sparats med Lokalise API och har en separat, exakt API-läsning efteråt. Det bekräftar sparat innehåll, inte extern granskning, sammanslagning eller en utgåva.
