# Kodi PVR clients, remaining component review

Whole Swedish PO exports downloaded from Kodi Weblate on 2026-11-02.
The PVR client group is now covered by individual reviewed archive files.

| Component | Messages | Swedish correction made | SHA-256 |
| --- | ---: | --- | --- |
| `pvr-dvblink` | 86 | `channel handle` → `kanalidentifierare` | `649fec2a71895e0b011804c69cf247f9ea040c9787421e9054f5ad8895c1e693` |
| `pvr-nextpvr` | 110 | Quality review; no wording change needed | `5241a4135df257b1112e59b15948330c87de031b4151a8b6a301f1a389c28883` |
| `pvr-hts` | 99 | Quality review; no wording change needed | `c63568da04682966ecc5a4ba3786d32770633aad2fa88db546bcba577a2ffd3e` |
| `pvr-vuplus` | 268 | Swedish wording, Kodi spelling and `33 %` spacing | `5443c4873a99bc7d07cc41e235f42799d31f20e5fa9765ce4fefbcc77fb7a0a7` |
| `pvr-mythtv` | 112 | `show` labels translated as Swedish programme labels | `bab10bfb0e413c3a5e6c9affb65fda40c34eb60eb5af0fd3b1c3a6b0e87d4f74` |

`msgfmt --check`, `l10n-lint` and `svlang skrivregler` pass for every file.
The default export header has no editor/date; that is normal for a newly exported
Weblate PO and is intentionally left for Weblate to populate on import.

All five files are separate Weblate import candidates. This environment has not
performed the browser import.
