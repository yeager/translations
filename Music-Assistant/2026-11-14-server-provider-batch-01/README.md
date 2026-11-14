# Music Assistant Server – svensk leverantörsbatch 1

Datum: 2026-11-14

Komponent: `music-assistant/server`, Lokalise-projektet **MA Server**.

Deltafilen innehåller 13 nya, radgranskade svenska översättningar för ABC Radio Network, AcoustID Lookup och AirPlay Receiver. En befintlig svensk ABC Radio-översättning bevaras i Lokalise och ingår därför inte längre. Källan är `dev` från 2026-11-14 och kontrollen av releasesidan visar version 2.10.11, publicerad 2026-11-13.

## Terminologibeslut

- `stream` är *ljudström* i beskrivande text och *strömma* som verb.
- `fingerprint` är *fingeravtryck* i AcoustID-/Chromaprint-kontext.
- Synliga produkt-, protokoll- och standardnamn behålls: AirPlay, AcoustID, Chromaprint, ISRC och MusicBrainz Recording ID.
- `plugin` är *insticksmodul*, enligt projektets befintliga terminologilista.

## Omfattning

Den tidigare lokala kandidaten från den stängda PR:en `yeager/music-assistant-server#7640` innehåller 2 083 aktuella källnycklar. Den aktuella engelska katalogen har 3 175 nycklar. Denna batch ökar den lokalt förberedda omfattningen till 2 097 nycklar; 1 078 aktuella källnycklar återstår.

## Kontroller

- JSON-syntax
- samma platshållare och URL:er som i källan
- kontroll av tre identiska konsonanter i följd
- `l10n-lint`, `svlang` och `hunspell-sv` när verktygens formatstöd räcker
- `git diff --check` och Gitleaks före arkivering

`msgfmt` är inte tillämpligt eftersom Lokalise-exporten är JSON.

## Upstreamstatus

`provider.abc_radio_network.config_entries.state.description` kontrollerades i MA Server på Lokalise 2026-11-14 och har redan en svensk översättning; den bevaras. Övriga 13 rader är ännu inte uppladdade, föreslagna eller inskickade. Projektet avvisade PR-vägen och hänvisade till Lokalise. Den inloggade webbläsarsessionen har verifierats ha redigeringsbehörighet för enskilda strängar. Läs tillbaka importerade, hoppade över och saknade strängar efter en eventuell deltaimport.
