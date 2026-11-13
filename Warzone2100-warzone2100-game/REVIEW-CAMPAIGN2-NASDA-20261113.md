# Warzone 2100 – svensk granskning: kampanj 2, NASDA och The Collective

Datum: 2026-11-13

## Omfattning

45 strängar från kampanj 2:s NASDA-briefingar, NEXUS-rapporter och The Collectives sändningar. Varje text har granskats i sin sekvens- och berättelsekontext.

## Terminologibeslut

- NASDA skrivs oförändrat; den förklaras som **Nordamerikanska strategiska försvarsmyndigheten**.
- *LasSat* behålls som synligt systemspecifikt namn.
- *counterstrike* → **motanfall** och *high orbit* → **hög omloppsbana**.
- *Nexus Intruder Virus* → **NEXUS Intruder-virus**.
- Fraktionsnamnen The Collective och NEXUS behålls i de diegetiska sändningarna.

## Lokal kontroll

- msgfmt --check --statistics: godkänd; huvudkatalogen hade 776 översatta och 3 171 oöversatta meddelanden.
- git diff --check: godkänd.
- gitleaks detect --no-git --source po/sv.po: godkänd, inga läckor.
- Trippelkonsonantkontroll: endast engelska källhänvisningar, inga svenska översättningar.

## Status

Arkiverad lokalt granskad kopia. Ingen uppladdning till Crowdin och inget upstream-inskick har gjorts.
