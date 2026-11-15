# ADNS – NextDNS-JSON, radgranskning batch 006

Datum: 15 november 2026

Sträng 501–600 av 774 i `nextdns-strings` har granskats rad för rad mot
aktuell engelsk källa. Tre materiella rättningar behövdes: de två
SafeSearch-åtgärderna använder nu idiomatisk imperativform och
statistiketiketten har en fullständig svensk sats.

Produktnamn, markup, ICU-platshållare, domäntermer och källans em dash är
bevarade. Inget em dash har införts.

Kontroller före inskick: JSON-validering, `l10n-lint`, `git diff --check` och
Gitleaks. `msgfmt` är inte tillämpligt på JSON. Hunspell körs inte för att
begränsa CPU-belastningen.

## Upstreamstatus

Hosted Weblates API tog 15 november 2026 emot tre granskningsförslag. Inga
poster hoppades över eller saknades. Förslagen väntar på godkännande och är
inte publicerade i den svenska katalogen.
