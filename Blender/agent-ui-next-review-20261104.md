# Oberoende granskning: Blender UI — action slots och datablock

Underlag: `agent-ui-next-candidates-20261104.md`, råexporten
`exports/2026-11-04/blender-ui-ui-sv.po`, `TERMINOLOGY.md` och befintliga
UI-deltafiler.

## Resultat

| Källa | Bedömning | Slutlig svensk form |
| --- | --- | --- |
| `Slot` | Godkänd | `Slot` |
| `Slot Handle` | Godkänd | `Slothandtag` |
| `Slot Identifier` | Godkänd | `Slotidentifierare` |
| `Slot Display Name` | Godkänd | `Slotvisningsnamn` |
| `Action Slot Handle` | Godkänd | `Åtgärdsslothandtag` |
| `Not yet specified...data-block` | Godkänd | `Inte angiven ännu. När denna slot först tilldelas ett datablock anges den till datablockets typ` |

## Kontrollspår

- Råexporten har de verifierade felaktiga formerna `Slott`,
  `Slotthandtag`, `Slottidentifierare`, `Slottvisningsnamn`,
  `Åtgärdsslotthandtag` och `datablokets`.
- Projektets terminologi fastställer *slot* som `slot` i denna Blender- och
  animeringskontext. `Slott` skulle i stället betyda en byggnad på svenska.
- De sex posterna finns inte i tidigare UI-deltafiler. Inga API-namn,
  markeringar eller formatplatshållare ändras.

## Slutsats

Alla sex kandidater kan föras in i en separat UI-deltafil efter den vanliga
format-, språk- och sekretesskontrollen.
