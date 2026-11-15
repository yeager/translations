# BikeSharingHub – svensk radgranskning

Datum: 15 november 2026

Källan `bikesharinghub` (83 översatta poster) har jämförts rad för rad med
den engelska Android-resursfilen från Hosted Weblate. Appens senaste GitHub-
release är från 2026 och uppfyller därmed aktualitetskravet.

Deltafilen innehåller 13 materiella svenska rättningar. De omfattar en faktisk
stavning, idiomatiska åtgärdsetiketter, korrekt gemen i löpande text,
terminologin *navigationsapp*, svensk förkortningsskrivning för *API-URL* samt
tydligare texter om platsbehörighet och systemtid. Platshållare, radbrytningar,
produktnamn och formatnamn bevaras.

Kontroller före inskick: XML-validering, `l10n-lint`, Androids
resurskompilering när verktyget finns, `git diff --check` och Gitleaks.
`msgfmt` är inte tillämpligt på Android-XML. Hunspell körs inte för att
begränsa CPU-belastningen.

## Upstreamstatus

Hosted Weblates API tog 15 november 2026 emot hela deltafilen som förslag:
13 accepterade ändringar, 0 hoppade över och 0 saknade poster. Förslagen
väntar på granskning och är därför ännu inte införda i den publicerade svenska
katalogen.
