# ADNS – NextDNS-JSON, radgranskning batch 001

Datum: 15 november 2026

De första 100 av 774 svenska JSON-strängar i komponenten `nextdns-strings`
har granskats rad för rad mot den aktuella engelska källan. Fyra
navigations- och åtgärdsetiketter normaliseras mot ADNS Android-komponent:
*Konfiguration*, *blockeringslista*, *tillåtelselista* och *Rensa sökningen*.

HTML-liknande markup, ICU-platshållare, produktnamn, kontovärden och
betalningsformat lämnas oförändrade. Em dash har inte införts.

Kontroller före inskick: JSON-validering, `l10n-lint`, `git diff --check` och
Gitleaks. `msgfmt` är inte tillämpligt på JSON. Hunspell körs inte för att
begränsa CPU-belastningen.

## Upstreamstatus

Hosted Weblates API tog 15 november 2026 emot fyra granskningsförslag. Inga
poster hoppades över eller saknades. Förslagen väntar på godkännande och är
därför ännu inte publicerade i den svenska katalogen.
