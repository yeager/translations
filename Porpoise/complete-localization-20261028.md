# Porpoise: komplett svensk lokalisering, 28 oktober 2026

Projektets officiella release `v4.0` publicerades 2026-10-21 och uppfyller
kravet på en release yngre än 48 månader. Arbetet utgår från den aktiva
huvudgrenen, som kontrollerades samma dag.

`porpoise-sv-complete-20261028.json` är den kompletta svenska katalogen med
1 803 av 1 803 nycklar. SHA-256 är
`6be0456964d2f826db6fe4a57482c702195664585dfc324c55a600b382ff0873`.

Denna slutliga runda normaliserar 26 synliga statusellipser till `…` och
procenttypografin i en sträng. Katalogens nycklar och `{…}`-platshållare är
identiska med den engelska källistan. Den genererade C++-tabellen kompilerar
med C++17, `-Wall`, `-Wextra` och `-Werror`. Den svenska flaggresursen är
reproducerbar från `tools/make-flags.py` och består av 17 celler à 96 × 64
pixlar.

`l10n-lint` kan inte använda Porpoises objektbaserade `strings.json` som
referenskatalog: varje källpost är ett objekt med fältet `en`, medan verktyget
förväntar sig en direkt nyckel-till-värde-katalog. Dess katalogfel i denna
körning gäller därför formatstödet, inte en avvikelse i katalogens verifierade
nyckelmängd. `svlang` och Hunspell användes som granskningsunderlag; deras
återstående träffar omfattar främst tekniska namn, filformat, produktnamn och
längre hjälptexter och är inte automatiskt ändrade.

Full PS5-körning är inte verifierad i denna arbetsmiljö. PR:n ska därför
beskriva den lokala generator- och kompilatorverifieringen, men inte påstå
fysisk konsoltestning.
