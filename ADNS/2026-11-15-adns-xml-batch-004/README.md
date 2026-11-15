# ADNS – Android-XML, radgranskning batch 004

Datum: 15 november 2026

Sträng 301–400 av 432 i `adns-xml-strings` har granskats rad för rad mot den
aktuella engelska resursfilen. Sju materiella rättningar behövdes:
*privata DNS* har korrekt svensk gemen i löpande text, och den interna
Android-tjänsten heter nu konsekvent *bakgrundstjänst* i användargränssnittets
status- och feltexter. En Wi-Fi-regel pausas *för* ett nätverk, inte *i* det.

Protokoll, produktnamn, SSID, Wi-Fi, VPN, platshållare och källans semikolon
är bevarade. Em dash har inte införts.

Kontroller före inskick: XML-validering, `l10n-lint`, `git diff --check` och
Gitleaks. `msgfmt` är inte tillämpligt på Android-XML. Hunspell körs inte för
att begränsa CPU-belastningen.

## Upstreamstatus

Hosted Weblates API tog 15 november 2026 emot sju granskningsförslag. Inga
poster hoppades över eller saknades. Förslagen väntar på godkännande och är
därför ännu inte publicerade i den svenska katalogen.
