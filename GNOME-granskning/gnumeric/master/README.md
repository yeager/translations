# Gnumeric — master — svenska kataloger

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/gnumeric/master/po/sv/> och <https://l10n.gnome.org/vertimus/gnumeric/master/po-functions/sv/>.
- GNOME-inskick: `po` och `po-functions` skickades 2026-11-23 via Damned Lies API med kommentaren `Granskad och klar`; båda uppladdningarna returnerade `{"result":"OK"}`.
- Översättarmetadata i ändrade kataloger: `Daniel Nylander <gnome@danielnylander.se>`, 2026-11-23.

## `po`

- Aktuell källa: GNOME Damned Lies-aktivitet och senaste POT hämtade 2026-11-25. POT SHA-256: `0da1f1ec01e75ea5a2e84608d8e4265f436808f086095ba846e7499a036f5e45`.
- Före granskning mot senaste POT: 3 969 översatta, 28 fuzzy, 11 oöversatta (4 008 poster).
- Efter granskning: 4 008 översatta, 0 fuzzy, 0 oöversatta. 55 pluralposter. 86 katalogposter ändrade jämfört med arkiverat original: 11 nya översättningar, 28 fuzzy-poster färdigställda och 47 befintliga översättningar rättade.
- Full QA: `msgfmt --check` godkänd; platshållare, pluralformer, markup och acceleratorer kontrollerade. `l10n-lint --language sv`: 0 fel, 2 varningar för gemenstavat filformat `xbase` i två källsträngar. 1-2-3-formatnamnet är bevarat. Hunspell-sv körd; tekniska identifierare och funktionsnamn är rimliga undantag.
- Översättarmetadata i ändrad katalog: `Daniel Nylander <gnome@danielnylander.se>`.
- GNOME-inskick: 2026-11-25 via Damned Lies API, kommentaren `Granskad och klar. Argumentnamnen i funktionssignaturerna är översatta; funktionsidentifierarna är bevarade.` Aktivitetssidan visar uppladdningen och 4 008/0/0; statistik-API:t returnerade ännu äldre cachad statistik vid efterkontrollen.

## `po-functions`

- Aktuell källa: Damned Lies-POT och svensk PO hämtade 2026-11-23.
- Före granskning: 2 183 aktiva poster, 11 oöversatta och 43 fuzzy.
- Efter granskning: 2 183 aktiva poster, 0 oöversatta och 0 fuzzy.
- Ändringar: 11 nya svenska översättningar och 43 korrigerade fuzzy-poster.
- Validering: `msgfmt --check`, egen kontroll av platshållare, pluralformer, tabbar och radbrytningar samt `l10n-lint --language sv --skip-fuzzy`.
- Dokumenterat lint-undantag: `l10n-lint` misstolkar Gnumerics avsiktligt översatta `@{argument}` som Python-platshållare. Gnumerics `README.translators` kräver uttryckligen översättning av användarvisade argumentnamn och konsekvent användning i `@{…}`. Versala funktionsnamn före kolon lämnas oförändrade.

## Återstår

Gnumerics hjälp (`help`) är också radgranskad mot senaste POT; se [hjälprapporten](help/README.md).

## Korrigering av kommandoradsmetavariabler (2026-11-24)

- 1 befintlig sträng korrigerad: beskrivande kommandoradsargument översatta till svenska.
- Validering: `msgfmt --check`; `l10n-lint`-regeln `metavariable-translation` ger inga kvarvarande träffar i de 295 granskade huvudgrenarnas kataloger.
- Ändringen är lokal och har inte skickats till GNOME.
