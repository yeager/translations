# gimp-help — gimp-help-3-0 — svensk dokumentation

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/gimp-help/gimp-help-3-0/dialogs/sv/>.
- Granskade kataloger: `po/sv/appendix.po`, `concepts.po`, `dialogs.po`, `glossary.po` och `toolbox.po`.
- Åtgärd: Exakt överföring från den granskade masterkatalogen, därefter radvis översättning och granskning av de återstående 69 posterna i `concepts.po`, inklusive DocBook-bildreferenser.
- Slutlig lokal statistik: samtliga aktiva svenska poster är översatta och fuzzy-fria. Obsoleta fuzzy-poster i `concepts.po` är historik och ingår inte i den aktiva katalogen.
- Validering: `msgfmt --check`, `l10n-lint --language sv --skip-fuzzy` och `git diff --check` gav inga fel. Hunspell granskades på enbart svenska `msgstr`; träffarna består huvudsakligen av GIMP-termer, filnamn, kommandoradsflaggor och tekniska identifierare.
- Översättarmetadata i ändrade filer: Daniel Nylander <gnome@danielnylander.se>, 2026-11-23.
- GNOME-inskick: inget — enligt arbetsinstruktionen.
