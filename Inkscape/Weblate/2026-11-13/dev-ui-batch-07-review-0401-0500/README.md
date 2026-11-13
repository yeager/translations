# Inkscape Weblate: utvecklingsgrenen, radgranskning 0401–0500

- Källa: `inkscape/master/inkscape`, svenska.
- Omfattning: poster 401–500: filtergalleriet, linjemarkörer och inledande palettposter.
- Ändrade poster: 19.
- Rättelser: idiomatiska filterbenämningar, korrekta geometriska markörer, linjeavslutningar, svensk sammansättning samt återställda färgkoder i paletten.
- Kontroller: `msgfmt --check`, l10n-lint (0 fel), diffkontroll och Gitleaks passerade. Den enda l10n-lint-varningen gäller katalogens äldre pluralformel i deltafilens huvud.
- Weblate API: första importen genomfördes, men det lokala kommandot avslutades efter importen innan kvittot kunde sparas. En omkörning rapporterade 0 accepterade och 19 hoppade över. Återläsning visar att samtliga 19 granskade måltolkningar finns i den aktuella katalogen.
- Återläsning: `msgfmt` passerade och l10n-lint rapporterade 0 fel (110 befintliga katalogvarningar).
- Status: lokalt granskat, arkiverat och inskickat. Upstream-granskning och publicering är inte verifierade.
