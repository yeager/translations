# ComfyUI svensk ombasning, manuell batch 6

Batchen omfattar 68 texter för gemensamma kontroller, 3D-ljus, linjärt läge,
3D-vyn, paketförvaltaren, jämförelsevyn, maskredigeraren och export.

Kontroller: JSON-parsning, exakt platshållarjämförelse, svlang, l10n-lint 1.23.27,
`git diff --check` och avgränsad Gitleaks. Antalet saknade `main.json`-nycklar
minskade från 472 till 404. Inga platshållaravvikelser finns.

Commit-hooken rapporterar att `lightInfo.directional`, `lightInfo.point` och
`lightInfo.spot` ännu saknar kodreferenser uppströms. De har översatts men
varningen påverkar inte katalogens giltighet.
