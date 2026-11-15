# ADNS – Android-XML, radgranskning batch 005

Datum: 15 november 2026

Återstående 32 strängar i `adns-xml-strings` har granskats rad för rad mot
den aktuella engelska resursfilen. Tre materiella rättningar behövdes:
DNS-förfrågningar benämns tekniskt korrekt, den korta tidsangivelsen är nu
idiomatisk och varningen för en ej lanserad funktion återger korrekt att
webbplatser kan sluta fungera.

Detta slutför radgranskningen av samtliga 432 svenska Android-XML-strängar.
Platshållare, protokoll, ISP, Wi-Fi och produktnamn bevaras. Em dash har inte
införts.

Kontroller före inskick: XML-validering, `l10n-lint`, `git diff --check` och
Gitleaks. `msgfmt` är inte tillämpligt på Android-XML. Hunspell körs inte för
att begränsa CPU-belastningen.

## Upstreamstatus

Hosted Weblates API tog 15 november 2026 emot tre granskningsförslag. Inga
poster hoppades över eller saknades. Förslagen väntar på godkännande och är
därför ännu inte publicerade i den svenska katalogen.
