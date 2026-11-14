# Music Assistant Server – svensk leverantörsbatch 1

Datum: 2026-11-14

Komponent: `music-assistant/server`, Lokalise-projektet **MA Server**.

Den här deltafilen innehåller 14 nya, radgranskade svenska översättningar för ABC Radio Network, AcoustID Lookup och AirPlay Receiver. Källan är `dev` från 2026-11-14 och kontrollen av releasesidan visar version 2.10.11, publicerad 2026-11-13.

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

Inte uppladdad, föreslagen eller inskickad. Projektet avvisade PR-vägen och hänvisade till Lokalise. Den inloggade webbläsarsessionen har ännu inte verifierats ha redigeringsbehörighet till **MA Server**. Deltafilen ska därför laddas upp först när åtkomsten är bekräftad, följt av läsning tillbaka av importerade, hoppade över och saknade strängar.
