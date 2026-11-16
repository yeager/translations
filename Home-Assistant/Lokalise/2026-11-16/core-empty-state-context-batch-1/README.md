# Home Assistant Core: tomma statusvärden, batch 1

En exaktmatchning av samtliga 74 606 svenska Lokalise-översättningar hittade tio översättningar som är exakt `Tom` eller `Tomt`. Alla har källtexten `Empty`.

Sju behålls efter kontroll av den konkreta entitetskontexten. `Tom` är korrekt för exempelvis en behållare, en vattentank och den generella gemensamma statusen. Tre ändras till `Tomt`: ett batteri, tvättmedel och sköljmedel är neutra på svenska.

Kontroller före inskick:

- JSON och platshållare är giltiga.
- `l10n-lint`, Hunspell-sv och `svlang` har körts.
- `git diff --check` och Gitleaks har körts.
- `msgfmt` är inte tillämpligt eftersom Lokalise API-batchen är JSON, inte en PO-fil.

Upstreamstatus: alla tre rättningar har sparats med Lokalise API och har en separat, exakt API-läsning efteråt. Det bekräftar sparat innehåll, inte extern granskning, sammanslagning eller en utgåva.
