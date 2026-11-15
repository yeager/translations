# ADNS – NextDNS-JSON, radgranskning batch 005

Datum: 15 november 2026

Sträng 401–500 av 774 i `nextdns-strings` har granskats rad för rad mot
aktuell engelsk källa. Batchen omfattar hot- och integritetsfunktioner,
blockeringslistor, DNS-säkerhet och tjänstenamn.

Ingen ändring behövs. Säkerhetstermer, IANA-liknande förkortningar,
produktnamn, domänmönster, markup och källans em dash har bevarats i sitt
sammanhang. Inget em dash har införts.

Kontroller: JSON-källorna kan läsas, `git diff --check` och Gitleaks.
`msgfmt` är inte tillämpligt på JSON. Hunspell körs inte för att begränsa
CPU-belastningen.

Upstreamstatus: ingen ändring att skicka in för denna batch.
