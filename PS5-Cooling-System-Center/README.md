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

`sv-work-in-progress-20261026.json` är den tidigare granskade arbetskopian.

## Aktuell uppströmskontroll 2026-10-28

PR #1 stängdes utan merge och den svenska katalogen saknades i den aktuella
upstreamgrenen. Aktuell `main` jämfördes därför på nytt. Sedan den tidigare
katalogen har 48 nya tyska källtexter tillkommit, främst för PS4Mounts
uppdateringar och tilläggsinnehåll.

`sv-current-20261028.json` innehåller den aktuella kompletta katalogen med
4 508 av 4 508 extraherade källtexter. SHA-256 är
`786d51cb4b74c0e81d757b0b3c2656dc481bcbf8a128ccc641c0ccac336b2903`.
Projektets egen kontroll rapporterar 0 saknade och 0 formatfel. JSON och
JavaScript-syntax, `git diff --check` och scoped staged Gitleaks passerade.
Den platta exporten till l10n-lint rapporterar 0 fel; en varning för den
tekniska siffersekvensen `000` kvarstår.

Den uppdaterade katalogen är inskickad som
[PR #3](https://github.com/strongt1me/ps5-cooling-system-center-pro/pull/3)
och väntar på upstreamgranskning eller CI.
