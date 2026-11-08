# Blender UI – tilläggsåtgärd, batch 1 267

`Append Action` är inte en generell knapptext utan API-egenskapen
`BlendImportContextItem.append_action`: den anger hur ett datablock hanterades
vid tillägg från ett blendfilsbibliotek. Den projektspecifika termen är därför
**tilläggsåtgärd**, inte den blandade formen *Lägg till Action*.

| Källa | Granskad svensk text |
| --- | --- |
| Append Action | Tilläggsåtgärd |

Kontroller som passerade: `msgfmt`, l10n-lint, svlang (konsekvens,
skrivregler och svengelska), Hunspell, diffkontroll och Gitleaks.

SHA-256: `fb81e5f8c077f4dab2d04b2f9859534b1c9e5efe068e28cc4f03c664033c5619`.

Status: lokalt granskat och arkiverat. Weblate-import kräver separat
verifiering.
