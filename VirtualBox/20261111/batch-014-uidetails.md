# Batch 014: maskindetaljer

Datum: 2026-11-11
Komponent: `UIDetails`, 102 aktiva meddelanden.

## Radvis granskning

Hela kontexten `UIDetails` har granskats med sina detaljtypskommentarer.
Strängarna används i översikten för en virtuell maskin, inklusive system,
bildskärm, lagring, nätverk, ljud och användargränssnitt.

## Ändringar

- Rättade grammatik i otillgänglighetsmeddelandet och pluralböjning för aktiva
  USB-filter.
- Förtydligade nätverkskort, fjärrskrivbordsserverport, miniverktygsradens
  placering, visningsläge samt ljudets in- och utmatning.

## Kontroll

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `l10n-lint`: endast de två avsiktliga `--`-värdena i språkmetadata.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga läckta hemligheter.

## Upstream

Ändringarna är lokalt commitade som `5d00f40` och hålls kvar lokalt medan den
radvisa granskningen fortsätter.
