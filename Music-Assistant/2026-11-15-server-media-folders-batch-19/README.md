# Music Assistant Server – mediemappar, batch 19

Datum: 2026-11-15

## Omfattning

39 synliga mediemappsetiketter för tidsperioder, medietyper, genrer,
stämningar, årstider, radio och bibliotek.

## Terminologi och kontext

- Etiketterna används som korta navigationsnamn i Music Assistants medievyer.
- Etablerade genrer och formatnamn som jazz, rock och R&B behålls.
- `Sound Effects` översätts konsekvent som *ljudeffekter*; befintliga äldre
  katalogvärden förändras inte i denna deltafil.

## Kontroller

- Nycklar och källtexter kontrollerade mot aktuell `en.json` och
  `strings.json`.
- `l10n-lint --language sv`: godkänd.
- `svlang skrivregler`: godkänd.
- Hunspell-svenska: inga kvarvarande träffar.
- JSON-syntax och diffkontroll: godkända.
- Gitleaks: inga hemligheter hittades.
- `msgfmt` är inte tillämpligt eftersom resursformatet är JSON.

## Status

Lokalt granskad och arkiverad. Inte uppladdad, inskickad, granskad eller
integrerad upstream. Batchen täcker samtliga aktuella nycklar för
`common.media.folder` och väntar på fungerande Lokalise-åtkomst.
