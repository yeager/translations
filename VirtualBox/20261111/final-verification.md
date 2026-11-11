# Slutverifiering: VirtualBox svensk Qt TS-katalog

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox`,
`src/VBox/Frontends/VirtualBox/nls/VirtualBox_sv.ts`.

## Täckt omfattning

Alla 3 589 aktiva meddelanden i samtliga 209 aktiva kontexter är granskade
radvis och dokumenterade i batcherna 001–212. Katalogen innehåller 3 589
slutförda översättningar och 0 oavslutade översättningar.

## Slutkontroller

- `xmllint --noout`: godkänd.
- `lrelease`: godkänd; 3 589 slutförda översättningar och 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande
  formatkontroll.
- `l10n-lint --language sv --check`: avslutades med status 2 utan diagnostik.
  Den kan därför inte redovisas som godkänd; XML- och Qt-kontrollerna ovan
  är den verifierade formatvalideringen.
- `hunspell -d sv_SE`: körd som ordlista. Träffarna omfattar framför allt
  API-namn, produktnamn, filnamn, format, maskinvarubeteckningar och andra
  tekniska identifierare; de har inte behandlats som automatiska språkfel.

## Upstreamstatus

Den samlade katalogändringen är pushad till PR #848:s källgren
`yeager/update-swedish-l10n-completeness` i revision
`c63b77c5319f3c46e88b67fd1d5d5b4bc6cd717d`.

PR [#848](https://github.com/VirtualBox/virtualbox/pull/848) är öppen mot
`main`. GitHub bekräftar rätt huvudrevision; kontrollen `oca/oracle` är
köad. PR:n är ännu inte granskad eller mergad.
