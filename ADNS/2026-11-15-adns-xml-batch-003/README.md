# ADNS – Android-XML, radgranskning batch 003

Datum: 15 november 2026

Sträng 201–300 av 432 i `adns-xml-strings` har granskats rad för rad mot den
aktuella engelska resursfilen. Fem materiella rättningar behövdes:
*NextDNS-inställningsavsnittet* skrivs med bindestreck, och Androids generella
inställning för privat DNS följer svensk gemen och korrekt possessiv form i
fyra kontexter.

DNS-protokoll, leverantörsnamn, produktnamn, platshållare, citattecken och
källans tidsintervall är bevarade. Em dash har inte införts.

Kontroller före inskick: XML-validering, `l10n-lint`, `git diff --check` och
Gitleaks. `msgfmt` är inte tillämpligt på Android-XML. Hunspell körs inte för
att begränsa CPU-belastningen.

## Upstreamstatus

Hosted Weblates API tog 15 november 2026 emot fem granskningsförslag. Inga
poster hoppades över eller saknades. Förslagen väntar på godkännande och är
därför ännu inte publicerade i den svenska katalogen.
