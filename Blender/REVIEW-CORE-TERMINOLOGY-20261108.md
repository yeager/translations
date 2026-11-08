# Blender UI – kärnterminologi, batch 1 258

Den här deltafilen omfattar nio kontextbundna poster från Blender UI:s svenska
PO-export. Termerna har kontrollerats mot den projektspecifika
`TERMINOLOGY.md`; TM-poster som avvek har korrigerats, medan redan korrekta
poster behölls.

| Källa | Svensk term |
| --- | --- |
| Bone Envelope | Benomslutning |
| Soft Body Point Cache | Punktcache för mjukkropp |
| Dynamic Paint canvas settings | Dukinställningar |
| Remesh Modifier | Ommeshningsmodifierare |
| Curve Modifier | Kurvdeformeringsmodifierare |
| Voronoi Crackle | Voronoi-sprickmönster |
| Stereo 3D | Stereoskopisk 3D |
| Line Art | Linjekonst |

Kontroller: `msgfmt --check`, `l10n-lint`, `svlang consistency`,
`svlang skrivregler`, `svlang svengelska`, Hunspell och Gitleaks. Hunspell
markerar de projektspecifika sammansättningarna `mjukkropp`,
`Dukinställningar`, `Ommeshningsmodifierare`,
`Kurvdeformeringsmodifierare` och `Voronoi-sprickmönster`; de är avsiktliga
och dokumenterade Blender-termer.

SHA-256 för deltafilen:
`2a1a3331ed1d4f464d6f668cd26cd3a2f6ddf6b0f9e890b824d201d93017845c`.

Status: lokalt granskat och arkiverat. Weblate-import kräver separat verifiering.
