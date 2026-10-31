# Open Shaders – lokal slutgranskning av 82 strängar

## Underlag

Källan hämtades från `alandtse/open-shaders` på commit `5839634`
(30 oktober 2026). Jämförelsen mellan `en.json` och `sv.json` visade 82 tomma
svenska måltexter som saknade tidigare arkiverat granskningsunderlag.

De svenska texterna finns i
[`open-shaders-local-final-82-sv-20261031.json`](open-shaders-local-final-82-sv-20261031.json).

## Kvalitetskontroll

- `l10n-lint`: inga fel. Två dubblettnotiser berör separata nycklar med samma
  engelska källtext (`Comparing …` respektive `Change`).
- `svlang skrivregler`: inga fel.
- `hunspell-sv`: markerade endast facktermer, produktnamn och avsedda
  sammansättningar.
- Två saknade radbrytningar i hjälptipset för spelarskuggor upptäcktes och
  rättades före slutkontrollen.

## Uppladdningsstatus

Komponenten kan inte skickas in ännu: dess tidigare Weblate-status var låst,
och den sparade Weblate-behörigheten avvisas nu med HTTP 401. Underlaget är
därför arkiverat som en färdig lokal importkandidat, men inte uppladdat.
