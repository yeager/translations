# ORION Media Center – svenska

Källa: `XeN-Made/Orion-Media-Center`, commit
`7463a4550bb30e372b418bafd506cb16694a25f4`, release `01.104.000`
(2026-10-24).

Projektet använder egna `.lang`-filer och har redan inbyggt säkert återfall
till engelska för tomma texter. Den här första svenska satsen lägger till
`assets/lang/sv.lang` med 285 av 542 strängar: bibliotek, omslagsbilder,
grundläggande start- och uppdateringsflöden, kategorier, sortering, teman och
relativa datum.

Kontroller:

- Formatkontroll: 542 giltiga språkposter, inga syntaxfel.
- Projektets `tools/gen-lang.py --check`: 257 saknade svenska översättningar
  återstår; inga formatfel i de ifyllda posterna.
- Hunspell gav endast förväntade produkt- och tekniknamn.
- Ändringen klarade `git diff --check` och en avgränsad Gitleaks-kontroll.

Ingen uppströms-PR har skapats: filen är medvetet ofullständig och ska först
fyllas och granskas helt.
