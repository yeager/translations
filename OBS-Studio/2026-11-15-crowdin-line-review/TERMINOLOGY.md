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
| stream (settings-tab label) | Ström | Retain the established short tab label. |
| streaming | strömning | Use for the activity, service and adjective: `strömningstjänst`. |
| stream (live output/session) | direktsändning | Use in explanatory prose where `ström` would be unclear to an end user. |
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
| audio ducking | ljuddämpning | Windows audio setting; do not leave the English phrase exposed. |
| Advanced Audio Properties | Avancerade ljudegenskaper | Preserve the named UI route in help text. |
| Split by Time | dela efter tid | A duration criterion, not a clock time. |
| codec compatibility | kodekkompatibilitet | `kodek` denotes a format; do not confuse it with `kodare`. |
| bind (a network interface/address) | binda OBS till | Include the application as the subject in instructional error text. |
| socket loop | socketslinga | Low-level RTMP option. |
| Safe Mode | felsäkert läge | Use the established operating-system term consistently. |
| streamid | streamid | SRT protocol parameter; retain the literal parameter name. |
| bearer token | Bearer-token | Authentication-scheme name; not `ägartoken`. |
| encoding lag | kodningsfördröjning | Statistics label. |
| rendering lag | renderingsfördröjning | Statistics label. |
| Display Capture | bildskärmsfångst | Source-type label. |
| remuxing | remuxning | Use `remuxa` as the verb and `remuxning` as the noun. |

## Style decisions

- Use direct imperatives in UI guidance: `Försök igen`, `Flytta OBS …`; avoid `Var god`.
- Keep code, variables, format labels, product names and example options unchanged: `%1`, `NVENC`, `I010`, `P010`, `nvEncodeAPI`, `Windows Game DVR`.
- Use ordinary Swedish compounds when they improve readability: `JACK-server`, `JACK-ingångsklient`, `B-bildruta`.
- Use `i stället`, not `istället`.
- Do not introduce an em dash unless it occurs in the source.
