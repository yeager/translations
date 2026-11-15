# Music Assistant Server – vanliga fel, batch 10

Datum: 2026-11-15

## Omfattning

20 svenska felmeddelanden från `common.errors` för administratörer, inloggning,
musikkällor, spellistor, spelare, leverantörer och uppspelningsköer.

## Terminologi och kontext

- *Musikkälla*, *spellista*, *spelare* och *kö* följer befintliga svenska
  översättningar i Music Assistant.
- `provider` återges som *leverantör*.
- Platshållarna `{0}` och `{1}` har bevarats exakt från engelsk källa.

## Kontroller

- Källtext, nycklar och platshållare kontrollerade mot aktuell `en.json`.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: inga kvarvarande träffar.
- JSON-syntax och diffkontroll: godkända.
- Gitleaks: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Lokalt granskad och arkiverad. Inte uppladdad, inskickad, granskad eller
integrerad upstream. Batchen väntar på fungerande Lokalise-åtkomst.
