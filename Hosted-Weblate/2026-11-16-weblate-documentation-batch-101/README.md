# Weblate Documentation — svensk granskningsbatch 101

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- Git-undermoduler, tvingad push och grupptilldelade språk
- tvåfaktorsinloggning samt kölagda förrådsåtgärder
- AWS SES, Docker och transport av utgående e-post
- GitHub App, skärmbilder, granskningslogg och driftsättningsdiagnostik

UI-namn, miljövariabler, API-anrop, kod, kommandon, regionnamn och reST-markering har bevarats exakt. Terminologin använder bland annat *undermodul*, *bakgrundsbearbetning*, *granskningslogg*, *driftsättningsdiagnostik* och *statistikkolumn*.

## Lokal granskning

Varje enhet har granskats mot sin UI-, drift- eller integrationskontext. Behörighetsgränser, kölagda åtgärder och den exakta AWS SES-konfigurationen har bevarats i översättningarna.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
