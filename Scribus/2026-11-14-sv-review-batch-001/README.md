# Scribus svenska radgranskning, batch 001

Datum: 2026-11-14

Komponent: `scribus` på Transifex, språk `sv`.

Den lokala katalogen har 8 313 TS-poster. Transifex aktuella komponent innehåller 8 288 poster; 25 TS-poster är föråldrade poster och ändrades inte. Den första aktuella batchen granskades rad för rad. Nio konkreta språkliga och UI-kontextuella förbättringar sparades via Transifex API och lästes tillbaka med exakt samma målvärden.

Kontroller: Qt `lrelease`, diffkontroll, `svlang` för ändrade formuleringar och Hunspell-sv för de nya orden. `l10n-lint` kördes för hela katalogen; dess kvarvarande träffar omfattar historiska/föråldrade poster, källtextlika biblioteknamn och acceleratorer och behandlas successivt i kommande batcher.

Token saknar Transifex behörigheten att formellt markera en översättning som granskad. Importen är därmed verifierad som sparad, men formell Transifex-granskning är inte utförd.
