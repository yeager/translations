# ADNS – Android-XML, radgranskning batch 001

Datum: 15 november 2026

De första 100 av 432 svenska översättningsenheter i komponenten
`adns-xml-strings` har granskats rad för rad mot den aktuella engelska
Android-resursfilen från Hosted Weblate. ADNS v2.1.9 publicerades 3 november
2026 och projektet är aktivt.

Ingen ändring behövs i denna batch. DNS-, Android- och NextDNS-termerna är
korrekta i sitt gränssnittssammanhang. Platshållare, radbrytningar,
produktnamn, API-namn och kommandon är bevarade. Ord som redan är etablerade
i Android-gränssnittet, exempelvis *Privat DNS*, lämnas oförändrade.

Kontroller: XML-källorna kan läsas, `git diff --check` och Gitleaks. `msgfmt`
är inte tillämpligt på Android-XML. Androids `aapt2` är inte installerat i
körmiljön. Hunspell kördes inte för att begränsa CPU-belastningen.

Upstreamstatus: ingen ändring att skicka in för denna batch.
