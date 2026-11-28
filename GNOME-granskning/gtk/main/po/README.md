# GTK — main — po/sv

- GNOME-katalog: https://l10n.gnome.org/vertimus/gtk/main/po/sv/
- Upstream: https://gitlab.gnome.org/GNOME/gtk/-/tree/main/po
- Källgrenens HEAD vid granskning: `42cf1237457d302f957b8ebd95957f65470f8e87`.
- Senaste POT: uppladdad till Damned Lies 2026-11-26 23:35 lokal tid; POT-huvudets datum `2026-11-26 08:03+0000`.
- Status före granskning: 1 792 översatta, 16 fuzzy, 22 oöversatta av 1 830.
- Status efter granskning: 1 830 översatta, 0 fuzzy, 0 oöversatta.
- Granskade strängar: 1 830. Nya översättningar: 22. Rättade befintliga översättningar: 188 (varav 16 fuzzy-markerade). Ändrade poster totalt: 210.
- Validering: `msgcmp` godkänd; `msgfmt --check --check-format` godkänd; `l10n-lint --language sv` 0 fel och 0 varningar; separat kontroll av källmängd, platshållare, pluralformer, markup, radbrytningar och acceleratorer utan avvikelser. 70 informationsnotiser i l10n-lint är granskade, bland annat orörda tangentnamn och avsiktligt oförändrade identifierare.
- Hunspell-sv: `hunspell -d sv_SE -l`; 82 okända token granskades och dokumenterades i `hunspell-exceptions.md`. Ingen kvarstående stavningsanmärkning.
- Terminologi: GTK:s filhanterings- och utskriftsfel, Path Tool CLI, .node/PNG och OpenType-termer granskades. CLI-värden som `winding`, `even-odd`, `miter-clip`, `round`, `square`, kommandonamn och tekniska variabler bevaras exakt.
- Översättningsminne: `swedish-tm/sv-gnome.po` användes som stöd; exakta kandidatträffar för ändrade källsträngar dokumenteras i `tm-lookups.json` och granskades manuellt.
- Last-Translator: Daniel Nylander <gnome@danielnylander.se>.
- GNOME-inskick: uppladdad via Damned Lies API 2026-11-27 12:53 UTC med kommentaren ”Granskad och klar”. Aktivitetssidan och den sammanslagna filen bekräftar 1 830/0/0; samtliga 1 830 översättningar matchar den granskade filen exakt. Statistik-endpointen visar fortfarande den äldre baslinjen 1 792/16/22, vilket dokumenteras i `submission.json`.

## A11y-terminologi, 2026-11-28

`Show Accessibility warnings` korrigerades från *Visa tillgänglighetsvarningar* till *Visa hjälpmedelsvarningar* i den lokalt granskade filen. Ingen annan befintlig a11y-etikett kräver ändring. l10n-lint: 0 fel/varningar; inga Hunspell-anmärkningar. `msgfmt` kördes inte eftersom den aktuella katalogen inte är komplett. Aktivitetssidan visar 1 792/16/22, men den nedladdade aktuella PO-filen mot samma 1 830-strängars POT ger 1 789/16/25. Rapporten behåller därför statusen *Behöver arbete* och markerar inte katalogen klar. Se `gtk-main-a11y-terminology-2026-11-28.diff`.
