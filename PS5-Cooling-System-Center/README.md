# PS5 Cooling System Center – svenska

Utgångspunkt: `strongt1me/ps5-cooling-system-center-pro` vid commit
`8a927c8e5d81ee3a0bee8aa35484501069b3c0ac` (2026-10-26), senaste release
1.74.0 från 2026-10-22.

## Pågående batch 2026-10-26

Projektet har ungefär 4 461 översättningsbara tyska källsträngar och saknade
svenska helt. Den första batchen lägger till:

- `sv-SE` som valbar locale och *Svenska* i språklistan;
- en separat svensk JSON-katalog med 3 626 centrala gränssnittssträngar;
- översättningar för vanliga åtgärder, systemkontroller, kylning och
  bekräftelser.

Kontrollerat med JSON-tolkning, projektets `check_lang.py`, JavaScript-
syntaxkontroll, `git diff --check`, Hunspell och Gitleaks. Projektkontrollen
rapporterar 0 formatfel men 832 ännu oöversatta källsträngar. Ingen
uppströmsinsändning har därför skapats ännu.

`sv-work-in-progress-20261026.json` är den senaste granskade arbetskopian.
