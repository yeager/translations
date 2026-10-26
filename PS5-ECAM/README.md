# PS5-ECAM – svenska

Utgångspunkt: `premohq/PS5-ECAM` vid commit
`abbed4c0b893f5d221e32db92915ea771f0bd4fc` (2026-10-22), release 5.0.1.

Den svenska katalogen innehåller 1 669 av 1 669 översatta strängar. Den här
arkiveringen är den första avgränsade granskningsbatchen, inte ett påstående om
att hela katalogen redan har språkgranskats rad för rad.

## Batch 2026-10-26

- Rättar fyra felaktiga komman före *och*.
- Rättar gränssnittstermen *Preferenser* till *Inställningar*.
- `tools/lang.py check sv`, `git diff --check` och Gitleaks för den ändrade
  katalogen är godkända.

`l10n-lint` upptäcker återstående kandidater i den stora katalogen, men flera
är medvetet lika pluralformer, produktnamn eller kontrollens falska positiva
träffar. Fortsatt radgranskning behövs för övriga språkval och hjälprader.
