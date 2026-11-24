# Svensk översättning av guvcview

Källan är [guvcview.pot på SourceForge](https://sourceforge.net/p/guvcview/git-master/ci/master/tree/po/guvcview.pot), hämtad 2026-11-24. POT-huvudet anger att den skapades 2024-06-01.

Alla 257 meddelanden är översatta. `sv.po` innehåller svensk text och `sv.diff` visar ändringarna från POT-filen.

## Kontroller

- `msgfmt --check`: godkänd.
- `l10n-lint --language sv --max-warnings 3`: 0 fel och 1 varning. Källan har den felaktiga avslutningen `?.` i frågan om att starta om; svenskan använder korrekt frågetecken.
- Platshållarkontroll: `%s` bevarad; inga skillnader i formatplatshållare.
- Acceleratorer: ett `Ö` i `_Open` har flyttats till `p` i `Öp_pna`, så acceleratorn inte använder en nordisk bokstav.
- Hunspell-svenska lästes från `/home/yeager/.ordverk/upstream/hunspell-sv`. Kvarvarande träffar är tekniska namn, codec-/API-/enumvärden, filändelser, produktnamn och sammansättningar som `GOP-storlek`, `byteström`, `H.264-hjälpström` och `strömmultiplexering`.

Tekniska formatnamn och identifierare som `H.264`, `MJPG`, `YUY2`, `NV12`, `CABAC`, `CAVLC`, `SVC`, `SNR`, `FOURCC`, `WIDTHxHEIGHT`, `FPS_NUM[/FPS_DENOM]`, `TIME_IN_SEC`, API-namn och filändelser har bevarats.
