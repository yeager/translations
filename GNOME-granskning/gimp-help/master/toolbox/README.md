# GIMP Help — master — toolbox — svenska

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/gimp-help/master/toolbox/sv/>.
- Ursprunglig lokal katalog: 1 488 översatta och 168 oöversatta poster.
- Slutlig lokal katalog: 1 656 översatta, 0 fuzzy och 0 oöversatta poster.
- Åtgärd: hela verktygslådekatalogen har radgranskats och kompletterats, inklusive färgområde, pensel- och gradientverktyg samt justeringsverktyget.
- Validering: `msgfmt --check --statistics`, `git diff --check` och `l10n-lint --language sv --check` är godkända. `hunspell-sv` kördes; träffar är DocBook-/PO-metadata, filnamn, XML-ID:n, produktnamn och etablerade tekniska termer.
- Översättarmetadata: Daniel Nylander <gnome@danielnylander.se>, 2026-11-23.
- GNOME-inskick: inget — enligt arbetsinstruktionen.

## Riktad terminologikorrigering — 2026-11-26

Tolv befintliga poster använder nu **Fyll** som verktygsnamn och **fyllnadsverktyg** i löptext. Katalogens tidigare radgranskning och statistik ändras inte; ingen GNOME-inskickning har gjorts.
- Validering av termrättningen: `msgfmt --check --check-format` godkändes; l10n-lint rapporterade 0 fel och inga varningar i de ändrade posterna. Markup, platshållare, pluralformer och radbrytningar är oförändrade. Hunspell-SV markerade bara Wilber, GIMP-maskotens namn.

## Kontroll mot senaste POT — 2026-11-26

Senaste POT skapades 2026-11-24 och innehåller 478 poster. Den arkiverade granskningen från 2026-11-23 matchar inte längre POT:en; katalogen laddas inte upp och måste uppdateras mot aktuell mall. API-statistik vid kontrollen: 28 översatta, 42 fuzzy och 408 oöversatta.
