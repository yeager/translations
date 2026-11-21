# Verktyg: svlang-sökvägskontroll

Under Core-granskningen hittades ett falskt stavningslarm: `www` i den lokala sökvägen `/config/www/` markerades som trippelkonsonantfel.

`svlang` uppdaterades så att segment direkt mellan snedstreck behandlas som sökvägskod. Arbetskopians språkregeltester verifierades med:

`PYTHONPATH=tools/svlang/src python3 -m pytest -q tools/hunspell-sv/tests/test_swedish_rules.py tools/svlang/tests/test_skrivregler.py`

Resultat: 17 tester och 267 deltester godkända. Verktygsändringen är pushad till `yeager/svlang` i commit `27fb941`.
