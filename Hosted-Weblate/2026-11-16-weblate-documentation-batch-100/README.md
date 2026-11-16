# Weblate Documentation — svensk granskningsbatch 100

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- auktorisering av bakgrundsarbete och hantering av klient-IP
- webbkroksrisker, synliga statistikkolumner och VCS-URL:er
- länkade komponenter, Git LFS och Git-undermoduler
- versionshanteringsparametrar och GitLab-sammanslagningsbegäranden

Inställningsnycklar, Git-variabler, UI-namn, kod, URL:er och reST-markering har bevarats exakt. Terminologin använder bland annat *bakgrundsjobb*, *omvänd proxy*, *förråd*, *utcheckning*, *filmask* och *versionshanteringsparameter*.

## Lokal granskning

Varje enhet har granskats mot dess behörighets-, VCS- eller Git LFS-kontext. Särskilt har gränserna för redan auktoriserat bakgrundsarbete, filåtkomst i länkade komponenter och LFS-objektens hantering bevarats.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
