# ORION Media Center – svenska

Källa: `XeN-Made/Orion-Media-Center`, commit
`7463a4550bb30e372b418bafd506cb16694a25f4`, release `01.104.000`
(2026-10-24).

Projektet använder egna `.lang`-filer och har redan inbyggt säkert återfall
till engelska för tomma texter. Det kompletta svenska språkpaketet
`assets/lang/sv.lang` täcker nu samtliga 542 strängar: bibliotek,
omslagsbilder, start- och uppdateringsflöden, kategorier, sortering, teman,
relativa datum, inställningsguiden och speldetaljer.

Kontroller:

- Formatkontroll: 542 giltiga språkposter, inga syntaxfel eller tomma måltexter.
- Projektets `tools/gen-lang.py --check` godkänner katalogen.
- Platshållarkontroll: alla käll- och målplatshållare är identiska.
- Hunspell gav endast förväntade produkt- och tekniknamn, bland annat ORION,
  RetroArch, SteamGridDB, konsolnamn och styrknappar.
- Ändringen klarade `git diff --check` och en avgränsad Gitleaks-kontroll.
- `svlang` och `l10n-lint` saknar stöd för projektets egna `.lang`-format;
  deras filomfattande resultat är därför inte meningsfulla för denna katalog.

Ändringen är inskickad som uppströms-[PR #13](https://github.com/XeN-Made/Orion-Media-Center/pull/13).
Vid arkiveringstillfället är den öppen och väntar på CI samt underhållargranskning.
