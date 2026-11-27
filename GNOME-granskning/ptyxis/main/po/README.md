# Ptyxis — main/po

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/ptyxis/main/po/sv/>
- Aktuell POT: 473 aktiva strängar. Den hämtade svenska katalogen hade 12 oöversatta strängar och 0 fuzzy; den granskade filen har 0 oöversatta och 0 fuzzy.
- Granskning: hela katalogen är radgranskad. 12 nya översättningar har tillkommit och 85 befintliga formuleringar har rättats för betydelse, idiomatik, stavning och konsekvent terminalterminologi. Tekniska identifierare, platshållare och markup är bevarade.
- Acceleratorer: inga `_ä`, `_å` eller `_ö`; samtliga acceleratorer använder ASCII-bokstäver.
- Validering: `msgfmt --check` och `l10n-lint --check --language sv` utan fel. POT och granskad katalog har båda 473 aktiva nycklar, utan nyckel- eller platshållaravvikelser.
- Hunspell: tekniska identifierare och produktnamn är manuellt kontrollerade undantag, bland annat `Ptyxis`, `PTY`, `CJK`, `OSC`, `TTY`, `podman`, `toolbox`, `distrobox`, `cgroup`, kommandoflaggor samt acceleratorfragmentet `ppna` från `Ö_ppna`.
- GNOME-inskick: inskickad 2026-11-23 via Damned Lies API med kommentaren `Granskad och klar`; API:t returnerade `{"result":"OK"}`.

## Korrigering av kommandoradsmetavariabler (2026-11-24)

- 4 befintliga strängar korrigerade: beskrivande kommandoradsargument översatta till svenska.
- Validering: `msgfmt --check`; `l10n-lint`-regeln `metavariable-translation` ger inga kvarvarande träffar i de 295 granskade huvudgrenarnas kataloger.
- Ändringen är lokal och har inte skickats till GNOME.

## Uppföljning efter tidigare uppladdning

Fyra kommandoradsmetavariabler korrigerades 2026-11-24 efter uppladdningen 2026-11-23. En ytterligare formulering rättades 2026-11-27: `Removed profile “%s”` blev `Profilen ”%s” togs bort`. Uppföljningsfilen laddades upp 2026-11-27 21:09 UTC med kommentaren `Granskad och klar`; aktivitet 1582105 bekräftar 473/0/0. Den sammanslagna PO-filen matchar den granskade filen exakt. `l10n-lint` ger 0 fel och 0 varningar; informationsnotiserna gäller placering av giltiga ASCII-acceleratorer och valutastil.

- Hunspell: `hunspell-unknown.txt` innehåller stavningslexikonets okända token från den aktuella granskade filen. Träffarna är kontrollerade: tekniska namn/flaggor och svenska sammansättningar, acceleratorfragment samt den avsiktliga fontprovstexten `hwila` (pangram med bokstaven w).

- Uppladdningsverifiering: `submission.json`, `activity-after-upload.html` och `ptyxis.main.sv.submitted.merged.po`.
