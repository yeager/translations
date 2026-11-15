# Music Assistant Server – ljudströmmar, batch 25

Datum: 2026-11-15

## Omfattning

25 svenska strängar för lokala uppspelningskällor, kvalitetsuppgradering,
volymnormalisering och ljudströmsmotorns namn och beskrivning.

## Terminologi och kontext

- *Förlustfri*, *bithastighet*, *förstärkning*, *volymnormalisering* och
  *ljudström* följer etablerad svensk ljudteknisk användning.
- Termer för fast och reservbaserad förstärkning normaliseras lika för radio
  och spår.

## Kontroller

- Källtext och nycklar kontrollerade mot aktuell `en.json` och `strings.json`.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: återstående träffar är korrekt avstavning i
  *ljudströmning och -bearbetning* samt den sammansatta facktermen
  *volymnormaliseringsmetod*.
- JSON-syntax och diffkontroll: godkända.
- Gitleaks: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Lokalt granskad och arkiverad. Inte uppladdad, inskickad, granskad eller
integrerad upstream. Tillsammans med batch 24 täcker den samtliga aktuella
nycklar för `core.streams`.
