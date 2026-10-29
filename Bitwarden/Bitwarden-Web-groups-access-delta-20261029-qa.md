# Bitwarden Web: grupper och privilegierad åtkomst

Datum: 29 oktober 2026

`Bitwarden-Web-groups-access-delta-20261029.xliff` är ett litet häfte med
elva tidigare oöversatta webbsträngar. Källsträngarna kontrollerades i
Crowdins inloggade redigerare före översättning; de hade inga svenska
måltexter där.

## Terminologi

- *group* är `grupp`.
- *shared folder* är `delad mapp`.
- *credentials* är `inloggningsuppgifter` i den här säkerhets- och
  åtkomstkontexten.
- *privileged access rule* är `regel för privilegierad åtkomst`.

## Kontroller

- XML: `xmllint --noout` passerade.
- l10n-lint: 0 fel och 0 varningar.
- Strukturellt: 11 unika `trans-unit`-id:n.
- Platshållare: `$COUNT$`, `$QUANTITY$` och `$ORGANIZATIONNAME$` matchar
  exakt mellan källa och mål.
- svlang: `skrivregler` kördes per måltext utan träffar.
- Hunspell-sv: endast platshållarna återstod som förväntade träffar.
- Gitleaks: inga hemligheter hittades.
- Git: `git diff --check` passerade.

## Upstreamstatus

Häftet är lokalt klart men ännu inte sparat i Crowdin.
