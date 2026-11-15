# Music Assistant Server – lagring, batch 20

Datum: 2026-11-15

## Omfattning

15 svenska felmeddelanden för lagringsplatser, mappar, sökvägar och montering
av nätverksresurser i Music Assistants administrativa lagringsvy.

## Terminologi och kontext

- *Lagringsplats*, *nätverksresurs*, *montera* och *värddator* används
  konsekvent för storage-, share-, mount- och host-kontexten.
- *Container*, *volym* och `/` behålls där de betecknar tekniska kör- och
  filsystemsbegrepp.
- Platshållarna `{0}` har bevarats exakt från engelsk källa.

## Kontroller

- Källtext, nycklar och platshållare kontrollerade mot aktuell `en.json`.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: kvarvarande träffar är produktnamnet Music Assistant och
  avstavningen i *data- och cachemappar*.
- JSON-syntax och diffkontroll: godkända.
- Gitleaks: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Lokalt granskad och arkiverad. Inte uppladdad, inskickad, granskad eller
integrerad upstream. Batchen väntar på fungerande Lokalise-åtkomst.
