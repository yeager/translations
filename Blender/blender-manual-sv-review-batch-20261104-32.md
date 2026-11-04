# Blender Manual: granskningsbatch 32 — Pose Mode, del 2

Datum: 2026-11-04
Källa: exports/2026-11-04/blender-manual-manual-sv.po
Omfattning: 16 unika poster för återställning samt kopiering och inklistring
av poser.

Häftet utgår från UI-belagda operatorer för posebuffert, kopiering,
inklistring och spegling över X-axeln. Två oberoende motgranskningar har
kontrollerat svensk verbform, operatornamn, RST-roller och markeringens
räckvidd.

Kontroller: `msgfmt --check --check-header` och `l10n-lint` passerar.
`svlang` markerar enbart produktnamnet Blender, projektspecifika
sammansättningar som `posebuffert` och V2-falsklarm för rubriker och
imperativ. Gitleaks fann inga hemligheter och `git diff --check` passerar.

Status: lokalt dubbelgranskad; inte uppladdad. Häftet inväntar en större
manualbatch enligt Blenders uppladdningsintervall.
