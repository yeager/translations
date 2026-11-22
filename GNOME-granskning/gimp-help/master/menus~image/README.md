# GIMP Help — master — menus~image — svenska

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/gimp-help/master/menus~image/sv/>.
- Ursprunglig lokal katalog: 56 översatta, 60 fuzzy och 720 oöversatta användarvisade poster.
- Slutlig lokal katalog: 836 översatta, 0 fuzzy och 0 oöversatta användarvisade poster.
- Åtgärd: hela bildmenyn har radgranskats och kompletterats. 720 tidigare tomma poster har översatts och 61 befintliga poster har korrigerats eller granskats på nytt, inklusive DocBook-markup, precisionsexempel och svensk GIMP-terminologi.
- Avsiktliga undantag: 27 fuzzy och 42 tomma råa PO-poster börjar med `@@image:`. Källkommentarerna anger att bildhasharna inte används i översättning och därför ska lämnas utan översättning.
- Validering: `msgfmt --check --statistics` och `git diff --check` godkända. Kontroll av användarvisat innehåll ger 0 fuzzy och 0 tomma poster. `l10n-lint` ger 42 fel, samtliga avsiktliga tomma `@@image:`-poster, och 0 varningar. `hunspell-sv` kördes; återstående kandidater är produktnamn, filformat, protokoll, metadatafält, färgprofiler och etablerade GIMP-sammansättningar.
- Översättarmetadata: `Daniel Nylander <gnome@danielnylander.se>`, 2026-11-22.
- GNOME-inskick: inget — enligt arbetsinstruktionen.
