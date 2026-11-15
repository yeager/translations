# Audacity 4: svensk katalog och kompatibilitet, 15 november 2026

Den installerade macOS-versionen är Audacity 4.0.2. Den använder Qt-katalogen `Contents/Resources/locale/audacity_sv.qm`, medan den granskade upstream-PR:n #12778 gäller den äldre gettext-katalogen `au3/locale/sv.po`.

PO-katalogen har kontrollerats med `msgfmt` och kompilerats till Qt-format lokalt. En jämförelse med den installerade katalogen visar att den installerade versionen har 3 322 källsträngar, varav bara 1 277 delas med den granskade PO-katalogen. En direkt ersättning skulle därför tappa 2 045 Audacity 4-strängar och utfördes inte.

Den installerade katalogen använder redan "Mixa och rendera" för `Mix and Render`. Audacity 4 behöver granskas från sin egen Qt-källa innan dess fullständiga svenska katalog kan ersättas eller uppdateras säkert.
