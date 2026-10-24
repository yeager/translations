# ComfyUI svensk ombasning, manuell batch 12

Batchen omfattar 31 återstående generella gränssnittsetiketter, visningsnamn och
tekniska identifierare. Produkt- och kategorinamn har bevarats där de inte ska
översättas.

Kontroller: JSON-parsning, exakt platshållarjämförelse, svlang, l10n-lint 1.23.27,
`git diff --check` och avgränsad Gitleaks. Antalet saknade `main.json`-nycklar
minskade från 100 till 69. Inga platshållaravvikelser finns.
