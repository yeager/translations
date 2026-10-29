# Batch 06 – lokal granskningsfil

Den här sexsträngarsfilen skapades från en aktuell Weblate-export den
29 oktober 2026. Weblate exporterar strängar som behöver redigeras med tomma
måltexter. Därför slogs exporten samman lokalt med den tidigare fullständiga
svenska katalogen innan varje aktuell måltext granskades.

Ändringar:

- svensk titel och radbruten omslagstitel;
- naturligare bildbeskrivning av Adas kläder;
- `grenuttagslist` till `grenuttag`;
- `sköldpaddshalsringning` till `polokrage`;
- korrekt plural `tänger` och svensk uppräkning;
- naturligare formulering för ett FSFE-klistermärke.

Kontroller:

- `msgfmt --check` passerade (6 översatta meddelanden);
- `l10n-lint` gav inga fel eller varningar för ändringsfilen;
- `svlang skrivregler` gav inga träffar;
- Gitleaks fann inga hemligheter.

Filen är underlag för en separat Weblate-uppladdning. Den omfattar färre än
1 000 strängar enligt uppladdningspolicyn.
