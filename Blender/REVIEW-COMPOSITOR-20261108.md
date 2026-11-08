# Blender UI – kompositör, batch 1 266

I Blender avser **Compositor** den nodbaserade kompositören för bild- och
videobehandling. Projektets terminologi använder *kompositör*. Den äldre
formen *kompositerare* ersätts därför i den relevanta nod- och 3D-vykontexten.

| Källa | Granskad svensk text |
| --- | --- |
| Compositor | Kompositör |

Kontroller som passerade: `msgfmt`, l10n-lint, svlang (konsekvens,
skrivregler och svengelska), Hunspell, diffkontroll och Gitleaks.

## Översättningsminne

Den 8 november 2026 normaliserades också tre äldre Blender-segment i
`swedish-tm` som fortfarande använde *Kompositor* eller lämnade *Compositor*
oöversatt. Segmenten omfattar operatörs-, sekvens- och tom kontext och har
nu konsekvent den granskade termen *Kompositör*. Den aktuella Blender-filen
innehåller redan *Kompositör* i dessa UI-kontexter; minnesändringen är alltså
en kvalitetsrättning av historiska TM-förslag, inte en ny Weblate-import.

SHA-256: `b429f97931d2ba34d332de081cbb014a384971190099f5ed214b31f17f475280`.

Status: lokalt granskat och arkiverat. Weblate-import kräver separat
verifiering.
