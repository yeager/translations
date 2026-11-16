# Weblate Documentation — svensk granskningsbatch 111

Datum: 2026-11-16  
Projekt: Weblate  
Komponent: Documentation  
Språk: svenska

## Omfattning

20 dokumentationsenheter har granskats och översatts i sin tekniska kontext:

- utvecklingscontainerns felsökning, Chromium och Selenium
- Weblate-programprofil, Maildev och lokala portbindningar
- bakgrundsarbetare, integrationstestning och testdata
- Compose-profiler, databasåtkomst och migrering av utvecklingsmiljöer

Kommandon, flaggor, filvägar, miljövariabler, produktnamn och reST-markering har bevarats exakt. Terminologin använder bland annat *startskript*, *utvecklingsavbildning*, *testprofil*, *programprofil*, *arbetsträd* och *tillfällig programmiljö*.

## Lokal granskning

Varje enhet har granskats mot utvecklings- och QA-kontexten. Översättningarna bevarar säkerhetsgränserna för testdata, lokala portar, API-token och de separata livscyklerna för test- och programprofiler.

## Kontroller

- Diffkontroll: godkänd
- `msgfmt` mot aktuell svensk dokumentations-PO från projektets huvudgren: godkänd
- Gitleaks: godkänd, inga hemligheter hittades
- `l10n-lint`, `svlang` och `hunspell-sv`: inte körda, eftersom Hosted Weblate inte gav en lokal deltafil för batchen

## Upstreamstatus

De 20 enheterna sparades i Hosted Weblate via REST API och lästes tillbaka som översatta, med statusen **väntar på granskning**. De är inte verifierade som upstream-granskade eller mergade.
