# NetworkManager-fortisslvpn — main/po

- GNOME-aktivitet: <https://l10n.gnome.org/vertimus/networkmanager-fortisslvpn/main/po/sv/>
- Granskad: 2026-11-24
- Aktuell POT: 33 aktiva strängar; 33 översatta, 0 fuzzy och 0 oöversatta efter granskning.
- Nya översättningar: 0
- Rättade befintliga översättningar: 4

## Ändringar

Sammansättningar för SSLVPN har förtydligats, autentiseringsfältet *Realm* är översatt till *Domän* med svensk accelerator, och den felaktigt översatta konfigurationsplatshållaren `user <namn>` har återställts till exakt `user <name>`. Det engelska ordet *peer* har ersatts med *motparten*.

## Validering

`msgfmt --check`, `msgcmp --use-fuzzy` och `l10n-lint` har körts utan fel eller varningar. `l10n-lint` rapporterar enbart två informationsnotiser för avsiktligt ändrade acceleratorer i Avbryt och Verkställ. Platshållarkontrollen hittar inga avvikelser. Hunspell-utdata består endast av tekniska termer och ordfragment från acceleratormarkörer.

Ingen GNOME-inskickning har gjorts.

- GNOME-inskick: 2026-11-26 via Damned Lies API; kommentaren `Granskad och klar` och aktivitetssidan verifierade; statistik 33/0/0.
