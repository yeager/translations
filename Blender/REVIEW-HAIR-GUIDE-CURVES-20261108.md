# Blender UI – Hair Nodes guidekurvor, batch 1 260

I Hair Nodes betecknar *guide curve* en guidekurva som används av noderna
för interpolering och generering av hårkurvor. Exporten blandade tidigare
*guidekurva* med *styrkurva*. Den här batchen normaliserar de fyra poster som
kommer från `node_geo_interpolate_curves.cc` till projektets etablerade term
*guidekurva*.

| Källa | Granskad svensk text |
| --- | --- |
| Guide Group ID | Guidekurvsgrupp-ID |
| Maximum amount of close guide curves that are taken into account for interpolation | Maximalt antal nära guidekurvor som beaktas för interpolering |
| Index of the closest guide curve for each generated curve | Index för den närmaste guidekurvan för varje genererad kurva |
| Weight of the closest guide curve for each generated curve | Vikt för den närmaste guidekurvan för varje genererad kurva |

`Guidekurvsgrupp-ID` är en avsiktlig teknisk sammansättning och den enda
Hunspell-kandidaten. Kontroller som passerade: `msgfmt`, l10n-lint, svlang
(konsekvens, skrivregler och svengelska), Hunspell, diffkontroll och Gitleaks.

SHA-256: `21ae94dc156afe32bcd3772ee6af8ea58d52013ba7a15223a15dea651ddb26a0`.

Status: lokalt granskat och arkiverat. Weblate-import kräver separat
verifiering.
