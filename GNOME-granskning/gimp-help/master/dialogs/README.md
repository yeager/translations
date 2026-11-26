# GIMP Help — master — dialogs — svenska

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/gimp-help/master/dialogs/sv/>.
- Ursprunglig lokal katalog: 2 094 översatta, 148 fuzzy och 37 oöversatta poster.
- Slutlig lokal katalog: 2 279 översatta, 0 fuzzy och 0 oöversatta poster.
- Åtgärd: samtliga öppna poster var `@@image:`-metadata. Kontrollsummorna synkroniserades med källan; inga användarvisade textsträngar behövde omskrivas.
- Validering: `msgfmt --check --statistics` och `git diff --check` är godkända. `l10n-lint` gav 0 fel; dess varningar gäller befintliga DocBook-gränser och innehållsregler i äldre dokumentation.
- Avsiktliga undantag: inga aktiva `@@image:`-poster avviker från källan.
- Översättarmetadata: Daniel Nylander <gnome@danielnylander.se>, 2026-11-23.
- GNOME-inskick: inget — enligt arbetsinstruktionen.

## Riktad terminologikorrigering — 2026-11-26

Två befintliga poster använder nu **Fyll** som verktygsnamn och **fyllnadsverktyg** i löptext. Katalogens tidigare radgranskning och statistik ändras inte; ingen GNOME-inskickning har gjorts.
- Validering av termrättningen: `msgfmt --check --check-format` godkändes; l10n-lint rapporterade 0 fel och inga varningar i de ändrade posterna. Markup, platshållare, pluralformer och radbrytningar är oförändrade. Hunspell-SV markerade bara Wilber, GIMP-maskotens namn.
