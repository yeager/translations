# gimp-help — gimp-help-3-0 — svensk dokumentation

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/gimp-help/gimp-help-3-0/dialogs/sv/>.
- Granskade kataloger: `po/sv/appendix.po`, `concepts.po`, `dialogs.po`, `glossary.po` och `toolbox.po`.
- Åtgärd: Exakt överföring från den granskade masterkatalogen, därefter radvis översättning och granskning av de återstående 69 posterna i `concepts.po`, inklusive DocBook-bildreferenser.
- Slutlig lokal statistik: samtliga aktiva svenska poster är översatta och fuzzy-fria. Obsoleta fuzzy-poster i `concepts.po` är historik och ingår inte i den aktiva katalogen.
- Validering: `msgfmt --check`, `l10n-lint --language sv --skip-fuzzy` och `git diff --check` gav inga fel. Hunspell granskades på enbart svenska `msgstr`; träffarna består huvudsakligen av GIMP-termer, filnamn, kommandoradsflaggor och tekniska identifierare.
- Översättarmetadata i ändrade filer: Daniel Nylander <gnome@danielnylander.se>, 2026-11-23.
- GNOME-inskick: inget — enligt arbetsinstruktionen.

## Riktad terminologikorrigering — 2026-11-26

I katalogerna `dialogs.po`, `toolbox.po` och `glossary.po` korrigerades sammanlagt 15 befintliga översättningar: verktygsnamnet skrivs **Fyll**, och löptexten använder **fyllnadsverktyg**. Inga nya strängar tillkom. Detta är en avgränsad termrättning, inte en ny fullständig granskning.
- Validering av termrättningen: `msgfmt --check --check-format` godkändes i alla tre katalogerna; l10n-lint rapporterade 0 fel och inga varningar i de ändrade posterna. Markup, platshållare, pluralformer och radbrytningar är oförändrade. Hunspell-SV markerade bara Wilber, GIMP-maskotens namn.
