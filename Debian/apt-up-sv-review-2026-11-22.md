# APT – svensk PO-granskning

Den 22 november 2026 radgranskades `apt-up.sv.po` för Debians APT.

## Resultat

- 240 tidigare oöversatta eller `fuzzy`-markerade aktiva poster granskades
  och kompletterades.
- Katalogen har nu 946 översatta aktiva meddelanden, noll `fuzzy`-poster och
  noll tomma översättningar.
- Kommandoradsflaggor, manpages, formatsträngar, filnamn och APT-kommandon
  behölls som tekniska referenser.

## Validering

- `msgfmt --check --statistics`: godkänd, 946 översatta meddelanden.
- Pluralmedveten kontroll av C-formatargument: noll avvikelser.
- `svlang check`: godkänd för representativa CLI-termer och nya formuleringar.
- `hunspell-sv` användes som stöd; kvarvarande fackord och produktnamn
  granskades som avsedda tekniska termer.

Den granskade filen är `apt-up.sv-reviewed-20261122.po` och har SHA-256
`925704406645040444cfef7f711da7e1ab88bfa15b7ad3e19eb7a5ad7d0d3c4c`.
