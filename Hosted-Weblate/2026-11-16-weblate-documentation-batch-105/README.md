# Weblate Documentation — svensk granskningsbatch 105

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- WLC-kommandon för objekt, enheter och hämtning
- utdata, filkonvertering och uppdatering av översättningsenheter
- projektkonfiguration, API-nycklar och nya HTTP-försök
- tidsgränser och undantag för osäker transport

Kommandon, flaggor, kodvärden, konfigurationsnycklar, API-referenser och reST-markering har bevarats exakt. Terminologin använder bland annat *översättningsenhet*, *standardutdata*, *frågesyntax*, *nya försök* och *ursprungsavgränsad*.

## Lokal granskning

Varje enhet har granskats mot WLC:s CLI- och konfigurationskontext. Särskilt har utdataflöden, tillståndsvärden, nya HTTP-försök och hantering av API-nycklar bevarats utan att ändra den tekniska syntaxen.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
