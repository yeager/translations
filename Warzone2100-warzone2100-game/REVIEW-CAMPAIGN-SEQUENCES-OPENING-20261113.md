# Warzone 2100 – svensk granskning: kampanjsekvenser, inledning

Datum: 2026-11-13

## Omfattning

74 strängar från kampanj 1:s öppningssekvens, dess tidiga briefingtexter och övergången till kampanj 2. Innehållet omfattar berättarröst, fraktionsmeddelanden, tekniska rapporter och filmrubriker.

## Terminologibeslut

- *Team Alpha* → **Alpha-gruppen** och *Beta Base* → **Beta-basen**.
- *command turret* → **befälstorn**; dess funktion är att samordna enheter och utgöra en leveranspunkt.
- *synaptic link* → **synapslänk** och *core systems* → **kärnsystem**.
- NEXUS, New Paradigm, The Collective och NASDA behålls som egennamn.
- *power suit* → **stridsdräkt** i den historiska kampanjtexten.

## Lokal kontroll

- msgfmt --check --statistics: godkänd; huvudkatalogen hade 731 översatta och 3 216 oöversatta meddelanden.
- git diff --check: godkänd.
- gitleaks detect --no-git --source po/sv.po: godkänd, inga läckor.
- Trippelkonsonantkontroll: endast engelska källhänvisningar, inga svenska översättningar.

## Status

Arkiverad lokalt granskad kopia. Ingen uppladdning till Crowdin och inget upstream-inskick har gjorts.
