# Weblate Documentation — svensk granskningsbatch 097

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- åtkomstregler för projekt-, arbetsyte- och delade översättningsminnen
- webbplatsövergripande roller, komponentborttagning och granskningslogg
- webbkroksmål och säkerhetsklassificering
- betrodda proxyer, IP-adresser och VCS-värdlistor

Inställningsnycklar, API-namn, URL:er, reST-markering och tekniska identifierare har bevarats. Terminologin använder bland annat *begränsad komponent*, *översättningsminnesomfång*, *webbkrok*, *förråd*, *omvänd proxy* och *adressbindning*.

## Lokal granskning

Varje enhet har granskats mot dess åtkomst- eller säkerhetskontext. Särskilt har skiljelinjen mellan betrodda proxyvärden och klientstyrda uppgifter, samt VCS-undantagens exakta räckvidd, bevarats.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
