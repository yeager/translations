# rygel — master — svenska UI

- GNOME-status före granskning: 276 översatta, 3 fuzzy, 0 oöversatta.
- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/rygel/master/po/sv/>
- Granskad rad: `No configuration file found, using defaults` → `Ingen konfigurationsfil hittades, använder standardvärden`.
- Åtgärd: Konfigurationsmeddelanden och den uppdaterade medieetiketten granskades mot aktuell källa.
- Ändringar: 0 nya översättningar och 5 rättade befintliga strängar jämfört med arkiverat original. Tre ingick i uppladdningen 2026-11-23; två lintfynd rättades lokalt 2026-11-27.
- Validering efter uppföljningsrättningarna: `msgcmp` mot aktuell POT och `msgfmt --check --check-format` godkända. `l10n-lint` ger 0 fel och 0 varningar; kvarvarande notiser gäller markupgränser. `hunspell-sv`-wrappen saknas i miljön, så den tillgängliga Hunspell-installationen kördes med `sv_SE`: 67 okända token granskades. Undantagen är produkt- och protokollnamn (Rygel, GStreamer, UPnP, DLNA, MPRIS), API- och kodidentifierare samt tekniska svenska sammansättningar som `mediaserver`, `mediaobjekt`, `mediamotor`, `omindexering` och `insticksmodulsalternativ`.
- Översättarmetadata: `Daniel Nylander <gnome@danielnylander.se>`, 2026-11-22 00:00+0100.
- GNOME-inskick: den tidigare versionen laddades upp till Damned Lies 2026-11-23 efter reservation, med kommentaren `Granskad och klar` (`{"result":"OK"}`). Aktivitet 1581374 visar sammanslagning 279/0/0. De två efterföljande lint-rättningarna är inte inskickade.
- Slutlig lokal status mot POT 2026-11-27: 279 översatta, 0 fuzzy, 0 oöversatta. POT-hash: `97ac32b7818919cc6173a9b0fc595df43b776ff128da119192be197759a394ba`.
- Uppföljning 2026-11-27: extra blanksteg före kolon togs bort och `ill-formed response string` ändrades från `otydlig svarssträng` till `felaktigt formaterad svarssträng`. Ändringarna är lokala och väntar på inskickning.
