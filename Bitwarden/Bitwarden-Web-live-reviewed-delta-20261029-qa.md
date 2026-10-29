# Bitwarden Web: kvalitetssäkring av livegranskad deltafil

Datum: 29 oktober 2026

`Bitwarden-Web-live-reviewed-delta-20261029.xliff` innehåller 17 kontrollerade
ändringar efter en radvis jämförelse med Crowdins aktuella svenska måltexter.
Filen är separat från det äldre granskningshäftet och innehåller bara texter
som fortfarande har ett påvisat förbättringsbehov.

## Kontroller

- XML: `xmllint --noout` passerade.
- Strukturellt: 17 `trans-unit`-poster med 17 unika id:n.
- Platshållare: käll- och måltext har identiska uppsättningar. `$ID$`
  bevaras i de två berörda händelsetexterna.
- l10n-lint: `python3 work/l10n-lint/l10n_lint.py --language sv` rapporterade
  0 fel och 0 varningar.
- svlang: `skrivregler` kördes separat för varje måltext utan träffar.
- Hunspell-sv: återstående träffar är produktnamn, engelska menyetiketter,
  filformat eller XML-entiteter. De ska bevaras eftersom de hänvisar till
  respektive programs gränssnitt.
- Swedish TM och Swedish FOSS Terminology: `policy` används konsekvent som
  svensk fackterm i befintliga poster. Därför ersätts Crowdins felaktiga
  `principen` med `policyn` i de två policyhändelserna.
- Gitleaks: inga hemligheter hittades i deltafilen.
- Git: `git diff --check` passerade för de nya arkivfilerna.

## Särskilda rättningar

- Avast JSON sparar en JSON-fil, inte en CSV-fil.
- Importanvisningarna för Psono, Passky, ProtonPass, PasswordXP, NordPass och
  Password Depot 17 får naturligare svensk meningsbyggnad utan att ändra
  gränssnittets engelska etiketter.
- Händelser för automatisk användarbekräftelse och inbjudningslänkar skrivs
  som kompletta svenska logghändelser, med rätt fackterm och bestämd form.

## Upstreamstatus

Deltafilen är lokalt klar. Den är ännu inte inskickad till Crowdin.
