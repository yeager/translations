# PS5 Cooling System Center – svenska

Utgångspunkt: `strongt1me/ps5-cooling-system-center-pro` vid commit
`8a927c8e5d81ee3a0bee8aa35484501069b3c0ac` (2026-10-26), senaste release
1.74.0 från 2026-10-22.

## Pågående batch 2026-10-26

Projektet har ungefär 4 461 översättningsbara tyska källsträngar och saknade
svenska helt. Den första batchen lägger till:

- `sv-SE` som valbar locale och *Svenska* i språklistan;
- en separat svensk JSON-katalog med 4 336 centrala gränssnittssträngar;
- översättningar för vanliga åtgärder, systemkontroller, kylning och
  bekräftelser.

Kontrollerat med JSON-tolkning, projektets `check_lang.py`, JavaScript-
syntaxkontroll, `git diff --check`, Hunspell och Gitleaks. Projektkontrollen
rapporterar 0 formatfel och inga saknade strängar. Den färdiga katalogen
skickades den 27 oktober 2026 som
[PR #1](https://github.com/strongt1me/ps5-cooling-system-center-pro/pull/1).
Pull requesten är öppen och ren, men har ännu varken underhållargranskning
eller rapporterade CI-resultat.

`sv-work-in-progress-20261026.json` är den senaste granskade arbetskopian.
