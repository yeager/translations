# Weblate Documentation — svensk granskningsbatch 104

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- enspråkiga filer, filmasker och reguljära uttryck
- automatiskt modellval för Claude och OpenAI-kompatibla tjänster
- WLC-containeravbildningar och versionsetiketter
- API-nycklar, TLS och säker HTTP-konfiguration för WLC

Reguljära uttryck, UI-namn, miljövariabler, kommandoflaggor, URL:er och reST-markering har bevarats exakt. Terminologin använder bland annat *filmask*, *modellidentifiering*, *avbildning*, *källutcheckning* och *loopback-URL*.

## Lokal granskning

Varje enhet har granskats mot filhanterings-, maskinöversättnings- eller containerkontexten. Säkerhetsvillkoren för API-nycklar, HTTP och certifikatverifiering har bevarats utan att ändra konfigurationssyntax.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
