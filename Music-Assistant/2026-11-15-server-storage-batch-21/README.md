# Music Assistant Server – lagring, batch 21

Datum: 2026-11-15

## Omfattning

20 svenska texter för nätverksresurser, monteringsbehörighet, protokoll,
lagringsstatus och lagringskomponentens namn och beskrivning.

## Terminologi och kontext

- *Lagringsplats*, *nätverksresurs*, *montera* och *värddator* följer batch
  20 och används konsekvent.
- Produktnamnen Home Assistant och Music Assistant samt kodvärdet `host`
  behålls.
- Platshållarna `{0}` har bevarats exakt från engelsk källa.

## Kontroller

- Källtext, nycklar och platshållare kontrollerade mot aktuell `en.json`.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: kvarvarande träffar är produktnamnen Home Assistant och
  Music Assistant.
- JSON-syntax och diffkontroll: godkända.
- Gitleaks: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Lokalt granskad och arkiverad. Inte uppladdad, inskickad, granskad eller
integrerad upstream. Tillsammans med batch 20 täcker den samtliga aktuella
nycklar för `core.storage`.
