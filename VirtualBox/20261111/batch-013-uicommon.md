# Batch 013: gemensamma statusar och format

Datum: 2026-11-11
Komponent: `UICommon`, 281 aktiva meddelanden.

## Radvis granskning

Hela kontexten `UICommon` har lästs med respektive kommentarskontext och
anropsställe i källkoden där det behövdes. Den omfattar maskinstatus,
molnmaskiner, gästsessioner, processer, lagringsplatser, medieformat och
globala inställningsetiketter.

## Ändringar

- Rättade statusform från imperativ till status, exempelvis `Körs` och
  `Avslutas`.
- Förtydligade ögonblicksbild för en körande maskin och ersatte
  `Provisionerar` med det idiomatiska statusordet `Förbereder`.
- Rättade statusar för gästsessioner och processer, inklusive tidsgränser och
  normala respektive onormala avslut.
- Rättade sammansättningar och versalisering i IDE-platser, seriella portar,
  VMDK, VHD, QED och Intel-nätverkskort.
- Behöll `NEGOTIATE` oförändrat eftersom det är ett synligt tekniskt
  protokollnamn, inte löpande text.

## Kontroll

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `l10n-lint`: endast två avsiktliga `--`-värden i språkmetadata rapporteras
  som oavslutade.
- `hunspell-sv`: manuellt bedömd. Kvarvarande träffar är främst produktnamn,
  kommandon, filformat och tekniska identifierare.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga läckta hemligheter.
- `msgfmt`: inte tillämpligt på Qt TS; `lrelease` är formatets motsvarande
  kompileringskontroll.

## Upstream

Ändringarna är lokalt commitade som `356ce68` och hålls kvar lokalt medan den
manuella radvisa granskningen av resterande kontexter fortsätter.
