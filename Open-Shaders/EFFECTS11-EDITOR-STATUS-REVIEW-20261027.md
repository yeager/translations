# Open Shaders: Effects11-redigerarens status, häfte 47

Detta häfte omfattar tolv aktuella, tidigare tomma status- och
ändringsmeddelanden i Effects11-redigeraren. Källtexterna har jämförts med
Open Shaders `dev` vid revision `c1b1ef1` den 27 oktober 2026 och med den
svenska Weblate-exporten från 19 oktober 2026.

`CS` behålls som den etablerade förkortningen för Community Shaders. *Revert*
formuleras som *återställa* i det förklarande meddelandet, eftersom åtgärden
förkastar osparade ändringar. Räkneplatsmarkören `{count}` och radbrytningen
bevaras.

`open-shaders-effects11-editor-status-sv-20261027.json` är ett delta på tolv
nycklar. Det får importeras först efter upplåsning och en ny jämförelse med
Hosted Weblates aktuella export.

## Kontroll

JSON-syntax, `l10n-lint` och Gitleaks passerar. Källnycklarna,
räkneplatsmarkören `{count}` och radbrytningen matchar den engelska katalogen.
`svlang` ger 8,8 av 10 och rapporterar den normala infinitivfrasen ”Att
återställa förkastar …” som en falsk V2-varning. Hunspell markerar bara `CS`,
tekniktermen `shaders` och platsmarkören.
