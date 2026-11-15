# Music Assistant Server – lokala filer, batch 28

Datum: 2026-11-15

## Omfattning

28 svenska strängar för leverantören Lokala filer: innehållstyper,
biblioteksimport, dubblettvarning, mappar, lagringsfel och installationsflöde.

## Terminologi och kontext

- *Lagringsplats*, *nätverksresurs*, *spår*, *spellista*, *ljudbok* och
  *poddsändning* följer etablerad projektterminologi.
- M3U bevaras som etablerat filformat och Music Assistant som produktnamn.
- Platshållaren `{0}` och radbrytningar har bevarats exakt.

## Kontroller

- Källtext, nycklar, platshållare och radbrytningar kontrollerade mot aktuell
  `en.json`.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: återstående träffar är produktnamnet Music Assistant och
  filformatet M3U.
- JSON-syntax och diffkontroll: godkända.
- Gitleaks: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Lokalt granskad och arkiverad. Inte uppladdad, inskickad, granskad eller
integrerad upstream. Batchen väntar på fungerande Lokalise-åtkomst.
