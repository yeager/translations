# Hunspell-sv: granskade okända ord

Hunspell-sv markerade 87 tokenformer. Samtliga har kontrollerats mot den aktuella GStreamer-katalogen. Inga vanliga svenska stavfel återstår.

- **GStreamer- och GLib-namn:** `GStreamer`, `GstCaps`, `GstDateTime`, `GstPreset`, `GDate`, `GST_*`, `NULL`, `ANY`, `READY`, `PAUSED`, `PLAYING`, `EOS`, `PREROLL`, `PREROLLED`, `PREROLLING` och `TTY` är projektnamn, API-typer, miljövariabler eller tillstånd.
- **Format och protokoll:** `URI`, `ISO-639-1`, `ISO-639-2`, `WGS84`, `ISRC`, `ReplayGain` och `R128` är standardnamn eller metadataformat. `Code` och `Recording` förekommer i standardnamnet `International Standard Recording Code`.
- **Kommandorad och exempel:** `AUTOPLUG:5`, `:3`, `COLORS`, `INSPECT`, `PATH`, `off`, `on`, `disable`, `auto`, `unix`, `no-position`, `force-position`, `key=value`, `key[en]=comment`, `ANY` och `NULL` är oförändrade exempel, flaggvärden eller metavariabler.
- **GStreamer-termer:** `caps`, `pad`, `source-pad`, `sink-pad`, `typefind`, `demultiplexa` och `multiplexa` är etablerade tekniska termer i element- och strömbeskrivningar.
- **Svenska sammansättningar:** bland annat `caps-filtret`, `kodarversion`, `undertextkodek`, `licens-URI`, `upphovsrätts-URI`, `GStreamer-versionen`, `GStreamer-tidsenheter` och `maskintolkningsbar` är avsiktliga svenska sammansättningar.
- **Formatfragment:** former som `sElementflaggor`, `sImplementerade`, `sTotalt`, `-element`, `-strömmen` och `-egenskap` uppstår när Hunspell läser `%s`-platshållare intill översatta textfragment. De är inte ord i användartexten.

Översättningsminnet bekräftar etablerad användning av `kodek`, `dirigent`, `artist` och `skivbolag`. Termträffarna granskades i sammanhang; inget tillämpades automatiskt.
