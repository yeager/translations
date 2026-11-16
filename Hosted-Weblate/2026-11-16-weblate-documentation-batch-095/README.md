# Weblate Documentation — svensk granskningsbatch 095

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- Granian/ASGI, diagnostik, tillägg och översättningsminne
- prestanda, förrådsvarningar samt skyddade HTTP- och Git-anslutningar
- REST API, återställning av projektsäkerhetskopior och RSS
- juridiska dokument, listkolumner och språkbegränsningar

Bidragsgivarnamn har medvetet bevarats oförändrade. Referenser, UI-namn, säkerhetsadviseringar, inställningsnycklar och API-fältnamn har också bevarats exakt. Terminologin använder bland annat *diagnostik*, *förråd*, *adressbindning*, *integritetspolicy* och *översättningsminne*.

## Lokal granskning

Varje enhet har granskats mot sin utgåve-, säkerhets- eller administratörskontext. Särskilt har säkerhetsfixarnas betydelse och juridiska krav bevarats utan att ändra identifierare eller konfiguration.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
