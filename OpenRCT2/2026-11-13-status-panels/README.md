# OpenRCT2, svenska paneler och besökarstatus, 13 november 2026

OpenRCT2 är den fria vidareutvecklingen av RollerCoaster Tycoon 2. Den här UI-batchen fyller 25 verkliga svenska luckor i aktuell engelska huvudresurs.

Batchen omfattar:

- paneler för park- och datuminformation
- statusfält och stegstyrning i bandesignern och scenarioredigeraren
- besökarstatus, till exempel köar, går, lämnar parken och tittar på en åkattraktion

Interna formatmallar och den fristående färgpaletten lämnades orörda.

Kontroller:

- manuell kontroll av platshållaren STRINGID i samtliga berörda statussträngar
- Hunspell-sv: endast sammansättningen ”stegstyrning” saknas i ordlistan, men ordet är korrekt i denna kontext
- diffkontroll: godkänd
- Gitleaks för deltan: godkänd
- l10n-lint: stöder inte OpenRCT2:s id-baserade textformat
- svlang: inte tillämpligt på filformatet; verktyget analyserar hela katalogen som löpande text

Det ursprungliga inskicket [OpenRCT2 PR #27415](https://github.com/OpenRCT2/OpenRCT2/pull/27415)
stängdes den 13 november 2026, eftersom översättningarna förvaltas i det separata
arkivet `OpenRCT2/Localisation`. Batchen skickades därefter, tillsammans med
färgerna och formatmallarna, som [Localisation PR #3571](https://github.com/OpenRCT2/Localisation/pull/3571).
Den PR:en är öppen och väntar på granskning.
