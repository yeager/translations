# Nextcloud Introvox – svenska batch 9, 2026-11-12

- Komponent: `o:nextcloud:p:nextcloud:r:introvox`.
- Omfattning: 25 strängar, index 200–224 i den aktuella API-exporten. Batchen gäller Administration, media, HTML och stegredigering.
- Kontroller: platshållarna `{size}`, `{parts}`, `{address}`, `{path}`, `{page}` och `{element}`; HTML, em dash och tredubbla konsonanter bevarade; l10n-lint utan fel eller varningar, med en dokumenterad informativ gränsteckensskillnad kring `{element}`; Gitleaks godkänd. `msgfmt` är inte tillämpligt för JSON-resursen.
- Upstream: inte uppladdat på grund av `locked`-taggar. Transifex API returnerar HTTP 409 för översättningsuppdatering.
- Status: lokalt granskat och väntar på upplåsning.
