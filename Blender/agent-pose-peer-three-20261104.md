# Oberoende motgranskning: Blender Manual, Pose Mode, del 3

Datum: 2026-11-04
Underlag: `agent-next-candidates-20261104.md`,
`exports/2026-11-04/blender-manual-manual-sv.po` och
`exports/2026-11-04/blender-ui-ui-sv.po`.

Granskningen omfattar kandidat 23–33 i `copy_paste.rst`. UI-råexporten
belägger `Kopiera pose`, `Klistra in pose`, `Speglad över X-axeln`,
`Endast på markerade` och `Klistra in spegelvänd pose`. RST-menysyntax,
literalvärden och källans X-axel bevaras.

| Nr | Referens | Beslut | Motgranskning |
| --- | --- | --- | --- |
| 23 | `copy_paste.rst:13` | Godkänn | `Kopiera pose` är den UI-belagda operatorn. |
| 24 | `copy_paste.rst:18` | Godkänn | Menyvägen använder samma etablerade operatornamn och bevarar RST-rollen. |
| 25 | `copy_paste.rst:21` | Ändra | Föredra det neutrala dokumentationsordet `Endast`: `Kopierar posen för de markerade benen till posebufferten. Endast markerade ben tas med, vilket gör att enskilda delar av en pose kan kopieras.` |
| 26 | `copy_paste.rst:28` | Godkänn | `Klistra in pose` följer UI-översättningen. |
| 27 | `copy_paste.rst:33` | Godkänn | Menyvägen är korrekt och RST-rollen bevaras. |
| 28 | `copy_paste.rst:36` | Ändra | Källan är beskrivande, inte en uppmaning: `Tillämpar transformeringarna som lagrats i posebufferten på benen i den aktiva armaturen. Ben matchas efter namn, så endast ben med motsvarande namn påverkas.` |
| 29 | `copy_paste.rst:39` | Godkänn | `Speglad över X-axeln` är UI-belagt. |
| 30 | `copy_paste.rst:40` | Godkänn | `inklistrade posen` och `över X-axeln` är tydliga och korrekta. |
| 31 | `copy_paste.rst:43` | Ändra | Använd exakt UI-etikett: `Endast på markerade`. |
| 32 | `copy_paste.rst:44` | Ändra | Källan är beskrivande: `Tillämpar den lagrade posen endast på markerade ben. När alternativet är inaktiverat kan alla ben med matchande namn påverkas, oavsett markering.` |
| 33 | `copy_paste.rst:53` | Ändra | Använd exakt UI-operator: `Klistra in spegelvänd pose`. |

## Slutsats

Sex kandidater godkänns och fem ska justeras enligt ersättningstexterna
ovan. Inga PO-filer har ändrats av denna motgranskning.
