# GNOME Music — hjälp, gnome-51

Granskning av svenska hjälpöversättningar mot senaste POT-filen.

- Damned Lies: https://l10n.gnome.org/vertimus/gnome-music/gnome-51/help/sv/
- API-kontroll efter granskning: HTTP 200, 72 översatta, 0 fuzzy, 0 oöversatta; tillstånd `None`.
- POT: `POT-Creation-Date: 2026-11-28 08:13+0000`; SHA-256 `80d1424502b85c4249a0a1f587ce3598bef68d578e7f17e5940191412eeca4c1`.
- Granskade strängar: 72 av 72.
- Nya översättningar: 0.
- Befintliga översättningar rättade: 31.
- Slutstatus: 72 översatta, 0 fuzzy, 0 oöversatta.

## Granskning

Alla poster har jämförts med aktuell engelska källa och svensk UI-kontext. Rättelserna gör instruktionerna mer idiomatiska och konsekventa, bland annat för att markera album/låtar, skapa spellistor, upprepning, slumpmässig uppspelning och sökning. Appens befintliga UI-etiketter har bevarats där de används direkt i dokumentationen. Licensnamnet följer GNOME TM:s vedertagna svenska form.

## Validering

- `msgfmt --check --check-format`: godkänd.
- `msgcmp` mot senaste POT: katalogerna matchar.
- `l10n-lint --language sv --reference <latest.pot>`: 0 fel, 0 varningar.
- Egen kontroll: 72 poster matchar POT; 0 tomma, 0 fuzzy; markup, platshållare och logiska radbrytningar bevarade; inga acceleratorer förekommer i källan eller översättningen.
- `hunspell -d sv_SE`: endast rimliga undantag: `Shobha` och `Tyagi` (författarnamn), `Erkännande-DelaLika` (svensk licensterm) och `Unported` (officiell licensbeteckning).

Ingen fil har skickats till Damned Lies. Aktivitetssidan hämtades efter granskningen (HTTP 200); ingen ny aktivitet eller kommentar skapades.

## Arkiverade filer

- [Original PO](gnome-music.gnome-51.help.original.po)
- [Senaste POT](gnome-music.gnome-51.help.latest.pot)
- [Granskad PO](gnome-music.gnome-51.help.reviewed.po)
- [Diff](gnome-music.gnome-51.help.review.diff)
- [API före granskningen](api-before.json)
- [API efter granskningen](api-after.json)
- [Damned Lies-aktivitetssida efter granskningen](activity-after.html)
