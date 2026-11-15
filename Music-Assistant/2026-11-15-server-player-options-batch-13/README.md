# Music Assistant Server – spelaralternativ, batch 13

Datum: 2026-11-15

## Omfattning

20 svenska namn på spelaralternativ: ljudfördröjning, balans, bas,
dialogbehandling, equalizer, IR-repeater och länkade spelarfunktioner.

## Terminologi och kontext

- Dessa är korta synliga etiketter i spelarinställningarna, inte
  hjälptexter eller kommandon.
- DRC, DTS och IR bevaras som etablerade förkortningar.
- *Equalizer* och *ljudfördröjning* följer etablerad svensk ljudterminologi.

## Kontroller

- Nycklar och källtexter kontrollerade mot aktuell `en.json` och
  `strings.json`.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: återstående träffar är avsiktliga ljud- och
  förkortningstermer (DRC, DTS, equalizer och IR).
- JSON-syntax och diffkontroll: godkända.
- Gitleaks: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Lokalt granskad och arkiverad. Inte uppladdad, inskickad, granskad eller
integrerad upstream. Batchen väntar på fungerande Lokalise-åtkomst.
