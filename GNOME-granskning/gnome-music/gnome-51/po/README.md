# GNOME Music — gränssnitt, gnome-51

Radgranskning av den svenska UI-katalogen mot senaste POT.

- Damned Lies: https://l10n.gnome.org/vertimus/gnome-music/gnome-51/po/sv/
- POT-datum: 2026-11-22 11:54 UTC; SHA-256 `ac73896eee8411d6720cf98d3612b6c6fd16e1a07cb5c7b15c8c09a75a04b8f4`.
- GNOME-statistik före och efter granskning: 128 översatta, 0 fuzzy, 0 oöversatta.
- Granskade strängar: 128 av 128.
- Översättningar som fylldes i: 0.
- Befintliga översättningar som rättades: 7.
- 123 källnycklar återanvändes från den nyligen radgranskade `main/po`-katalogen. Fem gnome-51-specifika strängar granskades separat.

## Rättelser

Korrigerade album-/artistsidornas bestämda form, `Toggle repeat`, Tracker-versionstexterna, sökförslaget och en beskrivning av uppspelningslägen. Terminologin följer den nyligen granskade hjälpen och gnome-51 UI.

## Validering

- `msgfmt --check --check-format`: godkänd.
- `msgcmp` mot senaste POT: katalogerna matchar.
- `l10n-lint --language sv --reference <latest.pot>`: 0 fel, 0 varningar. Tre informationsnotiser är rimliga: två strängar blir långa på svenska och en accelerator flyttades till en giltig svensk bokstav.
- Alla 128 poster är översatta och fuzzy-fria. Markup, platshållare och radbrytningar kontrollerades; översättarnas kreditlista har avsiktligt en person per rad.
- Acceleratorer granskade i alla 12 berörda strängar: källans och svenskans markörantal matchar. Alla svenska acceleratorer använder icke-nordiska bokstäver.
- `hunspell -d sv_SE`: okända ord är dokumenterade undantag: `none`, `song`, `shuffle` och `disabled` är bokstavliga inställningsvärden; `ReplayGain`, `ReplayGain-metadata`, `Tracker`, `track` och `XDG-musikkatalog` är tekniska namn/termer; `Gisslén` är ett efternamn.

Damned Lies API efter granskningen svarar HTTP 200 med 128/0/0; aktivitetssidan hämtades också (HTTP 200). Ingen fil eller kommentar har skickats in.

## Arkiverade filer

- [Original PO](gnome-music.gnome-51.sv.original.po)
- [Senaste POT](gnome-music.gnome-51.pot)
- [Granskad PO](gnome-music.gnome-51.sv.reviewed.po)
- [Diff](gnome-music.gnome-51.sv.review.diff)
- [API före granskningen](api-before.json)
- [API efter granskningen](api-after.json)
- [Aktivitetssida efter granskningen](activity-after.html)
