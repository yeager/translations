# Batch 016: medier, nätverk, USB och kloning

Datum: 2026-11-11  
Källa: `VirtualBox/virtualbox` `main`, svensk Qt TS-katalog i arbetsgrenen
`virtualbox-sv-review-20261111`.

## Granskad omfattning

- `UIMediumManager`: 44 aktiva meddelanden.
- `UINetworkManager`: 111 aktiva meddelanden.
- `UIUSBFilterDetailsEditor` och `UIUSBFiltersEditor`: 36 aktiva meddelanden.
- `UIWizardCloneVM`: 50 aktiva meddelanden.

Samtliga ovanstående meddelanden lästes med källa, sammanhang och svensk
översättning. De säkra korrigeringarna infördes i lokal commit `69933e4`.

## Ändringar

- Mediehanteraren använder naturlig bestämdhet för uppgifter om aktuellt
  medium och `Stäng fönstret`.
- Nätverksgränssnittet normaliserar `ID`, `IPv4-nätmask` och `nedre gräns`.
- USB-filtren använder `tillverkar-ID`, `produkt-ID`, `decimalsiffra`,
  `USB-filtrets räckvidd` och korrekt neutrum i statusen `Aktivt`.
- Kloningsguiden har konsekventa maskin- och klonnamn samt `Allt` i stället
  för det oidiomatiska `Allting`.

## Kontroller

- `xmllint --noout`: godkänd.
- `lrelease`: 3 589 slutförda översättningar, 0 oavslutade.
- `svlang consistency`: godkänd.
- `git diff --check`: godkänd.
- `gitleaks detect --no-git --redact`: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt på Qt TS; `lrelease` är motsvarande kontroll.

## Status

Ändringarna är granskade och verifierade lokalt. De ingår ännu inte i den
upstream-pushade PR-huvudrevisionen eftersom den fullständiga radvisa
granskningen av katalogen fortfarande pågår.
