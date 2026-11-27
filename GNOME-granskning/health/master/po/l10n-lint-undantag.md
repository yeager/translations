# Motiverade l10n-lint-notiser — Health/master/po

`l10n-lint` rapporterar inga fel. Varningarna är bedömda enligt följande:

- 17 `same-plurals`: korrekt identiska former för svenska `steg`, `pund`, `kilogram`, `meter` och `yard`, trots olika engelska singular- och pluralformer.
- 1 `inconsistent-capitalization`: källan använder enhetsbeteckningen `KM`; målet använder standardiserad SI-symbol `km`.
- Informationsnotisen om `1` i `_Every 1 hour` är avsiktlig: svensk idiomatisk form är `_Varje timme`.
- Informationsnotisen om `7.500` återges som `7 500` enligt svensk tusentalsavgränsning.
- `Sync` → `Synkronisering` är korrekt sektionsrubrik; längdvarningen är inte ett språkfel.
- Acceleratorerna har flyttats till svenska bokstäver som inte är `å`, `ä` eller `ö`; boundary-notiserna visar endast att den understrukna bokstaven bytts.
