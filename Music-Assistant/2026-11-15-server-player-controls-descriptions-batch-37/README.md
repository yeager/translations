# Music Assistant Server – förklarande spelarkontroller, batch 37

Datum: 2026-11-15

## Omfattning

14 svenska hjälptexter för ICY-metadata, Home Assistant-exponering,
avstängning vid inaktivitet, volymgränser, ljudavstängning och ljudkodekar.

## Terminologi och kontext

- Hjälptexterna beskriver konsekvenser av valen utan att ändra deras tekniska
  innebörd, särskilt bandbredd, uppspelningskvalitet och samplingsfrekvens.
- ICY, AAC, FLAC, WAV, PCM, Home Assistant och Music Assistant bevaras som
  protokoll-, format- och produktnamn.
- *Köflödesläge*, *ljudavstängning*, *kodek*, *förlustfri* och *med förlust*
  följer terminologilistan.

## Kontroller

- Källtext, nycklar och radbrytningar kontrollerade mot aktuell `en.json`.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: kvarvarande träffar är dokumenterade produkt-, protokoll-
  och formatnamn samt projekttermen *köflödesläge*.
- JSON-syntax, diffkontroll och Gitleaks: godkända.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Nio strängar sparades manuellt och fyra befintliga upstream-översättningar
verifierades i Lokalise 2026-11-15. En tidigare snabbkontroll var inte
tillräcklig för den återstående raden;
de är markerade för radvis omkontroll innan deras status påstås. Arkivering och
push sker efter varje ändring:
Lokalise-tokenen saknar rättigheten `Upload files`.
