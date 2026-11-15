# ADNS – NextDNS-JSON, radgranskning batch 002

Datum: 15 november 2026

Sträng 101–200 av 774 i `nextdns-strings` har granskats rad för rad mot
aktuell engelsk källa. Batchen omfattar abonnemang, fakturor, betalningar,
företagsuppgifter, tvåfaktorsautentisering och API-nycklar.

Ingen ändring behövs. Svenska betalnings- och fakturatermer är korrekta,
liksom 2FA-termer, markup, ICU-platshållare, Apple- och PayPal-namn samt
källans em dash i Stripe-informationen. Inget em dash har införts.

Kontroller: JSON-källorna kan läsas, `git diff --check` och Gitleaks.
`msgfmt` är inte tillämpligt på JSON. Hunspell körs inte för att begränsa
CPU-belastningen.

Upstreamstatus: ingen ändring att skicka in för denna batch.
