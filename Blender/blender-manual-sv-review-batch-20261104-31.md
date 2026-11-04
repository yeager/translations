# Blender Manual: granskningsbatch 31 — Pose Mode, del 1

Datum: 2026-11-04
Källa: exports/2026-11-04/blender-manual-manual-sv.po
Omfattning: 17 unika poster i Pose Mode för att tillämpa och rensa
transformeringar.

Två oberoende granskningar ligger till grund för häftet. UI-belägg har
använts för viloposition, transformering, position och drivrutiner.
RST-roller och kortkommandon är bevarade.

Kontroller: `msgfmt --check --check-header` och `l10n-lint` passerar.
`svlang` markerar enbart RST-rollnamn, den etablerade sammansättningen
`posetransformeringar` och V2-falsklarm för rubriker och imperativ. Gitleaks
fann inga hemligheter och `git diff --check` passerar.

Status: lokalt dubbelgranskad; inte uppladdad. Häftet inväntar en större
manualbatch enligt Blenders uppladdningsintervall.
