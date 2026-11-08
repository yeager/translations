# Blender UI – 3D-vy: fästning, batch 1 263

Projektets terminologi anger **fäst/fästmål** för *snap* i 3D-transformering.
Fyra `space_view3d`-poster använde ändå *snäpp*. Den här batchen är begränsad
till 3D-vyn och ändrar därför inte sequencerns tidsbaserade snäppning eller
andra betydelser av *Snap*.

| Källa | Granskad svensk text |
| --- | --- |
| Snap Target for Individual Elements | Fästmål för enskilda element |
| Snap to Deformed Surface | Fäst vid deformerad yta |
| Snap to Nearest Surface | Fäst vid närmaste yta |
| Snap Vertices | Fäst hörnpunkter |

Kontroller som passerade: `msgfmt`, l10n-lint, svlang (konsekvens,
skrivregler och svengelska), Hunspell, diffkontroll och Gitleaks.

SHA-256: `e9cca2c215ee12c2f4868c3b9187b5d80e51135a6a73b1c88c583ab62e748059`.

Status: lokalt granskat och arkiverat. Weblate-import kräver separat
verifiering.
