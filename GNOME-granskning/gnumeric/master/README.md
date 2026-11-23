# Gnumeric — master — svenska kataloger

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/gnumeric/master/po/sv/> och <https://l10n.gnome.org/vertimus/gnumeric/master/po-functions/sv/>.
- GNOME-inskick: inget — enligt arbetsinstruktionen.
- Översättarmetadata i ändrade kataloger: `Daniel Nylander <gnome@danielnylander.se>`, 2026-11-23.

## `po`

- Aktuell källa: Damned Lies-POT och svensk PO hämtade 2026-11-23.
- Före granskning: 4 008 aktiva poster, 11 oöversatta och 28 fuzzy.
- Efter granskning: 4 008 aktiva poster, 0 oöversatta och 0 fuzzy.
- Ändringar: 11 nya svenska översättningar och 28 korrigerade fuzzy-poster.
- Validering: `msgfmt --check`; egen C-format- och pluralformskontroll; `l10n-lint --language sv` med 0 fel (123 informationsnotiser och 31 varningar); `hunspell-sv`.
- Hunspell-undantag: 678 träffar domineras av avsiktliga kommandon, filändelser, formatkoder, funktionsnamn, protokoll, statistiska termer och personnamn. Inga stavningsfel i de nyöversatta posterna identifierades.

## `po-functions`

- Aktuell källa: Damned Lies-POT och svensk PO hämtade 2026-11-23.
- Före granskning: 2 183 aktiva poster, 11 oöversatta och 43 fuzzy.
- Efter granskning: 2 183 aktiva poster, 0 oöversatta och 0 fuzzy.
- Ändringar: 11 nya svenska översättningar och 43 korrigerade fuzzy-poster.
- Validering: `msgfmt --check`, egen kontroll av platshållare, pluralformer, tabbar och radbrytningar samt `l10n-lint --language sv --skip-fuzzy`.
- Dokumenterat lint-undantag: `l10n-lint` misstolkar Gnumerics avsiktligt översatta `@{argument}` som Python-platshållare. Gnumerics `README.translators` kräver uttryckligen översättning av användarvisade argumentnamn och konsekvent användning i `@{…}`. Versala funktionsnamn före kolon lämnas oförändrade.

## Återstår

Gnumerics separata hjälpkatalog (`help`) är ännu inte radgranskad. Den är därför inte markerad som klar i GNOME-inventeringen.
