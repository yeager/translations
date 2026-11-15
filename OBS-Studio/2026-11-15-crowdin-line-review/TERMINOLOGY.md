# OBS Studio — Swedish terminology

Scope: UI text in OBS Studio and its audio, video and encoder plugins.  
Updated: 2026-11-15.

| English term | Swedish recommendation | Context / exception |
| --- | --- | --- |
| audio driver | ljuddrivrutin | Retain ASIO in `ASIO-ljuddrivrutin`. |
| audio monitoring | monitorering | Use `ASIO-monitorering` in the DAW/ASIO context. |
| bitrate | bithastighet | Never use `hastighet` when the source means encoded bit rate. |
| bitrate control / rate control | bithastighetskontroll | Encoder UI. |
| codec | kodek | Also in compounds such as `NVENC-kodek`. |
| encode | kodning | Use compounds: `10-bitarskodning`, `4:4:4-kodning`. |
| encoder | kodare | `utmatningskodare` where the source specifies output encoder. |
| frame | bildruta | `B-bildruta`, `nyckelbildruta`. |
| keyframe interval | nyckelbildsintervall | Include the unit if present in source. |
| GPU utilization / usage | GPU-användning | Prefer the familiar UI abbreviation over a long compound. |
| GPU load | GPU-belastning | Distinct from usage where source says load. |
| look-ahead | look-ahead | Retain the exposed feature name; explain it in Swedish prose. |
| sidechain source | sidechain-källa | Established audio-production loan/compound. |
| driver reload | läs in drivrutinen på nytt | Button/action label. |
| virtual camera | virtuell kamera | Use `virtuell webbkamera` only where source explicitly says webcam. |
| VST3 plugin | VST3-insticksmodul | OBS plugin UI. |
| adaptive quantization | adaptiv kvantisering | `tidsmässig/rumslig` for Temporal/Spatial. |
| perceived visual quality | upplevd bildkvalitet | Avoid vague `visuellt resultat`. |
| split encode | delad kodning | Setting label, not an imperative. |
| blur strength | oskärpestyrka | Filter UI. |
| every N frames | var N:e bildruta | Do not translate as “after N frames”. |
| noise removal | brusborttagning | NVIDIA Audio Effects UI. |
| room echo removal | rumsekoborttagning | NVIDIA Audio Effects UI. |

## Style decisions

- Use direct imperatives in UI guidance: `Försök igen`, `Flytta OBS …`; avoid `Var god`.
- Keep code, variables, format labels, product names and example options unchanged: `%1`, `NVENC`, `I010`, `P010`, `nvEncodeAPI`, `Windows Game DVR`.
- Use ordinary Swedish compounds when they improve readability: `JACK-server`, `JACK-ingångsklient`, `B-bildruta`.
- Do not introduce an em dash unless it occurs in the source.
