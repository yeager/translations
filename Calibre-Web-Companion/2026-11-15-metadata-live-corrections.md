# Calibre-Web Companion – svenska metadata

Granskad 15 november 2026 mot Hosted Weblates aktuella metadataenheter.

Tre rättningar är separerade i JSON-deltan:

- *Homescreen widgets* använder den svenska sammansättningen
  *startskärmswidgetar*.
- Exempelsökvägen `/series/book.epub` är ett tekniskt exempel och ska inte
  översättas.
- Särskrivningen *i stället* används i versionsanteckningen.

De återstående kontrollträffarna är versionsanteckningar med kodnamn,
produktnamn, citat eller medveten svensk meningsstruktur. Deltan ska skickas
som tre granskningsförslag, ett per Weblate-enhet.

## Inskick

Hosted Weblate tog emot samtliga tre förslag den 15 november 2026. De skapades
som förslag för enheterna `196655902`, `201612430` och `209054842` och väntar
på granskning; de har inte tillämpats på den publicerade katalogen.

JSON-syntax, `svlang skrivregler`, `git diff --check` och Gitleaks är
godkända. l10n-lint kan inte tolka manifestets Weblate-enhets-ID:n som ett
översättningsformat och rapporterar därför en formatspecifik falsk träff.
