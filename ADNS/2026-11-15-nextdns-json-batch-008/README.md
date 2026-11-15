# ADNS – NextDNS-JSON, radgranskning batch 008

Datum: 15 november 2026

Återstående 74 strängar i `nextdns-strings` har granskats rad för rad mot
aktuell engelsk källa. En materiell rättning behövdes:
*NextDNS-rotcertifikat* har korrekt sammansättning.

Detta slutför den radvisa granskningen av samtliga 774 JSON-strängar.
Markup, platshållare, IP-adresser, produktnamn, säkerhetstermer och källans
em dash är bevarade. Inget em dash har införts.

Kontroller före inskick: JSON-validering, `l10n-lint`, `git diff --check` och
Gitleaks. `msgfmt` är inte tillämpligt på JSON. Hunspell körs inte för att
begränsa CPU-belastningen.

## Upstreamstatus

Hosted Weblates API tog 15 november 2026 emot ett granskningsförslag. Inga
poster hoppades över eller saknades. Förslaget väntar på godkännande och är
inte publicerat i den svenska katalogen.
