# ADNS – NextDNS-JSON, radgranskning batch 007

Datum: 15 november 2026

Sträng 601–700 av 774 i `nextdns-strings` har granskats rad för rad mot
aktuell engelsk källa. Två materiella rättningar behövdes: NextDNS fogas med
bindestreck till *kommandoradsklient* och en intern sidreferens använder den
fastställda etiketten *Konfiguration*.

Loggtermer, DNS-termer, markup, ICU-platshållare och produktnamn är i övrigt
korrekta och bevarade. Inget em dash har införts.

Kontroller före inskick: JSON-validering, `l10n-lint`, `git diff --check` och
Gitleaks. `msgfmt` är inte tillämpligt på JSON. Hunspell körs inte för att
begränsa CPU-belastningen.

## Upstreamstatus

Hosted Weblates API tog 15 november 2026 emot två granskningsförslag. Inga
poster hoppades över eller saknades. Förslagen väntar på godkännande och är
inte publicerade i den svenska katalogen.
