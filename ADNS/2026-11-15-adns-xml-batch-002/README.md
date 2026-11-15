# ADNS – Android-XML, radgranskning batch 002

Datum: 15 november 2026

Sträng 101–200 av 432 i `adns-xml-strings` har granskats rad för rad mot
aktuell engelsk källa. En materiell rättning behövdes: den svenska
handlingsmeningen för tillfällig blockering har nu korrekt ordföljd,
*Pausa blockeringen tillfälligt*.

Produktnamn, DNS-protokoll, CLI-namn, citattecken, platshållare och den
källbaserade tidsintervalltypen är bevarade. Em dash har inte införts.

Kontroller före inskick: XML-validering, `l10n-lint`, `git diff --check` och
Gitleaks. `msgfmt` är inte tillämpligt på Android-XML. Hunspell körs inte för
att begränsa CPU-belastningen.

## Upstreamstatus

Hosted Weblates API tog 15 november 2026 emot ett granskningsförslag: en
accepterad ändring, inga hoppade över och inga saknade poster. Förslaget
väntar på godkännande och är ännu inte publicerat i den svenska katalogen.
