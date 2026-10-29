# Bitwarden Web: PAM-begärans återkoppling

Granskad 29 oktober 2026 mot Crowdins aktuella svenska redigerare och
Bitwarden `clients` `origin/main` på `e44dc1fed896c3fe37e415c0198f987b718f413f`.

Filen `Bitwarden-Web-pam-request-feedback-delta-20261029.xliff` innehåller
elva separata, fortfarande tomma måltexter för återkoppling i dialogen för
åtkomstbegäran. Den närliggande posten `requestAccessModalAlreadyActive`
uteslöts: Crowdin har redan den aktiva svenska texten `Du har redan aktiv
åtkomst till detta objekt.`.

Kontroller:

- XML: `xmllint --noout` godkänd.
- Svenska och format: `l10n_lint.py --language sv` godkänd utan fel eller varningar.
- Språkregler: `svlang skrivregler` godkänd.
- Platshållare: källa och mål har identiska uppsättningar av `$DURATION$`,
  `$START$` och `$END$`.
- Hunspell-sv: endast de avsedda platshållarnamnen `DURATION` och `END` saknas
  i ordlistan.
- Hemligheter: scoped Gitleaks-kontroll godkänd.

Filen är inte importerad i Crowdin ännu. Importera den som en egen liten
XLIFF-bunt och läs sedan tillbaka varje post i redigeraren.
