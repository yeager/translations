# Polari — main — svenska UI

- GNOME-status före granskning: 205 översatta, 0 fuzzy, 0 oöversatta.
- Aktuell POT hämtad från Damned Lies: 205 meddelanden. POT-huvudet är daterat 2026-05-31 15:27 UTC; aktivitetssidan visar mallen uppdaterad 10 november 2026.
- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/polari/main/po/sv/>
- Granskning: samtliga 205 aktiva meddelanden radgranskade. 77 befintliga översättningar rättade; 0 nya. Förbättringar omfattar IRC-terminologi, inställningar för NickServ/Identify, rum och kanaler, användarstatusar, offentliga delningstjänster, kommandohjälp och datumformat.
- Slutlig lokal status: 205 översatta, 0 fuzzy, 0 oöversatta.
- Validering: `msgfmt --check --check-format` och `msgcmp --use-fuzzy` godkända. `l10n-lint --language sv --reference` rapporterar 0 fel och 0 varningar; endast informationsnotiser om acceleratorer som flyttats till en naturligare svensk bokstav. Egen kontroll av `%`-platshållare, pluralformer, kommandometavariabler inom vinkelparenteser, radbrytningar och acceleratorantal godkänd. Inga aktiva nordiska acceleratorer.
- Hunspell-svenska: inga stavfel identifierade. Rimliga undantag: produktnamnet `Polari`, tekniska namn `Telepathy`, `Identify` och parametern `username`, samt acceleratorfragmentet `ndra` i `Ä_ndra`. `Avtysta` är korrekt i Polaris sammanhang: menyalternativet tar bort tystningen av en användare, inte ljuddämpning.
- Terminologi för rum/kanal, smeknamn, tysta/avtysta och offentlig delningstjänst finns i GNOME:s terminologilista.
- Översättarmetadata: `Daniel Nylander <gnome@danielnylander.se>`, 2026-11-26.
- GNOME-inskick: inget — enligt arbetsinstruktionen.
