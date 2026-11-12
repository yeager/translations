# Nextcloud Introvox – svenska batch 11, 2026-11-12

- Komponent: `o:nextcloud:p:nextcloud:r:introvox`.
- Omfattning: 25 strängar, index 250–274 i den aktuella API-exporten.
- Terminologi: rundtur, deltagare, välkomstrundtur, Inbyggd, användningsstatistik och aktivera/inaktivera.
- Kontroller: svenska pluralformer och `{app}`, `{page}`, `{groups}`, `{from}`, `{until}`, `{date}`, `{tour}` samt `%n` bevarade; l10n-lint utan fel eller varningar, med informativ gränsteckensskillnad vid `{tour}`; Gitleaks och diffkontroll godkända. `msgfmt` är inte tillämpligt för JSON-resursen.
- Upstream: inte uppladdat på grund av `locked`-taggar. Transifex API returnerar HTTP 409 för översättningsuppdatering.
- Status: lokalt granskat och väntar på upplåsning.
