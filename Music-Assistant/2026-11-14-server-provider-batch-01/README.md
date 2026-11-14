# Music Assistant Server – svensk leverantörsbatch 1

Datum: 2026-11-14

Komponent: `music-assistant/server`, Lokalise-projektet **MA Server**.

Källan är `dev` från 2026-11-14. Releasesidan kontrollerades för version 2.10.11, publicerad 2026-11-13.

## Terminologibeslut

- `stream` är *ljudström* i beskrivande text och *strömma* som verb.
- `fingerprint` är *fingeravtryck* i AcoustID-/Chromaprint-kontext.
- AirPlay, AcoustID, Chromaprint, ISRC och MusicBrainz Recording ID behålls som produkt-, protokoll- och standardnamn.
- `plugin` är *insticksmodul*.

## Kontroller

- JSON-syntax, URL:er och platshållare har kontrollerats.
- Tre identiska konsonanter i följd har kontrollerats.
- `svlang`- och Hunspell-träffar för produktnamn, protokoll, API-namn och JSON-nycklar har manuellt bedömts som falska positiva.
- `msgfmt` är inte tillämpligt eftersom Lokalise-exporten är JSON.
- Diffkontroll och Gitleaks körs före arkivering.

## Upstreamstatus

Åtta av de nio tidigare väntande värdena kontrollerades i MA Server på Lokalise 2026-11-14 och är redan sparade där. De lämnas oförändrade. Två värden är fortfarande tomma i Lokalise och ligger därför kvar i deltafilen: AcoustID Lookup-beskrivningen och AirPlay Receiver-namnmallens beskrivning. De har inte kunnat sparas via den aktuella Lokalise-redigeraren och är inte upstream-inskickade. Lokalise-granskning, kodsynkronisering och release är inte verifierade.
