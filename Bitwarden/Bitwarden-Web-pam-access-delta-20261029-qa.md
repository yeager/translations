# Bitwarden Web: Privileged Access Management

Datum: 29 oktober 2026

`Bitwarden-Web-pam-access-delta-20261029.xliff` innehåller 22 tidigare
oöversatta webbsträngar för Privileged Access Management. Källtexterna
granskades mot den befintliga svenska webbkatalogen så att återkommande termer
följer samma ordval.

## Terminologiska beslut

- *access* är `åtkomst` och *request access* är `begär åtkomst`, i linje med
  den befintliga katalogen.
- *credentials* är `inloggningsuppgifter` i säkerhetskontexten.
- Produktnamnet `Privileged Controls` lämnas oöversatt.
- *request* är `förfrågan` i list- och historiktext, men `begäran` när
  formuleringen beskriver ett krav på aktiv åtkomst.
- *lease duration* återges med `åtkomst i $DURATION$` eller `åtkomst i högst
  $DURATION$`, beroende på källans begränsning.

## Kontroller

- XML: `xmllint --noout` passerade.
- l10n-lint: 0 fel och 0 varningar. Två informationsnotiser om omordnad
  `$DURATION$` i en svensk sats är väntade och korrekta.
- Strukturellt: 22 unika `trans-unit`-id:n.
- Platshållare: `$DURATION$` och `$TIME$` matchar källtexterna exakt.
- svlang: `skrivregler` kördes separat för varje måltext utan träffar.
- Hunspell-sv: kvarvarande träffar är produktnamnet `Privileged Controls`
  och platshållarna.
- Gitleaks: inga hemligheter hittades.
- Git: `git diff --check` passerade.

## Upstreamstatus

Häftet är lokalt klart men ännu inte sparat i Crowdin.
