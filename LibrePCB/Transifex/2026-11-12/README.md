# LibrePCB, svenska, Transifex

Datum: 2026-11-12
Komponent: `librepcb` (`librepcb.ts`)
Källa: LibrePCB 2.1.1, publicerad 2026-06-12.
Upstream: https://app.transifex.com/librepcb/librepcb-application/translate/#sv/librepcb/

## Resultat

19 tidigare oöversatta strängar granskades i källkontext och skickades i ett
enda Transifex API-anrop. Uppladdningens svar omfattar samtliga 19 strängar.
Efterkontrollen via API visar 0 oöversatta strängar i komponenten.

`raw-missing-before.json` är den oförändrade råexporten före arbetet.
`sv-delta.json` innehåller enbart den granskade ändringsmängden.
`api-receipt.json` och `post-upload-missing.json` är API-kvitto respektive
efterkontroll.

## Kontroller

* Transifex API: alla 19 måltexter lästes tillbaka och stämde med deltat.
* l10n-lint: godkänd.
* svlang svengelska: inga anglicismer.
* hunspell-sv: träffen *padar* bedömdes som en legitim projektspecifik
  böjning av den etablerade LibrePCB-termen *pad*.
* `git diff --check`: godkänd för arkivändringen.
* gitleaks: inga hemligheter hittades.
* `msgfmt`: inte tillämpligt, då resursen är Qt TS. Qt Linguist finns lokalt;
  den fullständiga TS-exporten valideras när den hämtas från Transifex.

## Status

Inskickad och mottagen i Transifex. Strängarna är inte markerade som
granskade i Transifex och behöver därför fortfarande upstream-granskning.
