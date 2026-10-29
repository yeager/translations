# Bitwarden Web: PAM-dialog för åtkomstbegäran

Datum: 29 oktober 2026

`Bitwarden-Web-pam-request-dialog-delta-20261029.xliff` innehåller 16
oöversatta texter för tidsstyrd åtkomst och åtkomstbegäran i Privileged Access
Management.

## Terminologi och form

- *duration* är `varaktighet` som fältetikett och `tidslängd` i den
  användarorienterade listtexten.
- *start time* och *end time* är `starttid` respektive `sluttid`.
- Åtkomstbegäran använder samma uttryck `begär åtkomst` som den befintliga
  Bitwarden-katalogen.
- Svenska tidsintervall skrivs utan mellanrum kring tankstrecket:
  `$START$–$END$`.

## Kontroller

- XML: `xmllint --noout` passerade.
- l10n-lint: 0 fel och 0 varningar.
- Strukturellt: 16 unika `trans-unit`-id:n.
- Platshållare: `$DURATION$`, `$TIME$`, `$START$` och `$END$` matchar exakt.
- svlang: `skrivregler` kördes separat för varje måltext utan träffar.
- Hunspell-sv: endast platshållarna återstod som förväntade träffar.
- Gitleaks: inga hemligheter hittades.
- Git: `git diff --check` passerade.

## Upstreamstatus

Häftet är lokalt klart men ännu inte sparat i Crowdin.
