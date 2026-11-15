# ADNS – NextDNS-JSON, radgranskning batch 004

Datum: 15 november 2026

Sträng 301–400 av 774 i `nextdns-strings` har granskats rad för rad mot
aktuell engelsk källa. Två materiella rättningar behövdes: produktnamnet
NextDNS får bindestreck före den svenska sammansättningen
*kommandoradsklient* i macOS- och Linux-guiden.

Källbaserade UI-namn, kommandon, IP-adresser, markup, tekniska protokoll och
em dash i säkerhetsbeskrivningarna är bevarade. Inget em dash har införts.

Kontroller före inskick: JSON-validering, `l10n-lint`, `git diff --check` och
Gitleaks. `msgfmt` är inte tillämpligt på JSON. Hunspell körs inte för att
begränsa CPU-belastningen.

## Upstreamstatus

Hosted Weblates API tog 15 november 2026 emot två granskningsförslag. Inga
poster hoppades över eller saknades. Förslagen väntar på godkännande och är
därför ännu inte publicerade i den svenska katalogen.
