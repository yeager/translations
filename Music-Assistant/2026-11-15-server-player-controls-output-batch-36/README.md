# Music Assistant Server – spelarkontroller och ljudutmatning, batch 36

Datum: 2026-11-15

## Omfattning

23 svenska UI-etiketter och alternativ för ICY-metadata, spelarexponering,
volymgränser, nätverksupptäckt, ljudavstängning och ljudkodekar.

## Terminologi och kontext

- *Ljudavstängning*, *ljudströmning*, *kodek*, *förlustfri* och
  *med förlust* används konsekvent i spelarens inställningar.
- Protokoll, produktnamn och formatnamn som ICY, AAC, FLAC, WAV, PCM,
  Home Assistant och Music Assistant bevaras.

## Kontroller

- Källtext och nycklar kontrollerade mot aktuell `en.json`.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: kvarvarande träffar är dokumenterade produkt-, protokoll-
  och formatnamn.
- JSON-syntax, diffkontroll och Gitleaks: godkända.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Lokalt granskad och arkiverad. Inte uppladdad eller inskickad upstream:
Lokalise-tokenen saknar rättigheten `Upload files`.
