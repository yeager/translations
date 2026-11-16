# Weblate Documentation — svensk granskningsbatch 090

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- modellidentifierare och profillänkar för kodvärdar och Fediverse
- anpassade juridiska dokument, Django-mallar och Docker-sökvägar
- instruktioner för arbetsytor och översättningsbidrag
- dokumentation om Community diagnostics

Kod, modellnamn, CSS-klasser, sökvägar, reST-markering och synliga UI-namn har bevarats. Terminologin använder bland annat *kodvärd*, *förråd*, *arbetsyta*, *översättningsinstruktioner* och *juridiska dokument*.

## Lokal granskning

Varje enhet har granskats mot sin dokumentations- och UI-kontext. Formuleringarna förklarar CSS- och mallhantering idiomatiskt på svenska utan att förändra kommandon, inställningsnamn eller kodexempel.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
