# ADNS – NextDNS-JSON, radgranskning batch 003

Datum: 15 november 2026

Sträng 201–300 av 774 i `nextdns-strings` har granskats rad för rad mot
aktuell engelsk källa. Batchen omfattar profilanslutning, DNS-adresser, DDNS,
iCloud Private Relay samt instruktioner för Android, iOS, Windows och macOS.

Ingen ändring behövs. DNS- och UI-termerna är kontextkorrekta. Synliga
program- och systemmenynamn bevaras när instruktionen måste motsvara den
angivna produkten. Markup, IP-adresser, platshållare, protokoll och kommandon
är oförändrade.

Kontroller: JSON-källorna kan läsas, `git diff --check` och Gitleaks.
`msgfmt` är inte tillämpligt på JSON. Hunspell körs inte för att begränsa
CPU-belastningen.

Upstreamstatus: ingen ändring att skicka in för denna batch.
